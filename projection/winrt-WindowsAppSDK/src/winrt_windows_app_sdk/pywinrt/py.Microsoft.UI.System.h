// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Microsoft.UI.h")
#include "py.Microsoft.UI.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Microsoft.UI.h>
#include <winrt/Windows.Foundation.h>

#include <winrt/Microsoft.UI.System.h>

namespace py::proj::Microsoft::UI::System
{}

namespace py::impl::Microsoft::UI::System
{}

namespace py::wrapper::Microsoft::UI::System
{
    using ThemeSettings = py::winrt_wrapper<winrt::Microsoft::UI::System::ThemeSettings>;
}

namespace py
{

    template<>
    struct py_type<winrt::Microsoft::UI::System::ThemeSettings>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui.system";
        static constexpr const char* type_name = "ThemeSettings";
    };
}