// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "pybase.h"
#include "py.Windows.Storage.Compression.h"


namespace py::cpp::Windows::Storage::Compression
{
    // ----- Compressor class --------------------
    static constexpr const char* const type_name_Compressor = "Compressor";

    static PyObject* _new_Compressor(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        auto arg_count = PyTuple_Size(args);
        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IOutputStream>(args, 0);

                winrt::Windows::Storage::Compression::Compressor instance{ param0 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 3)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IOutputStream>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Storage::Compression::CompressAlgorithm>(args, 1);
                auto param2 = py::convert_to<uint32_t>(args, 2);

                winrt::Windows::Storage::Compression::Compressor instance{ param0, param1, param2 };
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

    static void _dealloc_Compressor(py::wrapper::Windows::Storage::Compression::Compressor* self) noexcept
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

    static PyObject* Compressor_Close(py::wrapper::Windows::Storage::Compression::Compressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Compressor", L"Close", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
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

    static PyObject* Compressor_DetachStream(py::wrapper::Windows::Storage::Compression::Compressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Compressor", L"DetachStream", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(self->obj.DetachStream());
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

    static PyObject* Compressor_FinishAsync(py::wrapper::Windows::Storage::Compression::Compressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Compressor", L"FinishAsync", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(self->obj.FinishAsync());
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

    static PyObject* Compressor_FlushAsync(py::wrapper::Windows::Storage::Compression::Compressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Compressor", L"FlushAsync", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(self->obj.FlushAsync());
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

    static PyObject* Compressor_WriteAsync(py::wrapper::Windows::Storage::Compression::Compressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Compressor", L"WriteAsync", 1))
            {
                py::set_arg_count_version_error(1);
                return nullptr;
            }

            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);

                return py::convert(self->obj.WriteAsync(param0));
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

    static PyObject* _assign_array_Compressor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Storage::Compression::Compressor>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_Compressor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Storage::Compression::Compressor>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_Compressor(py::wrapper::Windows::Storage::Compression::Compressor* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_Compressor(py::wrapper::Windows::Storage::Compression::Compressor* self) noexcept
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

    static PyMethodDef _methods_Compressor[] = {
        { "close", reinterpret_cast<PyCFunction>(Compressor_Close), METH_VARARGS, nullptr },
        { "detach_stream", reinterpret_cast<PyCFunction>(Compressor_DetachStream), METH_VARARGS, nullptr },
        { "finish_async", reinterpret_cast<PyCFunction>(Compressor_FinishAsync), METH_VARARGS, nullptr },
        { "flush_async", reinterpret_cast<PyCFunction>(Compressor_FlushAsync), METH_VARARGS, nullptr },
        { "write_async", reinterpret_cast<PyCFunction>(Compressor_WriteAsync), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_Compressor, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_Compressor), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_Compressor), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_Compressor), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_Compressor[] = {
        { }
    };

    static PyType_Slot _type_slots_Compressor[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_Compressor) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_Compressor) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_Compressor) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_Compressor) },
        { },
    };

    static PyType_Spec type_spec_Compressor =
    {
        "_winrt_windows_storage_compression.Compressor",
        sizeof(py::wrapper::Windows::Storage::Compression::Compressor),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_Compressor
    };

    // ----- Decompressor class --------------------
    static constexpr const char* const type_name_Decompressor = "Decompressor";

    static PyObject* _new_Decompressor(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        auto arg_count = PyTuple_Size(args);
        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IInputStream>(args, 0);

                winrt::Windows::Storage::Compression::Decompressor instance{ param0 };
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

    static void _dealloc_Decompressor(py::wrapper::Windows::Storage::Compression::Decompressor* self) noexcept
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

    static PyObject* Decompressor_Close(py::wrapper::Windows::Storage::Compression::Decompressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Decompressor", L"Close", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
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

    static PyObject* Decompressor_DetachStream(py::wrapper::Windows::Storage::Compression::Decompressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Decompressor", L"DetachStream", 0))
            {
                py::set_arg_count_version_error(0);
                return nullptr;
            }

            try
            {
                return py::convert(self->obj.DetachStream());
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

    static PyObject* Decompressor_ReadAsync(py::wrapper::Windows::Storage::Compression::Decompressor* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 3)
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Storage.Compression.Decompressor", L"ReadAsync", 3))
            {
                py::set_arg_count_version_error(3);
                return nullptr;
            }

            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);
                auto param1 = py::convert_to<uint32_t>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Storage::Streams::InputStreamOptions>(args, 2);

                return py::convert(self->obj.ReadAsync(param0, param1, param2));
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

    static PyObject* _assign_array_Decompressor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Storage::Compression::Decompressor>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_Decompressor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Storage::Compression::Decompressor>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_Decompressor(py::wrapper::Windows::Storage::Compression::Decompressor* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_Decompressor(py::wrapper::Windows::Storage::Compression::Decompressor* self) noexcept
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

    static PyMethodDef _methods_Decompressor[] = {
        { "close", reinterpret_cast<PyCFunction>(Decompressor_Close), METH_VARARGS, nullptr },
        { "detach_stream", reinterpret_cast<PyCFunction>(Decompressor_DetachStream), METH_VARARGS, nullptr },
        { "read_async", reinterpret_cast<PyCFunction>(Decompressor_ReadAsync), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_Decompressor, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_Decompressor), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_Decompressor), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_Decompressor), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_Decompressor[] = {
        { }
    };

    static PyType_Slot _type_slots_Decompressor[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_Decompressor) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_Decompressor) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_Decompressor) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_Decompressor) },
        { },
    };

    static PyType_Spec type_spec_Decompressor =
    {
        "_winrt_windows_storage_compression.Decompressor",
        sizeof(py::wrapper::Windows::Storage::Compression::Decompressor),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_Decompressor
    };

    // ----- Windows.Storage.Compression Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Storage::Compression");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_storage_compression",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::Storage::Compression

PyMODINIT_FUNC PyInit__winrt_windows_storage_compression(void) noexcept
{
    using namespace py::cpp::Windows::Storage::Compression;

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
    if (py::register_python_type(module.get(), type_name_Compressor, &type_spec_Compressor, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_Compressor, &type_spec_Compressor, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }

    #if PY_VERSION_HEX < 0x03090000
    if (py::register_python_type(module.get(), type_name_Decompressor, &type_spec_Decompressor, nullptr, object_bases.get(), nullptr) == -1)
    #else
    if (py::register_python_type(module.get(), type_name_Decompressor, &type_spec_Decompressor, object_bases.get(), nullptr) == -1)
    #endif
    {
        return nullptr;
    }


    return module.detach();
}