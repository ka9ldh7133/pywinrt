// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Foundation.Numerics.h")
#include "py.Windows.Foundation.Numerics.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.UI.h")
#include "py.Windows.UI.h"
#endif

#if __has_include("py.Windows.UI.Core.h")
#include "py.Windows.UI.Core.h"
#endif

#if __has_include("py.Windows.UI.Input.h")
#include "py.Windows.UI.Input.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Foundation.Numerics.h>
#include <winrt/Windows.Storage.Streams.h>
#include <winrt/Windows.UI.h>
#include <winrt/Windows.UI.Core.h>
#include <winrt/Windows.UI.Input.h>

#include <winrt/Windows.UI.Input.Inking.h>

namespace py::proj::Windows::UI::Input::Inking
{}

namespace py::impl::Windows::UI::Input::Inking
{}

namespace py::wrapper::Windows::UI::Input::Inking
{
    using InkDrawingAttributes = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkDrawingAttributes>;
    using InkDrawingAttributesPencilProperties = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkDrawingAttributesPencilProperties>;
    using InkInputConfiguration = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkInputConfiguration>;
    using InkInputProcessingConfiguration = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkInputProcessingConfiguration>;
    using InkManager = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkManager>;
    using InkModelerAttributes = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkModelerAttributes>;
    using InkPoint = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkPoint>;
    using InkPresenter = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkPresenter>;
    using InkPresenterProtractor = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkPresenterProtractor>;
    using InkPresenterRuler = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkPresenterRuler>;
    using InkRecognitionResult = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkRecognitionResult>;
    using InkRecognizer = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkRecognizer>;
    using InkRecognizerContainer = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkRecognizerContainer>;
    using InkStroke = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStroke>;
    using InkStrokeBuilder = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStrokeBuilder>;
    using InkStrokeContainer = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStrokeContainer>;
    using InkStrokeInput = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStrokeInput>;
    using InkStrokeRenderingSegment = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStrokeRenderingSegment>;
    using InkStrokesCollectedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStrokesCollectedEventArgs>;
    using InkStrokesErasedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkStrokesErasedEventArgs>;
    using InkSynchronizer = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkSynchronizer>;
    using InkUnprocessedInput = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::InkUnprocessedInput>;
    using PenAndInkSettings = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::PenAndInkSettings>;
    using IInkPointFactory = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::IInkPointFactory>;
    using IInkPresenterRulerFactory = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::IInkPresenterRulerFactory>;
    using IInkPresenterStencil = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::IInkPresenterStencil>;
    using IInkRecognizerContainer = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::IInkRecognizerContainer>;
    using IInkStrokeContainer = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::IInkStrokeContainer>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::HandwritingLineHeight> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkDrawingAttributesKind> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkHighContrastAdjustment> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkInputProcessingMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkInputRightDragAction> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkManipulationMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkPersistenceFormat> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkPresenterPredefinedConfiguration> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkPresenterStencilKind> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::InkRecognitionTarget> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::PenHandedness> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Input::Inking::PenTipShape> = "i";


    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::HandwritingLineHeight>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "HandwritingLineHeight";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkDrawingAttributesKind>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkDrawingAttributesKind";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkHighContrastAdjustment>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkHighContrastAdjustment";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkInputProcessingMode>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkInputProcessingMode";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkInputRightDragAction>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkInputRightDragAction";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkManipulationMode>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkManipulationMode";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPersistenceFormat>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPersistenceFormat";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPresenterPredefinedConfiguration>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPresenterPredefinedConfiguration";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPresenterStencilKind>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPresenterStencilKind";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkRecognitionTarget>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkRecognitionTarget";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::PenHandedness>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "PenHandedness";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::PenTipShape>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "PenTipShape";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkDrawingAttributes>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkDrawingAttributes";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkDrawingAttributesPencilProperties>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkDrawingAttributesPencilProperties";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkInputConfiguration>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkInputConfiguration";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkInputProcessingConfiguration>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkInputProcessingConfiguration";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkManager>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkManager";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkModelerAttributes>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkModelerAttributes";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPoint>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPoint";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPresenter>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPresenter";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPresenterProtractor>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPresenterProtractor";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkPresenterRuler>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkPresenterRuler";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkRecognitionResult>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkRecognitionResult";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkRecognizer>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkRecognizer";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkRecognizerContainer>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkRecognizerContainer";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStroke>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStroke";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStrokeBuilder>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStrokeBuilder";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStrokeContainer>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStrokeContainer";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStrokeInput>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStrokeInput";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStrokeRenderingSegment>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStrokeRenderingSegment";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStrokesCollectedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStrokesCollectedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkStrokesErasedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkStrokesErasedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkSynchronizer>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkSynchronizer";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::InkUnprocessedInput>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "InkUnprocessedInput";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::PenAndInkSettings>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "PenAndInkSettings";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::IInkPointFactory>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "IInkPointFactory";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::IInkPresenterRulerFactory>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "IInkPresenterRulerFactory";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::IInkPresenterStencil>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "IInkPresenterStencil";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::IInkRecognizerContainer>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "IInkRecognizerContainer";
    };

    template<>
    struct py_type<winrt::Windows::UI::Input::Inking::IInkStrokeContainer>
    {
        static constexpr const char* module_name = "winrt.windows.ui.input.inking";
        static constexpr const char* type_name = "IInkStrokeContainer";
    };
}