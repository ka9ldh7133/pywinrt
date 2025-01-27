// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Storage.h>
#include <winrt/Windows.System.h>

#include <winrt/Windows.Storage.Streams.h>

namespace py::proj::Windows::Storage::Streams
{
}

namespace py::impl::Windows::Storage::Streams
{
}

namespace py::wrapper::Windows::Storage::Streams
{
    using Buffer = py::winrt_wrapper<winrt::Windows::Storage::Streams::Buffer>;
    using DataReader = py::winrt_wrapper<winrt::Windows::Storage::Streams::DataReader>;
    using DataReaderLoadOperation = py::winrt_wrapper<winrt::Windows::Storage::Streams::DataReaderLoadOperation>;
    using DataWriter = py::winrt_wrapper<winrt::Windows::Storage::Streams::DataWriter>;
    using DataWriterStoreOperation = py::winrt_wrapper<winrt::Windows::Storage::Streams::DataWriterStoreOperation>;
    using FileInputStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::FileInputStream>;
    using FileOutputStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::FileOutputStream>;
    using FileRandomAccessStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::FileRandomAccessStream>;
    using InMemoryRandomAccessStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::InMemoryRandomAccessStream>;
    using InputStreamOverStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::InputStreamOverStream>;
    using OutputStreamOverStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::OutputStreamOverStream>;
    using RandomAccessStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::RandomAccessStream>;
    using RandomAccessStreamOverStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::RandomAccessStreamOverStream>;
    using RandomAccessStreamReference = py::winrt_wrapper<winrt::Windows::Storage::Streams::RandomAccessStreamReference>;
    using IBuffer = py::winrt_wrapper<winrt::Windows::Storage::Streams::IBuffer>;
    using IContentTypeProvider = py::winrt_wrapper<winrt::Windows::Storage::Streams::IContentTypeProvider>;
    using IDataReader = py::winrt_wrapper<winrt::Windows::Storage::Streams::IDataReader>;
    using IDataWriter = py::winrt_wrapper<winrt::Windows::Storage::Streams::IDataWriter>;
    using IInputStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::IInputStream>;
    using IInputStreamReference = py::winrt_wrapper<winrt::Windows::Storage::Streams::IInputStreamReference>;
    using IOutputStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::IOutputStream>;
    using IPropertySetSerializer = py::winrt_wrapper<winrt::Windows::Storage::Streams::IPropertySetSerializer>;
    using IRandomAccessStream = py::winrt_wrapper<winrt::Windows::Storage::Streams::IRandomAccessStream>;
    using IRandomAccessStreamReference = py::winrt_wrapper<winrt::Windows::Storage::Streams::IRandomAccessStreamReference>;
    using IRandomAccessStreamWithContentType = py::winrt_wrapper<winrt::Windows::Storage::Streams::IRandomAccessStreamWithContentType>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Storage::Streams::ByteOrder> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Storage::Streams::FileOpenDisposition> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Storage::Streams::InputStreamOptions> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Storage::Streams::UnicodeEncoding> = "i";


    template<>
    struct py_type<winrt::Windows::Storage::Streams::ByteOrder>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.ByteOrder";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "ByteOrder";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::FileOpenDisposition>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.FileOpenDisposition";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "FileOpenDisposition";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::InputStreamOptions>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.InputStreamOptions";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "InputStreamOptions";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::UnicodeEncoding>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.UnicodeEncoding";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "UnicodeEncoding";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::Buffer>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.Buffer";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "Buffer";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::DataReader>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.DataReader";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "DataReader";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::DataReaderLoadOperation>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.DataReaderLoadOperation";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "DataReaderLoadOperation";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::DataWriter>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.DataWriter";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "DataWriter";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::DataWriterStoreOperation>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.DataWriterStoreOperation";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "DataWriterStoreOperation";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::FileInputStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.FileInputStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "FileInputStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::FileOutputStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.FileOutputStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "FileOutputStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::FileRandomAccessStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.FileRandomAccessStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "FileRandomAccessStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::InMemoryRandomAccessStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.InMemoryRandomAccessStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "InMemoryRandomAccessStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::InputStreamOverStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.InputStreamOverStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "InputStreamOverStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::OutputStreamOverStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.OutputStreamOverStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "OutputStreamOverStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::RandomAccessStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.RandomAccessStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "RandomAccessStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::RandomAccessStreamOverStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.RandomAccessStreamOverStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "RandomAccessStreamOverStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::RandomAccessStreamReference>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.RandomAccessStreamReference";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "RandomAccessStreamReference";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IBuffer>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IBuffer";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IBuffer";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IContentTypeProvider>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IContentTypeProvider";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IContentTypeProvider";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IDataReader>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IDataReader";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IDataReader";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IDataWriter>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IDataWriter";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IDataWriter";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IInputStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IInputStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IInputStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IInputStreamReference>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IInputStreamReference";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IInputStreamReference";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IOutputStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IOutputStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IOutputStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IPropertySetSerializer>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IPropertySetSerializer";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IPropertySetSerializer";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IRandomAccessStream>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IRandomAccessStream";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IRandomAccessStream";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IRandomAccessStreamReference>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IRandomAccessStreamReference";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IRandomAccessStreamReference";
    };

    template<>
    struct py_type<winrt::Windows::Storage::Streams::IRandomAccessStreamWithContentType>
    {
        static constexpr std::string_view qualified_name = "winrt.windows.storage.streams.IRandomAccessStreamWithContentType";
        static constexpr const char* module_name = "winrt.windows.storage.streams";
        static constexpr const char* type_name = "IRandomAccessStreamWithContentType";
    };
}
