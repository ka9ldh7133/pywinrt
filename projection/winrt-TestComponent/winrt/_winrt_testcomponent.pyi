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
import winrt.windows.foundation.collections

from winrt.testcomponent import Array10Handler, Array11Handler, Array12Handler, Array13Handler, Array14Handler, Array15Handler, Array1Handler, Array2Handler, Array3Handler, Array4Handler, Array5Handler, Array6Handler, Array7Handler, Array8Handler, Array9Handler, Async1Handler, Async2Handler, Async3Handler, Async4Handler, Collection1Handler, Collection2Handler, Collection3Handler, Collection4Handler, Collection5Handler, Collection6Handler, Param10Handler, Param11Handler, Param12Handler, Param13Handler, Param14Handler, Param15Handler, Param1Handler, Param2Handler, Param3Handler, Param4Handler, Param5Handler, Param6Handler, Param7Handler, Param8Handler, Param9Handler, TestHandler

Self = typing.TypeVar('Self')

class Blittable:
    a: winrt.system.UInt8
    b: winrt.system.UInt16
    c: winrt.system.UInt32
    d: winrt.system.UInt64
    e: winrt.system.Int16
    f: winrt.system.Int32
    g: winrt.system.Int64
    h: winrt.system.Single
    i: winrt.system.Double
    j: _uuid.UUID
    def __init__(self, a: winrt.system.UInt8, b: winrt.system.UInt16, c: winrt.system.UInt32, d: winrt.system.UInt64, e: winrt.system.Int16, f: winrt.system.Int32, g: winrt.system.Int64, h: winrt.system.Single, i: winrt.system.Double, j: _uuid.UUID) -> None: ...

class Nested:
    blittable: Blittable
    non_blittable: NonBlittable
    def __init__(self, blittable: Blittable, non_blittable: NonBlittable) -> None: ...

class NonBlittable:
    a: bool
    b: winrt.system.Char16
    c: str
    d: winrt.system.Int64
    def __init__(self, a: bool, b: winrt.system.Char16, c: str, d: winrt.system.Int64) -> None: ...

class TestRunner_Static(type):
    def create_int32_vector(cls) -> typing.Optional[winrt.windows.foundation.collections.IVector[winrt.system.Int32]]: ...
    def create_string_vector(cls) -> typing.Optional[winrt.windows.foundation.collections.IVector[str]]: ...
    def create_stringable_vector(cls) -> typing.Optional[winrt.windows.foundation.collections.IVector[winrt.windows.foundation.IStringable]]: ...
    def make_tests(cls) -> typing.Optional[ITests]: ...
    def test_consumer(cls, caller: typing.Optional[TestHandler], /) -> winrt.system.UInt32: ...
    def test_producer(cls, callee: typing.Optional[ITests], /) -> None: ...
    def test_self(cls) -> None: ...

