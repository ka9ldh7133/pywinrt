# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.geolocation
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.storage.streams
import winrt.windows.ui

from winrt.windows.applicationmodel.wallet import WalletActionKind, WalletBarcodeSymbology, WalletDetailViewPosition, WalletItemKind, WalletSummaryViewPosition

Self = typing.TypeVar('Self')

class WalletBarcode(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletBarcode: ...
    @typing.overload
    def __new__(cls: typing.Type[WalletBarcode], symbology: WalletBarcodeSymbology, value: str) -> WalletBarcode:...
    @typing.overload
    def __new__(cls: typing.Type[WalletBarcode], stream_to_barcode_image: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> WalletBarcode:...
    def get_image_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @_property
    def symbology(self) -> WalletBarcodeSymbology: ...
    @_property
    def value(self) -> str: ...

class WalletItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletItem: ...
    def __new__(cls: typing.Type[WalletItem], kind: WalletItemKind, display_name: str) -> WalletItem:...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @_property
    def display_message(self) -> str: ...
    @display_message.setter
    def display_message(self, value: str) -> None: ...
    @_property
    def logo_text(self) -> str: ...
    @logo_text.setter
    def logo_text(self, value: str) -> None: ...
    @_property
    def body_font_color(self) -> winrt.windows.ui.Color: ...
    @body_font_color.setter
    def body_font_color(self, value: winrt.windows.ui.Color) -> None: ...
    @_property
    def body_color(self) -> winrt.windows.ui.Color: ...
    @body_color.setter
    def body_color(self, value: winrt.windows.ui.Color) -> None: ...
    @_property
    def body_background_image(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @body_background_image.setter
    def body_background_image(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def is_display_message_launchable(self) -> bool: ...
    @is_display_message_launchable.setter
    def is_display_message_launchable(self, value: bool) -> None: ...
    @_property
    def is_acknowledged(self) -> bool: ...
    @is_acknowledged.setter
    def is_acknowledged(self, value: bool) -> None: ...
    @_property
    def is_more_transaction_history_launchable(self) -> bool: ...
    @is_more_transaction_history_launchable.setter
    def is_more_transaction_history_launchable(self, value: bool) -> None: ...
    @_property
    def header_font_color(self) -> winrt.windows.ui.Color: ...
    @header_font_color.setter
    def header_font_color(self, value: winrt.windows.ui.Color) -> None: ...
    @_property
    def header_color(self) -> winrt.windows.ui.Color: ...
    @header_color.setter
    def header_color(self, value: winrt.windows.ui.Color) -> None: ...
    @_property
    def header_background_image(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @header_background_image.setter
    def header_background_image(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def expiration_date(self) -> typing.Optional[typing.Optional[datetime.datetime]]: ...
    @expiration_date.setter
    def expiration_date(self, value: typing.Optional[typing.Optional[datetime.datetime]]) -> None: ...
    @_property
    def logo99x99(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @logo99x99.setter
    def logo99x99(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def logo_image(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @logo_image.setter
    def logo_image(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def promotional_image(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @promotional_image.setter
    def promotional_image(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def logo159x159(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @logo159x159.setter
    def logo159x159(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def last_updated(self) -> typing.Optional[typing.Optional[datetime.datetime]]: ...
    @last_updated.setter
    def last_updated(self, value: typing.Optional[typing.Optional[datetime.datetime]]) -> None: ...
    @_property
    def issuer_display_name(self) -> str: ...
    @issuer_display_name.setter
    def issuer_display_name(self, value: str) -> None: ...
    @_property
    def barcode(self) -> typing.Optional[WalletBarcode]: ...
    @barcode.setter
    def barcode(self, value: typing.Optional[WalletBarcode]) -> None: ...
    @_property
    def relevant_date_display_message(self) -> str: ...
    @relevant_date_display_message.setter
    def relevant_date_display_message(self, value: str) -> None: ...
    @_property
    def relevant_date(self) -> typing.Optional[typing.Optional[datetime.datetime]]: ...
    @relevant_date.setter
    def relevant_date(self, value: typing.Optional[typing.Optional[datetime.datetime]]) -> None: ...
    @_property
    def logo336x336(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @logo336x336.setter
    def logo336x336(self, value: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def kind(self) -> WalletItemKind: ...
    @_property
    def display_properties(self) -> typing.Optional[winrt.windows.foundation.collections.IMap[str, WalletItemCustomProperty]]: ...
    @_property
    def id(self) -> str: ...
    @_property
    def relevant_locations(self) -> typing.Optional[winrt.windows.foundation.collections.IMap[str, WalletRelevantLocation]]: ...
    @_property
    def transaction_history(self) -> typing.Optional[winrt.windows.foundation.collections.IMap[str, WalletTransaction]]: ...
    @_property
    def verbs(self) -> typing.Optional[winrt.windows.foundation.collections.IMap[str, WalletVerb]]: ...

class WalletItemCustomProperty(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletItemCustomProperty: ...
    def __new__(cls: typing.Type[WalletItemCustomProperty], name: str, value: str) -> WalletItemCustomProperty:...
    @_property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str) -> None: ...
    @_property
    def summary_view_position(self) -> WalletSummaryViewPosition: ...
    @summary_view_position.setter
    def summary_view_position(self, value: WalletSummaryViewPosition) -> None: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @_property
    def detail_view_position(self) -> WalletDetailViewPosition: ...
    @detail_view_position.setter
    def detail_view_position(self, value: WalletDetailViewPosition) -> None: ...
    @_property
    def auto_detect_links(self) -> bool: ...
    @auto_detect_links.setter
    def auto_detect_links(self, value: bool) -> None: ...

class WalletItemStore(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletItemStore: ...
    def add_async(self, id: str, item: typing.Optional[WalletItem], /) -> winrt.windows.foundation.IAsyncAction: ...
    def clear_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def delete_async(self, id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def get_items_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[WalletItem]]: ...
    @typing.overload
    def get_items_async(self, kind: WalletItemKind, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[WalletItem]]: ...
    def get_wallet_item_async(self, id: str, /) -> winrt.windows.foundation.IAsyncOperation[WalletItem]: ...
    def import_item_async(self, stream: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference], /) -> winrt.windows.foundation.IAsyncOperation[WalletItem]: ...
    @typing.overload
    def show_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def show_async(self, id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def update_async(self, item: typing.Optional[WalletItem], /) -> winrt.windows.foundation.IAsyncAction: ...

class WalletManager_Static(type):
    def request_store_async(cls) -> winrt.windows.foundation.IAsyncOperation[WalletItemStore]: ...

class WalletManager(winrt.system.Object, metaclass=WalletManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletManager: ...

class WalletRelevantLocation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletRelevantLocation: ...
    def __new__(cls: typing.Type[WalletRelevantLocation]) -> WalletRelevantLocation:...
    @_property
    def position(self) -> winrt.windows.devices.geolocation.BasicGeoposition: ...
    @position.setter
    def position(self, value: winrt.windows.devices.geolocation.BasicGeoposition) -> None: ...
    @_property
    def display_message(self) -> str: ...
    @display_message.setter
    def display_message(self, value: str) -> None: ...

class WalletTransaction(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletTransaction: ...
    def __new__(cls: typing.Type[WalletTransaction]) -> WalletTransaction:...
    @_property
    def transaction_date(self) -> typing.Optional[typing.Optional[datetime.datetime]]: ...
    @transaction_date.setter
    def transaction_date(self, value: typing.Optional[typing.Optional[datetime.datetime]]) -> None: ...
    @_property
    def is_launchable(self) -> bool: ...
    @is_launchable.setter
    def is_launchable(self, value: bool) -> None: ...
    @_property
    def ignore_time_of_day(self) -> bool: ...
    @ignore_time_of_day.setter
    def ignore_time_of_day(self, value: bool) -> None: ...
    @_property
    def display_location(self) -> str: ...
    @display_location.setter
    def display_location(self, value: str) -> None: ...
    @_property
    def display_amount(self) -> str: ...
    @display_amount.setter
    def display_amount(self, value: str) -> None: ...
    @_property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...

class WalletVerb(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletVerb: ...
    def __new__(cls: typing.Type[WalletVerb], name: str) -> WalletVerb:...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
