# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system

from . import PhoneNumberFormat, PhoneNumberMatchResult, PhoneNumberParseResult, PredictedPhoneNumberKind

Self = typing.TypeVar('Self')

class PhoneNumberFormatter(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneNumberFormatter: ...
    def __new__(cls: typing.Type[PhoneNumberFormatter]) -> PhoneNumberFormatter:...
    @typing.overload
    def format(self, number: typing.Optional[PhoneNumberInfo], /) -> str: ...
    @typing.overload
    def format(self, number: typing.Optional[PhoneNumberInfo], number_format: PhoneNumberFormat, /) -> str: ...
    def format_partial_string(self, number: str, /) -> str: ...
    def format_string(self, number: str, /) -> str: ...
    def format_string_with_left_to_right_markers(self, number: str, /) -> str: ...
    @staticmethod
    def get_country_code_for_region(region_code: str, /) -> winrt.system.Int32: ...
    @staticmethod
    def get_national_direct_dialing_prefix_for_region(region_code: str, strip_non_digit: winrt.system.Boolean, /) -> str: ...
    @staticmethod
    def try_create(region_code: str, /) -> typing.Optional[PhoneNumberFormatter]: ...
    @staticmethod
    def wrap_with_left_to_right_markers(number: str, /) -> str: ...

class PhoneNumberInfo(winrt.system.Object):
    country_code: winrt.system.Int32
    phone_number: str
    def __str__(self) -> str: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneNumberInfo: ...
    def __new__(cls: typing.Type[PhoneNumberInfo], number: str) -> PhoneNumberInfo:...
    def check_number_match(self, other_number: typing.Optional[PhoneNumberInfo], /) -> PhoneNumberMatchResult: ...
    def get_geographic_region_code(self) -> str: ...
    def get_length_of_geographical_area_code(self) -> winrt.system.Int32: ...
    def get_length_of_national_destination_code(self) -> winrt.system.Int32: ...
    def get_national_significant_number(self) -> str: ...
    def predict_number_kind(self) -> PredictedPhoneNumberKind: ...
    def to_string(self) -> str: ...
    @typing.overload
    @staticmethod
    def try_parse(input: str, /) -> typing.Tuple[PhoneNumberParseResult, typing.Optional[PhoneNumberInfo]]: ...
    @typing.overload
    @staticmethod
    def try_parse(input: str, region_code: str, /) -> typing.Tuple[PhoneNumberParseResult, typing.Optional[PhoneNumberInfo]]: ...
