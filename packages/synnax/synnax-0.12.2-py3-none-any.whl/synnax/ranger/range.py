#  Copyright 2023 Synnax Labs, Inc.
#
#  Use of this software is governed by the Business Source License included in the file
#  licenses/BSL.txt.
#
#  As of the Change Date specified in that file, in accordance with the Business Source
#  License, use of this software will be governed by the Apache License, Version 2.0,
#  included in the file licenses/APL.txt.

from __future__ import annotations

from typing import overload
from uuid import UUID

import numpy as np
from pydantic import PrivateAttr

from synnax.channel import (
    ChannelKey,
    ChannelKeys,
    ChannelName,
    ChannelNames,
    ChannelParams,
    ChannelPayload,
    ChannelRetriever,
)
from synnax.exceptions import QueryError
from synnax.framer import Client, Frame
from synnax.ranger.alias import Aliaser
from synnax.ranger.kv import KV
from synnax.ranger.payload import RangePayload
from synnax.telem import Series, TimeRange, DataType, Rate
from synnax.util.interop import overload_comparison_operators, overload_operators


class RangeChannel(ChannelPayload):
    __range: Range | None = PrivateAttr(None)
    __frame_client: Client | None = PrivateAttr(None)
    __aliaser: Aliaser | None = PrivateAttr(None)

    def __new__(cls, *args, **kwargs):
        cls = overload_operators(cls, "__array__", ["__len__", "__getitem__"])
        cls = overload_comparison_operators(cls, "__array__")
        return super().__new__(cls)

    class Config:
        arbitrary_types_allowed = True

    def __init__(
        self,
        rng: Range,
        frame_client: Client,
        payload: ChannelPayload,
        aliaser: Aliaser | None = None,
    ):
        super().__init__(**payload.dict())
        self.__range = rng
        self.__frame_client = frame_client
        self.__aliaser = aliaser

    @property
    def time_range(self) -> TimeRange:
        return self.__range.time_range

    def __array__(self) -> np.ndarray:
        return self.read().__array__()

    def __len__(self):
        return len(self.read())

    def read(self) -> Series:
        return self.__frame_client.read(self.time_range, self.key)

    def set_alias(self, alias: str):
        self.__range.set_alias(self.key, alias)

    def __str__(self) -> str:
        return f"{super().__str__()} between {self.time_range.start} and {self.time_range.end}"


class MultiRangeChannel:
    __internal: list[RangeChannel]
    __query: str

    def __new__(cls, *args, **kwargs):
        cls = overload_operators(cls, "__array__", ["__len__", "__getitem__"])
        cls = overload_comparison_operators(cls, "__array__")
        return super().__new__(cls)

    def __init__(
        self,
        query: str,
        internal: list[RangeChannel],
    ):
        self.__internal = internal
        self.__query = query

    def __guard(self):
        if len(self.__internal) > 1:
            raise QueryError(f"""Multiple channels found for query '{self.__query}'""")

    def __array__(self):
        self.__guard()
        return self.__internal[0].__array__()

    @property
    def key(self) -> ChannelKey:
        self.__guard()
        return self.__internal[0].key

    @property
    def name(self) -> str:
        self.__guard()
        return self.__internal[0].name

    @property
    def data_type(self) -> DataType:
        self.__guard()
        return self.__internal[0].data_type

    @property
    def is_index(self) -> bool:
        self.__guard()
        return self.__internal[0].is_index

    @property
    def index(self) -> ChannelKey:
        self.__guard()
        return self.__internal[0].index

    @property
    def leaseholder(self) -> int:
        self.__guard()
        return self.__internal[0].leaseholder

    @property
    def rate(self) -> Rate:
        self.__guard()
        return self.__internal[0].rate

    def set_alias(self, alias: str):
        self.__guard()
        self.__internal[0].set_alias(alias)

    def __iter__(self):
        return iter(self.__internal)


_RANGE_NOT_CREATED = QueryError(
    """Cannot read from a range that has not been created.
Please call client.ranges.create(range) before attempting to read from a range."""
)


