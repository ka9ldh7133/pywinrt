# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.storage.streams

from . import TargetedContentAppInstallationState, TargetedContentAvailability, TargetedContentInteraction, TargetedContentObjectKind, TargetedContentValueKind

Self = typing.TypeVar('Self')

class TargetedContentAction(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentAction: ...
    def invoke_async(self) -> winrt.windows.foundation.IAsyncAction: ...

class TargetedContentAvailabilityChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentAvailabilityChangedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class TargetedContentChangedEventArgs(winrt.system.Object):
    has_previous_content_expired: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentChangedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class TargetedContentCollection(winrt.system.Object):
    collections: typing.Optional[winrt.windows.foundation.collections.IVectorView[TargetedContentCollection]]
    id: str
    items: typing.Optional[winrt.windows.foundation.collections.IVectorView[TargetedContentItem]]
    path: str
    properties: typing.Optional[winrt.windows.foundation.collections.IMapView[str, TargetedContentValue]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentCollection: ...
    def report_custom_interaction(self, custom_interaction_name: str, /) -> None: ...
    def report_interaction(self, interaction: TargetedContentInteraction, /) -> None: ...

class TargetedContentContainer(winrt.system.Object):
    availability: TargetedContentAvailability
    content: typing.Optional[TargetedContentCollection]
    id: str
    timestamp: datetime.datetime
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentContainer: ...
    @staticmethod
    def get_async(content_id: str, /) -> winrt.windows.foundation.IAsyncOperation[TargetedContentContainer]: ...
    def select_single_object(self, path: str, /) -> typing.Optional[TargetedContentObject]: ...

class TargetedContentFile(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentFile: ...
    def open_read_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.storage.streams.IRandomAccessStreamWithContentType]: ...

class TargetedContentImage(winrt.system.Object):
    height: winrt.system.UInt32
    width: winrt.system.UInt32
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentImage: ...
    def open_read_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.storage.streams.IRandomAccessStreamWithContentType]: ...

class TargetedContentItem(winrt.system.Object):
    collections: typing.Optional[winrt.windows.foundation.collections.IVectorView[TargetedContentCollection]]
    path: str
    properties: typing.Optional[winrt.windows.foundation.collections.IMapView[str, TargetedContentValue]]
    state: typing.Optional[TargetedContentItemState]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentItem: ...
    def report_custom_interaction(self, custom_interaction_name: str, /) -> None: ...
    def report_interaction(self, interaction: TargetedContentInteraction, /) -> None: ...

class TargetedContentItemState(winrt.system.Object):
    app_installation_state: TargetedContentAppInstallationState
    should_display: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentItemState: ...

class TargetedContentObject(winrt.system.Object):
    collection: typing.Optional[TargetedContentCollection]
    item: typing.Optional[TargetedContentItem]
    object_kind: TargetedContentObjectKind
    value: typing.Optional[TargetedContentValue]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentObject: ...

class TargetedContentStateChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentStateChangedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class TargetedContentSubscription(winrt.system.Object):
    id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentSubscription: ...
    @staticmethod
    def get_async(subscription_id: str, /) -> winrt.windows.foundation.IAsyncOperation[TargetedContentSubscription]: ...
    def get_content_container_async(self) -> winrt.windows.foundation.IAsyncOperation[TargetedContentContainer]: ...
    @staticmethod
    def get_options(subscription_id: str, /) -> typing.Optional[TargetedContentSubscriptionOptions]: ...
    def add_availability_changed(self, handler: winrt.windows.foundation.TypedEventHandler[TargetedContentSubscription, TargetedContentAvailabilityChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_availability_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_content_changed(self, handler: winrt.windows.foundation.TypedEventHandler[TargetedContentSubscription, TargetedContentChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_content_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_state_changed(self, handler: winrt.windows.foundation.TypedEventHandler[TargetedContentSubscription, TargetedContentStateChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_state_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class TargetedContentSubscriptionOptions(winrt.system.Object):
    allow_partial_content_availability: winrt.system.Boolean
    cloud_query_parameters: typing.Optional[winrt.windows.foundation.collections.IMap[str, str]]
    local_filters: typing.Optional[winrt.windows.foundation.collections.IVector[str]]
    subscription_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentSubscriptionOptions: ...
    def update(self) -> None: ...

class TargetedContentValue(winrt.system.Object):
    action: typing.Optional[TargetedContentAction]
    actions: typing.Optional[winrt.windows.foundation.collections.IVectorView[TargetedContentAction]]
    boolean: winrt.system.Boolean
    booleans: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.Boolean]]
    file: typing.Optional[TargetedContentFile]
    files: typing.Optional[winrt.windows.foundation.collections.IVectorView[TargetedContentFile]]
    image_file: typing.Optional[TargetedContentImage]
    image_files: typing.Optional[winrt.windows.foundation.collections.IVectorView[TargetedContentImage]]
    number: winrt.system.Double
    numbers: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.Double]]
    path: str
    string: str
    strings: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    uri: typing.Optional[winrt.windows.foundation.Uri]
    uris: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Uri]]
    value_kind: TargetedContentValueKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TargetedContentValue: ...
