# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_system_diagnostics_deviceportal

class DevicePortalConnectionClosedReason(enum.IntEnum):
    UNKNOWN = 0
    RESOURCE_LIMITS_EXCEEDED = 1
    PROTOCOL_ERROR = 2
    NOT_AUTHORIZED = 3
    USER_NOT_PRESENT = 4
    SERVICE_TERMINATED = 5

DevicePortalConnection = _winrt_windows_system_diagnostics_deviceportal.DevicePortalConnection
DevicePortalConnectionClosedEventArgs = _winrt_windows_system_diagnostics_deviceportal.DevicePortalConnectionClosedEventArgs
DevicePortalConnectionRequestReceivedEventArgs = _winrt_windows_system_diagnostics_deviceportal.DevicePortalConnectionRequestReceivedEventArgs