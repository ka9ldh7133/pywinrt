# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt._winrt_windows_storage_streams import (
    Buffer,
    DataReader,
    DataReaderLoadOperation,
    DataWriter,
    DataWriterStoreOperation,
    FileInputStream,
    FileOutputStream,
    FileRandomAccessStream,
    InMemoryRandomAccessStream,
    InputStreamOverStream,
    OutputStreamOverStream,
    RandomAccessStream,
    RandomAccessStreamOverStream,
    RandomAccessStreamReference,
    IBuffer,
    ImplementsIBuffer,
    IContentTypeProvider,
    ImplementsIContentTypeProvider,
    IDataReader,
    ImplementsIDataReader,
    IDataWriter,
    ImplementsIDataWriter,
    IInputStream,
    ImplementsIInputStream,
    IInputStreamReference,
    ImplementsIInputStreamReference,
    IOutputStream,
    ImplementsIOutputStream,
    IPropertySetSerializer,
    ImplementsIPropertySetSerializer,
    IRandomAccessStream,
    ImplementsIRandomAccessStream,
    IRandomAccessStreamReference,
    ImplementsIRandomAccessStreamReference,
    IRandomAccessStreamWithContentType,
    ImplementsIRandomAccessStreamWithContentType,
)

__all__ = [
    "ByteOrder",
    "FileOpenDisposition",
    "InputStreamOptions",
    "UnicodeEncoding",
    "Buffer",
    "DataReader",
    "DataReaderLoadOperation",
    "DataWriter",
    "DataWriterStoreOperation",
    "FileInputStream",
    "FileOutputStream",
    "FileRandomAccessStream",
    "InMemoryRandomAccessStream",
    "InputStreamOverStream",
    "OutputStreamOverStream",
    "RandomAccessStream",
    "RandomAccessStreamOverStream",
    "RandomAccessStreamReference",
    "IBuffer",
    "ImplementsIBuffer",
    "IContentTypeProvider",
    "ImplementsIContentTypeProvider",
    "IDataReader",
    "ImplementsIDataReader",
    "IDataWriter",
    "ImplementsIDataWriter",
    "IInputStream",
    "ImplementsIInputStream",
    "IInputStreamReference",
    "ImplementsIInputStreamReference",
    "IOutputStream",
    "ImplementsIOutputStream",
    "IPropertySetSerializer",
    "ImplementsIPropertySetSerializer",
    "IRandomAccessStream",
    "ImplementsIRandomAccessStream",
    "IRandomAccessStreamReference",
    "ImplementsIRandomAccessStreamReference",
    "IRandomAccessStreamWithContentType",
    "ImplementsIRandomAccessStreamWithContentType",
]

class ByteOrder(enum.IntEnum):
    LITTLE_ENDIAN = 0
    BIG_ENDIAN = 1

class FileOpenDisposition(enum.IntEnum):
    OPEN_EXISTING = 0
    OPEN_ALWAYS = 1
    CREATE_NEW = 2
    CREATE_ALWAYS = 3
    TRUNCATE_EXISTING = 4

class InputStreamOptions(enum.IntFlag):
    NONE = 0x0
    PARTIAL = 0x1
    READ_AHEAD = 0x2

class UnicodeEncoding(enum.IntEnum):
    UTF8 = 0
    UTF16_L_E = 1
    UTF16_B_E = 2

