// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.I2c.Provider.h")
#include "py.Windows.Devices.I2c.Provider.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Devices.I2c.Provider.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>

#include <winrt/Windows.Devices.I2c.h>

namespace py::proj::Windows::Devices::I2c
{}

namespace py::impl::Windows::Devices::I2c
{}

namespace py::wrapper::Windows::Devices::I2c
{
    using I2cConnectionSettings = py::winrt_wrapper<winrt::Windows::Devices::I2c::I2cConnectionSettings>;
    using I2cController = py::winrt_wrapper<winrt::Windows::Devices::I2c::I2cController>;
    using I2cDevice = py::winrt_wrapper<winrt::Windows::Devices::I2c::I2cDevice>;
    using II2cDeviceStatics = py::winrt_wrapper<winrt::Windows::Devices::I2c::II2cDeviceStatics>;
    using I2cTransferResult = py::winrt_struct_wrapper<winrt::Windows::Devices::I2c::I2cTransferResult>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::I2c::I2cBusSpeed> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::I2c::I2cSharingMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::I2c::I2cTransferStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::I2c::I2cTransferResult> = "T{i:status:I:bytes_transferred:}";


    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cBusSpeed>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cBusSpeed";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cSharingMode>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cSharingMode";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cTransferStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cTransferStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cConnectionSettings>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cConnectionSettings";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cController>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cController";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cDevice>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cDevice";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::II2cDeviceStatics>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "II2cDeviceStatics";
    };

    template<>
    struct py_type<winrt::Windows::Devices::I2c::I2cTransferResult>
    {
        static constexpr const char* module_name = "winrt.windows.devices.i2c";
        static constexpr const char* type_name = "I2cTransferResult";
    };
}