# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_devices_gpio_provider

class ProviderGpioPinDriveMode(enum.IntEnum):
    INPUT = 0
    OUTPUT = 1
    INPUT_PULL_UP = 2
    INPUT_PULL_DOWN = 3
    OUTPUT_OPEN_DRAIN = 4
    OUTPUT_OPEN_DRAIN_PULL_UP = 5
    OUTPUT_OPEN_SOURCE = 6
    OUTPUT_OPEN_SOURCE_PULL_DOWN = 7

class ProviderGpioPinEdge(enum.IntEnum):
    FALLING_EDGE = 0
    RISING_EDGE = 1

class ProviderGpioPinValue(enum.IntEnum):
    LOW = 0
    HIGH = 1

class ProviderGpioSharingMode(enum.IntEnum):
    EXCLUSIVE = 0
    SHARED_READ_ONLY = 1

GpioPinProviderValueChangedEventArgs = _winrt_windows_devices_gpio_provider.GpioPinProviderValueChangedEventArgs
IGpioControllerProvider = _winrt_windows_devices_gpio_provider.IGpioControllerProvider
IGpioPinProvider = _winrt_windows_devices_gpio_provider.IGpioPinProvider
IGpioProvider = _winrt_windows_devices_gpio_provider.IGpioProvider