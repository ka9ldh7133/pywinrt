# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import datetime
import sys
import types
import typing

import winrt.system

class SpeechRecognitionUIStatus(enum.IntEnum):
    SUCCEEDED = 0
    BUSY = 1
    CANCELLED = 2
    PREEMPTED = 3
    PRIVACY_POLICY_DECLINED = 4

Self = typing.TypeVar('Self')
