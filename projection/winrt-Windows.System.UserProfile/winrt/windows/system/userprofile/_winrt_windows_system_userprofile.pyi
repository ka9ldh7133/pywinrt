# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.globalization
import winrt.windows.storage
import winrt.windows.storage.streams
import winrt.windows.system

from . import AccountPictureKind, SetAccountPictureResult, SetImageFeedResult

Self = typing.TypeVar('Self')

class AdvertisingManager(winrt.system.Object):
    advertising_id: typing.ClassVar[str]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AdvertisingManager: ...
    @staticmethod
    def get_for_user(user: typing.Optional[winrt.windows.system.User], /) -> typing.Optional[AdvertisingManagerForUser]: ...

class AdvertisingManagerForUser(winrt.system.Object):
    advertising_id: str
    user: typing.Optional[winrt.windows.system.User]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AdvertisingManagerForUser: ...

class AssignedAccessSettings(winrt.system.Object):
    is_enabled: winrt.system.Boolean
    is_single_app_kiosk_mode: winrt.system.Boolean
    user: typing.Optional[winrt.windows.system.User]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AssignedAccessSettings: ...
    @staticmethod
    def get_default() -> typing.Optional[AssignedAccessSettings]: ...
    @staticmethod
    def get_for_user(user: typing.Optional[winrt.windows.system.User], /) -> typing.Optional[AssignedAccessSettings]: ...

class DiagnosticsSettings(winrt.system.Object):
    can_use_diagnostics_to_tailor_experiences: winrt.system.Boolean
    user: typing.Optional[winrt.windows.system.User]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DiagnosticsSettings: ...
    @staticmethod
    def get_default() -> typing.Optional[DiagnosticsSettings]: ...
    @staticmethod
    def get_for_user(user: typing.Optional[winrt.windows.system.User], /) -> typing.Optional[DiagnosticsSettings]: ...

class FirstSignInSettings(winrt.system.Object, typing.Mapping[str, winrt.system.Object]):
    size: winrt.system.UInt32
    def __len__(self) -> int: ...
    def __iter__(self) -> typing.Iterator[str]: ...
    def __contains__(self, key: object) -> bool:...
    def __getitem__(self, key: str) -> winrt.system.Object: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FirstSignInSettings: ...
    def first(self) -> typing.Optional[winrt.windows.foundation.collections.IIterator[winrt.windows.foundation.collections.IKeyValuePair[str, winrt.system.Object]]]: ...
    @staticmethod
    def get_default() -> typing.Optional[FirstSignInSettings]: ...
    def has_key(self, key: str, /) -> winrt.system.Boolean: ...
    def lookup(self, key: str, /) -> typing.Optional[winrt.system.Object]: ...
    def split(self) -> typing.Tuple[typing.Optional[winrt.windows.foundation.collections.IMapView[str, winrt.system.Object]], typing.Optional[winrt.windows.foundation.collections.IMapView[str, winrt.system.Object]]]: ...

class GlobalizationPreferences(winrt.system.Object):
    calendars: typing.ClassVar[typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]]
    clocks: typing.ClassVar[typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]]
    currencies: typing.ClassVar[typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]]
    home_geographic_region: typing.ClassVar[str]
    languages: typing.ClassVar[typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]]
    week_starts_on: typing.ClassVar[winrt.windows.globalization.DayOfWeek]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalizationPreferences: ...
    @staticmethod
    def get_for_user(user: typing.Optional[winrt.windows.system.User], /) -> typing.Optional[GlobalizationPreferencesForUser]: ...
    @staticmethod
    def try_set_home_geographic_region(region: str, /) -> winrt.system.Boolean: ...
    @staticmethod
    def try_set_languages(language_tags: typing.Iterable[str], /) -> winrt.system.Boolean: ...

class GlobalizationPreferencesForUser(winrt.system.Object):
    calendars: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    clocks: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    currencies: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    home_geographic_region: str
    languages: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    user: typing.Optional[winrt.windows.system.User]
    week_starts_on: winrt.windows.globalization.DayOfWeek
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalizationPreferencesForUser: ...

class LockScreen(winrt.system.Object):
    original_image_file: typing.ClassVar[typing.Optional[winrt.windows.foundation.Uri]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LockScreen: ...
    @staticmethod
    def get_image_stream() -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStream]: ...
    @staticmethod
    def request_set_image_feed_async(syndication_feed_uri: typing.Optional[winrt.windows.foundation.Uri], /) -> winrt.windows.foundation.IAsyncOperation[SetImageFeedResult]: ...
    @staticmethod
    def set_image_file_async(value: typing.Optional[winrt.windows.storage.IStorageFile], /) -> winrt.windows.foundation.IAsyncAction: ...
    @staticmethod
    def set_image_stream_async(value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], /) -> winrt.windows.foundation.IAsyncAction: ...
    @staticmethod
    def try_remove_image_feed() -> winrt.system.Boolean: ...

class UserInformation(winrt.system.Object):
    account_picture_change_enabled: typing.ClassVar[winrt.system.Boolean]
    name_access_allowed: typing.ClassVar[winrt.system.Boolean]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UserInformation: ...
    @staticmethod
    def get_account_picture(kind: AccountPictureKind, /) -> typing.Optional[winrt.windows.storage.IStorageFile]: ...
    @staticmethod
    def get_display_name_async() -> winrt.windows.foundation.IAsyncOperation[str]: ...
    @staticmethod
    def get_domain_name_async() -> winrt.windows.foundation.IAsyncOperation[str]: ...
    @staticmethod
    def get_first_name_async() -> winrt.windows.foundation.IAsyncOperation[str]: ...
    @staticmethod
    def get_last_name_async() -> winrt.windows.foundation.IAsyncOperation[str]: ...
    @staticmethod
    def get_principal_name_async() -> winrt.windows.foundation.IAsyncOperation[str]: ...
    @staticmethod
    def get_session_initiation_protocol_uri_async() -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.Uri]: ...
    @staticmethod
    def set_account_picture_async(image: typing.Optional[winrt.windows.storage.IStorageFile], /) -> winrt.windows.foundation.IAsyncOperation[SetAccountPictureResult]: ...
    @staticmethod
    def set_account_picture_from_stream_async(image: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], /) -> winrt.windows.foundation.IAsyncOperation[SetAccountPictureResult]: ...
    @staticmethod
    def set_account_pictures_async(small_image: typing.Optional[winrt.windows.storage.IStorageFile], large_image: typing.Optional[winrt.windows.storage.IStorageFile], video: typing.Optional[winrt.windows.storage.IStorageFile], /) -> winrt.windows.foundation.IAsyncOperation[SetAccountPictureResult]: ...
    @staticmethod
    def set_account_pictures_from_streams_async(small_image: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], large_image: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], video: typing.Optional[winrt.windows.storage.streams.IRandomAccessStream], /) -> winrt.windows.foundation.IAsyncOperation[SetAccountPictureResult]: ...
    @staticmethod
    def add_account_picture_changed(change_handler: winrt.windows.foundation.EventHandler[winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_account_picture_changed(token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class UserProfilePersonalizationSettings(winrt.system.Object):
    current: typing.ClassVar[typing.Optional[UserProfilePersonalizationSettings]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UserProfilePersonalizationSettings: ...
    @staticmethod
    def is_supported() -> winrt.system.Boolean: ...
    def try_set_lock_screen_image_async(self, image_file: typing.Optional[winrt.windows.storage.StorageFile], /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
    def try_set_wallpaper_image_async(self, image_file: typing.Optional[winrt.windows.storage.StorageFile], /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
