# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.applicationmodel.socialinfo
import winrt.windows.foundation
import winrt.windows.foundation.collections

Self = typing.TypeVar('Self')

class SocialDashboardItemUpdater(winrt.system.Object):
    timestamp: datetime.datetime
    thumbnail: typing.Optional[winrt.windows.applicationmodel.socialinfo.SocialItemThumbnail]
    target_uri: typing.Optional[winrt.windows.foundation.Uri]
    content: typing.Optional[winrt.windows.applicationmodel.socialinfo.SocialFeedContent]
    owner_remote_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialDashboardItemUpdater: ...
    def commit_async(self) -> winrt.windows.foundation.IAsyncAction: ...

class SocialFeedUpdater(winrt.system.Object):
    items: typing.Optional[winrt.windows.foundation.collections.IVector[winrt.windows.applicationmodel.socialinfo.SocialFeedItem]]
    kind: winrt.windows.applicationmodel.socialinfo.SocialFeedKind
    owner_remote_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialFeedUpdater: ...
    def commit_async(self) -> winrt.windows.foundation.IAsyncAction: ...

class SocialInfoProviderManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SocialInfoProviderManager: ...
    @staticmethod
    def create_dashboard_item_updater_async(owner_remote_id: str, /) -> winrt.windows.foundation.IAsyncOperation[SocialDashboardItemUpdater]: ...
    @staticmethod
    def create_social_feed_updater_async(kind: winrt.windows.applicationmodel.socialinfo.SocialFeedKind, mode: winrt.windows.applicationmodel.socialinfo.SocialFeedUpdateMode, owner_remote_id: str, /) -> winrt.windows.foundation.IAsyncOperation[SocialFeedUpdater]: ...
    @staticmethod
    def deprovision_async() -> winrt.windows.foundation.IAsyncAction: ...
    @staticmethod
    def provision_async() -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
    @staticmethod
    def report_new_content_available(contact_remote_id: str, kind: winrt.windows.applicationmodel.socialinfo.SocialFeedKind, /) -> None: ...
    @staticmethod
    def update_badge_count_value(item_remote_id: str, new_count: winrt.system.Int32, /) -> None: ...
