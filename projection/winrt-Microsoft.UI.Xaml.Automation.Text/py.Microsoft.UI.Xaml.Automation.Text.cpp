// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Microsoft.UI.Xaml.Automation.Text.h"


namespace py::cpp::Microsoft::UI::Xaml::Automation::Text
{
    // ----- Microsoft.UI.Xaml.Automation.Text Initialization --------------------
    PyDoc_STRVAR(module_doc, "Microsoft::UI::Xaml::Automation::Text");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_microsoft_ui_xaml_automation_text",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Microsoft::UI::Xaml::Automation::Text

PyMODINIT_FUNC PyInit__winrt_microsoft_ui_xaml_automation_text(void) noexcept
{
    using namespace py::cpp::Microsoft::UI::Xaml::Automation::Text;

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


    return module.detach();
}