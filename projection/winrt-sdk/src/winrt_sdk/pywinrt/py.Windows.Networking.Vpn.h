// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.Activation.h")
#include "py.Windows.ApplicationModel.Activation.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Networking.h")
#include "py.Windows.Networking.h"
#endif

#if __has_include("py.Windows.Networking.Sockets.h")
#include "py.Windows.Networking.Sockets.h"
#endif

#if __has_include("py.Windows.Security.Credentials.h")
#include "py.Windows.Security.Credentials.h"
#endif

#if __has_include("py.Windows.Security.Cryptography.Certificates.h")
#include "py.Windows.Security.Cryptography.Certificates.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#include <winrt/Windows.ApplicationModel.Activation.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Networking.h>
#include <winrt/Windows.Networking.Sockets.h>
#include <winrt/Windows.Security.Credentials.h>
#include <winrt/Windows.Security.Cryptography.Certificates.h>
#include <winrt/Windows.Storage.Streams.h>
#include <winrt/Windows.System.h>

#include <winrt/Windows.Networking.Vpn.h>

namespace py::proj::Windows::Networking::Vpn
{}

namespace py::impl::Windows::Networking::Vpn
{}

namespace py::wrapper::Windows::Networking::Vpn
{
    using VpnAppId = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnAppId>;
    using VpnChannel = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnChannel>;
    using VpnChannelActivityEventArgs = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnChannelActivityEventArgs>;
    using VpnChannelActivityStateChangedArgs = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnChannelActivityStateChangedArgs>;
    using VpnChannelConfiguration = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnChannelConfiguration>;
    using VpnCredential = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCredential>;
    using VpnCustomCheckBox = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomCheckBox>;
    using VpnCustomComboBox = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomComboBox>;
    using VpnCustomEditBox = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomEditBox>;
    using VpnCustomErrorBox = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomErrorBox>;
    using VpnCustomPromptBooleanInput = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomPromptBooleanInput>;
    using VpnCustomPromptOptionSelector = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomPromptOptionSelector>;
    using VpnCustomPromptText = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomPromptText>;
    using VpnCustomPromptTextInput = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomPromptTextInput>;
    using VpnCustomTextBox = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnCustomTextBox>;
    using VpnDomainNameAssignment = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnDomainNameAssignment>;
    using VpnDomainNameInfo = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnDomainNameInfo>;
    using VpnForegroundActivatedEventArgs = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnForegroundActivatedEventArgs>;
    using VpnForegroundActivationOperation = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnForegroundActivationOperation>;
    using VpnInterfaceId = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnInterfaceId>;
    using VpnManagementAgent = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnManagementAgent>;
    using VpnNamespaceAssignment = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnNamespaceAssignment>;
    using VpnNamespaceInfo = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnNamespaceInfo>;
    using VpnNativeProfile = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnNativeProfile>;
    using VpnPacketBuffer = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnPacketBuffer>;
    using VpnPacketBufferList = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnPacketBufferList>;
    using VpnPickedCredential = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnPickedCredential>;
    using VpnPlugInProfile = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnPlugInProfile>;
    using VpnRoute = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnRoute>;
    using VpnRouteAssignment = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnRouteAssignment>;
    using VpnSystemHealth = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnSystemHealth>;
    using VpnTrafficFilter = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnTrafficFilter>;
    using VpnTrafficFilterAssignment = py::winrt_wrapper<winrt::Windows::Networking::Vpn::VpnTrafficFilterAssignment>;
    using IVpnChannelStatics = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnChannelStatics>;
    using IVpnCredential = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnCredential>;
    using IVpnCustomPrompt = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnCustomPrompt>;
    using IVpnCustomPromptElement = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnCustomPromptElement>;
    using IVpnDomainNameInfoFactory = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnDomainNameInfoFactory>;
    using IVpnInterfaceIdFactory = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnInterfaceIdFactory>;
    using IVpnNamespaceInfoFactory = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnNamespaceInfoFactory>;
    using IVpnPacketBufferFactory = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnPacketBufferFactory>;
    using IVpnPlugIn = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnPlugIn>;
    using IVpnProfile = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnProfile>;
    using IVpnRouteFactory = py::winrt_wrapper<winrt::Windows::Networking::Vpn::IVpnRouteFactory>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnAppIdType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnAuthenticationMethod> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnChannelActivityEventType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnChannelRequestCredentialsOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnCredentialType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnDataPathType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnDomainNameType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnIPProtocol> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnManagementConnectionStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnManagementErrorStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnNativeProtocolType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnPacketBufferStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Networking::Vpn::VpnRoutingPolicyType> = "i";


    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnAppIdType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnAppIdType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnAuthenticationMethod>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnAuthenticationMethod";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnChannelActivityEventType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnChannelActivityEventType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnChannelRequestCredentialsOptions>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnChannelRequestCredentialsOptions";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCredentialType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCredentialType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnDataPathType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnDataPathType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnDomainNameType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnDomainNameType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnIPProtocol>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnIPProtocol";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnManagementConnectionStatus>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnManagementConnectionStatus";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnManagementErrorStatus>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnManagementErrorStatus";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnNativeProtocolType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnNativeProtocolType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnPacketBufferStatus>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnPacketBufferStatus";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnRoutingPolicyType>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnRoutingPolicyType";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnAppId>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnAppId";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnChannel>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnChannel";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnChannelActivityEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnChannelActivityEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnChannelActivityStateChangedArgs>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnChannelActivityStateChangedArgs";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnChannelConfiguration>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnChannelConfiguration";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCredential>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCredential";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomCheckBox>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomCheckBox";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomComboBox>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomComboBox";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomEditBox>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomEditBox";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomErrorBox>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomErrorBox";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomPromptBooleanInput>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomPromptBooleanInput";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomPromptOptionSelector>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomPromptOptionSelector";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomPromptText>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomPromptText";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomPromptTextInput>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomPromptTextInput";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnCustomTextBox>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnCustomTextBox";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnDomainNameAssignment>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnDomainNameAssignment";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnDomainNameInfo>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnDomainNameInfo";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnForegroundActivatedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnForegroundActivatedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnForegroundActivationOperation>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnForegroundActivationOperation";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnInterfaceId>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnInterfaceId";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnManagementAgent>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnManagementAgent";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnNamespaceAssignment>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnNamespaceAssignment";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnNamespaceInfo>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnNamespaceInfo";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnNativeProfile>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnNativeProfile";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnPacketBuffer>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnPacketBuffer";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnPacketBufferList>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnPacketBufferList";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnPickedCredential>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnPickedCredential";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnPlugInProfile>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnPlugInProfile";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnRoute>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnRoute";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnRouteAssignment>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnRouteAssignment";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnSystemHealth>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnSystemHealth";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnTrafficFilter>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnTrafficFilter";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::VpnTrafficFilterAssignment>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "VpnTrafficFilterAssignment";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnChannelStatics>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnChannelStatics";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnCredential>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnCredential";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnCustomPrompt>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnCustomPrompt";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnCustomPromptElement>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnCustomPromptElement";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnDomainNameInfoFactory>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnDomainNameInfoFactory";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnInterfaceIdFactory>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnInterfaceIdFactory";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnNamespaceInfoFactory>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnNamespaceInfoFactory";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnPacketBufferFactory>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnPacketBufferFactory";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnPlugIn>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnPlugIn";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnProfile>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnProfile";
    };

    template<>
    struct py_type<winrt::Windows::Networking::Vpn::IVpnRouteFactory>
    {
        static constexpr const char* module_name = "winrt.windows.networking.vpn";
        static constexpr const char* type_name = "IVpnRouteFactory";
    };
}