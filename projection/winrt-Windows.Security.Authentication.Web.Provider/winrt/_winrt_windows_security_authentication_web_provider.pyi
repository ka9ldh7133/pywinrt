# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.security.authentication.web
import winrt.windows.security.authentication.web.core
import winrt.windows.security.credentials
import winrt.windows.security.cryptography.core
import winrt.windows.storage.streams
import winrt.windows.system
import winrt.windows.web.http

from winrt.windows.security.authentication.web.provider import WebAccountClientViewType, WebAccountProviderOperationKind, WebAccountScope, WebAccountSelectionOptions

Self = typing.TypeVar('Self')

class WebAccountClientView(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountClientView: ...
    @typing.overload
    def __new__(cls: typing.Type[WebAccountClientView], view_type: WebAccountClientViewType, application_callback_uri: typing.Optional[winrt.windows.foundation.Uri]) -> WebAccountClientView:...
    @typing.overload
    def __new__(cls: typing.Type[WebAccountClientView], view_type: WebAccountClientViewType, application_callback_uri: typing.Optional[winrt.windows.foundation.Uri], account_pairwise_id: str) -> WebAccountClientView:...
    @_property
    def account_pairwise_id(self) -> str: ...
    @_property
    def application_callback_uri(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def type(self) -> WebAccountClientViewType: ...

class WebAccountManager_Static(type):
    @typing.overload
    def add_web_account_async(cls, web_account_id: str, web_account_user_name: str, props: winrt.windows.foundation.collections.IMapView[str, str], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    @typing.overload
    def add_web_account_async(cls, web_account_id: str, web_account_user_name: str, props: winrt.windows.foundation.collections.IMapView[str, str], scope: WebAccountScope, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    @typing.overload
    def add_web_account_async(cls, web_account_id: str, web_account_user_name: str, props: winrt.windows.foundation.collections.IMapView[str, str], scope: WebAccountScope, per_user_web_account_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    @typing.overload
    def add_web_account_for_user_async(cls, user: typing.Optional[winrt.windows.system.User], web_account_id: str, web_account_user_name: str, props: winrt.windows.foundation.collections.IMapView[str, str], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    @typing.overload
    def add_web_account_for_user_async(cls, user: typing.Optional[winrt.windows.system.User], web_account_id: str, web_account_user_name: str, props: winrt.windows.foundation.collections.IMapView[str, str], scope: WebAccountScope, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    @typing.overload
    def add_web_account_for_user_async(cls, user: typing.Optional[winrt.windows.system.User], web_account_id: str, web_account_user_name: str, props: winrt.windows.foundation.collections.IMapView[str, str], scope: WebAccountScope, per_user_web_account_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    def clear_per_user_from_per_app_account_async(cls, per_app_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncAction: ...
    def clear_view_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], application_callback_uri: typing.Optional[winrt.windows.foundation.Uri], /) -> winrt.windows.foundation.IAsyncAction: ...
    def clear_web_account_picture_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncAction: ...
    def delete_web_account_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncAction: ...
    def find_all_provider_web_accounts_async(cls) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[winrt.windows.security.credentials.WebAccount]]: ...
    def find_all_provider_web_accounts_for_user_async(cls, user: typing.Optional[winrt.windows.system.User], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[winrt.windows.security.credentials.WebAccount]]: ...
    def get_per_user_from_per_app_account_async(cls, per_app_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.credentials.WebAccount]: ...
    def get_scope(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> WebAccountScope: ...
    def get_views_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[WebAccountClientView]]: ...
    def invalidate_app_cache_for_account_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncAction: ...
    def invalidate_app_cache_for_all_accounts_async(cls) -> winrt.windows.foundation.IAsyncAction: ...
    def pull_cookies_async(cls, uri_string: str, caller_p_f_n: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def push_cookies_async(cls, uri: typing.Optional[winrt.windows.foundation.Uri], cookies: winrt.windows.foundation.collections.IVectorView[winrt.windows.web.http.HttpCookie], /) -> winrt.windows.foundation.IAsyncAction: ...
    def set_per_app_to_per_user_account_async(cls, per_app_account: typing.Optional[winrt.windows.security.credentials.WebAccount], per_user_web_account_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def set_scope_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], scope: WebAccountScope, /) -> winrt.windows.foundation.IAsyncAction: ...
    def set_view_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], view: typing.Optional[WebAccountClientView], /) -> winrt.windows.foundation.IAsyncAction: ...
    def set_web_account_picture_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], web_account_picture: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], /) -> winrt.windows.foundation.IAsyncAction: ...
    def update_web_account_properties_async(cls, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], web_account_user_name: str, additional_properties: winrt.windows.foundation.collections.IMapView[str, str], /) -> winrt.windows.foundation.IAsyncAction: ...

