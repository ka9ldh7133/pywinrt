# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_applicationmodel_userdataaccounts

class UserDataAccountContentKinds(enum.IntFlag):
    EMAIL = 0x1
    CONTACT = 0x2
    APPOINTMENT = 0x4

class UserDataAccountOtherAppReadAccess(enum.IntEnum):
    SYSTEM_ONLY = 0
    FULL = 1
    NONE = 2

class UserDataAccountStoreAccessType(enum.IntEnum):
    ALL_ACCOUNTS_READ_ONLY = 0
    APP_ACCOUNTS_READ_WRITE = 1

UserDataAccount = _winrt_windows_applicationmodel_userdataaccounts.UserDataAccount
UserDataAccountManager = _winrt_windows_applicationmodel_userdataaccounts.UserDataAccountManager
UserDataAccountManagerForUser = _winrt_windows_applicationmodel_userdataaccounts.UserDataAccountManagerForUser
UserDataAccountStore = _winrt_windows_applicationmodel_userdataaccounts.UserDataAccountStore
UserDataAccountStoreChangedEventArgs = _winrt_windows_applicationmodel_userdataaccounts.UserDataAccountStoreChangedEventArgs