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

from winrt.microsoft.windows.appnotifications import AppNotificationPriority, AppNotificationProgressResult, AppNotificationSetting

Self = typing.TypeVar('Self')

@typing.final
class AppNotification(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppNotification: ...
    def __new__(cls: typing.Type[Self], payload: str) -> Self: ...
    @_property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> None: ...
    @_property
    def suppress_display(self) -> bool: ...
    @suppress_display.setter
    def suppress_display(self, value: bool) -> None: ...
    @_property
    def progress(self) -> AppNotificationProgressData: ...
    @progress.setter
    def progress(self, value: AppNotificationProgressData) -> None: ...
    @_property
    def priority(self) -> AppNotificationPriority: ...
    @priority.setter
    def priority(self, value: AppNotificationPriority) -> None: ...
    @_property
    def group(self) -> str: ...
    @group.setter
    def group(self, value: str) -> None: ...
    @_property
    def expires_on_reboot(self) -> bool: ...
    @expires_on_reboot.setter
    def expires_on_reboot(self, value: bool) -> None: ...
    @_property
    def expiration(self) -> datetime.datetime: ...
    @expiration.setter
    def expiration(self, value: datetime.datetime) -> None: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def payload(self) -> str: ...

@typing.final
class AppNotificationActivatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppNotificationActivatedEventArgs: ...
    @_property
    def argument(self) -> str: ...
    @_property
    def user_input(self) -> typing.MutableMapping[str, str]: ...
    @_property
    def arguments(self) -> typing.MutableMapping[str, str]: ...

@typing.final
class AppNotificationManager_Static(type):
    def is_supported(cls) -> bool: ...
    @_property
    def default(cls) -> AppNotificationManager: ...

@typing.final
class AppNotificationManager(winrt.system.Object, metaclass=AppNotificationManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppNotificationManager: ...
    def get_all_async(self) -> windows_foundation.IAsyncOperation[typing.MutableSequence[AppNotification]]: ...
    @typing.overload
    def register(self) -> None: ...
    @typing.overload
    def register(self, display_name: str, icon_uri: windows_foundation.Uri, /) -> None: ...
    def remove_all_async(self) -> windows_foundation.IAsyncAction: ...
    def remove_by_group_async(self, group: str, /) -> windows_foundation.IAsyncAction: ...
    def remove_by_id_async(self, notification_id: winrt.system.UInt32, /) -> windows_foundation.IAsyncAction: ...
    def remove_by_tag_and_group_async(self, tag: str, group: str, /) -> windows_foundation.IAsyncAction: ...
    def remove_by_tag_async(self, tag: str, /) -> windows_foundation.IAsyncAction: ...
    def show(self, notification: AppNotification, /) -> None: ...
    def unregister(self) -> None: ...
    def unregister_all(self) -> None: ...
    def update_async(self, data: AppNotificationProgressData, tag: str, group: str, /) -> windows_foundation.IAsyncOperation[AppNotificationProgressResult]: ...
    def update_async2(self, data: AppNotificationProgressData, tag: str, /) -> windows_foundation.IAsyncOperation[AppNotificationProgressResult]: ...
    def add_notification_invoked(self, handler: windows_foundation.TypedEventHandler[AppNotificationManager, AppNotificationActivatedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_notification_invoked(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def setting(self) -> AppNotificationSetting: ...

@typing.final
class AppNotificationProgressData(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppNotificationProgressData: ...
    def __new__(cls: typing.Type[Self], sequence_number: winrt.system.UInt32) -> Self: ...
    @_property
    def value_string_override(self) -> str: ...
    @value_string_override.setter
    def value_string_override(self, value: str) -> None: ...
    @_property
    def value(self) -> winrt.system.Double: ...
    @value.setter
    def value(self, value: winrt.system.Double) -> None: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str) -> None: ...
    @_property
    def sequence_number(self) -> winrt.system.UInt32: ...
    @sequence_number.setter
    def sequence_number(self, value: winrt.system.UInt32) -> None: ...

