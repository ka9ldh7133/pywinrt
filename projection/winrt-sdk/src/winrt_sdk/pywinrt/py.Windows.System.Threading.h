// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Foundation.h>

#include <winrt/Windows.System.Threading.h>

namespace py::proj::Windows::System::Threading
{}

namespace py::impl::Windows::System::Threading
{
    struct TimerDestroyedHandler
    {
        static winrt::Windows::System::Threading::TimerDestroyedHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };

                py::pyobj_handle args{ PyTuple_Pack(1, py_param0.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };

    struct TimerElapsedHandler
    {
        static winrt::Windows::System::Threading::TimerElapsedHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };

                py::pyobj_handle args{ PyTuple_Pack(1, py_param0.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };

    struct WorkItemHandler
    {
        static winrt::Windows::System::Threading::WorkItemHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };

                py::pyobj_handle args{ PyTuple_Pack(1, py_param0.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };
}

namespace py::wrapper::Windows::System::Threading
{
    using ThreadPool = py::winrt_wrapper<winrt::Windows::System::Threading::ThreadPool>;
    using ThreadPoolTimer = py::winrt_wrapper<winrt::Windows::System::Threading::ThreadPoolTimer>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::System::Threading::WorkItemOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::System::Threading::WorkItemPriority> = "i";


    template<>
    struct py_type<winrt::Windows::System::Threading::WorkItemOptions>
    {
        static constexpr const char* module_name = "winrt.windows.system.threading";
        static constexpr const char* type_name = "WorkItemOptions";
    };

    template<>
    struct py_type<winrt::Windows::System::Threading::WorkItemPriority>
    {
        static constexpr const char* module_name = "winrt.windows.system.threading";
        static constexpr const char* type_name = "WorkItemPriority";
    };

    template<>
    struct py_type<winrt::Windows::System::Threading::ThreadPool>
    {
        static constexpr const char* module_name = "winrt.windows.system.threading";
        static constexpr const char* type_name = "ThreadPool";
    };

    template<>
    struct py_type<winrt::Windows::System::Threading::ThreadPoolTimer>
    {
        static constexpr const char* module_name = "winrt.windows.system.threading";
        static constexpr const char* type_name = "ThreadPoolTimer";
    };
    template <>
    struct delegate_python_type<winrt::Windows::System::Threading::TimerDestroyedHandler>
    {
        using type = py::impl::Windows::System::Threading::TimerDestroyedHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::System::Threading::TimerElapsedHandler>
    {
        using type = py::impl::Windows::System::Threading::TimerElapsedHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::System::Threading::WorkItemHandler>
    {
        using type = py::impl::Windows::System::Threading::WorkItemHandler;
    };

}