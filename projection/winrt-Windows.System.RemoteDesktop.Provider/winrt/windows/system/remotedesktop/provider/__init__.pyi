# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.ui

class RemoteDesktopConnectionStatus(enum.IntEnum):
    CONNECTING = 0
    CONNECTED = 1
    USER_INPUT_NEEDED = 2
    DISCONNECTED = 3

Self = typing.TypeVar('Self')

class RemoteDesktopConnectionInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RemoteDesktopConnectionInfo: ...
    @staticmethod
    def get_for_launch_uri(launch_uri: typing.Optional[winrt.windows.foundation.Uri], window_id: winrt.windows.ui.WindowId, /) -> typing.Optional[RemoteDesktopConnectionInfo]: ...
    def set_connection_status(self, value: RemoteDesktopConnectionStatus, /) -> None: ...
