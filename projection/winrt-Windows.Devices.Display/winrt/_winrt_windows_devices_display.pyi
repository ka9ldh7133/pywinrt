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
import winrt.windows.graphics

from winrt.windows.devices.display import DisplayMonitorConnectionKind, DisplayMonitorDescriptorKind, DisplayMonitorPhysicalConnectorKind, DisplayMonitorUsageKind

Self = typing.TypeVar('Self')

class DisplayMonitor_Static(type):
    def from_id_async(cls, device_id: str, /) -> winrt.windows.foundation.IAsyncOperation[DisplayMonitor]: ...
    def from_interface_id_async(cls, device_interface_id: str, /) -> winrt.windows.foundation.IAsyncOperation[DisplayMonitor]: ...
    def get_device_selector(cls) -> str: ...

class DisplayMonitor(winrt.system.Object, metaclass=DisplayMonitor_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DisplayMonitor: ...
    def get_descriptor(self, descriptor_kind: DisplayMonitorDescriptorKind, /) -> winrt.system.UInt8: ...
    @_property
    def blue_primary(self) -> winrt.windows.foundation.Point: ...
    @_property
    def connection_kind(self) -> DisplayMonitorConnectionKind: ...
    @_property
    def device_id(self) -> str: ...
    @_property
    def display_adapter_device_id(self) -> str: ...
    @_property
    def display_adapter_id(self) -> winrt.windows.graphics.DisplayAdapterId: ...
    @_property
    def display_adapter_target_id(self) -> winrt.system.UInt32: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def green_primary(self) -> winrt.windows.foundation.Point: ...
    @_property
    def max_average_full_frame_luminance_in_nits(self) -> winrt.system.Single: ...
    @_property
    def max_luminance_in_nits(self) -> winrt.system.Single: ...
    @_property
    def min_luminance_in_nits(self) -> winrt.system.Single: ...
    @_property
    def native_resolution_in_raw_pixels(self) -> winrt.windows.graphics.SizeInt32: ...
    @_property
    def physical_connector(self) -> DisplayMonitorPhysicalConnectorKind: ...
    @_property
    def physical_size_in_inches(self) -> typing.Optional[typing.Optional[winrt.windows.foundation.Size]]: ...
    @_property
    def raw_dpi_x(self) -> winrt.system.Single: ...
    @_property
    def raw_dpi_y(self) -> winrt.system.Single: ...
    @_property
    def red_primary(self) -> winrt.windows.foundation.Point: ...
    @_property
    def usage_kind(self) -> DisplayMonitorUsageKind: ...
    @_property
    def white_point(self) -> winrt.windows.foundation.Point: ...
    @_property
    def is_dolby_vision_supported_in_hdr_mode(self) -> bool: ...
