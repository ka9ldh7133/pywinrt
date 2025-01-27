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

from winrt.windows.security.authentication.web import TokenBindingKeyType, WebAuthenticationOptions, WebAuthenticationStatus

Self = typing.TypeVar('Self')

@typing.final
class WebAuthenticationBroker_Static(type):
    def authenticate_and_continue(cls, request_uri: windows_foundation.Uri, /) -> None: ...
    def authenticate_silently_async(cls, request_uri: windows_foundation.Uri, /) -> windows_foundation.IAsyncOperation[WebAuthenticationResult]: ...
    def authenticate_silently_with_options_async(cls, request_uri: windows_foundation.Uri, options: WebAuthenticationOptions, /) -> windows_foundation.IAsyncOperation[WebAuthenticationResult]: ...
    def authenticate_with_callback_uri_and_continue(cls, request_uri: windows_foundation.Uri, callback_uri: windows_foundation.Uri, /) -> None: ...
    def authenticate_with_callback_uri_async(cls, options: WebAuthenticationOptions, request_uri: windows_foundation.Uri, callback_uri: windows_foundation.Uri, /) -> windows_foundation.IAsyncOperation[WebAuthenticationResult]: ...
    def authenticate_with_callback_uri_continuation_data_and_options_and_continue(cls, request_uri: windows_foundation.Uri, callback_uri: windows_foundation.Uri, continuation_data: windows_foundation_collections.ValueSet, options: WebAuthenticationOptions, /) -> None: ...
    def authenticate_without_callback_uri_async(cls, options: WebAuthenticationOptions, request_uri: windows_foundation.Uri, /) -> windows_foundation.IAsyncOperation[WebAuthenticationResult]: ...
    def get_current_application_callback_uri(cls) -> windows_foundation.Uri: ...

@typing.final
class WebAuthenticationBroker(winrt.system.Object, metaclass=WebAuthenticationBroker_Static):
    pass

@typing.final
class WebAuthenticationResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAuthenticationResult: ...
    @_property
    def response_data(self) -> str: ...
    @_property
    def response_error_detail(self) -> winrt.system.UInt32: ...
    @_property
    def response_status(self) -> WebAuthenticationStatus: ...

