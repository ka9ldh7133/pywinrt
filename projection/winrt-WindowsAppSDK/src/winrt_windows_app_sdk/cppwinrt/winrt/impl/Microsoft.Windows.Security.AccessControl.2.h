// WARNING: Please don't edit this file. It was generated by C++/WinRT v2.0.240111.5

#pragma once
#ifndef WINRT_Microsoft_Windows_Security_AccessControl_2_H
#define WINRT_Microsoft_Windows_Security_AccessControl_2_H
#include "winrt/impl/Microsoft.Windows.Security.AccessControl.1.h"
WINRT_EXPORT namespace winrt::Microsoft::Windows::Security::AccessControl
{
    struct AppContainerNameAndAccess
    {
        hstring appContainerName;
        uint32_t accessMask;
    };
    inline bool operator==(AppContainerNameAndAccess const& left, AppContainerNameAndAccess const& right) noexcept
    {
        return left.appContainerName == right.appContainerName && left.accessMask == right.accessMask;
    }
    inline bool operator!=(AppContainerNameAndAccess const& left, AppContainerNameAndAccess const& right) noexcept
    {
        return !(left == right);
    }
    struct SecurityDescriptorHelpers
    {
        SecurityDescriptorHelpers() = delete;
        static auto GetSddlForAppContainerNames(array_view<winrt::Microsoft::Windows::Security::AccessControl::AppContainerNameAndAccess const> accessRequests, param::hstring const& principalStringSid, uint32_t principalAccessMask);
        static auto GetSecurityDescriptorBytesFromAppContainerNames(array_view<winrt::Microsoft::Windows::Security::AccessControl::AppContainerNameAndAccess const> accessRequests, param::hstring const& principalStringSid, uint32_t principalAccessMask);
    };
}
#endif