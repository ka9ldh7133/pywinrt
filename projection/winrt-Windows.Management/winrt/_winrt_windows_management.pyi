# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections

from winrt.windows.management import MdmAlertDataType, MdmAlertMark, MdmSessionState

Self = typing.TypeVar('Self')

@typing.final
class MdmAlert(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MdmAlert: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str) -> None: ...
    @_property
    def target(self) -> str: ...
    @target.setter
    def target(self, value: str) -> None: ...
    @_property
    def source(self) -> str: ...
    @source.setter
    def source(self, value: str) -> None: ...
    @_property
    def mark(self) -> MdmAlertMark: ...
    @mark.setter
    def mark(self, value: MdmAlertMark) -> None: ...
    @_property
    def format(self) -> MdmAlertDataType: ...
    @format.setter
    def format(self, value: MdmAlertDataType) -> None: ...
    @_property
    def data(self) -> str: ...
    @data.setter
    def data(self, value: str) -> None: ...
    @_property
    def status(self) -> winrt.system.UInt32: ...

@typing.final
class MdmSession(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MdmSession: ...
    def attach_async(self) -> windows_foundation.IAsyncAction: ...
    def delete(self) -> None: ...
    def start_async(self) -> windows_foundation.IAsyncAction: ...
    def start_with_alerts_async(self, alerts: typing.Iterable[MdmAlert], /) -> windows_foundation.IAsyncAction: ...
    @_property
    def alerts(self) -> typing.Sequence[MdmAlert]: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def id(self) -> str: ...
    @_property
    def state(self) -> MdmSessionState: ...

@typing.final
class MdmSessionManager_Static(type):
    def delete_session_by_id(cls, session_id: str, /) -> None: ...
    def get_session_by_id(cls, session_id: str, /) -> MdmSession: ...
    def try_create_session(cls) -> MdmSession: ...
    @_property
    def session_ids(cls) -> typing.Sequence[str]: ...

@typing.final
class MdmSessionManager(winrt.system.Object, metaclass=MdmSessionManager_Static):
    pass

