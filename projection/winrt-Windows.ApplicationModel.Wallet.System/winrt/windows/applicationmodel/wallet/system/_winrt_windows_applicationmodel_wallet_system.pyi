# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.applicationmodel.wallet
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.storage.streams

from . import WalletItemAppAssociation

Self = typing.TypeVar('Self')

class WalletItemSystemStore(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletItemSystemStore: ...
    def delete_async(self, item: typing.Optional[winrt.windows.applicationmodel.wallet.WalletItem], /) -> winrt.windows.foundation.IAsyncAction: ...
    def get_app_status_for_item(self, item: typing.Optional[winrt.windows.applicationmodel.wallet.WalletItem], /) -> WalletItemAppAssociation: ...
    def get_items_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[winrt.windows.applicationmodel.wallet.WalletItem]]: ...
    def import_item_async(self, stream: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.applicationmodel.wallet.WalletItem]: ...
    def launch_app_for_item_async(self, item: typing.Optional[winrt.windows.applicationmodel.wallet.WalletItem], /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
    def add_items_changed(self, handler: winrt.windows.foundation.TypedEventHandler[WalletItemSystemStore, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_items_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class WalletManagerSystem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletManagerSystem: ...
    @staticmethod
    def request_store_async() -> winrt.windows.foundation.IAsyncOperation[WalletItemSystemStore]: ...