class WebAccountManager(winrt.system.Object, metaclass=WebAccountManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountManager: ...

class WebAccountProviderAddAccountOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderAddAccountOperation: ...
    def report_completed(self) -> None: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...

class WebAccountProviderDeleteAccountOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderDeleteAccountOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    @_property
    def web_account(self) -> typing.Optional[winrt.windows.security.credentials.WebAccount]: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...

class WebAccountProviderGetTokenSilentOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderGetTokenSilentOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    @typing.overload
    def report_user_interaction_required(self) -> None: ...
    @typing.overload
    def report_user_interaction_required(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...
    @_property
    def cache_expiration_time(self) -> datetime.datetime: ...
    @cache_expiration_time.setter
    def cache_expiration_time(self, value: datetime.datetime) -> None: ...
    @_property
    def provider_request(self) -> typing.Optional[WebProviderTokenRequest]: ...
    @_property
    def provider_responses(self) -> typing.Optional[winrt.windows.foundation.collections.IVector[WebProviderTokenResponse]]: ...

class WebAccountProviderManageAccountOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderManageAccountOperation: ...
    def report_completed(self) -> None: ...
    @_property
    def web_account(self) -> typing.Optional[winrt.windows.security.credentials.WebAccount]: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...

class WebAccountProviderRequestTokenOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderRequestTokenOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    def report_user_canceled(self) -> None: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...
    @_property
    def cache_expiration_time(self) -> datetime.datetime: ...
    @cache_expiration_time.setter
    def cache_expiration_time(self, value: datetime.datetime) -> None: ...
    @_property
    def provider_request(self) -> typing.Optional[WebProviderTokenRequest]: ...
    @_property
    def provider_responses(self) -> typing.Optional[winrt.windows.foundation.collections.IVector[WebProviderTokenResponse]]: ...

class WebAccountProviderRetrieveCookiesOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderRetrieveCookiesOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...
    @_property
    def uri(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @uri.setter
    def uri(self, value: typing.Optional[winrt.windows.foundation.Uri]) -> None: ...
    @_property
    def application_callback_uri(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def context(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def cookies(self) -> typing.Optional[winrt.windows.foundation.collections.IVector[winrt.windows.web.http.HttpCookie]]: ...

class WebAccountProviderSignOutAccountOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderSignOutAccountOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...
    @_property
    def application_callback_uri(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def client_id(self) -> str: ...
    @_property
    def web_account(self) -> typing.Optional[winrt.windows.security.credentials.WebAccount]: ...

class WebAccountProviderTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAccountProviderTriggerDetails: ...
    @_property
    def operation(self) -> typing.Optional[IWebAccountProviderOperation]: ...
    @_property
    def user(self) -> typing.Optional[winrt.windows.system.User]: ...

class WebProviderTokenRequest(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebProviderTokenRequest: ...
    def check_application_for_capability_async(self, capability_name: str, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    def get_application_token_binding_key_async(self, key_type: winrt.windows.security.authentication.web.TokenBindingKeyType, target: typing.Optional[winrt.windows.foundation.Uri], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.cryptography.core.CryptographicKey]: ...
    def get_application_token_binding_key_id_async(self, key_type: winrt.windows.security.authentication.web.TokenBindingKeyType, target: typing.Optional[winrt.windows.foundation.Uri], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.storage.streams.IBuffer]: ...
    @_property
    def application_callback_uri(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def client_request(self) -> typing.Optional[winrt.windows.security.authentication.web.core.WebTokenRequest]: ...
    @_property
    def web_account_selection_options(self) -> WebAccountSelectionOptions: ...
    @_property
    def web_accounts(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.security.credentials.WebAccount]]: ...
    @_property
    def application_package_family_name(self) -> str: ...
    @_property
    def application_process_name(self) -> str: ...

class WebProviderTokenResponse(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebProviderTokenResponse: ...
    def __new__(cls: typing.Type[WebProviderTokenResponse], web_token_response: typing.Optional[winrt.windows.security.authentication.web.core.WebTokenResponse]) -> WebProviderTokenResponse:...
    @_property
    def client_response(self) -> typing.Optional[winrt.windows.security.authentication.web.core.WebTokenResponse]: ...

class IWebAccountProviderBaseReportOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderBaseReportOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...

class IWebAccountProviderOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderOperation: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...

class IWebAccountProviderSilentReportOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderSilentReportOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    @typing.overload
    def report_user_interaction_required(self) -> None: ...
    @typing.overload
    def report_user_interaction_required(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...

class IWebAccountProviderTokenObjects(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderTokenObjects: ...
    @_property
    def operation(self) -> typing.Optional[IWebAccountProviderOperation]: ...

class IWebAccountProviderTokenObjects2(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderTokenObjects2: ...
    @_property
    def user(self) -> typing.Optional[winrt.windows.system.User]: ...
    @_property
    def operation(self) -> typing.Optional[IWebAccountProviderOperation]: ...

class IWebAccountProviderTokenOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderTokenOperation: ...
    @_property
    def cache_expiration_time(self) -> datetime.datetime: ...
    @cache_expiration_time.setter
    def cache_expiration_time(self, value: datetime.datetime) -> None: ...
    @_property
    def provider_request(self) -> typing.Optional[WebProviderTokenRequest]: ...
    @_property
    def provider_responses(self) -> typing.Optional[winrt.windows.foundation.collections.IVector[WebProviderTokenResponse]]: ...
    @_property
    def kind(self) -> WebAccountProviderOperationKind: ...

class IWebAccountProviderUIReportOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebAccountProviderUIReportOperation: ...
    def report_completed(self) -> None: ...
    def report_error(self, value: typing.Optional[winrt.windows.security.authentication.web.core.WebProviderError], /) -> None: ...
    def report_user_canceled(self) -> None: ...
