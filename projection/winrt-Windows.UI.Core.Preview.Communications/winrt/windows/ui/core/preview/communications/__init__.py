# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_ui_core_preview_communications

class PreviewMeetingInfoDisplayKind(enum.IntEnum):
    ORGANIZER_AND_TIME = 0
    ORGANIZER_TIME_AND_TITLE = 1

class PreviewSystemState(enum.IntEnum):
    PREPARING = 0
    REBOOTING = 1
    ERROR = 2
    SESSION_PAUSED = 3
    READY = 4

class PreviewTeamEndMeetingKind(enum.IntEnum):
    SHOW_DEFAULT_VIEW = 0
    CLOSE_VIEW = 1

class PreviewTeamViewCommand(enum.IntEnum):
    TOGGLE_CALL_CONTROL = 0
    SHOW_PEOPLE = 1
    SHOW_MESSAGING = 2
    SHOW_CONTENT = 3
    TOGGLE_MICROPHONE = 4
    TOGGLE_CAMERA = 5
    SHOW_CALENDAR = 6
    TOGGLE_SCREEN_SHARING = 7
    TOGGLE_FULL_SCREEN = 8

PreviewTeamCleanupRequestedEventArgs = _winrt_windows_ui_core_preview_communications.PreviewTeamCleanupRequestedEventArgs
PreviewTeamCommandInvokedEventArgs = _winrt_windows_ui_core_preview_communications.PreviewTeamCommandInvokedEventArgs
PreviewTeamDeviceCredentials = _winrt_windows_ui_core_preview_communications.PreviewTeamDeviceCredentials
PreviewTeamEndMeetingRequestedEventArgs = _winrt_windows_ui_core_preview_communications.PreviewTeamEndMeetingRequestedEventArgs
PreviewTeamJoinMeetingRequestedEventArgs = _winrt_windows_ui_core_preview_communications.PreviewTeamJoinMeetingRequestedEventArgs
PreviewTeamView = _winrt_windows_ui_core_preview_communications.PreviewTeamView