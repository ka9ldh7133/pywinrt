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
import winrt.windows.storage as windows_storage
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.devices.humaninterfacedevice import HidCollectionType, HidReportType

Self = typing.TypeVar('Self')

@typing.final
class HidBooleanControl(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidBooleanControl: ...
    @_property
    def is_active(self) -> bool: ...
    @is_active.setter
    def is_active(self, value: bool) -> None: ...
    @_property
    def control_description(self) -> HidBooleanControlDescription: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...

@typing.final
class HidBooleanControlDescription(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidBooleanControlDescription: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def parent_collections(self) -> typing.Sequence[HidCollection]: ...
    @_property
    def report_id(self) -> winrt.system.UInt16: ...
    @_property
    def report_type(self) -> HidReportType: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...
    @_property
    def is_absolute(self) -> bool: ...

@typing.final
class HidCollection(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidCollection: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def type(self) -> HidCollectionType: ...
    @_property
    def usage_id(self) -> winrt.system.UInt32: ...
    @_property
    def usage_page(self) -> winrt.system.UInt32: ...

@typing.final
class HidDevice_Static(type):
    def from_id_async(cls, device_id: str, access_mode: windows_storage.FileAccessMode, /) -> windows_foundation.IAsyncOperation[HidDevice]: ...
    def get_device_selector(cls, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> str: ...
    def get_device_selector_vid_pid(cls, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, vendor_id: winrt.system.UInt16, product_id: winrt.system.UInt16, /) -> str: ...

@typing.final
class HidDevice(winrt.system.Object, windows_foundation.ImplementsIClosable, metaclass=HidDevice_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidDevice: ...
    def close(self) -> None: ...
    def create_feature_report(self) -> HidFeatureReport: ...
    def create_feature_report_by_id(self, report_id: winrt.system.UInt16, /) -> HidFeatureReport: ...
    def create_output_report(self) -> HidOutputReport: ...
    def create_output_report_by_id(self, report_id: winrt.system.UInt16, /) -> HidOutputReport: ...
    def get_boolean_control_descriptions(self, report_type: HidReportType, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Sequence[HidBooleanControlDescription]: ...
    def get_feature_report_async(self) -> windows_foundation.IAsyncOperation[HidFeatureReport]: ...
    def get_feature_report_by_id_async(self, report_id: winrt.system.UInt16, /) -> windows_foundation.IAsyncOperation[HidFeatureReport]: ...
    def get_input_report_async(self) -> windows_foundation.IAsyncOperation[HidInputReport]: ...
    def get_input_report_by_id_async(self, report_id: winrt.system.UInt16, /) -> windows_foundation.IAsyncOperation[HidInputReport]: ...
    def get_numeric_control_descriptions(self, report_type: HidReportType, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Sequence[HidNumericControlDescription]: ...
    def send_feature_report_async(self, feature_report: HidFeatureReport, /) -> windows_foundation.IAsyncOperation[winrt.system.UInt32]: ...
    def send_output_report_async(self, output_report: HidOutputReport, /) -> windows_foundation.IAsyncOperation[winrt.system.UInt32]: ...
    def add_input_report_received(self, report_handler: windows_foundation.TypedEventHandler[HidDevice, HidInputReportReceivedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_input_report_received(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def product_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...
    @_property
    def vendor_id(self) -> winrt.system.UInt16: ...
    @_property
    def version(self) -> winrt.system.UInt16: ...

@typing.final
class HidFeatureReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidFeatureReport: ...
    def get_boolean_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> HidBooleanControl: ...
    def get_boolean_control_by_description(self, control_description: HidBooleanControlDescription, /) -> HidBooleanControl: ...
    def get_numeric_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> HidNumericControl: ...
    def get_numeric_control_by_description(self, control_description: HidNumericControlDescription, /) -> HidNumericControl: ...
    @_property
    def data(self) -> windows_storage_streams.IBuffer: ...
    @data.setter
    def data(self, value: windows_storage_streams.ImplementsIBuffer) -> None: ...
    @_property
    def id(self) -> winrt.system.UInt16: ...

@typing.final
class HidInputReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidInputReport: ...
    def get_boolean_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> HidBooleanControl: ...
    def get_boolean_control_by_description(self, control_description: HidBooleanControlDescription, /) -> HidBooleanControl: ...
    def get_numeric_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> HidNumericControl: ...
    def get_numeric_control_by_description(self, control_description: HidNumericControlDescription, /) -> HidNumericControl: ...
    @_property
    def activated_boolean_controls(self) -> typing.Sequence[HidBooleanControl]: ...
    @_property
    def data(self) -> windows_storage_streams.IBuffer: ...
    @_property
    def id(self) -> winrt.system.UInt16: ...
    @_property
    def transitioned_boolean_controls(self) -> typing.Sequence[HidBooleanControl]: ...

@typing.final
class HidInputReportReceivedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidInputReportReceivedEventArgs: ...
    @_property
    def report(self) -> HidInputReport: ...

@typing.final
class HidNumericControl(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidNumericControl: ...
    @_property
    def value(self) -> winrt.system.Int64: ...
    @value.setter
    def value(self, value: winrt.system.Int64) -> None: ...
    @_property
    def scaled_value(self) -> winrt.system.Int64: ...
    @scaled_value.setter
    def scaled_value(self, value: winrt.system.Int64) -> None: ...
    @_property
    def control_description(self) -> HidNumericControlDescription: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def is_grouped(self) -> bool: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...

@typing.final
class HidNumericControlDescription(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidNumericControlDescription: ...
    @_property
    def has_null(self) -> bool: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def is_absolute(self) -> bool: ...
    @_property
    def logical_maximum(self) -> winrt.system.Int32: ...
    @_property
    def logical_minimum(self) -> winrt.system.Int32: ...
    @_property
    def parent_collections(self) -> typing.Sequence[HidCollection]: ...
    @_property
    def physical_maximum(self) -> winrt.system.Int32: ...
    @_property
    def physical_minimum(self) -> winrt.system.Int32: ...
    @_property
    def report_count(self) -> winrt.system.UInt32: ...
    @_property
    def report_id(self) -> winrt.system.UInt16: ...
    @_property
    def report_size(self) -> winrt.system.UInt32: ...
    @_property
    def report_type(self) -> HidReportType: ...
    @_property
    def unit(self) -> winrt.system.UInt32: ...
    @_property
    def unit_exponent(self) -> winrt.system.UInt32: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...

@typing.final
class HidOutputReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidOutputReport: ...
    def get_boolean_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> HidBooleanControl: ...
    def get_boolean_control_by_description(self, control_description: HidBooleanControlDescription, /) -> HidBooleanControl: ...
    def get_numeric_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> HidNumericControl: ...
    def get_numeric_control_by_description(self, control_description: HidNumericControlDescription, /) -> HidNumericControl: ...
    @_property
    def data(self) -> windows_storage_streams.IBuffer: ...
    @data.setter
    def data(self, value: windows_storage_streams.ImplementsIBuffer) -> None: ...
    @_property
    def id(self) -> winrt.system.UInt16: ...

