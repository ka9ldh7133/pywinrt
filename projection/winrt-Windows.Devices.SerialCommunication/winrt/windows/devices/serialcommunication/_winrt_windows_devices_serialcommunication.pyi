# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.storage.streams

from . import SerialError, SerialHandshake, SerialParity, SerialPinChange, SerialStopBitCount

Self = typing.TypeVar('Self')

class ErrorReceivedEventArgs(winrt.system.Object):
    error: SerialError
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ErrorReceivedEventArgs: ...

class PinChangedEventArgs(winrt.system.Object):
    pin_change: SerialPinChange
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PinChangedEventArgs: ...

class SerialDevice(winrt.system.Object):
    is_data_terminal_ready_enabled: winrt.system.Boolean
    data_bits: winrt.system.UInt16
    handshake: SerialHandshake
    break_signal_state: winrt.system.Boolean
    baud_rate: winrt.system.UInt32
    write_timeout: datetime.timedelta
    stop_bits: SerialStopBitCount
    read_timeout: datetime.timedelta
    parity: SerialParity
    is_request_to_send_enabled: winrt.system.Boolean
    bytes_received: winrt.system.UInt32
    carrier_detect_state: winrt.system.Boolean
    clear_to_send_state: winrt.system.Boolean
    data_set_ready_state: winrt.system.Boolean
    input_stream: typing.Optional[winrt.windows.storage.streams.IInputStream]
    output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream]
    port_name: str
    usb_product_id: winrt.system.UInt16
    usb_vendor_id: winrt.system.UInt16
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SerialDevice: ...
    def close(self) -> None: ...
    @staticmethod
    def from_id_async(device_id: str, /) -> winrt.windows.foundation.IAsyncOperation[SerialDevice]: ...
    @typing.overload
    @staticmethod
    def get_device_selector() -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector(port_name: str, /) -> str: ...
    @staticmethod
    def get_device_selector_from_usb_vid_pid(vendor_id: winrt.system.UInt16, product_id: winrt.system.UInt16, /) -> str: ...
    def add_error_received(self, report_handler: winrt.windows.foundation.TypedEventHandler[SerialDevice, ErrorReceivedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_error_received(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pin_changed(self, report_handler: winrt.windows.foundation.TypedEventHandler[SerialDevice, PinChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pin_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
