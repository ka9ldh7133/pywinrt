// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"


#include <winrt/Windows.UI.UIAutomation.h>

namespace py::proj::Windows::UI::UIAutomation
{}

namespace py::impl::Windows::UI::UIAutomation
{}

namespace py::wrapper::Windows::UI::UIAutomation
{
    using AutomationConnection = py::winrt_wrapper<winrt::Windows::UI::UIAutomation::AutomationConnection>;
    using AutomationConnectionBoundObject = py::winrt_wrapper<winrt::Windows::UI::UIAutomation::AutomationConnectionBoundObject>;
    using AutomationElement = py::winrt_wrapper<winrt::Windows::UI::UIAutomation::AutomationElement>;
    using AutomationTextRange = py::winrt_wrapper<winrt::Windows::UI::UIAutomation::AutomationTextRange>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::UI::UIAutomation::AutomationConnection>
    {
        static constexpr const char* module_name = "winrt.windows.ui.uiautomation";
        static constexpr const char* type_name = "AutomationConnection";
    };

    template<>
    struct py_type<winrt::Windows::UI::UIAutomation::AutomationConnectionBoundObject>
    {
        static constexpr const char* module_name = "winrt.windows.ui.uiautomation";
        static constexpr const char* type_name = "AutomationConnectionBoundObject";
    };

    template<>
    struct py_type<winrt::Windows::UI::UIAutomation::AutomationElement>
    {
        static constexpr const char* module_name = "winrt.windows.ui.uiautomation";
        static constexpr const char* type_name = "AutomationElement";
    };

    template<>
    struct py_type<winrt::Windows::UI::UIAutomation::AutomationTextRange>
    {
        static constexpr const char* module_name = "winrt.windows.ui.uiautomation";
        static constexpr const char* type_name = "AutomationTextRange";
    };
}