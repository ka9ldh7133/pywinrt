// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "pybase.h"
#include "py.Windows.Phone.System.Profile.h"


namespace py::cpp::Windows::Phone::System::Profile
{
    // ----- RetailMode class --------------------
    static constexpr const char* const type_name_RetailMode = "RetailMode";

    static PyObject* _new_RetailMode(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_RetailMode);
        return nullptr;
    }

    static PyObject* RetailMode_get_RetailModeEnabled(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Phone.System.Profile.RetailMode", L"RetailModeEnabled"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(winrt::Windows::Phone::System::Profile::RetailMode::RetailModeEnabled());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_RetailMode[] = {
        { }
    };

    static PyGetSetDef _getset_RetailMode[] = {
        { }
    };

    static PyType_Slot _type_slots_RetailMode[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_RetailMode) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_RetailMode) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_RetailMode) },
        { },
    };

    static PyType_Spec type_spec_RetailMode =
    {
        "_winrt_windows_phone_system_profile.RetailMode",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_RetailMode
    };

    static PyGetSetDef getset_RetailMode_Meta[] = {
        { "retail_mode_enabled", reinterpret_cast<getter>(RetailMode_get_RetailModeEnabled), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot type_slots_RetailMode_Meta[] = 
    {
        { Py_tp_base, reinterpret_cast<void*>(&PyType_Type) },
        { Py_tp_getset, reinterpret_cast<void*>(getset_RetailMode_Meta) },
        { }
    };

    static PyType_Spec type_spec_RetailMode_Meta =
    {
        "_winrt_windows_phone_system_profile.RetailMode_Meta",
        static_cast<int>(PyType_Type.tp_basicsize),
        static_cast<int>(PyType_Type.tp_itemsize),
        Py_TPFLAGS_DEFAULT,
        type_slots_RetailMode_Meta
    };

    // ----- Windows.Phone.System.Profile Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Phone::System::Profile");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_phone_system_profile",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::Phone::System::Profile

PyMODINIT_FUNC PyInit__winrt_windows_phone_system_profile(void) noexcept
{
    using namespace py::cpp::Windows::Phone::System::Profile;

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

    py::pyobj_handle type_RetailMode_Meta{PyType_FromSpec(&type_spec_RetailMode_Meta)};
    if (!type_RetailMode_Meta)
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_RetailMode, &type_spec_RetailMode, nullptr, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_RetailMode_Meta.get())) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_RetailMode, &type_spec_RetailMode, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_RetailMode_Meta.get())) == -1)
    #endif
    {
        return nullptr;
    }


    return module.detach();
}