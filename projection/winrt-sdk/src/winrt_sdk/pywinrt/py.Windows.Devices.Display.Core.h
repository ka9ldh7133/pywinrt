// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Display.h")
#include "py.Windows.Devices.Display.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Foundation.Numerics.h")
#include "py.Windows.Foundation.Numerics.h"
#endif

#if __has_include("py.Windows.Graphics.h")
#include "py.Windows.Graphics.h"
#endif

#if __has_include("py.Windows.Graphics.DirectX.h")
#include "py.Windows.Graphics.DirectX.h"
#endif

#if __has_include("py.Windows.Graphics.DirectX.Direct3D11.h")
#include "py.Windows.Graphics.DirectX.Direct3D11.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Devices.Display.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Foundation.Numerics.h>
#include <winrt/Windows.Graphics.h>
#include <winrt/Windows.Graphics.DirectX.h>
#include <winrt/Windows.Graphics.DirectX.Direct3D11.h>
#include <winrt/Windows.Storage.Streams.h>

#include <winrt/Windows.Devices.Display.Core.h>

namespace py::proj::Windows::Devices::Display::Core
{}

namespace py::impl::Windows::Devices::Display::Core
{}

namespace py::wrapper::Windows::Devices::Display::Core
{
    using DisplayAdapter = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayAdapter>;
    using DisplayDevice = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayDevice>;
    using DisplayFence = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayFence>;
    using DisplayManager = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayManager>;
    using DisplayManagerChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayManagerChangedEventArgs>;
    using DisplayManagerDisabledEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayManagerDisabledEventArgs>;
    using DisplayManagerEnabledEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayManagerEnabledEventArgs>;
    using DisplayManagerPathsFailedOrInvalidatedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayManagerPathsFailedOrInvalidatedEventArgs>;
    using DisplayManagerResultWithState = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayManagerResultWithState>;
    using DisplayModeInfo = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayModeInfo>;
    using DisplayPath = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayPath>;
    using DisplayPrimaryDescription = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayPrimaryDescription>;
    using DisplayScanout = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayScanout>;
    using DisplaySource = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplaySource>;
    using DisplayState = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayState>;
    using DisplayStateOperationResult = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayStateOperationResult>;
    using DisplaySurface = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplaySurface>;
    using DisplayTarget = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayTarget>;
    using DisplayTask = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayTask>;
    using DisplayTaskPool = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayTaskPool>;
    using DisplayTaskResult = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayTaskResult>;
    using DisplayView = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayView>;
    using DisplayWireFormat = py::winrt_wrapper<winrt::Windows::Devices::Display::Core::DisplayWireFormat>;
    using DisplayPresentationRate = py::winrt_struct_wrapper<winrt::Windows::Devices::Display::Core::DisplayPresentationRate>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayBitsPerChannel> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayDeviceCapability> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayManagerOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayManagerResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayModeQueryOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayPathScaling> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayPathStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayPresentStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayRotation> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayScanoutOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplaySourceStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayStateApplyOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayStateFunctionalizeOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayStateOperationStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayTargetPersistence> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayTaskSignalKind> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayWireFormatColorSpace> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayWireFormatEotf> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayWireFormatHdrMetadata> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayWireFormatPixelEncoding> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Display::Core::DisplayPresentationRate> = "T{T{I:numerator:I:denominator:}:vertical_sync_rate:i:vertical_syncs_per_presentation:}";


    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayBitsPerChannel>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayBitsPerChannel";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayDeviceCapability>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayDeviceCapability";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerResult>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerResult";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayModeQueryOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayModeQueryOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayPathScaling>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayPathScaling";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayPathStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayPathStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayPresentStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayPresentStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayRotation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayRotation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayScanoutOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayScanoutOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplaySourceStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplaySourceStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayStateApplyOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayStateApplyOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayStateFunctionalizeOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayStateFunctionalizeOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayStateOperationStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayStateOperationStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayTargetPersistence>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayTargetPersistence";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayTaskSignalKind>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayTaskSignalKind";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayWireFormatColorSpace>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayWireFormatColorSpace";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayWireFormatEotf>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayWireFormatEotf";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayWireFormatHdrMetadata>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayWireFormatHdrMetadata";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayWireFormatPixelEncoding>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayWireFormatPixelEncoding";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayAdapter>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayAdapter";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayDevice>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayDevice";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayFence>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayFence";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManager>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManager";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerDisabledEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerDisabledEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerEnabledEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerEnabledEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerPathsFailedOrInvalidatedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerPathsFailedOrInvalidatedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayManagerResultWithState>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayManagerResultWithState";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayModeInfo>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayModeInfo";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayPath>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayPath";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayPrimaryDescription>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayPrimaryDescription";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayScanout>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayScanout";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplaySource>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplaySource";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayState>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayState";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayStateOperationResult>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayStateOperationResult";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplaySurface>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplaySurface";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayTarget>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayTarget";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayTask>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayTask";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayTaskPool>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayTaskPool";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayTaskResult>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayTaskResult";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayView>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayView";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayWireFormat>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayWireFormat";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Display::Core::DisplayPresentationRate>
    {
        static constexpr const char* module_name = "winrt.windows.devices.display.core";
        static constexpr const char* type_name = "DisplayPresentationRate";
    };
}