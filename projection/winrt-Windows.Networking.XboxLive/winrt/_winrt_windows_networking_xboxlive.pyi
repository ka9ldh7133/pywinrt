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
import winrt.windows.networking as windows_networking
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.networking.xboxlive import XboxLiveEndpointPairCreationBehaviors, XboxLiveEndpointPairCreationStatus, XboxLiveEndpointPairState, XboxLiveNetworkAccessKind, XboxLiveQualityOfServiceMeasurementStatus, XboxLiveQualityOfServiceMetric, XboxLiveSocketKind

Self = typing.TypeVar('Self')

@typing.final
class XboxLiveDeviceAddress_Static(type):
    def create_from_snapshot_base64(cls, base64: str, /) -> XboxLiveDeviceAddress: ...
    def create_from_snapshot_buffer(cls, buffer: windows_storage_streams.ImplementsIBuffer, /) -> XboxLiveDeviceAddress: ...
    def create_from_snapshot_bytes(cls, buffer: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.ReadableBuffer], /) -> XboxLiveDeviceAddress: ...
    def get_local(cls) -> XboxLiveDeviceAddress: ...
    @_property
    def max_snapshot_bytes_size(cls) -> winrt.system.UInt32: ...

@typing.final
class XboxLiveDeviceAddress(winrt.system.Object, metaclass=XboxLiveDeviceAddress_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveDeviceAddress: ...
    def compare(self, other_device_address: XboxLiveDeviceAddress, /) -> winrt.system.Int32: ...
    def get_snapshot_as_base64(self) -> str: ...
    def get_snapshot_as_buffer(self) -> windows_storage_streams.IBuffer: ...
    def get_snapshot_as_bytes(self, buffer: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.WriteableBuffer], /) -> winrt.system.UInt32: ...
    def add_snapshot_changed(self, handler: windows_foundation.TypedEventHandler[XboxLiveDeviceAddress, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_snapshot_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def is_local(self) -> bool: ...
    @_property
    def is_valid(self) -> bool: ...
    @_property
    def network_access_kind(self) -> XboxLiveNetworkAccessKind: ...

@typing.final
class XboxLiveEndpointPair_Static(type):
    def find_endpoint_pair_by_host_names_and_ports(cls, local_host_name: windows_networking.HostName, local_port: str, remote_host_name: windows_networking.HostName, remote_port: str, /) -> XboxLiveEndpointPair: ...
    def find_endpoint_pair_by_socket_address_bytes(cls, local_socket_address: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.ReadableBuffer], remote_socket_address: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.ReadableBuffer], /) -> XboxLiveEndpointPair: ...

