# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_applicationmodel_appointments

class AppointmentBusyStatus(enum.IntEnum):
    BUSY = 0
    TENTATIVE = 1
    FREE = 2
    OUT_OF_OFFICE = 3
    WORKING_ELSEWHERE = 4

class AppointmentCalendarOtherAppReadAccess(enum.IntEnum):
    SYSTEM_ONLY = 0
    LIMITED = 1
    FULL = 2
    NONE = 3

class AppointmentCalendarOtherAppWriteAccess(enum.IntEnum):
    NONE = 0
    SYSTEM_ONLY = 1
    LIMITED = 2

class AppointmentCalendarSyncStatus(enum.IntEnum):
    IDLE = 0
    SYNCING = 1
    UP_TO_DATE = 2
    AUTHENTICATION_ERROR = 3
    POLICY_ERROR = 4
    UNKNOWN_ERROR = 5
    MANUAL_ACCOUNT_REMOVAL_REQUIRED = 6

class AppointmentConflictType(enum.IntEnum):
    NONE = 0
    ADJACENT = 1
    OVERLAP = 2

class AppointmentDaysOfWeek(enum.IntFlag):
    NONE = 0
    SUNDAY = 0x1
    MONDAY = 0x2
    TUESDAY = 0x4
    WEDNESDAY = 0x8
    THURSDAY = 0x10
    FRIDAY = 0x20
    SATURDAY = 0x40

class AppointmentDetailsKind(enum.IntEnum):
    PLAIN_TEXT = 0
    HTML = 1

class AppointmentParticipantResponse(enum.IntEnum):
    NONE = 0
    TENTATIVE = 1
    ACCEPTED = 2
    DECLINED = 3
    UNKNOWN = 4

class AppointmentParticipantRole(enum.IntEnum):
    REQUIRED_ATTENDEE = 0
    OPTIONAL_ATTENDEE = 1
    RESOURCE = 2

class AppointmentRecurrenceUnit(enum.IntEnum):
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    MONTHLY_ON_DAY = 3
    YEARLY = 4
    YEARLY_ON_DAY = 5

class AppointmentSensitivity(enum.IntEnum):
    PUBLIC = 0
    PRIVATE = 1

class AppointmentStoreAccessType(enum.IntEnum):
    APP_CALENDARS_READ_WRITE = 0
    ALL_CALENDARS_READ_ONLY = 1
    ALL_CALENDARS_READ_WRITE = 2

class AppointmentStoreChangeType(enum.IntEnum):
    APPOINTMENT_CREATED = 0
    APPOINTMENT_MODIFIED = 1
    APPOINTMENT_DELETED = 2
    CHANGE_TRACKING_LOST = 3
    CALENDAR_CREATED = 4
    CALENDAR_MODIFIED = 5
    CALENDAR_DELETED = 6

class AppointmentSummaryCardView(enum.IntEnum):
    SYSTEM = 0
    APP = 1

class AppointmentWeekOfMonth(enum.IntEnum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3
    LAST = 4

class FindAppointmentCalendarsOptions(enum.IntFlag):
    NONE = 0
    INCLUDE_HIDDEN = 0x1

class RecurrenceType(enum.IntEnum):
    MASTER = 0
    INSTANCE = 1
    EXCEPTION_INSTANCE = 2

Appointment = _winrt_windows_applicationmodel_appointments.Appointment
AppointmentCalendar = _winrt_windows_applicationmodel_appointments.AppointmentCalendar
AppointmentCalendarSyncManager = _winrt_windows_applicationmodel_appointments.AppointmentCalendarSyncManager
AppointmentConflictResult = _winrt_windows_applicationmodel_appointments.AppointmentConflictResult
AppointmentException = _winrt_windows_applicationmodel_appointments.AppointmentException
AppointmentInvitee = _winrt_windows_applicationmodel_appointments.AppointmentInvitee
AppointmentManager = _winrt_windows_applicationmodel_appointments.AppointmentManager
AppointmentManagerForUser = _winrt_windows_applicationmodel_appointments.AppointmentManagerForUser
AppointmentOrganizer = _winrt_windows_applicationmodel_appointments.AppointmentOrganizer
AppointmentProperties = _winrt_windows_applicationmodel_appointments.AppointmentProperties
AppointmentRecurrence = _winrt_windows_applicationmodel_appointments.AppointmentRecurrence
AppointmentStore = _winrt_windows_applicationmodel_appointments.AppointmentStore
AppointmentStoreChange = _winrt_windows_applicationmodel_appointments.AppointmentStoreChange
AppointmentStoreChangeReader = _winrt_windows_applicationmodel_appointments.AppointmentStoreChangeReader
AppointmentStoreChangeTracker = _winrt_windows_applicationmodel_appointments.AppointmentStoreChangeTracker
AppointmentStoreChangedDeferral = _winrt_windows_applicationmodel_appointments.AppointmentStoreChangedDeferral
AppointmentStoreChangedEventArgs = _winrt_windows_applicationmodel_appointments.AppointmentStoreChangedEventArgs
AppointmentStoreNotificationTriggerDetails = _winrt_windows_applicationmodel_appointments.AppointmentStoreNotificationTriggerDetails
FindAppointmentsOptions = _winrt_windows_applicationmodel_appointments.FindAppointmentsOptions
IAppointmentParticipant = _winrt_windows_applicationmodel_appointments.IAppointmentParticipant