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
import winrt.windows.storage
import winrt.windows.storage.streams

from winrt.windows.devices.humaninterfacedevice import HidCollectionType, HidReportType

Self = typing.TypeVar('Self')

class HidBooleanControl(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidBooleanControl: ...
    @_property
    def is_active(self) -> bool: ...
    @is_active.setter
    def is_active(self, value: bool) -> None: ...
    @_property
    def control_description(self) -> typing.Optional[HidBooleanControlDescription]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...

class HidBooleanControlDescription(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidBooleanControlDescription: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def parent_collections(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[HidCollection]]: ...
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

class HidDevice_Static(type):
    def from_id_async(cls, device_id: str, access_mode: winrt.windows.storage.FileAccessMode, /) -> winrt.windows.foundation.IAsyncOperation[HidDevice]: ...
    @typing.overload
    def get_device_selector(cls, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> str: ...
    @typing.overload
    def get_device_selector(cls, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, vendor_id: winrt.system.UInt16, product_id: winrt.system.UInt16, /) -> str: ...

class HidDevice(winrt.system.Object, metaclass=HidDevice_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidDevice: ...
    def close(self) -> None: ...
    @typing.overload
    def create_feature_report(self) -> typing.Optional[HidFeatureReport]: ...
    @typing.overload
    def create_feature_report(self, report_id: winrt.system.UInt16, /) -> typing.Optional[HidFeatureReport]: ...
    @typing.overload
    def create_output_report(self) -> typing.Optional[HidOutputReport]: ...
    @typing.overload
    def create_output_report(self, report_id: winrt.system.UInt16, /) -> typing.Optional[HidOutputReport]: ...
    def get_boolean_control_descriptions(self, report_type: HidReportType, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[HidBooleanControlDescription]]: ...
    @typing.overload
    def get_feature_report_async(self) -> winrt.windows.foundation.IAsyncOperation[HidFeatureReport]: ...
    @typing.overload
    def get_feature_report_async(self, report_id: winrt.system.UInt16, /) -> winrt.windows.foundation.IAsyncOperation[HidFeatureReport]: ...
    @typing.overload
    def get_input_report_async(self) -> winrt.windows.foundation.IAsyncOperation[HidInputReport]: ...
    @typing.overload
    def get_input_report_async(self, report_id: winrt.system.UInt16, /) -> winrt.windows.foundation.IAsyncOperation[HidInputReport]: ...
    def get_numeric_control_descriptions(self, report_type: HidReportType, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[HidNumericControlDescription]]: ...
    def send_feature_report_async(self, feature_report: typing.Optional[HidFeatureReport], /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.UInt32]: ...
    def send_output_report_async(self, output_report: typing.Optional[HidOutputReport], /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.UInt32]: ...
    def add_input_report_received(self, report_handler: winrt.windows.foundation.TypedEventHandler[HidDevice, HidInputReportReceivedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_input_report_received(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
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

class HidFeatureReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidFeatureReport: ...
    def get_boolean_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[HidBooleanControl]: ...
    def get_boolean_control_by_description(self, control_description: typing.Optional[HidBooleanControlDescription], /) -> typing.Optional[HidBooleanControl]: ...
    def get_numeric_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[HidNumericControl]: ...
    def get_numeric_control_by_description(self, control_description: typing.Optional[HidNumericControlDescription], /) -> typing.Optional[HidNumericControl]: ...
    @_property
    def data(self) -> typing.Optional[winrt.windows.storage.streams.IBuffer]: ...
    @data.setter
    def data(self, value: typing.Optional[winrt.windows.storage.streams.IBuffer]) -> None: ...
    @_property
    def id(self) -> winrt.system.UInt16: ...

class HidInputReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidInputReport: ...
    def get_boolean_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[HidBooleanControl]: ...
    def get_boolean_control_by_description(self, control_description: typing.Optional[HidBooleanControlDescription], /) -> typing.Optional[HidBooleanControl]: ...
    def get_numeric_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[HidNumericControl]: ...
    def get_numeric_control_by_description(self, control_description: typing.Optional[HidNumericControlDescription], /) -> typing.Optional[HidNumericControl]: ...
    @_property
    def activated_boolean_controls(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[HidBooleanControl]]: ...
    @_property
    def data(self) -> typing.Optional[winrt.windows.storage.streams.IBuffer]: ...
    @_property
    def id(self) -> winrt.system.UInt16: ...
    @_property
    def transitioned_boolean_controls(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[HidBooleanControl]]: ...

class HidInputReportReceivedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidInputReportReceivedEventArgs: ...
    @_property
    def report(self) -> typing.Optional[HidInputReport]: ...

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
    def control_description(self) -> typing.Optional[HidNumericControlDescription]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def is_grouped(self) -> bool: ...
    @_property
    def usage_id(self) -> winrt.system.UInt16: ...
    @_property
    def usage_page(self) -> winrt.system.UInt16: ...

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
    def parent_collections(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[HidCollection]]: ...
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

class HidOutputReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HidOutputReport: ...
    def get_boolean_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[HidBooleanControl]: ...
    def get_boolean_control_by_description(self, control_description: typing.Optional[HidBooleanControlDescription], /) -> typing.Optional[HidBooleanControl]: ...
    def get_numeric_control(self, usage_page: winrt.system.UInt16, usage_id: winrt.system.UInt16, /) -> typing.Optional[HidNumericControl]: ...
    def get_numeric_control_by_description(self, control_description: typing.Optional[HidNumericControlDescription], /) -> typing.Optional[HidNumericControl]: ...
    @_property
    def data(self) -> typing.Optional[winrt.windows.storage.streams.IBuffer]: ...
    @data.setter
    def data(self, value: typing.Optional[winrt.windows.storage.streams.IBuffer]) -> None: ...
    @_property
    def id(self) -> winrt.system.UInt16: ...
