// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Geolocation.h")
#include "py.Windows.Devices.Geolocation.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Devices.Geolocation.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>

#include <winrt/Windows.Devices.Geolocation.Geofencing.h>

namespace py::proj::Windows::Devices::Geolocation::Geofencing
{}

namespace py::impl::Windows::Devices::Geolocation::Geofencing
{}

namespace py::wrapper::Windows::Devices::Geolocation::Geofencing
{
    using Geofence = py::winrt_wrapper<winrt::Windows::Devices::Geolocation::Geofencing::Geofence>;
    using GeofenceMonitor = py::winrt_wrapper<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceMonitor>;
    using GeofenceStateChangeReport = py::winrt_wrapper<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceStateChangeReport>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceMonitorStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceRemovalReason> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceState> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Geolocation::Geofencing::MonitoredGeofenceStates> = "I";


    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceMonitorStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "GeofenceMonitorStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceRemovalReason>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "GeofenceRemovalReason";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceState>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "GeofenceState";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::MonitoredGeofenceStates>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "MonitoredGeofenceStates";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::Geofence>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "Geofence";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceMonitor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "GeofenceMonitor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Geolocation::Geofencing::GeofenceStateChangeReport>
    {
        static constexpr const char* module_name = "winrt.windows.devices.geolocation.geofencing";
        static constexpr const char* type_name = "GeofenceStateChangeReport";
    };
}