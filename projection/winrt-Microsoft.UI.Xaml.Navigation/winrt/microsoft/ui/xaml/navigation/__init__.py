# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import typing
import uuid as _uuid

import winrt.system
from winrt import _winrt_microsoft_ui_xaml_navigation

__all__ = [
    "NavigationCacheMode",
    "NavigationMode",
    "FrameNavigationOptions",
    "NavigatingCancelEventArgs",
    "NavigationEventArgs",
    "NavigationFailedEventArgs",
    "PageStackEntry",
    "NavigatedEventHandler",
    "NavigatingCancelEventHandler",
    "NavigationFailedEventHandler",
    "NavigationStoppedEventHandler",
]

class NavigationCacheMode(enum.IntEnum):
    DISABLED = 0
    REQUIRED = 1
    ENABLED = 2

class NavigationMode(enum.IntEnum):
    NEW = 0
    BACK = 1
    FORWARD = 2
    REFRESH = 3

FrameNavigationOptions = _winrt_microsoft_ui_xaml_navigation.FrameNavigationOptions
NavigatingCancelEventArgs = _winrt_microsoft_ui_xaml_navigation.NavigatingCancelEventArgs
NavigationEventArgs = _winrt_microsoft_ui_xaml_navigation.NavigationEventArgs
NavigationFailedEventArgs = _winrt_microsoft_ui_xaml_navigation.NavigationFailedEventArgs
PageStackEntry = _winrt_microsoft_ui_xaml_navigation.PageStackEntry
NavigatedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[NavigationEventArgs]], None]
NavigatingCancelEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[NavigatingCancelEventArgs]], None]
NavigationFailedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[NavigationFailedEventArgs]], None]
NavigationStoppedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[NavigationEventArgs]], None]