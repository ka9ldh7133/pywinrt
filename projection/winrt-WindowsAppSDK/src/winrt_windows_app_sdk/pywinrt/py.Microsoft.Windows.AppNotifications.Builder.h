// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Microsoft.Windows.AppNotifications.h")
#include "py.Microsoft.Windows.AppNotifications.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Microsoft.Windows.AppNotifications.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>

#include <winrt/Microsoft.Windows.AppNotifications.Builder.h>

namespace py::proj::Microsoft::Windows::AppNotifications::Builder
{}

namespace py::impl::Microsoft::Windows::AppNotifications::Builder
{}

namespace py::wrapper::Microsoft::Windows::AppNotifications::Builder
{
    using AppNotificationBuilder = py::winrt_wrapper<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationBuilder>;
    using AppNotificationButton = py::winrt_wrapper<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationButton>;
    using AppNotificationComboBox = py::winrt_wrapper<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationComboBox>;
    using AppNotificationProgressBar = py::winrt_wrapper<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationProgressBar>;
    using AppNotificationTextProperties = py::winrt_wrapper<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationTextProperties>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationAudioLooping> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationButtonStyle> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationDuration> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationImageCrop> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationScenario> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationSoundEvent> = "i";


    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationAudioLooping>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationAudioLooping";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationButtonStyle>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationButtonStyle";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationDuration>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationDuration";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationImageCrop>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationImageCrop";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationScenario>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationScenario";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationSoundEvent>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationSoundEvent";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationBuilder>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationBuilder";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationButton>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationButton";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationComboBox>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationComboBox";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationProgressBar>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationProgressBar";
    };

    template<>
    struct py_type<winrt::Microsoft::Windows::AppNotifications::Builder::AppNotificationTextProperties>
    {
        static constexpr const char* module_name = "winrt.microsoft.windows.appnotifications.builder";
        static constexpr const char* type_name = "AppNotificationTextProperties";
    };
}