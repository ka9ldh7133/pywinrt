// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.SocialInfo.h")
#include "py.Windows.ApplicationModel.SocialInfo.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.ApplicationModel.SocialInfo.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>

#include <winrt/Windows.ApplicationModel.SocialInfo.Provider.h>

namespace py::proj::Windows::ApplicationModel::SocialInfo::Provider
{}

namespace py::impl::Windows::ApplicationModel::SocialInfo::Provider
{}

namespace py::wrapper::Windows::ApplicationModel::SocialInfo::Provider
{
    using SocialDashboardItemUpdater = py::winrt_wrapper<winrt::Windows::ApplicationModel::SocialInfo::Provider::SocialDashboardItemUpdater>;
    using SocialFeedUpdater = py::winrt_wrapper<winrt::Windows::ApplicationModel::SocialInfo::Provider::SocialFeedUpdater>;
    using SocialInfoProviderManager = py::winrt_wrapper<winrt::Windows::ApplicationModel::SocialInfo::Provider::SocialInfoProviderManager>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::ApplicationModel::SocialInfo::Provider::SocialDashboardItemUpdater>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.socialinfo.provider";
        static constexpr const char* type_name = "SocialDashboardItemUpdater";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::SocialInfo::Provider::SocialFeedUpdater>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.socialinfo.provider";
        static constexpr const char* type_name = "SocialFeedUpdater";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::SocialInfo::Provider::SocialInfoProviderManager>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.socialinfo.provider";
        static constexpr const char* type_name = "SocialInfoProviderManager";
    };
}