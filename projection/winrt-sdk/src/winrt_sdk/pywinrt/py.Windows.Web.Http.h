// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Networking.Sockets.h")
#include "py.Windows.Networking.Sockets.h"
#endif

#if __has_include("py.Windows.Security.Cryptography.Certificates.h")
#include "py.Windows.Security.Cryptography.Certificates.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.Web.Http.Filters.h")
#include "py.Windows.Web.Http.Filters.h"
#endif

#if __has_include("py.Windows.Web.Http.Headers.h")
#include "py.Windows.Web.Http.Headers.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Networking.Sockets.h>
#include <winrt/Windows.Security.Cryptography.Certificates.h>
#include <winrt/Windows.Storage.Streams.h>
#include <winrt/Windows.Web.Http.Filters.h>
#include <winrt/Windows.Web.Http.Headers.h>

#include <winrt/Windows.Web.Http.h>

namespace py::proj::Windows::Web::Http
{}

namespace py::impl::Windows::Web::Http
{}

namespace py::wrapper::Windows::Web::Http
{
    using HttpBufferContent = py::winrt_wrapper<winrt::Windows::Web::Http::HttpBufferContent>;
    using HttpClient = py::winrt_wrapper<winrt::Windows::Web::Http::HttpClient>;
    using HttpCookie = py::winrt_wrapper<winrt::Windows::Web::Http::HttpCookie>;
    using HttpCookieCollection = py::winrt_wrapper<winrt::Windows::Web::Http::HttpCookieCollection>;
    using HttpCookieManager = py::winrt_wrapper<winrt::Windows::Web::Http::HttpCookieManager>;
    using HttpFormUrlEncodedContent = py::winrt_wrapper<winrt::Windows::Web::Http::HttpFormUrlEncodedContent>;
    using HttpGetBufferResult = py::winrt_wrapper<winrt::Windows::Web::Http::HttpGetBufferResult>;
    using HttpGetInputStreamResult = py::winrt_wrapper<winrt::Windows::Web::Http::HttpGetInputStreamResult>;
    using HttpGetStringResult = py::winrt_wrapper<winrt::Windows::Web::Http::HttpGetStringResult>;
    using HttpMethod = py::winrt_wrapper<winrt::Windows::Web::Http::HttpMethod>;
    using HttpMultipartContent = py::winrt_wrapper<winrt::Windows::Web::Http::HttpMultipartContent>;
    using HttpMultipartFormDataContent = py::winrt_wrapper<winrt::Windows::Web::Http::HttpMultipartFormDataContent>;
    using HttpRequestMessage = py::winrt_wrapper<winrt::Windows::Web::Http::HttpRequestMessage>;
    using HttpRequestResult = py::winrt_wrapper<winrt::Windows::Web::Http::HttpRequestResult>;
    using HttpResponseMessage = py::winrt_wrapper<winrt::Windows::Web::Http::HttpResponseMessage>;
    using HttpStreamContent = py::winrt_wrapper<winrt::Windows::Web::Http::HttpStreamContent>;
    using HttpStringContent = py::winrt_wrapper<winrt::Windows::Web::Http::HttpStringContent>;
    using HttpTransportInformation = py::winrt_wrapper<winrt::Windows::Web::Http::HttpTransportInformation>;
    using IHttpContent = py::winrt_wrapper<winrt::Windows::Web::Http::IHttpContent>;
    using HttpProgress = py::winrt_struct_wrapper<winrt::Windows::Web::Http::HttpProgress>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Web::Http::HttpCompletionOption> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Web::Http::HttpProgressStage> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Web::Http::HttpResponseMessageSource> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Web::Http::HttpStatusCode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Web::Http::HttpVersion> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Web::Http::HttpProgress> = "T{i:stage:Q:bytes_sent:Q:total_bytes_to_send:Q:bytes_received:Q:total_bytes_to_receive:I:retries:}";


    template<>
    struct py_type<winrt::Windows::Web::Http::HttpCompletionOption>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpCompletionOption";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpProgressStage>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpProgressStage";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpResponseMessageSource>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpResponseMessageSource";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpStatusCode>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpStatusCode";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpVersion>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpVersion";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpBufferContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpBufferContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpClient>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpClient";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpCookie>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpCookie";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpCookieCollection>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpCookieCollection";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpCookieManager>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpCookieManager";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpFormUrlEncodedContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpFormUrlEncodedContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpGetBufferResult>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpGetBufferResult";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpGetInputStreamResult>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpGetInputStreamResult";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpGetStringResult>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpGetStringResult";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpMethod>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpMethod";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpMultipartContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpMultipartContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpMultipartFormDataContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpMultipartFormDataContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpRequestMessage>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpRequestMessage";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpRequestResult>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpRequestResult";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpResponseMessage>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpResponseMessage";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpStreamContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpStreamContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpStringContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpStringContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpTransportInformation>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpTransportInformation";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::IHttpContent>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "IHttpContent";
    };

    template<>
    struct py_type<winrt::Windows::Web::Http::HttpProgress>
    {
        static constexpr const char* module_name = "winrt.windows.web.http";
        static constexpr const char* type_name = "HttpProgress";
    };
}