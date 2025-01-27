# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.graphics.imaging as windows_graphics_imaging
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.applicationmodel.socialinfo import SocialFeedItemStyle, SocialFeedKind, SocialFeedUpdateMode, SocialItemBadgeStyle

Self = typing.TypeVar('Self')

@typing.final
class SocialFeedChildItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialFeedChildItem: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def timestamp(self) -> datetime.datetime: ...
    @timestamp.setter
    def timestamp(self, value: datetime.datetime) -> None: ...
    @_property
    def target_uri(self) -> windows_foundation.Uri: ...
    @target_uri.setter
    def target_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def shared_item(self) -> SocialFeedSharedItem: ...
    @shared_item.setter
    def shared_item(self, value: SocialFeedSharedItem) -> None: ...
    @_property
    def author(self) -> SocialUserInfo: ...
    @_property
    def primary_content(self) -> SocialFeedContent: ...
    @_property
    def secondary_content(self) -> SocialFeedContent: ...
    @_property
    def thumbnails(self) -> typing.MutableSequence[SocialItemThumbnail]: ...

@typing.final
class SocialFeedContent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialFeedContent: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def target_uri(self) -> windows_foundation.Uri: ...
    @target_uri.setter
    def target_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...

@typing.final
class SocialFeedItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialFeedItem: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def timestamp(self) -> datetime.datetime: ...
    @timestamp.setter
    def timestamp(self, value: datetime.datetime) -> None: ...
    @_property
    def target_uri(self) -> windows_foundation.Uri: ...
    @target_uri.setter
    def target_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def style(self) -> SocialFeedItemStyle: ...
    @style.setter
    def style(self, value: SocialFeedItemStyle) -> None: ...
    @_property
    def shared_item(self) -> SocialFeedSharedItem: ...
    @shared_item.setter
    def shared_item(self, value: SocialFeedSharedItem) -> None: ...
    @_property
    def remote_id(self) -> str: ...
    @remote_id.setter
    def remote_id(self, value: str) -> None: ...
    @_property
    def child_item(self) -> SocialFeedChildItem: ...
    @child_item.setter
    def child_item(self, value: SocialFeedChildItem) -> None: ...
    @_property
    def badge_style(self) -> SocialItemBadgeStyle: ...
    @badge_style.setter
    def badge_style(self, value: SocialItemBadgeStyle) -> None: ...
    @_property
    def badge_count_value(self) -> winrt.system.Int32: ...
    @badge_count_value.setter
    def badge_count_value(self, value: winrt.system.Int32) -> None: ...
    @_property
    def author(self) -> SocialUserInfo: ...
    @_property
    def thumbnails(self) -> typing.MutableSequence[SocialItemThumbnail]: ...
    @_property
    def primary_content(self) -> SocialFeedContent: ...
    @_property
    def secondary_content(self) -> SocialFeedContent: ...

@typing.final
class SocialFeedSharedItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialFeedSharedItem: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def timestamp(self) -> datetime.datetime: ...
    @timestamp.setter
    def timestamp(self, value: datetime.datetime) -> None: ...
    @_property
    def thumbnail(self) -> SocialItemThumbnail: ...
    @thumbnail.setter
    def thumbnail(self, value: SocialItemThumbnail) -> None: ...
    @_property
    def target_uri(self) -> windows_foundation.Uri: ...
    @target_uri.setter
    def target_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def original_source(self) -> windows_foundation.Uri: ...
    @original_source.setter
    def original_source(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def content(self) -> SocialFeedContent: ...

@typing.final
class SocialItemThumbnail(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialItemThumbnail: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    # @deprecated("ISocialItemThumbnail is deprecated and might not work on all platforms. For more info, see MSDN.")
    def set_image_async(self, image: windows_storage_streams.ImplementsIInputStream, /) -> windows_foundation.IAsyncAction: ...
    @_property
    def target_uri(self) -> windows_foundation.Uri: ...
    @target_uri.setter
    def target_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def image_uri(self) -> windows_foundation.Uri: ...
    @image_uri.setter
    def image_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def bitmap_size(self) -> windows_graphics_imaging.BitmapSize: ...
    @bitmap_size.setter
    def bitmap_size(self, value: windows_graphics_imaging.BitmapSize) -> None: ...

@typing.final
class SocialUserInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialUserInfo: ...
    @_property
    def user_name(self) -> str: ...
    @user_name.setter
    def user_name(self, value: str) -> None: ...
    @_property
    def target_uri(self) -> windows_foundation.Uri: ...
    @target_uri.setter
    def target_uri(self, value: windows_foundation.Uri) -> None: ...
    @_property
    def remote_id(self) -> str: ...
    @remote_id.setter
    def remote_id(self, value: str) -> None: ...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...

