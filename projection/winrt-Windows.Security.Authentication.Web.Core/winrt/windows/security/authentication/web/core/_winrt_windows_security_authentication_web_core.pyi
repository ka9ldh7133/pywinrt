# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.security.credentials
import winrt.windows.system

from . import FindAllWebAccountsStatus, WebTokenRequestPromptType, WebTokenRequestStatus

Self = typing.TypeVar('Self')

class FindAllAccountsResult(winrt.system.Object):
    accounts: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.security.credentials.WebAccount]]
    provider_error: typing.Optional[WebProviderError]
    status: FindAllWebAccountsStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FindAllAccountsResult: ...

class WebAccountEventArgs(winrt.system.Object):
    account: typing.Optional[winrt.windows.security.credentials.WebAccount]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountEventArgs: ...

class WebAccountMonitor(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountMonitor: ...
    def add_default_sign_in_account_changed(self, handler: winrt.windows.foundation.TypedEventHandler[WebAccountMonitor, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_default_sign_in_account_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_removed(self, handler: winrt.windows.foundation.TypedEventHandler[WebAccountMonitor, WebAccountEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_removed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_updated(self, handler: winrt.windows.foundation.TypedEventHandler[WebAccountMonitor, WebAccountEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_updated(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_account_picture_updated(self, handler: winrt.windows.foundation.TypedEventHandler[WebAccountMonitor, WebAccountEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_account_picture_updated(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class WebAuthenticationCoreManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAuthenticationCoreManager: ...
    @staticmethod
    def create_web_account_monitor(web_accounts: typing.Iterable[winrt.windows.security.credentials.WebAccount], /) -> typing.Optional[WebAccountMonitor]: ...
    @staticmethod
    def find_account_async(provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider], web_account_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    @typing.overload
    @staticmethod
    def find_account_provider_async(web_account_provider_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccountProvider]: ...
    @typing.overload
    @staticmethod
    def find_account_provider_async(web_account_provider_id: str, authority: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccountProvider]: ...
    @typing.overload
    @staticmethod
    def find_account_provider_async(web_account_provider_id: str, authority: str, user: typing.Optional[winrt.windows.system.User], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccountProvider]: ...
    @typing.overload
    @staticmethod
    def find_all_accounts_async(provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider], /) -> winrt.windows.foundation.IAsyncOperation[FindAllAccountsResult]: ...
    @typing.overload
    @staticmethod
    def find_all_accounts_async(provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider], client_id: str, /) -> winrt.windows.foundation.IAsyncOperation[FindAllAccountsResult]: ...
    @typing.overload
    @staticmethod
    def find_system_account_provider_async(web_account_provider_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccountProvider]: ...
    @typing.overload
    @staticmethod
    def find_system_account_provider_async(web_account_provider_id: str, authority: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccountProvider]: ...
    @typing.overload
    @staticmethod
    def find_system_account_provider_async(web_account_provider_id: str, authority: str, user: typing.Optional[winrt.windows.system.User], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccountProvider]: ...
    @typing.overload
    @staticmethod
    def get_token_silently_async(request: typing.Optional[WebTokenRequest], /) -> winrt.windows.foundation.IAsyncOperation[WebTokenRequestResult]: ...
    @typing.overload
    @staticmethod
    def get_token_silently_async(request: typing.Optional[WebTokenRequest], web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncOperation[WebTokenRequestResult]: ...
    @typing.overload
    @staticmethod
    def request_token_async(request: typing.Optional[WebTokenRequest], /) -> winrt.windows.foundation.IAsyncOperation[WebTokenRequestResult]: ...
    @typing.overload
    @staticmethod
    def request_token_async(request: typing.Optional[WebTokenRequest], web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncOperation[WebTokenRequestResult]: ...

class WebProviderError(winrt.system.Object):
    error_code: winrt.system.UInt32
    error_message: str
    properties: typing.Optional[winrt.windows.foundation.collections.IMap[str, str]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebProviderError: ...
    def __new__(cls: typing.Type[WebProviderError], error_code: winrt.system.UInt32, error_message: str) -> WebProviderError:...

class WebTokenRequest(winrt.system.Object):
    client_id: str
    prompt_type: WebTokenRequestPromptType
    properties: typing.Optional[winrt.windows.foundation.collections.IMap[str, str]]
    scope: str
    web_account_provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider]
    app_properties: typing.Optional[winrt.windows.foundation.collections.IMap[str, str]]
    correlation_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebTokenRequest: ...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenRequest], provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider], scope: str, client_id: str) -> WebTokenRequest:...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenRequest], provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider], scope: str, client_id: str, prompt_type: WebTokenRequestPromptType) -> WebTokenRequest:...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenRequest], provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider]) -> WebTokenRequest:...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenRequest], provider: typing.Optional[winrt.windows.security.credentials.WebAccountProvider], scope: str) -> WebTokenRequest:...

class WebTokenRequestResult(winrt.system.Object):
    response_data: typing.Optional[winrt.windows.foundation.collections.IVectorView[WebTokenResponse]]
    response_error: typing.Optional[WebProviderError]
    response_status: WebTokenRequestStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebTokenRequestResult: ...
    def invalidate_cache_async(self) -> winrt.windows.foundation.IAsyncAction: ...

class WebTokenResponse(winrt.system.Object):
    properties: typing.Optional[winrt.windows.foundation.collections.IMap[str, str]]
    provider_error: typing.Optional[WebProviderError]
    token: str
    web_account: typing.Optional[winrt.windows.security.credentials.WebAccount]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebTokenResponse: ...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenResponse], token: str) -> WebTokenResponse:...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenResponse], token: str, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount]) -> WebTokenResponse:...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenResponse], token: str, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], error: typing.Optional[WebProviderError]) -> WebTokenResponse:...
    @typing.overload
    def __new__(cls: typing.Type[WebTokenResponse]) -> WebTokenResponse:...
