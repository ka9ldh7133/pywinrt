// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Numerics.h")
#include "py.Windows.Foundation.Numerics.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Numerics.h>

#include <winrt/Windows.Gaming.Input.ForceFeedback.h>

namespace py::proj::Windows::Gaming::Input::ForceFeedback
{}

namespace py::impl::Windows::Gaming::Input::ForceFeedback
{}

namespace py::wrapper::Windows::Gaming::Input::ForceFeedback
{
    using ConditionForceEffect = py::winrt_wrapper<winrt::Windows::Gaming::Input::ForceFeedback::ConditionForceEffect>;
    using ConstantForceEffect = py::winrt_wrapper<winrt::Windows::Gaming::Input::ForceFeedback::ConstantForceEffect>;
    using ForceFeedbackMotor = py::winrt_wrapper<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackMotor>;
    using PeriodicForceEffect = py::winrt_wrapper<winrt::Windows::Gaming::Input::ForceFeedback::PeriodicForceEffect>;
    using RampForceEffect = py::winrt_wrapper<winrt::Windows::Gaming::Input::ForceFeedback::RampForceEffect>;
    using IForceFeedbackEffect = py::winrt_wrapper<winrt::Windows::Gaming::Input::ForceFeedback::IForceFeedbackEffect>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Gaming::Input::ForceFeedback::ConditionForceEffectKind> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackEffectAxes> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackEffectState> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackLoadEffectResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Gaming::Input::ForceFeedback::PeriodicForceEffectKind> = "i";


    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ConditionForceEffectKind>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ConditionForceEffectKind";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackEffectAxes>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ForceFeedbackEffectAxes";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackEffectState>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ForceFeedbackEffectState";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackLoadEffectResult>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ForceFeedbackLoadEffectResult";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::PeriodicForceEffectKind>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "PeriodicForceEffectKind";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ConditionForceEffect>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ConditionForceEffect";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ConstantForceEffect>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ConstantForceEffect";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::ForceFeedbackMotor>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "ForceFeedbackMotor";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::PeriodicForceEffect>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "PeriodicForceEffect";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::RampForceEffect>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "RampForceEffect";
    };

    template<>
    struct py_type<winrt::Windows::Gaming::Input::ForceFeedback::IForceFeedbackEffect>
    {
        static constexpr const char* module_name = "winrt.windows.gaming.input.forcefeedback";
        static constexpr const char* type_name = "IForceFeedbackEffect";
    };
}