# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.ui.composition

Self = typing.TypeVar('Self')

class PalmRejectionDelayZonePreview(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PalmRejectionDelayZonePreview: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create_for_visual(input_panel_visual: typing.Optional[winrt.windows.ui.composition.Visual], input_panel_rect: winrt.windows.foundation.Rect, /) -> typing.Optional[PalmRejectionDelayZonePreview]: ...
    @typing.overload
    @staticmethod
    def create_for_visual(input_panel_visual: typing.Optional[winrt.windows.ui.composition.Visual], input_panel_rect: winrt.windows.foundation.Rect, viewport_visual: typing.Optional[winrt.windows.ui.composition.Visual], viewport_rect: winrt.windows.foundation.Rect, /) -> typing.Optional[PalmRejectionDelayZonePreview]: ...
