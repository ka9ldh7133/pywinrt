// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "pybase.h"
#include "py.Windows.System.Display.h"


namespace py::cpp::Windows::System::Display
{
    // ----- DisplayRequest class --------------------
    static constexpr const char* const type_name_DisplayRequest = "DisplayRequest";

    static PyObject* _new_DisplayRequest(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        auto arg_count = PyTuple_Size(args);
        if (arg_count == 0)
        {
            try
            {
                winrt::Windows::System::Display::DisplayRequest instance{  };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static void _dealloc_DisplayRequest(py::wrapper::Windows::System::Display::DisplayRequest* self) noexcept
    {
        auto tp = Py_TYPE(self);

        if (PyType_IS_GC(tp))
        {
            PyObject_GC_UnTrack(self);
        }

        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* DisplayRequest_RequestActive(py::wrapper::Windows::System::Display::DisplayRequest* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.System.Display.DisplayRequest", L"RequestActive", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                self->obj.RequestActive();
                Py_RETURN_NONE;
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* DisplayRequest_RequestRelease(py::wrapper::Windows::System::Display::DisplayRequest* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.System.Display.DisplayRequest", L"RequestRelease", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                self->obj.RequestRelease();
                Py_RETURN_NONE;
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* _assign_array_DisplayRequest(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::System::Display::DisplayRequest>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_DisplayRequest(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Display::DisplayRequest>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_DisplayRequest[] = {
        { "request_active", reinterpret_cast<PyCFunction>(DisplayRequest_RequestActive), METH_VARARGS, nullptr },
        { "request_release", reinterpret_cast<PyCFunction>(DisplayRequest_RequestRelease), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_DisplayRequest, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_DisplayRequest), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_DisplayRequest[] = {
        { }
    };

    static PyType_Slot _type_slots_DisplayRequest[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_DisplayRequest) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_DisplayRequest) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_DisplayRequest) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_DisplayRequest) },
        { },
    };

    static PyType_Spec type_spec_DisplayRequest =
    {
        "_winrt_windows_system_display.DisplayRequest",
        sizeof(py::wrapper::Windows::System::Display::DisplayRequest),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_DisplayRequest
    };

    // ----- Windows.System.Display Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::System::Display");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_system_display",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::System::Display

PyMODINIT_FUNC PyInit__winrt_windows_system_display(void) noexcept
{
    using namespace py::cpp::Windows::System::Display;

    py::pyobj_handle module{PyModule_Create(&module_def)};

    if (!module)
    {
        return nullptr;
    }

    auto object_type = py::get_object_type();
    if (!object_type)
    {
        return nullptr;
    }

    py::pyobj_handle object_bases{PyTuple_Pack(1, object_type)};

    if (!object_bases)
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_DisplayRequest, &type_spec_DisplayRequest, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_DisplayRequest, &type_spec_DisplayRequest, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }


    return module.detach();
}