class TestRunner(winrt.system.Object, metaclass=TestRunner_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TestRunner: ...

class ITests(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ITests: ...
    def array1(self, a: winrt.system.Array[bool], b: winrt.system.Array[bool], /) -> typing.Tuple[bool, winrt.system.Array[bool]]: ...
    def array10(self, a: winrt.system.Array[winrt.system.Double], b: winrt.system.Array[winrt.system.Double], /) -> typing.Tuple[winrt.system.Double, winrt.system.Array[winrt.system.Double]]: ...
    def array10_call(self, handler: typing.Optional[Array10Handler], /) -> None: ...
    def array11(self, a: winrt.system.Array[winrt.system.Char16], b: winrt.system.Array[winrt.system.Char16], /) -> typing.Tuple[winrt.system.Char16, winrt.system.Array[winrt.system.Char16]]: ...
    def array11_call(self, handler: typing.Optional[Array11Handler], /) -> None: ...
    def array12(self, a: winrt.system.Array[str], b: winrt.system.Array[str], /) -> typing.Tuple[str, winrt.system.Array[str]]: ...
    def array12_call(self, handler: typing.Optional[Array12Handler], /) -> None: ...
    def array13(self, a: winrt.system.Array[Blittable], b: winrt.system.Array[Blittable], /) -> typing.Tuple[Blittable, winrt.system.Array[Blittable]]: ...
    def array13_call(self, handler: typing.Optional[Array13Handler], /) -> None: ...
    def array14(self, a: winrt.system.Array[NonBlittable], b: winrt.system.Array[NonBlittable], /) -> typing.Tuple[NonBlittable, winrt.system.Array[NonBlittable]]: ...
    def array14_call(self, handler: typing.Optional[Array14Handler], /) -> None: ...
    def array15(self, a: winrt.system.Array[Nested], b: winrt.system.Array[Nested], /) -> typing.Tuple[Nested, winrt.system.Array[Nested]]: ...
    def array15_call(self, handler: typing.Optional[Array15Handler], /) -> None: ...
    def array1_call(self, handler: typing.Optional[Array1Handler], /) -> None: ...
    def array2(self, a: winrt.system.Array[winrt.system.UInt8], b: winrt.system.Array[winrt.system.UInt8], /) -> typing.Tuple[winrt.system.UInt8, winrt.system.Array[winrt.system.UInt8]]: ...
    def array2_call(self, handler: typing.Optional[Array2Handler], /) -> None: ...
    def array3(self, a: winrt.system.Array[winrt.system.UInt16], b: winrt.system.Array[winrt.system.UInt16], /) -> typing.Tuple[winrt.system.UInt16, winrt.system.Array[winrt.system.UInt16]]: ...
    def array3_call(self, handler: typing.Optional[Array3Handler], /) -> None: ...
    def array4(self, a: winrt.system.Array[winrt.system.UInt32], b: winrt.system.Array[winrt.system.UInt32], /) -> typing.Tuple[winrt.system.UInt32, winrt.system.Array[winrt.system.UInt32]]: ...
    def array4_call(self, handler: typing.Optional[Array4Handler], /) -> None: ...
    def array5(self, a: winrt.system.Array[winrt.system.UInt64], b: winrt.system.Array[winrt.system.UInt64], /) -> typing.Tuple[winrt.system.UInt64, winrt.system.Array[winrt.system.UInt64]]: ...
    def array5_call(self, handler: typing.Optional[Array5Handler], /) -> None: ...
    def array6(self, a: winrt.system.Array[winrt.system.Int16], b: winrt.system.Array[winrt.system.Int16], /) -> typing.Tuple[winrt.system.Int16, winrt.system.Array[winrt.system.Int16]]: ...
    def array6_call(self, handler: typing.Optional[Array6Handler], /) -> None: ...
    def array7(self, a: winrt.system.Array[winrt.system.Int32], b: winrt.system.Array[winrt.system.Int32], /) -> typing.Tuple[winrt.system.Int32, winrt.system.Array[winrt.system.Int32]]: ...
    def array7_call(self, handler: typing.Optional[Array7Handler], /) -> None: ...
    def array8(self, a: winrt.system.Array[winrt.system.Int64], b: winrt.system.Array[winrt.system.Int64], /) -> typing.Tuple[winrt.system.Int64, winrt.system.Array[winrt.system.Int64]]: ...
    def array8_call(self, handler: typing.Optional[Array8Handler], /) -> None: ...
    def array9(self, a: winrt.system.Array[winrt.system.Single], b: winrt.system.Array[winrt.system.Single], /) -> typing.Tuple[winrt.system.Single, winrt.system.Array[winrt.system.Single]]: ...
    def array9_call(self, handler: typing.Optional[Array9Handler], /) -> None: ...
    def async1(self, suspend: winrt.windows.foundation.IAsyncAction, fail: bool, /) -> winrt.windows.foundation.IAsyncAction: ...
    def async1_call(self, handler: typing.Optional[Async1Handler], /) -> None: ...
    def async2(self, suspend: winrt.windows.foundation.IAsyncAction, fail: bool, progress: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncActionWithProgress[winrt.system.Int32]: ...
    def async2_call(self, handler: typing.Optional[Async2Handler], /) -> None: ...
    def async3(self, suspend: winrt.windows.foundation.IAsyncAction, fail: bool, result: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Int32]: ...
    def async3_call(self, handler: typing.Optional[Async3Handler], /) -> None: ...
    def async4(self, suspend: winrt.windows.foundation.IAsyncAction, fail: bool, result: winrt.system.Int32, progress: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.system.Int32, winrt.system.Int32]: ...
    def async4_call(self, handler: typing.Optional[Async4Handler], /) -> None: ...
    def collection1(self, a: typing.Iterable[str], /) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IIterable[str]], typing.Optional[winrt.windows.foundation.collections.IIterable[str]]]: ...
    def collection1_call(self, handler: typing.Optional[Collection1Handler], /) -> None: ...
    def collection2(self, a: typing.Iterable[winrt.windows.foundation.collections.IKeyValuePair[str, str]], /) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IIterable[winrt.windows.foundation.collections.IKeyValuePair[str, str]]], typing.Optional[winrt.windows.foundation.collections.IIterable[winrt.windows.foundation.collections.IKeyValuePair[str, str]]]]: ...
    def collection2_call(self, handler: typing.Optional[Collection2Handler], /) -> None: ...
    def collection3(self, a: winrt.windows.foundation.collections.IMap[str, str], /) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IMap[str, str]], typing.Optional[winrt.windows.foundation.collections.IMap[str, str]]]: ...
    def collection3_call(self, handler: typing.Optional[Collection3Handler], /) -> None: ...
    def collection4(self, a: winrt.windows.foundation.collections.IMapView[str, str], /) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IMapView[str, str]], typing.Optional[winrt.windows.foundation.collections.IMapView[str, str]]]: ...
    def collection4_call(self, handler: typing.Optional[Collection4Handler], /) -> None: ...
    def collection5(self, a: winrt.windows.foundation.collections.IVector[str], /) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IVector[str]], typing.Optional[winrt.windows.foundation.collections.IVector[str]]]: ...
    def collection5_call(self, handler: typing.Optional[Collection5Handler], /) -> None: ...
    def collection6(self, a: winrt.windows.foundation.collections.IVectorView[str], /) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IVectorView[str]], typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]]: ...
    def collection6_call(self, handler: typing.Optional[Collection6Handler], /) -> None: ...
    def event1_call(self, value: winrt.system.Int32, /) -> None: ...
    def event2_call(self, value: winrt.system.Int32, /) -> None: ...
    def param1(self, a: bool, /) -> typing.Tuple[bool, bool]: ...
    def param10(self, a: winrt.system.Double, /) -> typing.Tuple[winrt.system.Double, winrt.system.Double]: ...
    def param10_call(self, handler: typing.Optional[Param10Handler], /) -> None: ...
    def param11(self, a: winrt.system.Char16, /) -> typing.Tuple[winrt.system.Char16, winrt.system.Char16]: ...
    def param11_call(self, handler: typing.Optional[Param11Handler], /) -> None: ...
    def param12(self, a: str, /) -> typing.Tuple[str, str]: ...
    def param12_call(self, handler: typing.Optional[Param12Handler], /) -> None: ...
    def param13(self, a: Blittable, b: Blittable, /) -> typing.Tuple[Blittable, Blittable]: ...
    def param13_call(self, handler: typing.Optional[Param13Handler], /) -> None: ...
    def param14(self, a: NonBlittable, b: NonBlittable, /) -> typing.Tuple[NonBlittable, NonBlittable]: ...
    def param14_call(self, handler: typing.Optional[Param14Handler], /) -> None: ...
    def param15(self, a: Nested, b: Nested, /) -> typing.Tuple[Nested, Nested]: ...
    def param15_call(self, handler: typing.Optional[Param15Handler], /) -> None: ...
    def param1_call(self, handler: typing.Optional[Param1Handler], /) -> None: ...
    def param2(self, a: winrt.system.UInt8, /) -> typing.Tuple[winrt.system.UInt8, winrt.system.UInt8]: ...
    def param2_call(self, handler: typing.Optional[Param2Handler], /) -> None: ...
    def param3(self, a: winrt.system.UInt16, /) -> typing.Tuple[winrt.system.UInt16, winrt.system.UInt16]: ...
    def param3_call(self, handler: typing.Optional[Param3Handler], /) -> None: ...
    def param4(self, a: winrt.system.UInt32, /) -> typing.Tuple[winrt.system.UInt32, winrt.system.UInt32]: ...
    def param4_call(self, handler: typing.Optional[Param4Handler], /) -> None: ...
    def param5(self, a: winrt.system.UInt64, /) -> typing.Tuple[winrt.system.UInt64, winrt.system.UInt64]: ...
    def param5_call(self, handler: typing.Optional[Param5Handler], /) -> None: ...
    def param6(self, a: winrt.system.Int16, /) -> typing.Tuple[winrt.system.Int16, winrt.system.Int16]: ...
    def param6_call(self, handler: typing.Optional[Param6Handler], /) -> None: ...
    def param7(self, a: winrt.system.Int32, /) -> typing.Tuple[winrt.system.Int32, winrt.system.Int32]: ...
    def param7_call(self, handler: typing.Optional[Param7Handler], /) -> None: ...
    def param8(self, a: winrt.system.Int64, /) -> typing.Tuple[winrt.system.Int64, winrt.system.Int64]: ...
    def param8_call(self, handler: typing.Optional[Param8Handler], /) -> None: ...
    def param9(self, a: winrt.system.Single, /) -> typing.Tuple[winrt.system.Single, winrt.system.Single]: ...
    def param9_call(self, handler: typing.Optional[Param9Handler], /) -> None: ...
    def simple(self) -> None: ...
    def add_event1(self, handler: winrt.windows.foundation.EventHandler[winrt.system.Int32], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_event1(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_event2(self, handler: winrt.windows.foundation.TypedEventHandler[ITests, winrt.system.Int32], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_event2(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def percentage(self) -> winrt.system.UInt32: ...
