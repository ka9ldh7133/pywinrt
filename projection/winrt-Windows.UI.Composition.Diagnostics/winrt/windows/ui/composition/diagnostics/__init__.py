# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_ui_composition_diagnostics

class CompositionDebugOverdrawContentKinds(enum.IntFlag):
    NONE = 0
    OFFSCREEN_RENDERED = 0x1
    COLORS = 0x2
    EFFECTS = 0x4
    SHADOWS = 0x8
    LIGHTS = 0x10
    SURFACES = 0x20
    SWAP_CHAINS = 0x40
    ALL = 0xffffffff

CompositionDebugHeatMaps = _winrt_windows_ui_composition_diagnostics.CompositionDebugHeatMaps
CompositionDebugSettings = _winrt_windows_ui_composition_diagnostics.CompositionDebugSettings