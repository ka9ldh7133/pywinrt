// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "pybase.h"
#include "py.Windows.Media.AppBroadcasting.h"


namespace py::cpp::Windows::Media::AppBroadcasting
{
    // ----- AppBroadcastingMonitor class --------------------
    static constexpr const char* const type_name_AppBroadcastingMonitor = "AppBroadcastingMonitor";

    static PyObject* _new_AppBroadcastingMonitor(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Media::AppBroadcasting::AppBroadcastingMonitor instance{  };
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

    static void _dealloc_AppBroadcastingMonitor(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingMonitor* self) noexcept
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

    static PyObject* AppBroadcastingMonitor_get_IsCurrentAppBroadcasting(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingMonitor* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingMonitor", L"IsCurrentAppBroadcasting"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsCurrentAppBroadcasting());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingMonitor_add_IsCurrentAppBroadcastingChanged(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingMonitor* self, PyObject* arg) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsEventPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingMonitor", L"IsCurrentAppBroadcastingChanged"))
        {
            PyErr_SetString(PyExc_AttributeError, "event is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::Media::AppBroadcasting::AppBroadcastingMonitor, winrt::Windows::Foundation::IInspectable>>(arg);

            return py::convert(self->obj.IsCurrentAppBroadcastingChanged(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingMonitor_remove_IsCurrentAppBroadcastingChanged(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingMonitor* self, PyObject* arg) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsEventPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingMonitor", L"IsCurrentAppBroadcastingChanged"))
        {
            PyErr_SetString(PyExc_AttributeError, "event is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.IsCurrentAppBroadcastingChanged(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_AppBroadcastingMonitor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Media::AppBroadcasting::AppBroadcastingMonitor>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_AppBroadcastingMonitor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::AppBroadcasting::AppBroadcastingMonitor>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_AppBroadcastingMonitor[] = {
        { "add_is_current_app_broadcasting_changed", reinterpret_cast<PyCFunction>(AppBroadcastingMonitor_add_IsCurrentAppBroadcastingChanged), METH_O, nullptr },
        { "remove_is_current_app_broadcasting_changed", reinterpret_cast<PyCFunction>(AppBroadcastingMonitor_remove_IsCurrentAppBroadcastingChanged), METH_O, nullptr },
        { "_assign_array_", _assign_array_AppBroadcastingMonitor, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_AppBroadcastingMonitor), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AppBroadcastingMonitor[] = {
        { "is_current_app_broadcasting", reinterpret_cast<getter>(AppBroadcastingMonitor_get_IsCurrentAppBroadcasting), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_AppBroadcastingMonitor[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_AppBroadcastingMonitor) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_AppBroadcastingMonitor) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_AppBroadcastingMonitor) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_AppBroadcastingMonitor) },
        { },
    };

    static PyType_Spec type_spec_AppBroadcastingMonitor =
    {
        "_winrt_windows_media_appbroadcasting.AppBroadcastingMonitor",
        sizeof(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingMonitor),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AppBroadcastingMonitor
    };

    // ----- AppBroadcastingStatus class --------------------
    static constexpr const char* const type_name_AppBroadcastingStatus = "AppBroadcastingStatus";

    static PyObject* _new_AppBroadcastingStatus(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_AppBroadcastingStatus);
        return nullptr;
    }

    static void _dealloc_AppBroadcastingStatus(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatus* self) noexcept
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

    static PyObject* AppBroadcastingStatus_get_CanStartBroadcast(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatus* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatus", L"CanStartBroadcast"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.CanStartBroadcast());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatus_get_Details(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatus* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatus", L"Details"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.Details());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_AppBroadcastingStatus(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Media::AppBroadcasting::AppBroadcastingStatus>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_AppBroadcastingStatus(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::AppBroadcasting::AppBroadcastingStatus>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_AppBroadcastingStatus[] = {
        { "_assign_array_", _assign_array_AppBroadcastingStatus, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_AppBroadcastingStatus), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AppBroadcastingStatus[] = {
        { "can_start_broadcast", reinterpret_cast<getter>(AppBroadcastingStatus_get_CanStartBroadcast), nullptr, nullptr, nullptr },
        { "details", reinterpret_cast<getter>(AppBroadcastingStatus_get_Details), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_AppBroadcastingStatus[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_AppBroadcastingStatus) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_AppBroadcastingStatus) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_AppBroadcastingStatus) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_AppBroadcastingStatus) },
        { },
    };

    static PyType_Spec type_spec_AppBroadcastingStatus =
    {
        "_winrt_windows_media_appbroadcasting.AppBroadcastingStatus",
        sizeof(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatus),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AppBroadcastingStatus
    };

    // ----- AppBroadcastingStatusDetails class --------------------
    static constexpr const char* const type_name_AppBroadcastingStatusDetails = "AppBroadcastingStatusDetails";

    static PyObject* _new_AppBroadcastingStatusDetails(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_AppBroadcastingStatusDetails);
        return nullptr;
    }

    static void _dealloc_AppBroadcastingStatusDetails(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self) noexcept
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

    static PyObject* AppBroadcastingStatusDetails_get_IsAnyAppBroadcasting(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsAnyAppBroadcasting"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsAnyAppBroadcasting());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsAppInactive(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsAppInactive"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsAppInactive());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsBlockedForApp(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsBlockedForApp"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsBlockedForApp());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsCaptureResourceUnavailable(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsCaptureResourceUnavailable"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsCaptureResourceUnavailable());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsDisabledBySystem(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsDisabledBySystem"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsDisabledBySystem());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsDisabledByUser(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsDisabledByUser"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsDisabledByUser());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsGameStreamInProgress(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsGameStreamInProgress"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsGameStreamInProgress());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppBroadcastingStatusDetails_get_IsGpuConstrained(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails* self, void* /*unused*/) noexcept
    {
        if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails", L"IsGpuConstrained"))
        {
            PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
            return nullptr;
        }

        try
        {
            return py::convert(self->obj.IsGpuConstrained());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_AppBroadcastingStatusDetails(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_AppBroadcastingStatusDetails(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_AppBroadcastingStatusDetails[] = {
        { "_assign_array_", _assign_array_AppBroadcastingStatusDetails, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_AppBroadcastingStatusDetails), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AppBroadcastingStatusDetails[] = {
        { "is_any_app_broadcasting", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsAnyAppBroadcasting), nullptr, nullptr, nullptr },
        { "is_app_inactive", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsAppInactive), nullptr, nullptr, nullptr },
        { "is_blocked_for_app", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsBlockedForApp), nullptr, nullptr, nullptr },
        { "is_capture_resource_unavailable", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsCaptureResourceUnavailable), nullptr, nullptr, nullptr },
        { "is_disabled_by_system", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsDisabledBySystem), nullptr, nullptr, nullptr },
        { "is_disabled_by_user", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsDisabledByUser), nullptr, nullptr, nullptr },
        { "is_game_stream_in_progress", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsGameStreamInProgress), nullptr, nullptr, nullptr },
        { "is_gpu_constrained", reinterpret_cast<getter>(AppBroadcastingStatusDetails_get_IsGpuConstrained), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_AppBroadcastingStatusDetails[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_AppBroadcastingStatusDetails) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_AppBroadcastingStatusDetails) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_AppBroadcastingStatusDetails) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_AppBroadcastingStatusDetails) },
        { },
    };

    static PyType_Spec type_spec_AppBroadcastingStatusDetails =
    {
        "_winrt_windows_media_appbroadcasting.AppBroadcastingStatusDetails",
        sizeof(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingStatusDetails),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AppBroadcastingStatusDetails
    };

    // ----- AppBroadcastingUI class --------------------
    static constexpr const char* const type_name_AppBroadcastingUI = "AppBroadcastingUI";

    static PyObject* _new_AppBroadcastingUI(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_AppBroadcastingUI);
        return nullptr;
    }

    static void _dealloc_AppBroadcastingUI(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingUI* self) noexcept
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

    static PyObject* AppBroadcastingUI_GetDefault(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingUI", L"GetDefault", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(winrt::Windows::Media::AppBroadcasting::AppBroadcastingUI::GetDefault());
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

    static PyObject* AppBroadcastingUI_GetForUser(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingUI", L"GetForUser", 1))
            {
                py::set_arg_count_version_error(1);
                return nullptr;
            }

            try
            {
                auto param0 = py::convert_to<winrt::Windows::System::User>(args, 0);

                return py::convert(winrt::Windows::Media::AppBroadcasting::AppBroadcastingUI::GetForUser(param0));
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

    static PyObject* AppBroadcastingUI_GetStatus(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingUI* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingUI", L"GetStatus", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(self->obj.GetStatus());
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

    static PyObject* AppBroadcastingUI_ShowBroadcastUI(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingUI* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.AppBroadcasting.AppBroadcastingUI", L"ShowBroadcastUI", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                self->obj.ShowBroadcastUI();
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

    static PyObject* _assign_array_AppBroadcastingUI(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Media::AppBroadcasting::AppBroadcastingUI>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_AppBroadcastingUI(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::AppBroadcasting::AppBroadcastingUI>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_AppBroadcastingUI[] = {
        { "get_default", reinterpret_cast<PyCFunction>(AppBroadcastingUI_GetDefault), METH_VARARGS | METH_STATIC, nullptr },
        { "get_for_user", reinterpret_cast<PyCFunction>(AppBroadcastingUI_GetForUser), METH_VARARGS | METH_STATIC, nullptr },
        { "get_status", reinterpret_cast<PyCFunction>(AppBroadcastingUI_GetStatus), METH_VARARGS, nullptr },
        { "show_broadcast_u_i", reinterpret_cast<PyCFunction>(AppBroadcastingUI_ShowBroadcastUI), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_AppBroadcastingUI, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_AppBroadcastingUI), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AppBroadcastingUI[] = {
        { }
    };

    static PyType_Slot _type_slots_AppBroadcastingUI[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_AppBroadcastingUI) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_AppBroadcastingUI) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_AppBroadcastingUI) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_AppBroadcastingUI) },
        { },
    };

    static PyType_Spec type_spec_AppBroadcastingUI =
    {
        "_winrt_windows_media_appbroadcasting.AppBroadcastingUI",
        sizeof(py::wrapper::Windows::Media::AppBroadcasting::AppBroadcastingUI),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AppBroadcastingUI
    };

    // ----- Windows.Media.AppBroadcasting Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Media::AppBroadcasting");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_media_appbroadcasting",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::Media::AppBroadcasting

PyMODINIT_FUNC PyInit__winrt_windows_media_appbroadcasting(void) noexcept
{
    using namespace py::cpp::Windows::Media::AppBroadcasting;

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
    if (py::register_python_type(module.get(), type_name_AppBroadcastingMonitor, &type_spec_AppBroadcastingMonitor, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_AppBroadcastingMonitor, &type_spec_AppBroadcastingMonitor, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_AppBroadcastingStatus, &type_spec_AppBroadcastingStatus, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_AppBroadcastingStatus, &type_spec_AppBroadcastingStatus, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_AppBroadcastingStatusDetails, &type_spec_AppBroadcastingStatusDetails, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_AppBroadcastingStatusDetails, &type_spec_AppBroadcastingStatusDetails, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_AppBroadcastingUI, &type_spec_AppBroadcastingUI, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_AppBroadcastingUI, &type_spec_AppBroadcastingUI, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }


    return module.detach();
}