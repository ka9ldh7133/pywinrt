// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.UI.h")
#include "py.Windows.UI.h"
#endif

#include <winrt/Windows.UI.h>

#include <winrt/Windows.UI.Notifications.Preview.h>

namespace py::proj::Windows::UI::Notifications::Preview
{}

namespace py::impl::Windows::UI::Notifications::Preview
{}

namespace py::wrapper::Windows::UI::Notifications::Preview
{
    using ToastOcclusionManagerPreview = py::winrt_wrapper<winrt::Windows::UI::Notifications::Preview::ToastOcclusionManagerPreview>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::UI::Notifications::Preview::ToastOcclusionManagerPreview>
    {
        static constexpr const char* module_name = "winrt.windows.ui.notifications.preview";
        static constexpr const char* type_name = "ToastOcclusionManagerPreview";
    };
}