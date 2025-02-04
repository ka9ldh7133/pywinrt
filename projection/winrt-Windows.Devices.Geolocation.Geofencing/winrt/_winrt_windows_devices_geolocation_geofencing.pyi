# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.geolocation as windows_devices_geolocation
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections

from winrt.windows.devices.geolocation.geofencing import GeofenceMonitorStatus, GeofenceRemovalReason, GeofenceState, MonitoredGeofenceStates

Self = typing.TypeVar('Self')

@typing.final
class Geofence(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Geofence: ...
    @typing.overload
    def __new__(cls: typing.Type[Self], id: str, geoshape: windows_devices_geolocation.ImplementsIGeoshape) -> Self: ...
    @typing.overload
    def __new__(cls: typing.Type[Self], id: str, geoshape: windows_devices_geolocation.ImplementsIGeoshape, monitored_states: MonitoredGeofenceStates, single_use: bool) -> Self: ...
    @typing.overload
    def __new__(cls: typing.Type[Self], id: str, geoshape: windows_devices_geolocation.ImplementsIGeoshape, monitored_states: MonitoredGeofenceStates, single_use: bool, dwell_time: datetime.timedelta) -> Self: ...
    @typing.overload
    def __new__(cls: typing.Type[Self], id: str, geoshape: windows_devices_geolocation.ImplementsIGeoshape, monitored_states: MonitoredGeofenceStates, single_use: bool, dwell_time: datetime.timedelta, start_time: datetime.datetime, duration: datetime.timedelta) -> Self: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def dwell_time(self) -> datetime.timedelta: ...
    @_property
    def geoshape(self) -> windows_devices_geolocation.IGeoshape: ...
    @_property
    def id(self) -> str: ...
    @_property
    def monitored_states(self) -> MonitoredGeofenceStates: ...
    @_property
    def single_use(self) -> bool: ...
    @_property
    def start_time(self) -> datetime.datetime: ...

@typing.final
class GeofenceMonitor_Static(type):
    @_property
    def current(cls) -> GeofenceMonitor: ...

@typing.final
class GeofenceMonitor(winrt.system.Object, metaclass=GeofenceMonitor_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GeofenceMonitor: ...
    def read_reports(self) -> typing.Sequence[GeofenceStateChangeReport]: ...
    def add_geofence_state_changed(self, event_handler: windows_foundation.TypedEventHandler[GeofenceMonitor, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_geofence_state_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_status_changed(self, event_handler: windows_foundation.TypedEventHandler[GeofenceMonitor, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_status_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def geofences(self) -> typing.MutableSequence[Geofence]: ...
    @_property
    def last_known_geoposition(self) -> windows_devices_geolocation.Geoposition: ...
    @_property
    def status(self) -> GeofenceMonitorStatus: ...

@typing.final
class GeofenceStateChangeReport(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GeofenceStateChangeReport: ...
    @_property
    def geofence(self) -> Geofence: ...
    @_property
    def geoposition(self) -> windows_devices_geolocation.Geoposition: ...
    @_property
    def new_state(self) -> GeofenceState: ...
    @_property
    def removal_reason(self) -> GeofenceRemovalReason: ...

