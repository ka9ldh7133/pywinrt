// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Storage.Streams.h>

#include <winrt/Windows.Services.TargetedContent.h>

namespace py::proj::Windows::Services::TargetedContent
{}

namespace py::impl::Windows::Services::TargetedContent
{}

namespace py::wrapper::Windows::Services::TargetedContent
{
    using TargetedContentAction = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentAction>;
    using TargetedContentAvailabilityChangedEventArgs = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentAvailabilityChangedEventArgs>;
    using TargetedContentChangedEventArgs = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentChangedEventArgs>;
    using TargetedContentCollection = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentCollection>;
    using TargetedContentContainer = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentContainer>;
    using TargetedContentFile = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentFile>;
    using TargetedContentImage = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentImage>;
    using TargetedContentItem = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentItem>;
    using TargetedContentItemState = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentItemState>;
    using TargetedContentObject = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentObject>;
    using TargetedContentStateChangedEventArgs = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentStateChangedEventArgs>;
    using TargetedContentSubscription = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentSubscription>;
    using TargetedContentSubscriptionOptions = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentSubscriptionOptions>;
    using TargetedContentValue = py::winrt_wrapper<winrt::Windows::Services::TargetedContent::TargetedContentValue>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Services::TargetedContent::TargetedContentAppInstallationState> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Services::TargetedContent::TargetedContentAvailability> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Services::TargetedContent::TargetedContentInteraction> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Services::TargetedContent::TargetedContentObjectKind> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Services::TargetedContent::TargetedContentValueKind> = "i";


    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentAppInstallationState>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentAppInstallationState";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentAvailability>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentAvailability";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentInteraction>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentInteraction";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentObjectKind>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentObjectKind";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentValueKind>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentValueKind";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentAction>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentAction";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentAvailabilityChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentAvailabilityChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentCollection>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentCollection";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentContainer>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentContainer";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentFile>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentFile";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentImage>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentImage";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentItem>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentItem";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentItemState>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentItemState";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentObject>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentObject";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentStateChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentStateChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentSubscription>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentSubscription";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentSubscriptionOptions>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentSubscriptionOptions";
    };

    template<>
    struct py_type<winrt::Windows::Services::TargetedContent::TargetedContentValue>
    {
        static constexpr const char* module_name = "winrt.windows.services.targetedcontent";
        static constexpr const char* type_name = "TargetedContentValue";
    };
}