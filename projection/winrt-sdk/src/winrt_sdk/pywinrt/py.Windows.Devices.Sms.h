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

#include <winrt/Windows.Devices.Sms.h>

namespace py::proj::Windows::Devices::Sms
{}

namespace py::impl::Windows::Devices::Sms
{
    struct SmsDeviceStatusChangedEventHandler
    {
        static winrt::Windows::Devices::Sms::SmsDeviceStatusChangedEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };

                py::pyobj_handle args{ PyTuple_Pack(1, py_param0.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };

    struct SmsMessageReceivedEventHandler
    {
        static winrt::Windows::Devices::Sms::SmsMessageReceivedEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };
                py::pyobj_handle py_param1{ py::convert(param1) };

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };
}

namespace py::wrapper::Windows::Devices::Sms
{
    using DeleteSmsMessageOperation = py::winrt_wrapper<winrt::Windows::Devices::Sms::DeleteSmsMessageOperation>;
    using DeleteSmsMessagesOperation = py::winrt_wrapper<winrt::Windows::Devices::Sms::DeleteSmsMessagesOperation>;
    using GetSmsDeviceOperation = py::winrt_wrapper<winrt::Windows::Devices::Sms::GetSmsDeviceOperation>;
    using GetSmsMessageOperation = py::winrt_wrapper<winrt::Windows::Devices::Sms::GetSmsMessageOperation>;
    using GetSmsMessagesOperation = py::winrt_wrapper<winrt::Windows::Devices::Sms::GetSmsMessagesOperation>;
    using SendSmsMessageOperation = py::winrt_wrapper<winrt::Windows::Devices::Sms::SendSmsMessageOperation>;
    using SmsAppMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsAppMessage>;
    using SmsBinaryMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsBinaryMessage>;
    using SmsBroadcastMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsBroadcastMessage>;
    using SmsDevice = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsDevice>;
    using SmsDevice2 = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsDevice2>;
    using SmsDeviceMessageStore = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsDeviceMessageStore>;
    using SmsFilterRule = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsFilterRule>;
    using SmsFilterRules = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsFilterRules>;
    using SmsMessageReceivedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsMessageReceivedEventArgs>;
    using SmsMessageReceivedTriggerDetails = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsMessageReceivedTriggerDetails>;
    using SmsMessageRegistration = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsMessageRegistration>;
    using SmsReceivedEventDetails = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsReceivedEventDetails>;
    using SmsSendMessageResult = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsSendMessageResult>;
    using SmsStatusMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsStatusMessage>;
    using SmsTextMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsTextMessage>;
    using SmsTextMessage2 = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsTextMessage2>;
    using SmsVoicemailMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsVoicemailMessage>;
    using SmsWapMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::SmsWapMessage>;
    using ISmsBinaryMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::ISmsBinaryMessage>;
    using ISmsDevice = py::winrt_wrapper<winrt::Windows::Devices::Sms::ISmsDevice>;
    using ISmsMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::ISmsMessage>;
    using ISmsMessageBase = py::winrt_wrapper<winrt::Windows::Devices::Sms::ISmsMessageBase>;
    using ISmsTextMessage = py::winrt_wrapper<winrt::Windows::Devices::Sms::ISmsTextMessage>;
    using SmsEncodedLength = py::winrt_struct_wrapper<winrt::Windows::Devices::Sms::SmsEncodedLength>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::CellularClass> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsBroadcastType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsDataFormat> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsDeviceStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsEncoding> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsFilterActionType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsGeographicalScope> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsMessageClass> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsMessageFilter> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsMessageType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsModemErrorCode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sms::SmsEncodedLength> = "T{I:segment_count:I:character_count_last_segment:I:characters_per_segment:I:byte_count_last_segment:I:bytes_per_segment:}";


    template<>
    struct py_type<winrt::Windows::Devices::Sms::CellularClass>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "CellularClass";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsBroadcastType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsBroadcastType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsDataFormat>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsDataFormat";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsDeviceStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsDeviceStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsEncoding>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsEncoding";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsFilterActionType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsFilterActionType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsGeographicalScope>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsGeographicalScope";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsMessageClass>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsMessageClass";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsMessageFilter>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsMessageFilter";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsMessageType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsMessageType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsModemErrorCode>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsModemErrorCode";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::DeleteSmsMessageOperation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "DeleteSmsMessageOperation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::DeleteSmsMessagesOperation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "DeleteSmsMessagesOperation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::GetSmsDeviceOperation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "GetSmsDeviceOperation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::GetSmsMessageOperation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "GetSmsMessageOperation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::GetSmsMessagesOperation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "GetSmsMessagesOperation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SendSmsMessageOperation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SendSmsMessageOperation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsAppMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsAppMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsBinaryMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsBinaryMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsBroadcastMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsBroadcastMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsDevice>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsDevice";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsDevice2>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsDevice2";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsDeviceMessageStore>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsDeviceMessageStore";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsFilterRule>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsFilterRule";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsFilterRules>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsFilterRules";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsMessageReceivedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsMessageReceivedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsMessageReceivedTriggerDetails>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsMessageReceivedTriggerDetails";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsMessageRegistration>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsMessageRegistration";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsReceivedEventDetails>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsReceivedEventDetails";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsSendMessageResult>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsSendMessageResult";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsStatusMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsStatusMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsTextMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsTextMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsTextMessage2>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsTextMessage2";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsVoicemailMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsVoicemailMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsWapMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsWapMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::ISmsBinaryMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "ISmsBinaryMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::ISmsDevice>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "ISmsDevice";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::ISmsMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "ISmsMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::ISmsMessageBase>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "ISmsMessageBase";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::ISmsTextMessage>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "ISmsTextMessage";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sms::SmsEncodedLength>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sms";
        static constexpr const char* type_name = "SmsEncodedLength";
    };
    template <>
    struct delegate_python_type<winrt::Windows::Devices::Sms::SmsDeviceStatusChangedEventHandler>
    {
        using type = py::impl::Windows::Devices::Sms::SmsDeviceStatusChangedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::Devices::Sms::SmsMessageReceivedEventHandler>
    {
        using type = py::impl::Windows::Devices::Sms::SmsMessageReceivedEventHandler;
    };

}