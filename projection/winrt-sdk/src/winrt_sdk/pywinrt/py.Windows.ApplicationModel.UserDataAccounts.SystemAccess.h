// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Security.Credentials.h")
#include "py.Windows.Security.Credentials.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Security.Credentials.h>

#include <winrt/Windows.ApplicationModel.UserDataAccounts.SystemAccess.h>

namespace py::proj::Windows::ApplicationModel::UserDataAccounts::SystemAccess
{}

namespace py::impl::Windows::ApplicationModel::UserDataAccounts::SystemAccess
{}

namespace py::wrapper::Windows::ApplicationModel::UserDataAccounts::SystemAccess
{
    using DeviceAccountConfiguration = py::winrt_wrapper<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountConfiguration>;
    using UserDataAccountSystemAccessManager = py::winrt_wrapper<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::UserDataAccountSystemAccessManager>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountAuthenticationType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountIconId> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountMailAgeFilter> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountServerType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountSyncScheduleKind> = "i";


    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountAuthenticationType>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "DeviceAccountAuthenticationType";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountIconId>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "DeviceAccountIconId";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountMailAgeFilter>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "DeviceAccountMailAgeFilter";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountServerType>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "DeviceAccountServerType";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountSyncScheduleKind>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "DeviceAccountSyncScheduleKind";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::DeviceAccountConfiguration>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "DeviceAccountConfiguration";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::UserDataAccounts::SystemAccess::UserDataAccountSystemAccessManager>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.userdataaccounts.systemaccess";
        static constexpr const char* type_name = "UserDataAccountSystemAccessManager";
    };
}