# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.devices.geolocation
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.globalization
import winrt.windows.services.maps

class LocalLocationFinderStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    INVALID_CATEGORY = 3
    INVALID_SEARCH_TERM = 4
    INVALID_SEARCH_AREA = 5
    NETWORK_FAILURE = 6
    NOT_SUPPORTED = 7

Self = typing.TypeVar('Self')

class LocalCategories(winrt.system.Object):
    all: typing.ClassVar[str]
    bank_and_credit_unions: typing.ClassVar[str]
    eat_drink: typing.ClassVar[str]
    hospitals: typing.ClassVar[str]
    hotels_and_motels: typing.ClassVar[str]
    parking: typing.ClassVar[str]
    see_do: typing.ClassVar[str]
    shop: typing.ClassVar[str]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LocalCategories: ...

class LocalLocation(winrt.system.Object):
    address: typing.Optional[winrt.windows.services.maps.MapAddress]
    data_attribution: str
    description: str
    display_name: str
    identifier: str
    phone_number: str
    point: typing.Optional[winrt.windows.devices.geolocation.Geopoint]
    category: str
    hours_of_operation: typing.Optional[winrt.windows.foundation.collections.IVectorView[LocalLocationHoursOfOperationItem]]
    rating_info: typing.Optional[LocalLocationRatingInfo]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LocalLocation: ...

class LocalLocationFinder(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LocalLocationFinder: ...
    @staticmethod
    def find_local_locations_async(search_term: str, search_area: typing.Optional[winrt.windows.devices.geolocation.Geocircle], local_category: str, max_results: winrt.system.UInt32, /) -> winrt.windows.foundation.IAsyncOperation[LocalLocationFinderResult]: ...

class LocalLocationFinderResult(winrt.system.Object):
    local_locations: typing.Optional[winrt.windows.foundation.collections.IVectorView[LocalLocation]]
    status: LocalLocationFinderStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LocalLocationFinderResult: ...

class LocalLocationHoursOfOperationItem(winrt.system.Object):
    day: winrt.windows.globalization.DayOfWeek
    span: datetime.timedelta
    start: datetime.timedelta
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LocalLocationHoursOfOperationItem: ...

class LocalLocationRatingInfo(winrt.system.Object):
    aggregate_rating: typing.Optional[typing.Optional[winrt.system.Double]]
    provider_identifier: str
    rating_count: typing.Optional[typing.Optional[winrt.system.Int32]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LocalLocationRatingInfo: ...

class PlaceInfoHelper(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlaceInfoHelper: ...
    @staticmethod
    def create_from_local_location(location: typing.Optional[LocalLocation], /) -> typing.Optional[winrt.windows.services.maps.PlaceInfo]: ...
