// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "pybase.h"
#include "py.Windows.ApplicationModel.Calls.Provider.h"


namespace py::cpp::Windows::ApplicationModel::Calls::Provider
{
    // ----- PhoneCallOrigin class --------------------
    static constexpr const char* const type_name_PhoneCallOrigin = "PhoneCallOrigin";

    static PyObject* _new_PhoneCallOrigin(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin instance{  };
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

    static void _dealloc_PhoneCallOrigin(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self) noexcept
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

    static PyObject* PhoneCallOrigin_get_Location(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"Location"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.Location());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PhoneCallOrigin_put_Location(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"Location"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return -1;
        }

        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Location(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PhoneCallOrigin_get_CategoryDescription(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"CategoryDescription"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.CategoryDescription());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PhoneCallOrigin_put_CategoryDescription(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"CategoryDescription"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return -1;
        }

        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.CategoryDescription(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PhoneCallOrigin_get_Category(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"Category"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.Category());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PhoneCallOrigin_put_Category(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"Category"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return -1;
        }

        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Category(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PhoneCallOrigin_get_DisplayName(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"DisplayName"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.DisplayName());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PhoneCallOrigin_put_DisplayName(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"DisplayName"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return -1;
        }

        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.DisplayName(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PhoneCallOrigin_get_DisplayPicture(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"DisplayPicture"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.DisplayPicture());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PhoneCallOrigin_put_DisplayPicture(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin", L"DisplayPicture"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return -1;
        }

        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Storage::StorageFile>(arg);

            self->obj.DisplayPicture(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _assign_array_PhoneCallOrigin(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_PhoneCallOrigin(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PhoneCallOrigin[] = {
        { "_assign_array_", _assign_array_PhoneCallOrigin, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PhoneCallOrigin), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PhoneCallOrigin[] = {
        { "location", reinterpret_cast<getter>(PhoneCallOrigin_get_Location), reinterpret_cast<setter>(PhoneCallOrigin_put_Location), nullptr, nullptr },
        { "category_description", reinterpret_cast<getter>(PhoneCallOrigin_get_CategoryDescription), reinterpret_cast<setter>(PhoneCallOrigin_put_CategoryDescription), nullptr, nullptr },
        { "category", reinterpret_cast<getter>(PhoneCallOrigin_get_Category), reinterpret_cast<setter>(PhoneCallOrigin_put_Category), nullptr, nullptr },
        { "display_name", reinterpret_cast<getter>(PhoneCallOrigin_get_DisplayName), reinterpret_cast<setter>(PhoneCallOrigin_put_DisplayName), nullptr, nullptr },
        { "display_picture", reinterpret_cast<getter>(PhoneCallOrigin_get_DisplayPicture), reinterpret_cast<setter>(PhoneCallOrigin_put_DisplayPicture), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PhoneCallOrigin[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_PhoneCallOrigin) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_PhoneCallOrigin) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_PhoneCallOrigin) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_PhoneCallOrigin) },
        { },
    };

    static PyType_Spec type_spec_PhoneCallOrigin =
    {
        "_winrt_windows_applicationmodel_calls_provider.PhoneCallOrigin",
        sizeof(py::wrapper::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PhoneCallOrigin
    };

    // ----- PhoneCallOriginManager class --------------------
    static constexpr const char* const type_name_PhoneCallOriginManager = "PhoneCallOriginManager";

    static PyObject* _new_PhoneCallOriginManager(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_PhoneCallOriginManager);
        return nullptr;
    }

    static PyObject* PhoneCallOriginManager_RequestSetAsActiveCallOriginAppAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager", L"RequestSetAsActiveCallOriginAppAsync", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOriginManager::RequestSetAsActiveCallOriginAppAsync());
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

    static PyObject* PhoneCallOriginManager_SetCallOrigin(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager", L"SetCallOrigin", 2))
            {
                py::set_arg_count_version_error(2);
                return nullptr;
            }

            try
            {
                auto param0 = py::convert_to<winrt::guid>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOrigin>(args, 1);

                winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOriginManager::SetCallOrigin(param0, param1);
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

    static PyObject* PhoneCallOriginManager_ShowPhoneCallOriginSettingsUI(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager", L"ShowPhoneCallOriginSettingsUI", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOriginManager::ShowPhoneCallOriginSettingsUI();
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

    static PyObject* PhoneCallOriginManager_get_IsCurrentAppActiveCallOriginApp(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager", L"IsCurrentAppActiveCallOriginApp"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOriginManager::IsCurrentAppActiveCallOriginApp());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PhoneCallOriginManager_get_IsSupported(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager", L"IsSupported"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Calls::Provider::PhoneCallOriginManager::IsSupported());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PhoneCallOriginManager[] = {
        { "request_set_as_active_call_origin_app_async", reinterpret_cast<PyCFunction>(PhoneCallOriginManager_RequestSetAsActiveCallOriginAppAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "set_call_origin", reinterpret_cast<PyCFunction>(PhoneCallOriginManager_SetCallOrigin), METH_VARARGS | METH_STATIC, nullptr },
        { "show_phone_call_origin_settings_u_i", reinterpret_cast<PyCFunction>(PhoneCallOriginManager_ShowPhoneCallOriginSettingsUI), METH_VARARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PhoneCallOriginManager[] = {
        { }
    };

    static PyType_Slot _type_slots_PhoneCallOriginManager[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_PhoneCallOriginManager) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_PhoneCallOriginManager) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_PhoneCallOriginManager) },
        { },
    };

    static PyType_Spec type_spec_PhoneCallOriginManager =
    {
        "_winrt_windows_applicationmodel_calls_provider.PhoneCallOriginManager",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PhoneCallOriginManager
    };

    static PyGetSetDef getset_PhoneCallOriginManager_Meta[] = {
        { "is_current_app_active_call_origin_app", reinterpret_cast<getter>(PhoneCallOriginManager_get_IsCurrentAppActiveCallOriginApp), nullptr, nullptr, nullptr },
        { "is_supported", reinterpret_cast<getter>(PhoneCallOriginManager_get_IsSupported), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot type_slots_PhoneCallOriginManager_Meta[] = 
    {
        { Py_tp_base, reinterpret_cast<void*>(&PyType_Type) },
        { Py_tp_getset, reinterpret_cast<void*>(getset_PhoneCallOriginManager_Meta) },
        { }
    };

    static PyType_Spec type_spec_PhoneCallOriginManager_Meta =
    {
        "_winrt_windows_applicationmodel_calls_provider.PhoneCallOriginManager_Meta",
        static_cast<int>(PyType_Type.tp_basicsize),
        static_cast<int>(PyType_Type.tp_itemsize),
        Py_TPFLAGS_DEFAULT,
        type_slots_PhoneCallOriginManager_Meta
    };

    // ----- Windows.ApplicationModel.Calls.Provider Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::ApplicationModel::Calls::Provider");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_applicationmodel_calls_provider",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::ApplicationModel::Calls::Provider

PyMODINIT_FUNC PyInit__winrt_windows_applicationmodel_calls_provider(void) noexcept
{
    using namespace py::cpp::Windows::ApplicationModel::Calls::Provider;

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
    if (py::register_python_type(module.get(), type_name_PhoneCallOrigin, &type_spec_PhoneCallOrigin, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_PhoneCallOrigin, &type_spec_PhoneCallOrigin, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }

    py::pyobj_handle type_PhoneCallOriginManager_Meta{PyType_FromSpec(&type_spec_PhoneCallOriginManager_Meta)};
    if (!type_PhoneCallOriginManager_Meta)
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_PhoneCallOriginManager, &type_spec_PhoneCallOriginManager, nullptr, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_PhoneCallOriginManager_Meta.get())) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_PhoneCallOriginManager, &type_spec_PhoneCallOriginManager, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_PhoneCallOriginManager_Meta.get())) == -1)
    #endif
    {
        return nullptr;
    }


    return module.detach();
}