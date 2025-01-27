# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.microsoft.ui.composition as microsoft_ui_composition
import winrt.microsoft.ui.xaml.controls as microsoft_ui_xaml_controls
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.ui as windows_ui

Self = typing.TypeVar('Self')

@typing.final
class AnimatedAcceptVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedAcceptVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedBackVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedBackVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedChevronDownSmallVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedChevronDownSmallVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedChevronRightDownSmallVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedChevronRightDownSmallVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedChevronUpDownSmallVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedChevronUpDownSmallVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedFindVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedFindVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedGlobalNavigationButtonVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedGlobalNavigationButtonVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

@typing.final
class AnimatedSettingsVisualSource(winrt.system.Object, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource2, microsoft_ui_xaml_controls.ImplementsIAnimatedVisualSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimatedSettingsVisualSource: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    def set_color_property(self, property_name: str, value: windows_ui.Color, /) -> None: ...
    def try_create_animated_visual(self, compositor: microsoft_ui_composition.Compositor, /) -> typing.Tuple[microsoft_ui_xaml_controls.IAnimatedVisual, winrt.system.Object]: ...
    @_property
    def markers(self) -> typing.Mapping[str, winrt.system.Double]: ...

