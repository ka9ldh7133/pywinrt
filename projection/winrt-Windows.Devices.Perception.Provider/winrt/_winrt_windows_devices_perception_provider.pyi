# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.perception as windows_devices_perception
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.foundation.numerics as windows_foundation_numerics
import winrt.windows.graphics.imaging as windows_graphics_imaging
import winrt.windows.media as windows_media

from winrt.windows.devices.perception.provider import PerceptionStartFaceAuthenticationHandler, PerceptionStopFaceAuthenticationHandler

Self = typing.TypeVar('Self')

@typing.final
class KnownPerceptionFrameKind_Static(type):
    @_property
    def color(cls) -> str: ...
    @_property
    def depth(cls) -> str: ...
    @_property
    def infrared(cls) -> str: ...

@typing.final
class KnownPerceptionFrameKind(winrt.system.Object, metaclass=KnownPerceptionFrameKind_Static):
    pass

@typing.final
class PerceptionControlGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionControlGroup: ...
    def __new__(cls: typing.Type[Self], ids: typing.Iterable[str]) -> Self: ...
    @_property
    def frame_provider_ids(self) -> typing.Sequence[str]: ...

@typing.final
class PerceptionCorrelation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionCorrelation: ...
    def __new__(cls: typing.Type[Self], target_id: str, position: windows_foundation_numerics.Vector3, orientation: windows_foundation_numerics.Quaternion) -> Self: ...
    @_property
    def orientation(self) -> windows_foundation_numerics.Quaternion: ...
    @_property
    def position(self) -> windows_foundation_numerics.Vector3: ...
    @_property
    def target_id(self) -> str: ...

@typing.final
class PerceptionCorrelationGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionCorrelationGroup: ...
    def __new__(cls: typing.Type[Self], relative_locations: typing.Iterable[PerceptionCorrelation]) -> Self: ...
    @_property
    def relative_locations(self) -> typing.Sequence[PerceptionCorrelation]: ...

@typing.final
class PerceptionFaceAuthenticationGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionFaceAuthenticationGroup: ...
    def __new__(cls: typing.Type[Self], ids: typing.Iterable[str], start_handler: PerceptionStartFaceAuthenticationHandler, stop_handler: PerceptionStopFaceAuthenticationHandler) -> Self: ...
    @_property
    def frame_provider_ids(self) -> typing.Sequence[str]: ...

@typing.final
class PerceptionFrame(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionFrame: ...
    @_property
    def relative_time(self) -> datetime.timedelta: ...
    @relative_time.setter
    def relative_time(self, value: datetime.timedelta) -> None: ...
    @_property
    def frame_data(self) -> windows_foundation.IMemoryBuffer: ...
    @_property
    def properties(self) -> windows_foundation_collections.ValueSet: ...

@typing.final
class PerceptionFrameProviderInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionFrameProviderInfo: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @_property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, value: bool) -> None: ...
    @_property
    def frame_kind(self) -> str: ...
    @frame_kind.setter
    def frame_kind(self, value: str) -> None: ...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @_property
    def device_kind(self) -> str: ...
    @device_kind.setter
    def device_kind(self, value: str) -> None: ...

@typing.final
class PerceptionFrameProviderManagerService_Static(type):
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def publish_frame_for_provider(cls, provider: ImplementsIPerceptionFrameProvider, frame: PerceptionFrame, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def register_control_group(cls, manager: ImplementsIPerceptionFrameProviderManager, control_group: PerceptionControlGroup, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def register_correlation_group(cls, manager: ImplementsIPerceptionFrameProviderManager, correlation_group: PerceptionCorrelationGroup, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def register_face_authentication_group(cls, manager: ImplementsIPerceptionFrameProviderManager, face_authentication_group: PerceptionFaceAuthenticationGroup, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def register_frame_provider_info(cls, manager: ImplementsIPerceptionFrameProviderManager, frame_provider_info: PerceptionFrameProviderInfo, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def unregister_control_group(cls, manager: ImplementsIPerceptionFrameProviderManager, control_group: PerceptionControlGroup, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def unregister_correlation_group(cls, manager: ImplementsIPerceptionFrameProviderManager, correlation_group: PerceptionCorrelationGroup, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def unregister_face_authentication_group(cls, manager: ImplementsIPerceptionFrameProviderManager, face_authentication_group: PerceptionFaceAuthenticationGroup, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def unregister_frame_provider_info(cls, manager: ImplementsIPerceptionFrameProviderManager, frame_provider_info: PerceptionFrameProviderInfo, /) -> None: ...
    # @deprecated("PerceptionFrameProviderManagerService may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def update_availability_for_provider(cls, provider: ImplementsIPerceptionFrameProvider, available: bool, /) -> None: ...

@typing.final
class PerceptionFrameProviderManagerService(winrt.system.Object, metaclass=PerceptionFrameProviderManagerService_Static):
    pass

@typing.final
class PerceptionPropertyChangeRequest(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionPropertyChangeRequest: ...
    # @deprecated("PerceptionPropertyChangeRequest may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def get_deferral(self) -> windows_foundation.Deferral: ...
    @_property
    def status(self) -> windows_devices_perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @status.setter
    def status(self, value: windows_devices_perception.PerceptionFrameSourcePropertyChangeStatus) -> None: ...
    @_property
    def name(self) -> str: ...
    @_property
    def value(self) -> winrt.system.Object: ...

@typing.final
class PerceptionVideoFrameAllocator(winrt.system.Object, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PerceptionVideoFrameAllocator: ...
    def __new__(cls: typing.Type[Self], max_outstanding_frame_count_for_write: winrt.system.UInt32, format: windows_graphics_imaging.BitmapPixelFormat, resolution: windows_foundation.Size, alpha: windows_graphics_imaging.BitmapAlphaMode) -> Self: ...
    # @deprecated("PerceptionVideoFrameAllocator may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def allocate_frame(self) -> PerceptionFrame: ...
    def close(self) -> None: ...
    # @deprecated("PerceptionVideoFrameAllocator may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def copy_from_video_frame(self, frame: windows_media.VideoFrame, /) -> PerceptionFrame: ...

class ImplementsIPerceptionFrameProvider():
    pass

@typing.final
class IPerceptionFrameProvider(winrt.system.Object, ImplementsIPerceptionFrameProvider, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IPerceptionFrameProvider: ...
    def close(self) -> None: ...
    # @deprecated("IPerceptionFrameProvider may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def set_property(self, value: PerceptionPropertyChangeRequest, /) -> None: ...
    # @deprecated("IPerceptionFrameProvider may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def start(self) -> None: ...
    # @deprecated("IPerceptionFrameProvider may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def stop(self) -> None: ...
    @_property
    def available(self) -> bool: ...
    @_property
    def frame_provider_info(self) -> PerceptionFrameProviderInfo: ...
    @_property
    def properties(self) -> windows_foundation_collections.IPropertySet: ...

class ImplementsIPerceptionFrameProviderManager():
    pass

@typing.final
class IPerceptionFrameProviderManager(winrt.system.Object, ImplementsIPerceptionFrameProviderManager, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IPerceptionFrameProviderManager: ...
    def close(self) -> None: ...
    # @deprecated("IPerceptionFrameProviderManager may be unavailable after Windows Creator Update. Please refer to AVStream on MSDN.")
    def get_frame_provider(self, frame_provider_info: PerceptionFrameProviderInfo, /) -> IPerceptionFrameProvider: ...