class Range(RangePayload):
    """A range is a user-defined region of a cluster's data. It's identified by a name,
    time range, and uniquely generated key. See
    https://docs.synnaxlabs.com/concepts/read-range for an introduction to ranges and
    how they work.
    """

    __frame_client: Client | None = PrivateAttr(None)
    __channel_retriever: ChannelRetriever | None = PrivateAttr(None)
    __kv: KV | None = PrivateAttr(None)
    __aliaser: Aliaser | None = PrivateAttr(None)

    class Config:
        arbitrary_types_allowed = True

    def __init__(
        self,
        name: str,
        time_range: TimeRange,
        key: UUID = UUID(int=0),
        _frame_client: Client | None = None,
        _channel_retriever: ChannelRetriever | None = None,
        _kv: KV | None = None,
        _aliaser: Aliaser | None = None,
    ):
        """Initializes a new Range using the given parameters. It's important to note
        that this does not create the Range in the cluster. To create the range, call
        client.ranges.create(range).

        :param name: A human-readable name for the range. This should represent the data
            that the range contains i.e. "Hotfire 1", "Print 22", or "Tank Burst Test.".
        :param time_range: The time region spanned by the range. Note that this range
            is end inclusive and end exclusive i.e. the start represents the timestamp
            of just before or at the first data point in the range, and the end represents
            the timestamp of the just after the last data point in the range.
        :param key: A UUID that uniquely identifies the range. This is typically not
            set by the user, and is generated by the cluster upon creating the range.
        :param _frame_client: The backing client for reading and writing data to
            and from the cluster. This is provided by Synnax during calls to
            .ranges.create() and .ranges.retrieve(), and should not be set by the user.
        :param _channel_retriever: The backing client for retrieving channels to
            and from the cluster. This is provided by Synnax during calls to
            .ranges.create() and .ranges.retrieve(), and should not be set by the user.
        """
        super().__init__(name=name, time_range=time_range, key=key)
        self.__frame_client = _frame_client
        self.__channel_retriever = _channel_retriever
        self.__kv = _kv
        self.__aliaser = _aliaser

    def __getattr__(self, name: str) -> MultiRangeChannel:
        channels = self._channel_retriever.retrieve(name)
        aliases = self._aliaser.resolve([name])
        print(aliases)
        for alias in aliases.values():
            channels.extend(self._channel_retriever.retrieve(alias))

        if len(channels) == 0:
            raise QueryError(f"Channel {name} not found")

        return MultiRangeChannel(name, [RangeChannel(rng=self, frame_client=self._frame_client, payload=ch) for ch in channels])

    def __getitem__(self, name: str) -> MultiRangeChannel:
        return self.__getattr__(name)

    @property
    def meta_data(self):
        if self.__kv is None:
            raise _RANGE_NOT_CREATED
        return self.__kv

    @property
    def _aliaser(self):
        if self.__aliaser is None:
            raise _RANGE_NOT_CREATED
        return self.__aliaser

    @property
    def _frame_client(self) -> Client:
        if self.__frame_client is None:
            raise _RANGE_NOT_CREATED
        return self.__frame_client

    @property
    def _channel_retriever(self) -> ChannelRetriever:
        if self.__channel_retriever is None:
            raise _RANGE_NOT_CREATED
        return self.__channel_retriever

    @overload
    def read(self, params: ChannelKey | ChannelName) -> Series:
        ...

    @overload
    def read(self, params: ChannelKeys | ChannelNames) -> Frame:
        ...

    def read(
        self,
        params: ChannelParams,
    ) -> Series | Frame:
        return self.__frame_client.read(
            self.time_range,
            params,
        )

    def set_alias(self, channel: ChannelKey | ChannelName, alias: str):
        ...

    def set_alias(self, channel: dict[ChannelKey | ChannelName, str]):
        ...

    def set_alias(
        self,
        channel: ChannelKey | ChannelName | dict[ChannelKey | ChannelName, str],
        alias: str = None,
    ):
        if not isinstance(channel, dict):
            if alias is None:
                raise ValueError("Alias must be provided if channel is not a dict")
            channel = {channel: alias}

        corrected = {}
        for ch, alias in channel.items():
            if isinstance(ch, ChannelName):
                res = self._channel_retriever.retrieve(ch)
                if len(res) == 0:
                    raise QueryError(f"Channel {ch} not found")
                corrected[res[0].key] = alias
            else:
                corrected[ch] = alias
        self._aliaser.set(corrected)

    def to_payload(self) -> RangePayload:
        return RangePayload(name=self.name, time_range=self.time_range, key=self.key)
