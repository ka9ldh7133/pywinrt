// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Microsoft.Windows.Storage.h"

namespace py::cpp::Microsoft::Windows::Storage
{
    // ----- ApplicationData class --------------------

    static PyObject* _new_ApplicationData(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Microsoft::Windows::Storage::ApplicationData>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Microsoft::Windows::Storage::ApplicationData>::type_name);
        return nullptr;
    }

    static void _dealloc_ApplicationData(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* ApplicationData_ClearAsync(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"ClearAsync", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Microsoft::Windows::Storage::ApplicationDataLocality>(args, 0);

                return py::convert(self->obj.ClearAsync(param0));
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

    static PyObject* ApplicationData_ClearPublisherCacheFolderAsync(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"ClearPublisherCacheFolderAsync", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.ClearPublisherCacheFolderAsync(param0));
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

    static PyObject* ApplicationData_Close(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"Close", 0);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(0);
                    return nullptr;
                }

                self->obj.Close();
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

    static PyObject* ApplicationData_GetDefault(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"GetDefault", 0);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(0);
                    return nullptr;
                }

                return py::convert(winrt::Microsoft::Windows::Storage::ApplicationData::GetDefault());
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

    static PyObject* ApplicationData_GetForPackageFamily(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"GetForPackageFamily", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Microsoft::Windows::Storage::ApplicationData::GetForPackageFamily(param0));
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

    static PyObject* ApplicationData_GetForUser(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"GetForUser", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Windows::System::User>(args, 0);

                return py::convert(winrt::Microsoft::Windows::Storage::ApplicationData::GetForUser(param0));
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

    static PyObject* ApplicationData_GetPublisherCacheFolder(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"GetPublisherCacheFolder", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.GetPublisherCacheFolder(param0));
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

    static PyObject* ApplicationData_GetPublisherCachePath(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationData", L"GetPublisherCachePath", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.GetPublisherCachePath(param0));
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

    static PyObject* ApplicationData_get_IsMachinePathSupported(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"IsMachinePathSupported");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.IsMachinePathSupported());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_LocalCacheFolder(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"LocalCacheFolder");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.LocalCacheFolder());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_LocalCachePath(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"LocalCachePath");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.LocalCachePath());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_LocalFolder(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"LocalFolder");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.LocalFolder());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_LocalPath(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"LocalPath");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.LocalPath());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_LocalSettings(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"LocalSettings");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.LocalSettings());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_MachineFolder(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"MachineFolder");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.MachineFolder());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_MachinePath(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"MachinePath");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.MachinePath());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_SharedLocalFolder(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"SharedLocalFolder");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.SharedLocalFolder());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_SharedLocalPath(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"SharedLocalPath");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.SharedLocalPath());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_TemporaryFolder(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"TemporaryFolder");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.TemporaryFolder());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationData_get_TemporaryPath(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationData", L"TemporaryPath");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.TemporaryPath());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_ApplicationData(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Microsoft::Windows::Storage::ApplicationData>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_ApplicationData(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Microsoft::Windows::Storage::ApplicationData>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_ApplicationData(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* /*unused*/) noexcept
    {
        return Py_NewRef(self);
    }

    static PyObject* _exit_ApplicationData(py::wrapper::Microsoft::Windows::Storage::ApplicationData* self, PyObject* /*unused*/) noexcept
    {
        try
        {
            self->obj.Close();
            Py_RETURN_FALSE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ApplicationData[] = {
        { "clear_async", reinterpret_cast<PyCFunction>(ApplicationData_ClearAsync), METH_VARARGS, nullptr },
        { "clear_publisher_cache_folder_async", reinterpret_cast<PyCFunction>(ApplicationData_ClearPublisherCacheFolderAsync), METH_VARARGS, nullptr },
        { "close", reinterpret_cast<PyCFunction>(ApplicationData_Close), METH_VARARGS, nullptr },
        { "get_publisher_cache_folder", reinterpret_cast<PyCFunction>(ApplicationData_GetPublisherCacheFolder), METH_VARARGS, nullptr },
        { "get_publisher_cache_path", reinterpret_cast<PyCFunction>(ApplicationData_GetPublisherCachePath), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_ApplicationData, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ApplicationData), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_ApplicationData), METH_NOARGS, nullptr },
        { "__exit__", reinterpret_cast<PyCFunction>(_exit_ApplicationData), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_ApplicationData[] = {
        { "is_machine_path_supported", reinterpret_cast<getter>(ApplicationData_get_IsMachinePathSupported), nullptr, nullptr, nullptr },
        { "local_cache_folder", reinterpret_cast<getter>(ApplicationData_get_LocalCacheFolder), nullptr, nullptr, nullptr },
        { "local_cache_path", reinterpret_cast<getter>(ApplicationData_get_LocalCachePath), nullptr, nullptr, nullptr },
        { "local_folder", reinterpret_cast<getter>(ApplicationData_get_LocalFolder), nullptr, nullptr, nullptr },
        { "local_path", reinterpret_cast<getter>(ApplicationData_get_LocalPath), nullptr, nullptr, nullptr },
        { "local_settings", reinterpret_cast<getter>(ApplicationData_get_LocalSettings), nullptr, nullptr, nullptr },
        { "machine_folder", reinterpret_cast<getter>(ApplicationData_get_MachineFolder), nullptr, nullptr, nullptr },
        { "machine_path", reinterpret_cast<getter>(ApplicationData_get_MachinePath), nullptr, nullptr, nullptr },
        { "shared_local_folder", reinterpret_cast<getter>(ApplicationData_get_SharedLocalFolder), nullptr, nullptr, nullptr },
        { "shared_local_path", reinterpret_cast<getter>(ApplicationData_get_SharedLocalPath), nullptr, nullptr, nullptr },
        { "temporary_folder", reinterpret_cast<getter>(ApplicationData_get_TemporaryFolder), nullptr, nullptr, nullptr },
        { "temporary_path", reinterpret_cast<getter>(ApplicationData_get_TemporaryPath), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_ApplicationData[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_ApplicationData) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_ApplicationData) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_ApplicationData) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_ApplicationData) },
        { }
    };

    static PyType_Spec type_spec_ApplicationData = {
        "winrt._winrt_microsoft_windows_storage.ApplicationData",
        sizeof(py::wrapper::Microsoft::Windows::Storage::ApplicationData),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ApplicationData};

    static PyGetSetDef getset_ApplicationData_Static[] = {
        { }
    };

    static PyMethodDef methods_ApplicationData_Static[] = {
        { "get_default", reinterpret_cast<PyCFunction>(ApplicationData_GetDefault), METH_VARARGS, nullptr },
        { "get_for_package_family", reinterpret_cast<PyCFunction>(ApplicationData_GetForPackageFamily), METH_VARARGS, nullptr },
        { "get_for_user", reinterpret_cast<PyCFunction>(ApplicationData_GetForUser), METH_VARARGS, nullptr },
        { }
    };

    static PyType_Slot type_slots_ApplicationData_Static[] = 
    {
        { Py_tp_base, reinterpret_cast<void*>(&PyType_Type) },
        { Py_tp_getset, reinterpret_cast<void*>(getset_ApplicationData_Static) },
        { Py_tp_methods, reinterpret_cast<void*>(methods_ApplicationData_Static) },
        { }
    };

    static PyType_Spec type_spec_ApplicationData_Static =
    {
        "winrt._winrt_microsoft_windows_storage.ApplicationData_Static",
        static_cast<int>(PyType_Type.tp_basicsize),
        static_cast<int>(PyType_Type.tp_itemsize),
        Py_TPFLAGS_DEFAULT,
        type_slots_ApplicationData_Static
    };

    // ----- ApplicationDataContainer class --------------------

    static PyObject* _new_ApplicationDataContainer(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Microsoft::Windows::Storage::ApplicationDataContainer>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Microsoft::Windows::Storage::ApplicationDataContainer>::type_name);
        return nullptr;
    }

    static void _dealloc_ApplicationDataContainer(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* ApplicationDataContainer_Close(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"Close", 0);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(0);
                    return nullptr;
                }

                self->obj.Close();
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

    static PyObject* ApplicationDataContainer_CreateContainer(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"CreateContainer", 2);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(2);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::Microsoft::Windows::Storage::ApplicationDataCreateDisposition>(args, 1);

                return py::convert(self->obj.CreateContainer(param0, param1));
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

    static PyObject* ApplicationDataContainer_DeleteContainer(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"DeleteContainer", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                self->obj.DeleteContainer(param0);
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

    static PyObject* ApplicationDataContainer_get_Containers(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"Containers");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Containers());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationDataContainer_get_Locality(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"Locality");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Locality());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationDataContainer_get_Name(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"Name");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Name());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ApplicationDataContainer_get_Values(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Microsoft.Windows.Storage.ApplicationDataContainer", L"Values");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Values());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_ApplicationDataContainer(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Microsoft::Windows::Storage::ApplicationDataContainer>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_ApplicationDataContainer(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Microsoft::Windows::Storage::ApplicationDataContainer>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_ApplicationDataContainer(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, PyObject* /*unused*/) noexcept
    {
        return Py_NewRef(self);
    }

    static PyObject* _exit_ApplicationDataContainer(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer* self, PyObject* /*unused*/) noexcept
    {
        try
        {
            self->obj.Close();
            Py_RETURN_FALSE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ApplicationDataContainer[] = {
        { "close", reinterpret_cast<PyCFunction>(ApplicationDataContainer_Close), METH_VARARGS, nullptr },
        { "create_container", reinterpret_cast<PyCFunction>(ApplicationDataContainer_CreateContainer), METH_VARARGS, nullptr },
        { "delete_container", reinterpret_cast<PyCFunction>(ApplicationDataContainer_DeleteContainer), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_ApplicationDataContainer, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ApplicationDataContainer), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_ApplicationDataContainer), METH_NOARGS, nullptr },
        { "__exit__", reinterpret_cast<PyCFunction>(_exit_ApplicationDataContainer), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_ApplicationDataContainer[] = {
        { "containers", reinterpret_cast<getter>(ApplicationDataContainer_get_Containers), nullptr, nullptr, nullptr },
        { "locality", reinterpret_cast<getter>(ApplicationDataContainer_get_Locality), nullptr, nullptr, nullptr },
        { "name", reinterpret_cast<getter>(ApplicationDataContainer_get_Name), nullptr, nullptr, nullptr },
        { "values", reinterpret_cast<getter>(ApplicationDataContainer_get_Values), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_ApplicationDataContainer[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_ApplicationDataContainer) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_ApplicationDataContainer) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_ApplicationDataContainer) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_ApplicationDataContainer) },
        { }
    };

    static PyType_Spec type_spec_ApplicationDataContainer = {
        "winrt._winrt_microsoft_windows_storage.ApplicationDataContainer",
        sizeof(py::wrapper::Microsoft::Windows::Storage::ApplicationDataContainer),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ApplicationDataContainer};

    // ----- Microsoft.Windows.Storage Initialization --------------------

    PyDoc_STRVAR(module_doc, "Microsoft.Windows.Storage");

    static PyModuleDef module_def = {
        PyModuleDef_HEAD_INIT,
        "_winrt_microsoft_windows_storage",
        module_doc,
        0,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr};
} // py::cpp::Microsoft::Windows::Storage

PyMODINIT_FUNC PyInit__winrt_microsoft_windows_storage(void) noexcept
{
    using namespace py::cpp::Microsoft::Windows::Storage;

    if (py::import_winrt_runtime() == -1)
    {
        return nullptr;
    }

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

    py::pyobj_handle type_ApplicationData_Static{PyType_FromSpec(&type_spec_ApplicationData_Static)};
    if (!type_ApplicationData_Static)
    {
        return nullptr;
    }

    py::pytype_handle ApplicationData_type{py::register_python_type(module.get(), &type_spec_ApplicationData, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_ApplicationData_Static.get()))};
    if (!ApplicationData_type)
    {
        return nullptr;
    }

    py::pytype_handle ApplicationDataContainer_type{py::register_python_type(module.get(), &type_spec_ApplicationDataContainer, object_bases.get(), nullptr)};
    if (!ApplicationDataContainer_type)
    {
        return nullptr;
    }


    return module.detach();
}