# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel as windows_applicationmodel
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.management.deployment as windows_management_deployment

from winrt.windows.phone.management.deployment import EnterpriseEnrollmentStatus, EnterpriseStatus

Self = typing.TypeVar('Self')

@typing.final
class Enterprise(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Enterprise: ...
    @_property
    def enrollment_valid_from(self) -> datetime.datetime: ...
    @_property
    def enrollment_valid_to(self) -> datetime.datetime: ...
    @_property
    def id(self) -> _uuid.UUID: ...
    @_property
    def name(self) -> str: ...
    @_property
    def status(self) -> EnterpriseStatus: ...
    @_property
    def workplace_id(self) -> winrt.system.Int32: ...

@typing.final
class EnterpriseEnrollmentManager_Static(type):
    def request_enrollment_async(cls, enrollment_token: str, /) -> windows_foundation.IAsyncOperation[EnterpriseEnrollmentResult]: ...
    def request_unenrollment_async(cls, enterprise: Enterprise, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def validate_enterprises_async(cls) -> windows_foundation.IAsyncAction: ...
    @_property
    def current_enterprise(cls) -> Enterprise: ...
    @_property
    def enrolled_enterprises(cls) -> typing.Sequence[Enterprise]: ...

@typing.final
class EnterpriseEnrollmentManager(winrt.system.Object, metaclass=EnterpriseEnrollmentManager_Static):
    pass

@typing.final
class EnterpriseEnrollmentResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> EnterpriseEnrollmentResult: ...
    @_property
    def enrolled_enterprise(self) -> Enterprise: ...
    @_property
    def status(self) -> EnterpriseEnrollmentStatus: ...

@typing.final
class InstallationManager_Static(type):
    def add_package_async(cls, title: str, source_location: windows_foundation.Uri, /) -> windows_foundation.IAsyncOperationWithProgress[PackageInstallResult, winrt.system.UInt32]: ...
    def add_package_preloaded_async(cls, title: str, source_location: windows_foundation.Uri, instance_id: str, offer_id: str, license: windows_foundation.Uri, /) -> windows_foundation.IAsyncOperationWithProgress[PackageInstallResult, winrt.system.UInt32]: ...
    def find_packages(cls) -> typing.Iterable[windows_applicationmodel.Package]: ...
    def find_packages_by_name_publisher(cls, package_name: str, package_publisher: str, /) -> typing.Iterable[windows_applicationmodel.Package]: ...
    def find_packages_for_current_publisher(cls) -> typing.Iterable[windows_applicationmodel.Package]: ...
    def get_pending_package_installs(cls) -> typing.Iterable[windows_foundation.IAsyncOperationWithProgress[PackageInstallResult, winrt.system.UInt32]]: ...
    def register_package_async(cls, manifest_uri: windows_foundation.Uri, dependency_package_uris: typing.Iterable[windows_foundation.Uri], deployment_options: windows_management_deployment.DeploymentOptions, /) -> windows_foundation.IAsyncOperationWithProgress[PackageInstallResult, winrt.system.UInt32]: ...
    def remove_package_async(cls, package_full_name: str, removal_options: windows_management_deployment.RemovalOptions, /) -> windows_foundation.IAsyncOperationWithProgress[PackageInstallResult, winrt.system.UInt32]: ...

@typing.final
class InstallationManager(winrt.system.Object, metaclass=InstallationManager_Static):
    pass

@typing.final
class PackageInstallResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageInstallResult: ...
    @_property
    def install_state(self) -> windows_management_deployment.PackageInstallState: ...
    @_property
    def product_id(self) -> str: ...
    @_property
    def error_text(self) -> str: ...

