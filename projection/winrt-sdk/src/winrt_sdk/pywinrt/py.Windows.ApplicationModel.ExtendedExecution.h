// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Foundation.h>

#include <winrt/Windows.ApplicationModel.ExtendedExecution.h>

namespace py::proj::Windows::ApplicationModel::ExtendedExecution
{}

namespace py::impl::Windows::ApplicationModel::ExtendedExecution
{}

namespace py::wrapper::Windows::ApplicationModel::ExtendedExecution
{
    using ExtendedExecutionRevokedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionRevokedEventArgs>;
    using ExtendedExecutionSession = py::winrt_wrapper<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionSession>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionReason> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionRevokedReason> = "i";


    template<>
    struct py_type<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionReason>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.extendedexecution";
        static constexpr const char* type_name = "ExtendedExecutionReason";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionResult>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.extendedexecution";
        static constexpr const char* type_name = "ExtendedExecutionResult";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionRevokedReason>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.extendedexecution";
        static constexpr const char* type_name = "ExtendedExecutionRevokedReason";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionRevokedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.extendedexecution";
        static constexpr const char* type_name = "ExtendedExecutionRevokedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::ExtendedExecution::ExtendedExecutionSession>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.extendedexecution";
        static constexpr const char* type_name = "ExtendedExecutionSession";
    };
}