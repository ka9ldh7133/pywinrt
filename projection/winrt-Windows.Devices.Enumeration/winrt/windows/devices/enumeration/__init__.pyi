# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.applicationmodel.background
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.security.credentials
import winrt.windows.storage.streams
import winrt.windows.ui
import winrt.windows.ui.popups

class DeviceAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    ALLOWED = 1
    DENIED_BY_USER = 2
    DENIED_BY_SYSTEM = 3

class DeviceClass(enum.IntEnum):
    ALL = 0
    AUDIO_CAPTURE = 1
    AUDIO_RENDER = 2
    PORTABLE_STORAGE_DEVICE = 3
    VIDEO_CAPTURE = 4
    IMAGE_SCANNER = 5
    LOCATION = 6

class DeviceInformationKind(enum.IntEnum):
    UNKNOWN = 0
    DEVICE_INTERFACE = 1
    DEVICE_CONTAINER = 2
    DEVICE = 3
    DEVICE_INTERFACE_CLASS = 4
    ASSOCIATION_ENDPOINT = 5
    ASSOCIATION_ENDPOINT_CONTAINER = 6
    ASSOCIATION_ENDPOINT_SERVICE = 7
    DEVICE_PANEL = 8

class DevicePairingKinds(enum.IntFlag):
    NONE = 0
    CONFIRM_ONLY = 0x1
    DISPLAY_PIN = 0x2
    PROVIDE_PIN = 0x4
    CONFIRM_PIN_MATCH = 0x8
    PROVIDE_PASSWORD_CREDENTIAL = 0x10

class DevicePairingProtectionLevel(enum.IntEnum):
    DEFAULT = 0
    NONE = 1
    ENCRYPTION = 2
    ENCRYPTION_AND_AUTHENTICATION = 3

class DevicePairingResultStatus(enum.IntEnum):
    PAIRED = 0
    NOT_READY_TO_PAIR = 1
    NOT_PAIRED = 2
    ALREADY_PAIRED = 3
    CONNECTION_REJECTED = 4
    TOO_MANY_CONNECTIONS = 5
    HARDWARE_FAILURE = 6
    AUTHENTICATION_TIMEOUT = 7
    AUTHENTICATION_NOT_ALLOWED = 8
    AUTHENTICATION_FAILURE = 9
    NO_SUPPORTED_PROFILES = 10
    PROTECTION_LEVEL_COULD_NOT_BE_MET = 11
    ACCESS_DENIED = 12
    INVALID_CEREMONY_DATA = 13
    PAIRING_CANCELED = 14
    OPERATION_ALREADY_IN_PROGRESS = 15
    REQUIRED_HANDLER_NOT_REGISTERED = 16
    REJECTED_BY_HANDLER = 17
    REMOTE_DEVICE_HAS_ASSOCIATION = 18
    FAILED = 19

class DevicePickerDisplayStatusOptions(enum.IntFlag):
    NONE = 0
    SHOW_PROGRESS = 0x1
    SHOW_DISCONNECT_BUTTON = 0x2
    SHOW_RETRY_BUTTON = 0x4

class DeviceUnpairingResultStatus(enum.IntEnum):
    UNPAIRED = 0
    ALREADY_UNPAIRED = 1
    OPERATION_ALREADY_IN_PROGRESS = 2
    ACCESS_DENIED = 3
    FAILED = 4

class DeviceWatcherEventKind(enum.IntEnum):
    ADD = 0
    UPDATE = 1
    REMOVE = 2

class DeviceWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class Panel(enum.IntEnum):
    UNKNOWN = 0
    FRONT = 1
    BACK = 2
    TOP = 3
    BOTTOM = 4
    LEFT = 5
    RIGHT = 6

Self = typing.TypeVar('Self')

class DeviceAccessChangedEventArgs(winrt.system.Object):
    status: DeviceAccessStatus
    id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceAccessChangedEventArgs: ...

