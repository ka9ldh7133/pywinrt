# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation

Self = typing.TypeVar('Self')

class PerceptionTimestamp(winrt.system.Object):
    prediction_amount: datetime.timedelta
    target_time: datetime.datetime
    system_relative_target_time: datetime.timedelta
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionTimestamp: ...

class PerceptionTimestampHelper(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionTimestampHelper: ...
    @staticmethod
    def from_historical_target_time(target_time: datetime.datetime, /) -> typing.Optional[PerceptionTimestamp]: ...
    @staticmethod
    def from_system_relative_target_time(target_time: datetime.timedelta, /) -> typing.Optional[PerceptionTimestamp]: ...
