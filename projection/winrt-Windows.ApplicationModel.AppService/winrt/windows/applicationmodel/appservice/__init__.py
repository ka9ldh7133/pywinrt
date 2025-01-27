# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt._winrt_windows_applicationmodel_appservice import (
    AppServiceCatalog,
    AppServiceClosedEventArgs,
    AppServiceConnection,
    AppServiceDeferral,
    AppServiceRequest,
    AppServiceRequestReceivedEventArgs,
    AppServiceResponse,
    AppServiceTriggerDetails,
    StatelessAppServiceResponse,
)

__all__ = [
    "AppServiceClosedStatus",
    "AppServiceConnectionStatus",
    "AppServiceResponseStatus",
    "StatelessAppServiceResponseStatus",
    "AppServiceCatalog",
    "AppServiceClosedEventArgs",
    "AppServiceConnection",
    "AppServiceDeferral",
    "AppServiceRequest",
    "AppServiceRequestReceivedEventArgs",
    "AppServiceResponse",
    "AppServiceTriggerDetails",
    "StatelessAppServiceResponse",
]

class AppServiceClosedStatus(enum.IntEnum):
    COMPLETED = 0
    CANCELED = 1
    RESOURCE_LIMITS_EXCEEDED = 2
    UNKNOWN = 3

class AppServiceConnectionStatus(enum.IntEnum):
    SUCCESS = 0
    APP_NOT_INSTALLED = 1
    APP_UNAVAILABLE = 2
    APP_SERVICE_UNAVAILABLE = 3
    UNKNOWN = 4
    REMOTE_SYSTEM_UNAVAILABLE = 5
    REMOTE_SYSTEM_NOT_SUPPORTED_BY_APP = 6
    NOT_AUTHORIZED = 7
    AUTHENTICATION_ERROR = 8
    NETWORK_NOT_AVAILABLE = 9
    DISABLED_BY_POLICY = 10
    WEB_SERVICE_UNAVAILABLE = 11

class AppServiceResponseStatus(enum.IntEnum):
    SUCCESS = 0
    FAILURE = 1
    RESOURCE_LIMITS_EXCEEDED = 2
    UNKNOWN = 3
    REMOTE_SYSTEM_UNAVAILABLE = 4
    MESSAGE_SIZE_TOO_LARGE = 5
    APP_UNAVAILABLE = 6
    AUTHENTICATION_ERROR = 7
    NETWORK_NOT_AVAILABLE = 8
    DISABLED_BY_POLICY = 9
    WEB_SERVICE_UNAVAILABLE = 10

class StatelessAppServiceResponseStatus(enum.IntEnum):
    SUCCESS = 0
    APP_NOT_INSTALLED = 1
    APP_UNAVAILABLE = 2
    APP_SERVICE_UNAVAILABLE = 3
    REMOTE_SYSTEM_UNAVAILABLE = 4
    REMOTE_SYSTEM_NOT_SUPPORTED_BY_APP = 5
    NOT_AUTHORIZED = 6
    RESOURCE_LIMITS_EXCEEDED = 7
    MESSAGE_SIZE_TOO_LARGE = 8
    FAILURE = 9
    UNKNOWN = 10
    AUTHENTICATION_ERROR = 11
    NETWORK_NOT_AVAILABLE = 12
    DISABLED_BY_POLICY = 13
    WEB_SERVICE_UNAVAILABLE = 14