class DeviceAccessInformation(winrt.system.Object):
    current_status: DeviceAccessStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceAccessInformation: ...
    @staticmethod
    def create_from_device_class(device_class: DeviceClass, /) -> typing.Optional[DeviceAccessInformation]: ...
    @staticmethod
    def create_from_device_class_id(device_class_id: winrt.system.Guid, /) -> typing.Optional[DeviceAccessInformation]: ...
    @staticmethod
    def create_from_id(device_id: str, /) -> typing.Optional[DeviceAccessInformation]: ...
    def add_access_changed(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceAccessInformation, DeviceAccessChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_access_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class DeviceConnectionChangeTriggerDetails(winrt.system.Object):
    device_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceConnectionChangeTriggerDetails: ...

class DeviceDisconnectButtonClickedEventArgs(winrt.system.Object):
    device: typing.Optional[DeviceInformation]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceDisconnectButtonClickedEventArgs: ...

class DeviceInformation(winrt.system.Object):
    enclosure_location: typing.Optional[EnclosureLocation]
    id: str
    is_default: winrt.system.Boolean
    is_enabled: winrt.system.Boolean
    name: str
    properties: typing.Optional[winrt.windows.foundation.collections.IMapView[str, winrt.system.Object]]
    kind: DeviceInformationKind
    pairing: typing.Optional[DeviceInformationPairing]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformation: ...
    @typing.overload
    @staticmethod
    def create_from_id_async(device_id: str, /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    @staticmethod
    def create_from_id_async(device_id: str, additional_properties: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    @staticmethod
    def create_from_id_async(device_id: str, additional_properties: typing.Iterable[str], kind: DeviceInformationKind, /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    @staticmethod
    def create_watcher() -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    @staticmethod
    def create_watcher(device_class: DeviceClass, /) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    @staticmethod
    def create_watcher(aqs_filter: str, additional_properties: typing.Iterable[str], /) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    @staticmethod
    def create_watcher(aqs_filter: str, additional_properties: typing.Iterable[str], kind: DeviceInformationKind, /) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    @staticmethod
    def find_all_async() -> winrt.windows.foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @typing.overload
    @staticmethod
    def find_all_async(device_class: DeviceClass, /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @typing.overload
    @staticmethod
    def find_all_async(aqs_filter: str, additional_properties: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @typing.overload
    @staticmethod
    def find_all_async(aqs_filter: str, additional_properties: typing.Iterable[str], kind: DeviceInformationKind, /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @staticmethod
    def get_aqs_filter_from_device_class(device_class: DeviceClass, /) -> str: ...
    def get_glyph_thumbnail_async(self) -> winrt.windows.foundation.IAsyncOperation[DeviceThumbnail]: ...
    def get_thumbnail_async(self) -> winrt.windows.foundation.IAsyncOperation[DeviceThumbnail]: ...
    def update(self, update_info: typing.Optional[DeviceInformationUpdate], /) -> None: ...

class DeviceInformationCollection(winrt.system.Object, typing.Sequence[DeviceInformation]):
    size: winrt.system.UInt32
    def __len__(self) -> int: ...
    @typing.overload
    def __getitem__(self, index: int) -> DeviceInformation: ...
    @typing.overload
    def __getitem__(self, index: slice) -> winrt.system.Array[DeviceInformation]: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationCollection: ...
    def first(self) -> typing.Optional[winrt.windows.foundation.collections.IIterator[DeviceInformation]]: ...
    def get_at(self, index: winrt.system.UInt32, /) -> typing.Optional[DeviceInformation]: ...
    def get_many(self, start_index: winrt.system.UInt32, items: winrt.system.Array[DeviceInformation], /) -> winrt.system.UInt32: ...
    def index_of(self, value: typing.Optional[DeviceInformation], /) -> typing.Tuple[winrt.system.Boolean, winrt.system.UInt32]: ...

class DeviceInformationCustomPairing(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationCustomPairing: ...
    @typing.overload
    def pair_async(self, pairing_kinds_supported: DevicePairingKinds, /) -> winrt.windows.foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, pairing_kinds_supported: DevicePairingKinds, min_protection_level: DevicePairingProtectionLevel, /) -> winrt.windows.foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, pairing_kinds_supported: DevicePairingKinds, min_protection_level: DevicePairingProtectionLevel, device_pairing_settings: typing.Optional[IDevicePairingSettings], /) -> winrt.windows.foundation.IAsyncOperation[DevicePairingResult]: ...
    def add_pairing_requested(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceInformationCustomPairing, DevicePairingRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pairing_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class DeviceInformationPairing(winrt.system.Object):
    can_pair: winrt.system.Boolean
    is_paired: winrt.system.Boolean
    custom: typing.Optional[DeviceInformationCustomPairing]
    protection_level: DevicePairingProtectionLevel
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationPairing: ...
    @typing.overload
    def pair_async(self) -> winrt.windows.foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, min_protection_level: DevicePairingProtectionLevel, /) -> winrt.windows.foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, min_protection_level: DevicePairingProtectionLevel, device_pairing_settings: typing.Optional[IDevicePairingSettings], /) -> winrt.windows.foundation.IAsyncOperation[DevicePairingResult]: ...
    @staticmethod
    def try_register_for_all_inbound_pairing_requests(pairing_kinds_supported: DevicePairingKinds, /) -> winrt.system.Boolean: ...
    @staticmethod
    def try_register_for_all_inbound_pairing_requests_with_protection_level(pairing_kinds_supported: DevicePairingKinds, min_protection_level: DevicePairingProtectionLevel, /) -> winrt.system.Boolean: ...
    def unpair_async(self) -> winrt.windows.foundation.IAsyncOperation[DeviceUnpairingResult]: ...

class DeviceInformationUpdate(winrt.system.Object):
    id: str
    properties: typing.Optional[winrt.windows.foundation.collections.IMapView[str, winrt.system.Object]]
    kind: DeviceInformationKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationUpdate: ...

class DevicePairingRequestedEventArgs(winrt.system.Object):
    device_information: typing.Optional[DeviceInformation]
    pairing_kind: DevicePairingKinds
    pin: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePairingRequestedEventArgs: ...
    @typing.overload
    def accept(self) -> None: ...
    @typing.overload
    def accept(self, pin: str, /) -> None: ...
    def accept_with_password_credential(self, password_credential: typing.Optional[winrt.windows.security.credentials.PasswordCredential], /) -> None: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class DevicePairingResult(winrt.system.Object):
    protection_level_used: DevicePairingProtectionLevel
    status: DevicePairingResultStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePairingResult: ...

class DevicePicker(winrt.system.Object):
    appearance: typing.Optional[DevicePickerAppearance]
    filter: typing.Optional[DevicePickerFilter]
    requested_properties: typing.Optional[winrt.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePicker: ...
    def __new__(cls: typing.Type[DevicePicker]) -> DevicePicker:...
    def hide(self) -> None: ...
    @typing.overload
    def pick_single_device_async(self, selection: winrt.windows.foundation.Rect, /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    def pick_single_device_async(self, selection: winrt.windows.foundation.Rect, placement: winrt.windows.ui.popups.Placement, /) -> winrt.windows.foundation.IAsyncOperation[DeviceInformation]: ...
    def set_display_status(self, device: typing.Optional[DeviceInformation], status: str, options: DevicePickerDisplayStatusOptions, /) -> None: ...
    @typing.overload
    def show(self, selection: winrt.windows.foundation.Rect, /) -> None: ...
    @typing.overload
    def show(self, selection: winrt.windows.foundation.Rect, placement: winrt.windows.ui.popups.Placement, /) -> None: ...
    def add_device_picker_dismissed(self, handler: winrt.windows.foundation.TypedEventHandler[DevicePicker, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_device_picker_dismissed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_device_selected(self, handler: winrt.windows.foundation.TypedEventHandler[DevicePicker, DeviceSelectedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_device_selected(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_disconnect_button_clicked(self, handler: winrt.windows.foundation.TypedEventHandler[DevicePicker, DeviceDisconnectButtonClickedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_disconnect_button_clicked(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class DevicePickerAppearance(winrt.system.Object):
    title: str
    selected_foreground_color: winrt.windows.ui.Color
    selected_background_color: winrt.windows.ui.Color
    selected_accent_color: winrt.windows.ui.Color
    foreground_color: winrt.windows.ui.Color
    background_color: winrt.windows.ui.Color
    accent_color: winrt.windows.ui.Color
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePickerAppearance: ...

class DevicePickerFilter(winrt.system.Object):
    supported_device_classes: typing.Optional[winrt.windows.foundation.collections.IVector[DeviceClass]]
    supported_device_selectors: typing.Optional[winrt.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePickerFilter: ...

class DeviceSelectedEventArgs(winrt.system.Object):
    selected_device: typing.Optional[DeviceInformation]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceSelectedEventArgs: ...

class DeviceThumbnail(winrt.system.Object):
    content_type: str
    size: winrt.system.UInt64
    can_read: winrt.system.Boolean
    can_write: winrt.system.Boolean
    position: winrt.system.UInt64
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceThumbnail: ...
    def clone_stream(self) -> typing.Optional[winrt.windows.storage.streams.IRandomAccessStream]: ...
    def close(self) -> None: ...
    def flush_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
    def get_input_stream_at(self, position: winrt.system.UInt64, /) -> typing.Optional[winrt.windows.storage.streams.IInputStream]: ...
    def get_output_stream_at(self, position: winrt.system.UInt64, /) -> typing.Optional[winrt.windows.storage.streams.IOutputStream]: ...
    def read_async(self, buffer: typing.Optional[winrt.windows.storage.streams.IBuffer], count: winrt.system.UInt32, options: winrt.windows.storage.streams.InputStreamOptions, /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.windows.storage.streams.IBuffer, winrt.system.UInt32]: ...
    def seek(self, position: winrt.system.UInt64, /) -> None: ...
    def write_async(self, buffer: typing.Optional[winrt.windows.storage.streams.IBuffer], /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...

class DeviceUnpairingResult(winrt.system.Object):
    status: DeviceUnpairingResultStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceUnpairingResult: ...

class DeviceWatcher(winrt.system.Object):
    status: DeviceWatcherStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceWatcher: ...
    def get_background_trigger(self, requested_event_kinds: typing.Iterable[DeviceWatcherEventKind], /) -> typing.Optional[winrt.windows.applicationmodel.background.DeviceWatcherTrigger]: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_added(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceWatcher, DeviceInformation], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_added(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_enumeration_completed(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceWatcher, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_enumeration_completed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_removed(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceWatcher, DeviceInformationUpdate], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_removed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_stopped(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceWatcher, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_stopped(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_updated(self, handler: winrt.windows.foundation.TypedEventHandler[DeviceWatcher, DeviceInformationUpdate], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_updated(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class DeviceWatcherEvent(winrt.system.Object):
    device_information: typing.Optional[DeviceInformation]
    device_information_update: typing.Optional[DeviceInformationUpdate]
    kind: DeviceWatcherEventKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceWatcherEvent: ...

class DeviceWatcherTriggerDetails(winrt.system.Object):
    device_watcher_events: typing.Optional[winrt.windows.foundation.collections.IVectorView[DeviceWatcherEvent]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceWatcherTriggerDetails: ...

class EnclosureLocation(winrt.system.Object):
    in_dock: winrt.system.Boolean
    in_lid: winrt.system.Boolean
    panel: Panel
    rotation_angle_in_degrees_clockwise: winrt.system.UInt32
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> EnclosureLocation: ...

class IDevicePairingSettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IDevicePairingSettings: ...
