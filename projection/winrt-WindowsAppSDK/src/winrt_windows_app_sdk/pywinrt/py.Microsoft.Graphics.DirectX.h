// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");


#include <winrt/Microsoft.Graphics.DirectX.h>

namespace py::proj::Microsoft::Graphics::DirectX
{}

namespace py::impl::Microsoft::Graphics::DirectX
{}

namespace py::wrapper::Microsoft::Graphics::DirectX
{
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Graphics::DirectX::DirectXAlphaMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Graphics::DirectX::DirectXColorSpace> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Graphics::DirectX::DirectXPixelFormat> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::Graphics::DirectX::DirectXPrimitiveTopology> = "i";


    template<>
    struct py_type<winrt::Microsoft::Graphics::DirectX::DirectXAlphaMode>
    {
        static constexpr const char* module_name = "winrt.microsoft.graphics.directx";
        static constexpr const char* type_name = "DirectXAlphaMode";
    };

    template<>
    struct py_type<winrt::Microsoft::Graphics::DirectX::DirectXColorSpace>
    {
        static constexpr const char* module_name = "winrt.microsoft.graphics.directx";
        static constexpr const char* type_name = "DirectXColorSpace";
    };

    template<>
    struct py_type<winrt::Microsoft::Graphics::DirectX::DirectXPixelFormat>
    {
        static constexpr const char* module_name = "winrt.microsoft.graphics.directx";
        static constexpr const char* type_name = "DirectXPixelFormat";
    };

    template<>
    struct py_type<winrt::Microsoft::Graphics::DirectX::DirectXPrimitiveTopology>
    {
        static constexpr const char* module_name = "winrt.microsoft.graphics.directx";
        static constexpr const char* type_name = "DirectXPrimitiveTopology";
    };
}