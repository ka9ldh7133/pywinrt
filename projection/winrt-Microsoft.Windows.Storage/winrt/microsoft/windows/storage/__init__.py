# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt import _winrt_microsoft_windows_storage

__all__ = [
    "ApplicationDataCreateDisposition",
    "ApplicationDataLocality",
    "ApplicationData",
    "ApplicationDataContainer",
]

class ApplicationDataCreateDisposition(enum.IntEnum):
    ALWAYS = 0
    EXISTING = 1

class ApplicationDataLocality(enum.IntEnum):
    LOCAL = 0
    LOCAL_CACHE = 3
    SHARED_LOCAL = 4
    TEMPORARY = 2
    MACHINE = 1000

ApplicationData = _winrt_microsoft_windows_storage.ApplicationData
ApplicationDataContainer = _winrt_microsoft_windows_storage.ApplicationDataContainer