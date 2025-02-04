# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.enumeration as windows_devices_enumeration
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.networking as windows_networking
import winrt.windows.networking.sockets as windows_networking_sockets
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.devices.wifidirect.services import WiFiDirectServiceAdvertisementStatus, WiFiDirectServiceConfigurationMethod, WiFiDirectServiceError, WiFiDirectServiceIPProtocol, WiFiDirectServiceSessionErrorStatus, WiFiDirectServiceSessionStatus, WiFiDirectServiceStatus

Self = typing.TypeVar('Self')

@typing.final
class WiFiDirectService_Static(type):
    def from_id_async(cls, device_id: str, /) -> windows_foundation.IAsyncOperation[WiFiDirectService]: ...
    def get_selector(cls, service_name: str, /) -> str: ...
    def get_selector_with_filter(cls, service_name: str, service_info_filter: windows_storage_streams.ImplementsIBuffer, /) -> str: ...

@typing.final
class WiFiDirectService(winrt.system.Object, metaclass=WiFiDirectService_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectService: ...
    def connect_async(self) -> windows_foundation.IAsyncOperation[WiFiDirectServiceSession]: ...
    def connect_async_with_pin(self, pin: str, /) -> windows_foundation.IAsyncOperation[WiFiDirectServiceSession]: ...
    def get_provisioning_info_async(self, selected_configuration_method: WiFiDirectServiceConfigurationMethod, /) -> windows_foundation.IAsyncOperation[WiFiDirectServiceProvisioningInfo]: ...
    def add_session_deferred(self, handler: windows_foundation.TypedEventHandler[WiFiDirectService, WiFiDirectServiceSessionDeferredEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_session_deferred(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def session_info(self) -> windows_storage_streams.IBuffer: ...
    @session_info.setter
    def session_info(self, value: windows_storage_streams.ImplementsIBuffer) -> None: ...
    @_property
    def prefer_group_owner_mode(self) -> bool: ...
    @prefer_group_owner_mode.setter
    def prefer_group_owner_mode(self, value: bool) -> None: ...
    @_property
    def remote_service_info(self) -> windows_storage_streams.IBuffer: ...
    @_property
    def service_error(self) -> WiFiDirectServiceError: ...
    @_property
    def supported_configuration_methods(self) -> typing.Sequence[WiFiDirectServiceConfigurationMethod]: ...

@typing.final
class WiFiDirectServiceAdvertiser(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceAdvertiser: ...
    def __new__(cls: typing.Type[Self], service_name: str) -> Self: ...
    def connect_async(self, device_info: windows_devices_enumeration.DeviceInformation, /) -> windows_foundation.IAsyncOperation[WiFiDirectServiceSession]: ...
    def connect_async_with_pin(self, device_info: windows_devices_enumeration.DeviceInformation, pin: str, /) -> windows_foundation.IAsyncOperation[WiFiDirectServiceSession]: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_advertisement_status_changed(self, handler: windows_foundation.TypedEventHandler[WiFiDirectServiceAdvertiser, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_advertisement_status_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_auto_accept_session_connected(self, handler: windows_foundation.TypedEventHandler[WiFiDirectServiceAdvertiser, WiFiDirectServiceAutoAcceptSessionConnectedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_auto_accept_session_connected(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_session_requested(self, handler: windows_foundation.TypedEventHandler[WiFiDirectServiceAdvertiser, WiFiDirectServiceSessionRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_session_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def service_status(self) -> WiFiDirectServiceStatus: ...
    @service_status.setter
    def service_status(self, value: WiFiDirectServiceStatus) -> None: ...
    @_property
    def service_info(self) -> windows_storage_streams.IBuffer: ...
    @service_info.setter
    def service_info(self, value: windows_storage_streams.ImplementsIBuffer) -> None: ...
    @_property
    def prefer_group_owner_mode(self) -> bool: ...
    @prefer_group_owner_mode.setter
    def prefer_group_owner_mode(self, value: bool) -> None: ...
    @_property
    def deferred_session_info(self) -> windows_storage_streams.IBuffer: ...
    @deferred_session_info.setter
    def deferred_session_info(self, value: windows_storage_streams.ImplementsIBuffer) -> None: ...
    @_property
    def custom_service_status_code(self) -> winrt.system.UInt32: ...
    @custom_service_status_code.setter
    def custom_service_status_code(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def auto_accept_session(self) -> bool: ...
    @auto_accept_session.setter
    def auto_accept_session(self, value: bool) -> None: ...
    @_property
    def service_error(self) -> WiFiDirectServiceError: ...
    @_property
    def preferred_configuration_methods(self) -> typing.MutableSequence[WiFiDirectServiceConfigurationMethod]: ...
    @_property
    def service_name(self) -> str: ...
    @_property
    def service_name_prefixes(self) -> typing.MutableSequence[str]: ...
    @_property
    def advertisement_status(self) -> WiFiDirectServiceAdvertisementStatus: ...

@typing.final
class WiFiDirectServiceAutoAcceptSessionConnectedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceAutoAcceptSessionConnectedEventArgs: ...
    @_property
    def session(self) -> WiFiDirectServiceSession: ...
    @_property
    def session_info(self) -> windows_storage_streams.IBuffer: ...

@typing.final
class WiFiDirectServiceProvisioningInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceProvisioningInfo: ...
    @_property
    def is_group_formation_needed(self) -> bool: ...
    @_property
    def selected_configuration_method(self) -> WiFiDirectServiceConfigurationMethod: ...

@typing.final
class WiFiDirectServiceRemotePortAddedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceRemotePortAddedEventArgs: ...
    @_property
    def endpoint_pairs(self) -> typing.Sequence[windows_networking.EndpointPair]: ...
    @_property
    def protocol(self) -> WiFiDirectServiceIPProtocol: ...

@typing.final
class WiFiDirectServiceSession(winrt.system.Object, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceSession: ...
    def add_datagram_socket_async(self, value: windows_networking_sockets.DatagramSocket, /) -> windows_foundation.IAsyncAction: ...
    def add_stream_socket_listener_async(self, value: windows_networking_sockets.StreamSocketListener, /) -> windows_foundation.IAsyncAction: ...
    def close(self) -> None: ...
    def get_connection_endpoint_pairs(self) -> typing.Sequence[windows_networking.EndpointPair]: ...
    def add_remote_port_added(self, handler: windows_foundation.TypedEventHandler[WiFiDirectServiceSession, WiFiDirectServiceRemotePortAddedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_remote_port_added(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_session_status_changed(self, handler: windows_foundation.TypedEventHandler[WiFiDirectServiceSession, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_session_status_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def advertisement_id(self) -> winrt.system.UInt32: ...
    @_property
    def error_status(self) -> WiFiDirectServiceSessionErrorStatus: ...
    @_property
    def service_address(self) -> str: ...
    @_property
    def service_name(self) -> str: ...
    @_property
    def session_address(self) -> str: ...
    @_property
    def session_id(self) -> winrt.system.UInt32: ...
    @_property
    def status(self) -> WiFiDirectServiceSessionStatus: ...

@typing.final
class WiFiDirectServiceSessionDeferredEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceSessionDeferredEventArgs: ...
    @_property
    def deferred_session_info(self) -> windows_storage_streams.IBuffer: ...

@typing.final
class WiFiDirectServiceSessionRequest(winrt.system.Object, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceSessionRequest: ...
    def close(self) -> None: ...
    @_property
    def device_information(self) -> windows_devices_enumeration.DeviceInformation: ...
    @_property
    def provisioning_info(self) -> WiFiDirectServiceProvisioningInfo: ...
    @_property
    def session_info(self) -> windows_storage_streams.IBuffer: ...

@typing.final
class WiFiDirectServiceSessionRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WiFiDirectServiceSessionRequestedEventArgs: ...
    def get_session_request(self) -> WiFiDirectServiceSessionRequest: ...

