// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Storage.Streams.h>

#include <winrt/Windows.Security.Credentials.UI.h>

namespace py::proj::Windows::Security::Credentials::UI
{}

namespace py::impl::Windows::Security::Credentials::UI
{}

namespace py::wrapper::Windows::Security::Credentials::UI
{
    using CredentialPicker = py::winrt_wrapper<winrt::Windows::Security::Credentials::UI::CredentialPicker>;
    using CredentialPickerOptions = py::winrt_wrapper<winrt::Windows::Security::Credentials::UI::CredentialPickerOptions>;
    using CredentialPickerResults = py::winrt_wrapper<winrt::Windows::Security::Credentials::UI::CredentialPickerResults>;
    using UserConsentVerifier = py::winrt_wrapper<winrt::Windows::Security::Credentials::UI::UserConsentVerifier>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Security::Credentials::UI::AuthenticationProtocol> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Security::Credentials::UI::CredentialSaveOption> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Security::Credentials::UI::UserConsentVerificationResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Security::Credentials::UI::UserConsentVerifierAvailability> = "i";


    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::AuthenticationProtocol>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "AuthenticationProtocol";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::CredentialSaveOption>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "CredentialSaveOption";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::UserConsentVerificationResult>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "UserConsentVerificationResult";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::UserConsentVerifierAvailability>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "UserConsentVerifierAvailability";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::CredentialPicker>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "CredentialPicker";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::CredentialPickerOptions>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "CredentialPickerOptions";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::CredentialPickerResults>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "CredentialPickerResults";
    };

    template<>
    struct py_type<winrt::Windows::Security::Credentials::UI::UserConsentVerifier>
    {
        static constexpr const char* module_name = "winrt.windows.security.credentials.ui";
        static constexpr const char* type_name = "UserConsentVerifier";
    };
}