// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Microsoft.UI.Xaml.Markup.h")
#include "py.Microsoft.UI.Xaml.Markup.h"
#endif

#if __has_include("py.Windows.UI.Xaml.Interop.h")
#include "py.Windows.UI.Xaml.Interop.h"
#endif

#include <winrt/Microsoft.UI.Xaml.Markup.h>
#include <winrt/Windows.UI.Xaml.Interop.h>

#include <winrt/Microsoft.UI.Xaml.XamlTypeInfo.h>

namespace py::proj::Microsoft::UI::Xaml::XamlTypeInfo
{}

namespace py::impl::Microsoft::UI::Xaml::XamlTypeInfo
{}

namespace py::wrapper::Microsoft::UI::Xaml::XamlTypeInfo
{
    using XamlControlsXamlMetaDataProvider = py::winrt_wrapper<winrt::Microsoft::UI::Xaml::XamlTypeInfo::XamlControlsXamlMetaDataProvider>;
}

namespace py
{

    template<>
    struct py_type<winrt::Microsoft::UI::Xaml::XamlTypeInfo::XamlControlsXamlMetaDataProvider>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui.xaml.xamltypeinfo";
        static constexpr const char* type_name = "XamlControlsXamlMetaDataProvider";
    };
}