# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system

Self = typing.TypeVar('Self')

class ClassicAppManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ClassicAppManager: ...
    @staticmethod
    def find_installed_app(app_uninstall_key: str, /) -> typing.Optional[InstalledClassicAppInfo]: ...

class InstalledClassicAppInfo(winrt.system.Object):
    display_name: str
    display_version: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InstalledClassicAppInfo: ...
