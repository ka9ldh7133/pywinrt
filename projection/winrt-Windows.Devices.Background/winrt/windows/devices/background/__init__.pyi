# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation

Self = typing.TypeVar('Self')

class DeviceServicingDetails(winrt.system.Object):
    arguments: str
    device_id: str
    expected_duration: datetime.timedelta
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceServicingDetails: ...

class DeviceUseDetails(winrt.system.Object):
    arguments: str
    device_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceUseDetails: ...