@typing.final
class XboxLiveEndpointPair(winrt.system.Object, metaclass=XboxLiveEndpointPair_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveEndpointPair: ...
    def delete_async(self) -> windows_foundation.IAsyncAction: ...
    def get_local_socket_address_bytes(self, socket_address: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.WriteableBuffer], /) -> None: ...
    def get_remote_socket_address_bytes(self, socket_address: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.WriteableBuffer], /) -> None: ...
    def add_state_changed(self, handler: windows_foundation.TypedEventHandler[XboxLiveEndpointPair, XboxLiveEndpointPairStateChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_state_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def local_host_name(self) -> windows_networking.HostName: ...
    @_property
    def local_port(self) -> str: ...
    @_property
    def remote_device_address(self) -> XboxLiveDeviceAddress: ...
    @_property
    def remote_host_name(self) -> windows_networking.HostName: ...
    @_property
    def remote_port(self) -> str: ...
    @_property
    def state(self) -> XboxLiveEndpointPairState: ...
    @_property
    def template(self) -> XboxLiveEndpointPairTemplate: ...

@typing.final
class XboxLiveEndpointPairCreationResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveEndpointPairCreationResult: ...
    @_property
    def device_address(self) -> XboxLiveDeviceAddress: ...
    @_property
    def endpoint_pair(self) -> XboxLiveEndpointPair: ...
    @_property
    def is_existing_path_evaluation(self) -> bool: ...
    @_property
    def status(self) -> XboxLiveEndpointPairCreationStatus: ...

@typing.final
class XboxLiveEndpointPairStateChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveEndpointPairStateChangedEventArgs: ...
    @_property
    def new_state(self) -> XboxLiveEndpointPairState: ...
    @_property
    def old_state(self) -> XboxLiveEndpointPairState: ...

@typing.final
class XboxLiveEndpointPairTemplate_Static(type):
    def get_template_by_name(cls, name: str, /) -> XboxLiveEndpointPairTemplate: ...
    @_property
    def templates(cls) -> typing.Sequence[XboxLiveEndpointPairTemplate]: ...

@typing.final
class XboxLiveEndpointPairTemplate(winrt.system.Object, metaclass=XboxLiveEndpointPairTemplate_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveEndpointPairTemplate: ...
    def create_endpoint_pair_default_async(self, device_address: XboxLiveDeviceAddress, /) -> windows_foundation.IAsyncOperation[XboxLiveEndpointPairCreationResult]: ...
    def create_endpoint_pair_for_ports_default_async(self, device_address: XboxLiveDeviceAddress, initiator_port: str, acceptor_port: str, /) -> windows_foundation.IAsyncOperation[XboxLiveEndpointPairCreationResult]: ...
    def create_endpoint_pair_for_ports_with_behaviors_async(self, device_address: XboxLiveDeviceAddress, initiator_port: str, acceptor_port: str, behaviors: XboxLiveEndpointPairCreationBehaviors, /) -> windows_foundation.IAsyncOperation[XboxLiveEndpointPairCreationResult]: ...
    def create_endpoint_pair_with_behaviors_async(self, device_address: XboxLiveDeviceAddress, behaviors: XboxLiveEndpointPairCreationBehaviors, /) -> windows_foundation.IAsyncOperation[XboxLiveEndpointPairCreationResult]: ...
    def add_inbound_endpoint_pair_created(self, handler: windows_foundation.TypedEventHandler[XboxLiveEndpointPairTemplate, XboxLiveInboundEndpointPairCreatedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_inbound_endpoint_pair_created(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def acceptor_bound_port_range_lower(self) -> winrt.system.UInt16: ...
    @_property
    def acceptor_bound_port_range_upper(self) -> winrt.system.UInt16: ...
    @_property
    def endpoint_pairs(self) -> typing.Sequence[XboxLiveEndpointPair]: ...
    @_property
    def initiator_bound_port_range_lower(self) -> winrt.system.UInt16: ...
    @_property
    def initiator_bound_port_range_upper(self) -> winrt.system.UInt16: ...
    @_property
    def name(self) -> str: ...
    @_property
    def socket_kind(self) -> XboxLiveSocketKind: ...

@typing.final
class XboxLiveInboundEndpointPairCreatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveInboundEndpointPairCreatedEventArgs: ...
    @_property
    def endpoint_pair(self) -> XboxLiveEndpointPair: ...

@typing.final
class XboxLiveQualityOfServiceMeasurement_Static(type):
    def clear_private_payload(cls) -> None: ...
    def publish_private_payload_bytes(cls, payload: typing.Union[winrt.system.Array[winrt.system.UInt8], winrt.system.ReadableBuffer], /) -> None: ...
    @_property
    def published_private_payload(cls) -> windows_storage_streams.IBuffer: ...
    @published_private_payload.setter
    def published_private_payload(cls, value: windows_storage_streams.ImplementsIBuffer) -> None: ...
    @_property
    def max_simultaneous_probe_connections(cls) -> winrt.system.UInt32: ...
    @max_simultaneous_probe_connections.setter
    def max_simultaneous_probe_connections(cls, value: winrt.system.UInt32) -> None: ...
    @_property
    def is_system_outbound_bandwidth_constrained(cls) -> bool: ...
    @is_system_outbound_bandwidth_constrained.setter
    def is_system_outbound_bandwidth_constrained(cls, value: bool) -> None: ...
    @_property
    def is_system_inbound_bandwidth_constrained(cls) -> bool: ...
    @is_system_inbound_bandwidth_constrained.setter
    def is_system_inbound_bandwidth_constrained(cls, value: bool) -> None: ...
    @_property
    def max_private_payload_size(cls) -> winrt.system.UInt32: ...

@typing.final
class XboxLiveQualityOfServiceMeasurement(winrt.system.Object, metaclass=XboxLiveQualityOfServiceMeasurement_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveQualityOfServiceMeasurement: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def get_metric_result(self, device_address: XboxLiveDeviceAddress, metric: XboxLiveQualityOfServiceMetric, /) -> XboxLiveQualityOfServiceMetricResult: ...
    def get_metric_results_for_device(self, device_address: XboxLiveDeviceAddress, /) -> typing.Sequence[XboxLiveQualityOfServiceMetricResult]: ...
    def get_metric_results_for_metric(self, metric: XboxLiveQualityOfServiceMetric, /) -> typing.Sequence[XboxLiveQualityOfServiceMetricResult]: ...
    def get_private_payload_result(self, device_address: XboxLiveDeviceAddress, /) -> XboxLiveQualityOfServicePrivatePayloadResult: ...
    def measure_async(self) -> windows_foundation.IAsyncAction: ...
    @_property
    def timeout_in_milliseconds(self) -> winrt.system.UInt32: ...
    @timeout_in_milliseconds.setter
    def timeout_in_milliseconds(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def should_request_private_payloads(self) -> bool: ...
    @should_request_private_payloads.setter
    def should_request_private_payloads(self, value: bool) -> None: ...
    @_property
    def number_of_probes_to_attempt(self) -> winrt.system.UInt32: ...
    @number_of_probes_to_attempt.setter
    def number_of_probes_to_attempt(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def device_addresses(self) -> typing.MutableSequence[XboxLiveDeviceAddress]: ...
    @_property
    def metric_results(self) -> typing.Sequence[XboxLiveQualityOfServiceMetricResult]: ...
    @_property
    def metrics(self) -> typing.MutableSequence[XboxLiveQualityOfServiceMetric]: ...
    @_property
    def number_of_results_pending(self) -> winrt.system.UInt32: ...
    @_property
    def private_payload_results(self) -> typing.Sequence[XboxLiveQualityOfServicePrivatePayloadResult]: ...

@typing.final
class XboxLiveQualityOfServiceMetricResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveQualityOfServiceMetricResult: ...
    @_property
    def device_address(self) -> XboxLiveDeviceAddress: ...
    @_property
    def metric(self) -> XboxLiveQualityOfServiceMetric: ...
    @_property
    def status(self) -> XboxLiveQualityOfServiceMeasurementStatus: ...
    @_property
    def value(self) -> winrt.system.UInt64: ...

@typing.final
class XboxLiveQualityOfServicePrivatePayloadResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> XboxLiveQualityOfServicePrivatePayloadResult: ...
    @_property
    def device_address(self) -> XboxLiveDeviceAddress: ...
    @_property
    def status(self) -> XboxLiveQualityOfServiceMeasurementStatus: ...
    @_property
    def value(self) -> windows_storage_streams.IBuffer: ...

