# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.pwm.provider as windows_devices_pwm_provider
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections

from winrt.windows.devices.pwm import PwmPulsePolarity

Self = typing.TypeVar('Self')

@typing.final
class PwmController_Static(type):
    def from_id_async(cls, device_id: str, /) -> windows_foundation.IAsyncOperation[PwmController]: ...
    def get_controllers_async(cls, provider: windows_devices_pwm_provider.ImplementsIPwmProvider, /) -> windows_foundation.IAsyncOperation[typing.Sequence[PwmController]]: ...
    def get_default_async(cls) -> windows_foundation.IAsyncOperation[PwmController]: ...
    def get_device_selector(cls) -> str: ...
    def get_device_selector_from_friendly_name(cls, friendly_name: str, /) -> str: ...

@typing.final
class PwmController(winrt.system.Object, metaclass=PwmController_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PwmController: ...
    def open_pin(self, pin_number: winrt.system.Int32, /) -> PwmPin: ...
    def set_desired_frequency(self, desired_frequency: winrt.system.Double, /) -> winrt.system.Double: ...
    @_property
    def actual_frequency(self) -> winrt.system.Double: ...
    @_property
    def max_frequency(self) -> winrt.system.Double: ...
    @_property
    def min_frequency(self) -> winrt.system.Double: ...
    @_property
    def pin_count(self) -> winrt.system.Int32: ...

@typing.final
class PwmPin(winrt.system.Object, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PwmPin: ...
    def close(self) -> None: ...
    def get_active_duty_cycle_percentage(self) -> winrt.system.Double: ...
    def set_active_duty_cycle_percentage(self, duty_cycle_percentage: winrt.system.Double, /) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @_property
    def polarity(self) -> PwmPulsePolarity: ...
    @polarity.setter
    def polarity(self, value: PwmPulsePolarity) -> None: ...
    @_property
    def controller(self) -> PwmController: ...
    @_property
    def is_started(self) -> bool: ...

