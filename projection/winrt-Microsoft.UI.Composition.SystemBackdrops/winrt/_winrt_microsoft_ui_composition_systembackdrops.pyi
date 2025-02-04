# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.microsoft.ui as microsoft_ui
import winrt.microsoft.ui.composition as microsoft_ui_composition
import winrt.windows.foundation as windows_foundation
import winrt.windows.ui as windows_ui
import winrt.windows.ui.composition as windows_ui_composition
import winrt.windows.ui.core as windows_ui_core

from winrt.microsoft.ui.composition.systembackdrops import DesktopAcrylicKind, MicaKind, SystemBackdropState, SystemBackdropTheme

Self = typing.TypeVar('Self')

@typing.final
class DesktopAcrylicController_Static(type):
    def is_supported(cls) -> bool: ...

@typing.final
class DesktopAcrylicController(winrt.system.Object, microsoft_ui.ImplementsIClosableNotifier, ImplementsISystemBackdropControllerWithTargets, ImplementsISystemBackdropController, windows_foundation.ImplementsIClosable, metaclass=DesktopAcrylicController_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DesktopAcrylicController: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def add_system_backdrop_target(self, system_backdrop_target: microsoft_ui_composition.ImplementsICompositionSupportsSystemBackdrop, /) -> bool: ...
    def close(self) -> None: ...
    def remove_all_system_backdrop_targets(self) -> None: ...
    def remove_system_backdrop_target(self, system_backdrop_target: microsoft_ui_composition.ImplementsICompositionSupportsSystemBackdrop, /) -> bool: ...
    def reset_properties(self) -> None: ...
    def set_system_backdrop_configuration(self, configuration: SystemBackdropConfiguration, /) -> None: ...
    def set_target_with_core_window(self, core_window: windows_ui_core.CoreWindow, composition_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def set_target_with_window_id(self, window_id: microsoft_ui.WindowId, desktop_window_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def add_state_changed(self, handler: windows_foundation.TypedEventHandler[ISystemBackdropControllerWithTargets, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_state_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_closed(self, handler: microsoft_ui.ClosableNotifierHandler, /) -> windows_foundation.EventRegistrationToken: ...
    def remove_closed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_framework_closed(self, handler: microsoft_ui.ClosableNotifierHandler, /) -> windows_foundation.EventRegistrationToken: ...
    def remove_framework_closed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def tint_opacity(self) -> winrt.system.Single: ...
    @tint_opacity.setter
    def tint_opacity(self, value: winrt.system.Single) -> None: ...
    @_property
    def tint_color(self) -> windows_ui.Color: ...
    @tint_color.setter
    def tint_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def luminosity_opacity(self) -> winrt.system.Single: ...
    @luminosity_opacity.setter
    def luminosity_opacity(self, value: winrt.system.Single) -> None: ...
    @_property
    def fallback_color(self) -> windows_ui.Color: ...
    @fallback_color.setter
    def fallback_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def kind(self) -> DesktopAcrylicKind: ...
    @kind.setter
    def kind(self, value: DesktopAcrylicKind) -> None: ...
    @_property
    def state(self) -> SystemBackdropState: ...
    @_property
    def is_closed(self) -> bool: ...

@typing.final
class MicaController_Static(type):
    def is_supported(cls) -> bool: ...

@typing.final
class MicaController(winrt.system.Object, microsoft_ui.ImplementsIClosableNotifier, ImplementsISystemBackdropControllerWithTargets, ImplementsISystemBackdropController, windows_foundation.ImplementsIClosable, metaclass=MicaController_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MicaController: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def add_system_backdrop_target(self, system_backdrop_target: microsoft_ui_composition.ImplementsICompositionSupportsSystemBackdrop, /) -> bool: ...
    def close(self) -> None: ...
    def remove_all_system_backdrop_targets(self) -> None: ...
    def remove_system_backdrop_target(self, system_backdrop_target: microsoft_ui_composition.ImplementsICompositionSupportsSystemBackdrop, /) -> bool: ...
    def reset_properties(self) -> None: ...
    def set_system_backdrop_configuration(self, configuration: SystemBackdropConfiguration, /) -> None: ...
    def set_target_with_core_window(self, core_window: windows_ui_core.CoreWindow, composition_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def set_target_with_window_id(self, window_id: microsoft_ui.WindowId, desktop_window_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def add_state_changed(self, handler: windows_foundation.TypedEventHandler[ISystemBackdropControllerWithTargets, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_state_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_closed(self, handler: microsoft_ui.ClosableNotifierHandler, /) -> windows_foundation.EventRegistrationToken: ...
    def remove_closed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_framework_closed(self, handler: microsoft_ui.ClosableNotifierHandler, /) -> windows_foundation.EventRegistrationToken: ...
    def remove_framework_closed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def tint_opacity(self) -> winrt.system.Single: ...
    @tint_opacity.setter
    def tint_opacity(self, value: winrt.system.Single) -> None: ...
    @_property
    def tint_color(self) -> windows_ui.Color: ...
    @tint_color.setter
    def tint_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def luminosity_opacity(self) -> winrt.system.Single: ...
    @luminosity_opacity.setter
    def luminosity_opacity(self, value: winrt.system.Single) -> None: ...
    @_property
    def fallback_color(self) -> windows_ui.Color: ...
    @fallback_color.setter
    def fallback_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def kind(self) -> MicaKind: ...
    @kind.setter
    def kind(self, value: MicaKind) -> None: ...
    @_property
    def state(self) -> SystemBackdropState: ...
    @_property
    def is_closed(self) -> bool: ...

@typing.final
class SystemBackdropConfiguration(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SystemBackdropConfiguration: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def theme(self) -> SystemBackdropTheme: ...
    @theme.setter
    def theme(self, value: SystemBackdropTheme) -> None: ...
    @_property
    def is_input_active(self) -> bool: ...
    @is_input_active.setter
    def is_input_active(self, value: bool) -> None: ...
    @_property
    def is_high_contrast(self) -> bool: ...
    @is_high_contrast.setter
    def is_high_contrast(self, value: bool) -> None: ...
    @_property
    def high_contrast_background_color(self) -> typing.Optional[windows_ui.Color]: ...
    @high_contrast_background_color.setter
    def high_contrast_background_color(self, value: typing.Optional[windows_ui.Color]) -> None: ...

class ImplementsISystemBackdropController():
    pass

@typing.final
class ISystemBackdropController(winrt.system.Object, ImplementsISystemBackdropController, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISystemBackdropController: ...
    def close(self) -> None: ...
    def set_target_with_core_window(self, core_window: windows_ui_core.CoreWindow, composition_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def set_target_with_window_id(self, window_id: microsoft_ui.WindowId, desktop_window_target: windows_ui_composition.CompositionTarget, /) -> bool: ...

class ImplementsISystemBackdropControllerWithTargets():
    pass

@typing.final
class ISystemBackdropControllerWithTargets(winrt.system.Object, ImplementsISystemBackdropControllerWithTargets, ImplementsISystemBackdropController, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISystemBackdropControllerWithTargets: ...
    def add_system_backdrop_target(self, system_backdrop_target: microsoft_ui_composition.ImplementsICompositionSupportsSystemBackdrop, /) -> bool: ...
    def close(self) -> None: ...
    def remove_all_system_backdrop_targets(self) -> None: ...
    def remove_system_backdrop_target(self, system_backdrop_target: microsoft_ui_composition.ImplementsICompositionSupportsSystemBackdrop, /) -> bool: ...
    def set_system_backdrop_configuration(self, configuration: SystemBackdropConfiguration, /) -> None: ...
    def set_target_with_core_window(self, core_window: windows_ui_core.CoreWindow, composition_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def set_target_with_window_id(self, window_id: microsoft_ui.WindowId, desktop_window_target: windows_ui_composition.CompositionTarget, /) -> bool: ...
    def add_state_changed(self, handler: windows_foundation.TypedEventHandler[ISystemBackdropControllerWithTargets, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_state_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def state(self) -> SystemBackdropState: ...

