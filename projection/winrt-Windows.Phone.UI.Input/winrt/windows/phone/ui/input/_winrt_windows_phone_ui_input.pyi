# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation

Self = typing.TypeVar('Self')

class BackPressedEventArgs(winrt.system.Object):
    handled: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BackPressedEventArgs: ...

class CameraEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CameraEventArgs: ...

class HardwareButtons(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HardwareButtons: ...
    @staticmethod
    def add_back_pressed(handler: winrt.windows.foundation.EventHandler[BackPressedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_back_pressed(token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @staticmethod
    def add_camera_half_pressed(handler: winrt.windows.foundation.EventHandler[CameraEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_camera_half_pressed(token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @staticmethod
    def add_camera_pressed(handler: winrt.windows.foundation.EventHandler[CameraEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_camera_pressed(token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @staticmethod
    def add_camera_released(handler: winrt.windows.foundation.EventHandler[CameraEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_camera_released(token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
