# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.applicationmodel.datatransfer
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.storage.streams
import winrt.windows.ui
import winrt.windows.web
import winrt.windows.web.http

from . import WebViewControlPermissionState, WebViewControlPermissionType

Self = typing.TypeVar('Self')

class WebViewControlContentLoadingEventArgs(winrt.system.Object):
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlContentLoadingEventArgs: ...

class WebViewControlDOMContentLoadedEventArgs(winrt.system.Object):
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlDOMContentLoadedEventArgs: ...

class WebViewControlDeferredPermissionRequest(winrt.system.Object):
    id: winrt.system.UInt32
    permission_type: WebViewControlPermissionType
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlDeferredPermissionRequest: ...
    def allow(self) -> None: ...
    def deny(self) -> None: ...

class WebViewControlLongRunningScriptDetectedEventArgs(winrt.system.Object):
    stop_page_script_execution: winrt.system.Boolean
    execution_time: datetime.timedelta
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlLongRunningScriptDetectedEventArgs: ...

class WebViewControlNavigationCompletedEventArgs(winrt.system.Object):
    is_success: winrt.system.Boolean
    uri: typing.Optional[winrt.windows.foundation.Uri]
    web_error_status: winrt.windows.web.WebErrorStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlNavigationCompletedEventArgs: ...

class WebViewControlNavigationStartingEventArgs(winrt.system.Object):
    cancel: winrt.system.Boolean
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlNavigationStartingEventArgs: ...

class WebViewControlNewWindowRequestedEventArgs(winrt.system.Object):
    handled: winrt.system.Boolean
    referrer: typing.Optional[winrt.windows.foundation.Uri]
    uri: typing.Optional[winrt.windows.foundation.Uri]
    new_window: typing.Optional[IWebViewControl]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlNewWindowRequestedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class WebViewControlPermissionRequest(winrt.system.Object):
    id: winrt.system.UInt32
    permission_type: WebViewControlPermissionType
    state: WebViewControlPermissionState
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlPermissionRequest: ...
    def allow(self) -> None: ...
    def defer(self) -> None: ...
    def deny(self) -> None: ...

class WebViewControlPermissionRequestedEventArgs(winrt.system.Object):
    permission_request: typing.Optional[WebViewControlPermissionRequest]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlPermissionRequestedEventArgs: ...

class WebViewControlScriptNotifyEventArgs(winrt.system.Object):
    uri: typing.Optional[winrt.windows.foundation.Uri]
    value: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlScriptNotifyEventArgs: ...

class WebViewControlSettings(winrt.system.Object):
    is_script_notify_allowed: winrt.system.Boolean
    is_java_script_enabled: winrt.system.Boolean
    is_indexed_d_b_enabled: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlSettings: ...

class WebViewControlUnsupportedUriSchemeIdentifiedEventArgs(winrt.system.Object):
    handled: winrt.system.Boolean
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlUnsupportedUriSchemeIdentifiedEventArgs: ...

class WebViewControlUnviewableContentIdentifiedEventArgs(winrt.system.Object):
    media_type: str
    referrer: typing.Optional[winrt.windows.foundation.Uri]
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlUnviewableContentIdentifiedEventArgs: ...

class WebViewControlWebResourceRequestedEventArgs(winrt.system.Object):
    response: typing.Optional[winrt.windows.web.http.HttpResponseMessage]
    request: typing.Optional[winrt.windows.web.http.HttpRequestMessage]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebViewControlWebResourceRequestedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class IWebViewControl(winrt.system.Object):
    can_go_back: winrt.system.Boolean
    can_go_forward: winrt.system.Boolean
    contains_full_screen_element: winrt.system.Boolean
    default_background_color: winrt.windows.ui.Color
    deferred_permission_requests: typing.Optional[winrt.windows.foundation.collections.IVectorView[WebViewControlDeferredPermissionRequest]]
    document_title: str
    settings: typing.Optional[WebViewControlSettings]
    source: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebViewControl: ...
    def build_local_stream_uri(self, content_identifier: str, relative_path: str, /) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    def capture_preview_to_stream_async(self, stream: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], /) -> winrt.windows.foundation.IAsyncAction: ...
    def capture_selected_content_to_data_package_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.applicationmodel.datatransfer.DataPackage]: ...
    def get_deferred_permission_request_by_id(self, id: winrt.system.UInt32, /) -> typing.Optional[WebViewControlDeferredPermissionRequest]: ...
    def go_back(self) -> None: ...
    def go_forward(self) -> None: ...
    def invoke_script_async(self, script_name: str, arguments: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[str]: ...
    def navigate(self, source: typing.Optional[winrt.windows.foundation.Uri], /) -> None: ...
    def navigate_to_local_stream_uri(self, source: typing.Optional[winrt.windows.foundation.Uri], stream_resolver: typing.Optional[winrt.windows.web.IUriToStreamResolver], /) -> None: ...
    def navigate_to_string(self, text: str, /) -> None: ...
    def navigate_with_http_request_message(self, request_message: typing.Optional[winrt.windows.web.http.HttpRequestMessage], /) -> None: ...
    def refresh(self) -> None: ...
    def stop(self) -> None: ...
    def add_contains_full_screen_element_changed(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_contains_full_screen_element_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_content_loading(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlContentLoadingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_content_loading(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_d_o_m_content_loaded(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlDOMContentLoadedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_d_o_m_content_loaded(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_frame_content_loading(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlContentLoadingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_frame_content_loading(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_frame_d_o_m_content_loaded(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlDOMContentLoadedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_frame_d_o_m_content_loaded(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_frame_navigation_completed(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlNavigationCompletedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_frame_navigation_completed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_frame_navigation_starting(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlNavigationStartingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_frame_navigation_starting(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_long_running_script_detected(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlLongRunningScriptDetectedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_long_running_script_detected(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_navigation_completed(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlNavigationCompletedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_navigation_completed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_navigation_starting(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlNavigationStartingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_navigation_starting(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_new_window_requested(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlNewWindowRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_new_window_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_permission_requested(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlPermissionRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_permission_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_script_notify(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlScriptNotifyEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_script_notify(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_unsafe_content_warning_displaying(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_unsafe_content_warning_displaying(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_unsupported_uri_scheme_identified(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlUnsupportedUriSchemeIdentifiedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_unsupported_uri_scheme_identified(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_unviewable_content_identified(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlUnviewableContentIdentifiedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_unviewable_content_identified(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_web_resource_requested(self, handler: winrt.windows.foundation.TypedEventHandler[IWebViewControl, WebViewControlWebResourceRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_web_resource_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class IWebViewControl2(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IWebViewControl2: ...
    def add_initialize_script(self, script: str, /) -> None: ...
