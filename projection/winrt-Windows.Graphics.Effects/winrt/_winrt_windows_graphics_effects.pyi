# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system

Self = typing.TypeVar('Self')

class ImplementsIGraphicsEffect():
    pass

@typing.final
class IGraphicsEffect(winrt.system.Object, ImplementsIGraphicsEffect, ImplementsIGraphicsEffectSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IGraphicsEffect: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...

class ImplementsIGraphicsEffectSource():
    pass

@typing.final
class IGraphicsEffectSource(winrt.system.Object, ImplementsIGraphicsEffectSource):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IGraphicsEffectSource: ...

