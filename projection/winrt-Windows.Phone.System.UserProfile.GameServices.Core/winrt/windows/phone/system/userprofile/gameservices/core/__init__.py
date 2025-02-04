# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt._winrt_windows_phone_system_userprofile_gameservices_core import (
    GameService,
    GameServicePropertyCollection,
)

__all__ = [
    "GameServiceGameOutcome",
    "GameServiceScoreKind",
    "GameService",
    "GameServicePropertyCollection",
]

class GameServiceGameOutcome(enum.IntEnum):
    NONE = 0
    WIN = 1
    LOSS = 2
    TIE = 3

class GameServiceScoreKind(enum.IntEnum):
    NUMBER = 0
    TIME = 1

