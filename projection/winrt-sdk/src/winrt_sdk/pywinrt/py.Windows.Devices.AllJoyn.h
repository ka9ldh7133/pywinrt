// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Enumeration.h")
#include "py.Windows.Devices.Enumeration.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Globalization.h")
#include "py.Windows.Globalization.h"
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

#include <winrt/Windows.Devices.Enumeration.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Globalization.h>
#include <winrt/Windows.Networking.Sockets.h>
#include <winrt/Windows.Security.Credentials.h>
#include <winrt/Windows.Security.Cryptography.Certificates.h>

#include <winrt/Windows.Devices.AllJoyn.h>

namespace py::proj::Windows::Devices::AllJoyn
{}

namespace py::impl::Windows::Devices::AllJoyn
{}

namespace py::wrapper::Windows::Devices::AllJoyn
{
    using AllJoynAboutData = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynAboutData>;
    using AllJoynAboutDataView = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynAboutDataView>;
    using AllJoynAcceptSessionJoinerEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynAcceptSessionJoinerEventArgs>;
    using AllJoynAuthenticationCompleteEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynAuthenticationCompleteEventArgs>;
    using AllJoynBusAttachment = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynBusAttachment>;
    using AllJoynBusAttachmentStateChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynBusAttachmentStateChangedEventArgs>;
    using AllJoynBusObject = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynBusObject>;
    using AllJoynBusObjectStoppedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynBusObjectStoppedEventArgs>;
    using AllJoynCredentials = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynCredentials>;
    using AllJoynCredentialsRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynCredentialsRequestedEventArgs>;
    using AllJoynCredentialsVerificationRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynCredentialsVerificationRequestedEventArgs>;
    using AllJoynMessageInfo = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynMessageInfo>;
    using AllJoynProducerStoppedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynProducerStoppedEventArgs>;
    using AllJoynServiceInfo = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynServiceInfo>;
    using AllJoynServiceInfoRemovedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynServiceInfoRemovedEventArgs>;
    using AllJoynSession = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynSession>;
    using AllJoynSessionJoinedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynSessionJoinedEventArgs>;
    using AllJoynSessionLostEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynSessionLostEventArgs>;
    using AllJoynSessionMemberAddedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynSessionMemberAddedEventArgs>;
    using AllJoynSessionMemberRemovedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynSessionMemberRemovedEventArgs>;
    using AllJoynStatus = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynStatus>;
    using AllJoynWatcherStoppedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::AllJoynWatcherStoppedEventArgs>;
    using IAllJoynAcceptSessionJoiner = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::IAllJoynAcceptSessionJoiner>;
    using IAllJoynProducer = py::winrt_wrapper<winrt::Windows::Devices::AllJoyn::IAllJoynProducer>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::AllJoyn::AllJoynAuthenticationMechanism> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::AllJoyn::AllJoynBusAttachmentState> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::AllJoyn::AllJoynSessionLostReason> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::AllJoyn::AllJoynTrafficType> = "i";


    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynAuthenticationMechanism>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynAuthenticationMechanism";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynBusAttachmentState>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynBusAttachmentState";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynSessionLostReason>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynSessionLostReason";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynTrafficType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynTrafficType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynAboutData>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynAboutData";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynAboutDataView>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynAboutDataView";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynAcceptSessionJoinerEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynAcceptSessionJoinerEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynAuthenticationCompleteEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynAuthenticationCompleteEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynBusAttachment>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynBusAttachment";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynBusAttachmentStateChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynBusAttachmentStateChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynBusObject>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynBusObject";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynBusObjectStoppedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynBusObjectStoppedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynCredentials>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynCredentials";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynCredentialsRequestedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynCredentialsRequestedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynCredentialsVerificationRequestedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynCredentialsVerificationRequestedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynMessageInfo>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynMessageInfo";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynProducerStoppedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynProducerStoppedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynServiceInfo>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynServiceInfo";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynServiceInfoRemovedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynServiceInfoRemovedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynSession>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynSession";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynSessionJoinedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynSessionJoinedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynSessionLostEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynSessionLostEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynSessionMemberAddedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynSessionMemberAddedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynSessionMemberRemovedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynSessionMemberRemovedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::AllJoynWatcherStoppedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "AllJoynWatcherStoppedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::IAllJoynAcceptSessionJoiner>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "IAllJoynAcceptSessionJoiner";
    };

    template<>
    struct py_type<winrt::Windows::Devices::AllJoyn::IAllJoynProducer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.alljoyn";
        static constexpr const char* type_name = "IAllJoynProducer";
    };
}