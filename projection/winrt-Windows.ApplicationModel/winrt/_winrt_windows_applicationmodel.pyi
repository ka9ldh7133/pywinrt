# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel.activation
import winrt.windows.applicationmodel.core
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.storage
import winrt.windows.storage.streams
import winrt.windows.system

from winrt.windows.applicationmodel import AddResourcePackageOptions, AppExecutionContext, AppInstallerPolicySource, FullTrustLaunchResult, LimitedAccessFeatureStatus, PackageContentGroupState, PackageRelationship, PackageSignatureKind, PackageUpdateAvailability, StartupTaskState

Self = typing.TypeVar('Self')

class PackageInstallProgress:
    percent_complete: winrt.system.UInt32
    def __init__(self, percent_complete: winrt.system.UInt32) -> None: ...

class PackageVersion:
    major: winrt.system.UInt16
    minor: winrt.system.UInt16
    build: winrt.system.UInt16
    revision: winrt.system.UInt16
    def __init__(self, major: winrt.system.UInt16, minor: winrt.system.UInt16, build: winrt.system.UInt16, revision: winrt.system.UInt16) -> None: ...

class AppDisplayInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppDisplayInfo: ...
    def get_logo(self, size: winrt.windows.foundation.Size, /) -> typing.Optional[winrt.windows.storage.streams.RandomAccessStreamReference]: ...
    @_property
    def description(self) -> str: ...
    @_property
    def display_name(self) -> str: ...

class AppInfo_Static(type):
    def get_from_app_user_model_id(cls, app_user_model_id: str, /) -> typing.Optional[AppInfo]: ...
    def get_from_app_user_model_id_for_user(cls, user: typing.Optional[winrt.windows.system.User], app_user_model_id: str, /) -> typing.Optional[AppInfo]: ...
    @_property
    def current(cls) -> typing.Optional[AppInfo]: ...

class AppInfo(winrt.system.Object, metaclass=AppInfo_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppInfo: ...
    @_property
    def app_user_model_id(self) -> str: ...
    @_property
    def display_info(self) -> typing.Optional[AppDisplayInfo]: ...
    @_property
    def id(self) -> str: ...
    @_property
    def package_family_name(self) -> str: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...
    @_property
    def execution_context(self) -> AppExecutionContext: ...
    @_property
    def supported_file_extensions(self) -> str: ...

class AppInstallerInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppInstallerInfo: ...
    @_property
    def uri(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def automatic_background_task(self) -> bool: ...
    @_property
    def dependency_package_uris(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Uri]]: ...
    @_property
    def force_update_from_any_version(self) -> bool: ...
    @_property
    def hours_between_update_checks(self) -> winrt.system.UInt32: ...
    @_property
    def is_auto_repair_enabled(self) -> bool: ...
    @_property
    def last_checked(self) -> datetime.datetime: ...
    @_property
    def on_launch(self) -> bool: ...
    @_property
    def optional_package_uris(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Uri]]: ...
    @_property
    def paused_until(self) -> typing.Optional[typing.Optional[datetime.datetime]]: ...
    @_property
    def policy_source(self) -> AppInstallerPolicySource: ...
    @_property
    def repair_uris(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Uri]]: ...
    @_property
    def show_prompt(self) -> bool: ...
    @_property
    def update_blocks_activation(self) -> bool: ...
    @_property
    def update_uris(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Uri]]: ...
    @_property
    def version(self) -> PackageVersion: ...

class AppInstance_Static(type):
    def find_or_register_instance_for_key(cls, key: str, /) -> typing.Optional[AppInstance]: ...
    def get_activated_event_args(cls) -> typing.Optional[winrt.windows.applicationmodel.activation.IActivatedEventArgs]: ...
    def get_instances(cls) -> typing.Optional[winrt.windows.foundation.collections.IVector[AppInstance]]: ...
    def unregister(cls) -> None: ...
    @_property
    def recommended_instance(cls) -> typing.Optional[AppInstance]: ...

class AppInstance(winrt.system.Object, metaclass=AppInstance_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppInstance: ...
    def redirect_activation_to(self) -> None: ...
    @_property
    def is_current_instance(self) -> bool: ...
    @_property
    def key(self) -> str: ...

class CameraApplicationManager_Static(type):
    def show_installed_applications_u_i(cls) -> None: ...

class CameraApplicationManager(winrt.system.Object, metaclass=CameraApplicationManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CameraApplicationManager: ...

class DesignMode_Static(type):
    @_property
    def design_mode_enabled(cls) -> bool: ...
    @_property
    def design_mode2_enabled(cls) -> bool: ...

class DesignMode(winrt.system.Object, metaclass=DesignMode_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DesignMode: ...

class EnteredBackgroundEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> EnteredBackgroundEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class FindRelatedPackagesOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FindRelatedPackagesOptions: ...
    def __new__(cls: typing.Type[FindRelatedPackagesOptions], relationship: PackageRelationship) -> FindRelatedPackagesOptions:...
    @_property
    def relationship(self) -> PackageRelationship: ...
    @relationship.setter
    def relationship(self, value: PackageRelationship) -> None: ...
    @_property
    def include_resources(self) -> bool: ...
    @include_resources.setter
    def include_resources(self, value: bool) -> None: ...
    @_property
    def include_optionals(self) -> bool: ...
    @include_optionals.setter
    def include_optionals(self, value: bool) -> None: ...
    @_property
    def include_host_runtimes(self) -> bool: ...
    @include_host_runtimes.setter
    def include_host_runtimes(self, value: bool) -> None: ...
    @_property
    def include_frameworks(self) -> bool: ...
    @include_frameworks.setter
    def include_frameworks(self, value: bool) -> None: ...

class FullTrustProcessLaunchResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FullTrustProcessLaunchResult: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def launch_result(self) -> FullTrustLaunchResult: ...

class FullTrustProcessLauncher_Static(type):
    @typing.overload
    def launch_full_trust_process_for_app_async(cls, full_trust_package_relative_app_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def launch_full_trust_process_for_app_async(cls, full_trust_package_relative_app_id: str, parameter_group_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def launch_full_trust_process_for_app_with_arguments_async(cls, full_trust_package_relative_app_id: str, command_line: str, /) -> winrt.windows.foundation.IAsyncOperation[FullTrustProcessLaunchResult]: ...
    @typing.overload
    def launch_full_trust_process_for_current_app_async(cls) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def launch_full_trust_process_for_current_app_async(cls, parameter_group_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def launch_full_trust_process_for_current_app_with_arguments_async(cls, command_line: str, /) -> winrt.windows.foundation.IAsyncOperation[FullTrustProcessLaunchResult]: ...

class FullTrustProcessLauncher(winrt.system.Object, metaclass=FullTrustProcessLauncher_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FullTrustProcessLauncher: ...

class LeavingBackgroundEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LeavingBackgroundEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class LimitedAccessFeatureRequestResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LimitedAccessFeatureRequestResult: ...
    @_property
    def estimated_removal_date(self) -> typing.Optional[typing.Optional[datetime.datetime]]: ...
    @_property
    def feature_id(self) -> str: ...
    @_property
    def status(self) -> LimitedAccessFeatureStatus: ...

class LimitedAccessFeatures_Static(type):
    def try_unlock_feature(cls, feature_id: str, token: str, attestation: str, /) -> typing.Optional[LimitedAccessFeatureRequestResult]: ...

class LimitedAccessFeatures(winrt.system.Object, metaclass=LimitedAccessFeatures_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LimitedAccessFeatures: ...

class Package_Static(type):
    @_property
    def current(cls) -> typing.Optional[Package]: ...

class Package(winrt.system.Object, metaclass=Package_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Package: ...
    def check_update_availability_async(self) -> winrt.windows.foundation.IAsyncOperation[PackageUpdateAvailabilityResult]: ...
    def find_related_packages(self, options: typing.Optional[FindRelatedPackagesOptions], /) -> typing.Optional[winrt.windows.foundation.collections.IVector[Package]]: ...
    def get_app_installer_info(self) -> typing.Optional[AppInstallerInfo]: ...
    def get_app_list_entries(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.applicationmodel.core.AppListEntry]]: ...
    def get_app_list_entries_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[winrt.windows.applicationmodel.core.AppListEntry]]: ...
    def get_content_group_async(self, name: str, /) -> winrt.windows.foundation.IAsyncOperation[PackageContentGroup]: ...
    def get_content_groups_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVector[PackageContentGroup]]: ...
    def get_logo_as_random_access_stream_reference(self, size: winrt.windows.foundation.Size, /) -> typing.Optional[winrt.windows.storage.streams.RandomAccessStreamReference]: ...
    def get_thumbnail_token(self) -> str: ...
    def launch(self, parameters: str, /) -> None: ...
    def set_in_use_async(self, in_use: bool, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def stage_content_groups_async(self, names: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVector[PackageContentGroup]]: ...
    @typing.overload
    def stage_content_groups_async(self, names: typing.Iterable[str], move_to_head_of_queue: bool, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVector[PackageContentGroup]]: ...
    def verify_content_integrity_async(self) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @_property
    def dependencies(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[Package]]: ...
    @_property
    def id(self) -> typing.Optional[PackageId]: ...
    @_property
    def installed_location(self) -> typing.Optional[winrt.windows.storage.StorageFolder]: ...
    @_property
    def is_framework(self) -> bool: ...
    @_property
    def description(self) -> str: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def is_bundle(self) -> bool: ...
    @_property
    def is_development_mode(self) -> bool: ...
    @_property
    def is_resource_package(self) -> bool: ...
    @_property
    def logo(self) -> typing.Optional[winrt.windows.foundation.Uri]: ...
    @_property
    def publisher_display_name(self) -> str: ...
    @_property
    def installed_date(self) -> datetime.datetime: ...
    @_property
    def status(self) -> typing.Optional[PackageStatus]: ...
    @_property
    def is_optional(self) -> bool: ...
    @_property
    def signature_kind(self) -> PackageSignatureKind: ...
    @_property
    def effective_location(self) -> typing.Optional[winrt.windows.storage.StorageFolder]: ...
    @_property
    def mutable_location(self) -> typing.Optional[winrt.windows.storage.StorageFolder]: ...
    @_property
    def effective_external_location(self) -> typing.Optional[winrt.windows.storage.StorageFolder]: ...
    @_property
    def effective_external_path(self) -> str: ...
    @_property
    def effective_path(self) -> str: ...
    @_property
    def installed_path(self) -> str: ...
    @_property
    def is_stub(self) -> bool: ...
    @_property
    def machine_external_location(self) -> typing.Optional[winrt.windows.storage.StorageFolder]: ...
    @_property
    def machine_external_path(self) -> str: ...
    @_property
    def mutable_path(self) -> str: ...
    @_property
    def user_external_location(self) -> typing.Optional[winrt.windows.storage.StorageFolder]: ...
    @_property
    def user_external_path(self) -> str: ...
    @_property
    def source_uri_scheme_name(self) -> str: ...
    @_property
    def install_date(self) -> datetime.datetime: ...

class PackageCatalog_Static(type):
    def open_for_current_package(cls) -> typing.Optional[PackageCatalog]: ...
    def open_for_current_user(cls) -> typing.Optional[PackageCatalog]: ...
    def open_for_package(cls, package: typing.Optional[Package], /) -> typing.Optional[PackageCatalog]: ...

class PackageCatalog(winrt.system.Object, metaclass=PackageCatalog_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageCatalog: ...
    def add_optional_package_async(self, optional_package_family_name: str, /) -> winrt.windows.foundation.IAsyncOperation[PackageCatalogAddOptionalPackageResult]: ...
    def add_resource_package_async(self, resource_package_family_name: str, resource_i_d: str, options: AddResourcePackageOptions, /) -> winrt.windows.foundation.IAsyncOperationWithProgress[PackageCatalogAddResourcePackageResult, PackageInstallProgress]: ...
    def remove_optional_packages_async(self, optional_package_family_names: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[PackageCatalogRemoveOptionalPackagesResult]: ...
    def remove_resource_packages_async(self, resource_packages: typing.Iterable[Package], /) -> winrt.windows.foundation.IAsyncOperation[PackageCatalogRemoveResourcePackagesResult]: ...
    def add_package_installing(self, handler: winrt.windows.foundation.TypedEventHandler[PackageCatalog, PackageInstallingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_package_installing(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_package_staging(self, handler: winrt.windows.foundation.TypedEventHandler[PackageCatalog, PackageStagingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_package_staging(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_package_status_changed(self, handler: winrt.windows.foundation.TypedEventHandler[PackageCatalog, PackageStatusChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_package_status_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_package_uninstalling(self, handler: winrt.windows.foundation.TypedEventHandler[PackageCatalog, PackageUninstallingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_package_uninstalling(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_package_updating(self, handler: winrt.windows.foundation.TypedEventHandler[PackageCatalog, PackageUpdatingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_package_updating(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_package_content_group_staging(self, handler: winrt.windows.foundation.TypedEventHandler[PackageCatalog, PackageContentGroupStagingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_package_content_group_staging(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class PackageCatalogAddOptionalPackageResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageCatalogAddOptionalPackageResult: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...

class PackageCatalogAddResourcePackageResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageCatalogAddResourcePackageResult: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def is_complete(self) -> bool: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...

class PackageCatalogRemoveOptionalPackagesResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageCatalogRemoveOptionalPackagesResult: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def packages_removed(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[Package]]: ...

class PackageCatalogRemoveResourcePackagesResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageCatalogRemoveResourcePackagesResult: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def packages_removed(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[Package]]: ...

class PackageContentGroup_Static(type):
    @_property
    def required_group_name(cls) -> str: ...

class PackageContentGroup(winrt.system.Object, metaclass=PackageContentGroup_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageContentGroup: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def name(self) -> str: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...
    @_property
    def state(self) -> PackageContentGroupState: ...

class PackageContentGroupStagingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageContentGroupStagingEventArgs: ...
    @_property
    def activity_id(self) -> _uuid.UUID: ...
    @_property
    def content_group_name(self) -> str: ...
    @_property
    def error_code(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def is_complete(self) -> bool: ...
    @_property
    def is_content_group_required(self) -> bool: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...
    @_property
    def progress(self) -> winrt.system.Double: ...

class PackageId(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageId: ...
    @_property
    def architecture(self) -> winrt.windows.system.ProcessorArchitecture: ...
    @_property
    def family_name(self) -> str: ...
    @_property
    def full_name(self) -> str: ...
    @_property
    def name(self) -> str: ...
    @_property
    def publisher(self) -> str: ...
    @_property
    def publisher_id(self) -> str: ...
    @_property
    def resource_id(self) -> str: ...
    @_property
    def version(self) -> PackageVersion: ...
    @_property
    def author(self) -> str: ...
    @_property
    def product_id(self) -> str: ...

class PackageInstallingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageInstallingEventArgs: ...
    @_property
    def activity_id(self) -> _uuid.UUID: ...
    @_property
    def error_code(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def is_complete(self) -> bool: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...
    @_property
    def progress(self) -> winrt.system.Double: ...

class PackageStagingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageStagingEventArgs: ...
    @_property
    def activity_id(self) -> _uuid.UUID: ...
    @_property
    def error_code(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def is_complete(self) -> bool: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...
    @_property
    def progress(self) -> winrt.system.Double: ...

class PackageStatus(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageStatus: ...
    def verify_is_o_k(self) -> bool: ...
    @_property
    def data_offline(self) -> bool: ...
    @_property
    def dependency_issue(self) -> bool: ...
    @_property
    def deployment_in_progress(self) -> bool: ...
    @_property
    def disabled(self) -> bool: ...
    @_property
    def license_issue(self) -> bool: ...
    @_property
    def modified(self) -> bool: ...
    @_property
    def needs_remediation(self) -> bool: ...
    @_property
    def not_available(self) -> bool: ...
    @_property
    def package_offline(self) -> bool: ...
    @_property
    def servicing(self) -> bool: ...
    @_property
    def tampered(self) -> bool: ...
    @_property
    def is_partially_staged(self) -> bool: ...

class PackageStatusChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageStatusChangedEventArgs: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...

class PackageUninstallingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageUninstallingEventArgs: ...
    @_property
    def activity_id(self) -> _uuid.UUID: ...
    @_property
    def error_code(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def is_complete(self) -> bool: ...
    @_property
    def package(self) -> typing.Optional[Package]: ...
    @_property
    def progress(self) -> winrt.system.Double: ...

class PackageUpdateAvailabilityResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageUpdateAvailabilityResult: ...
    @_property
    def availability(self) -> PackageUpdateAvailability: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...

class PackageUpdatingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PackageUpdatingEventArgs: ...
    @_property
    def activity_id(self) -> _uuid.UUID: ...
    @_property
    def error_code(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def is_complete(self) -> bool: ...
    @_property
    def progress(self) -> winrt.system.Double: ...
    @_property
    def source_package(self) -> typing.Optional[Package]: ...
    @_property
    def target_package(self) -> typing.Optional[Package]: ...

class StartupTask_Static(type):
    def get_async(cls, task_id: str, /) -> winrt.windows.foundation.IAsyncOperation[StartupTask]: ...
    def get_for_current_package_async(cls) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[StartupTask]]: ...

class StartupTask(winrt.system.Object, metaclass=StartupTask_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StartupTask: ...
    def disable(self) -> None: ...
    def request_enable_async(self) -> winrt.windows.foundation.IAsyncOperation[StartupTaskState]: ...
    @_property
    def state(self) -> StartupTaskState: ...
    @_property
    def task_id(self) -> str: ...

class SuspendingDeferral(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SuspendingDeferral: ...
    def complete(self) -> None: ...

class SuspendingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SuspendingEventArgs: ...
    @_property
    def suspending_operation(self) -> typing.Optional[SuspendingOperation]: ...

class SuspendingOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SuspendingOperation: ...
    def get_deferral(self) -> typing.Optional[SuspendingDeferral]: ...
    @_property
    def deadline(self) -> datetime.datetime: ...

class IEnteredBackgroundEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IEnteredBackgroundEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class ILeavingBackgroundEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ILeavingBackgroundEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...

class IPackageCatalogStatics2(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IPackageCatalogStatics2: ...
    def open_for_package(self, package: typing.Optional[Package], /) -> typing.Optional[PackageCatalog]: ...

class ISuspendingDeferral(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISuspendingDeferral: ...
    def complete(self) -> None: ...

class ISuspendingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISuspendingEventArgs: ...
    @_property
    def suspending_operation(self) -> typing.Optional[SuspendingOperation]: ...

class ISuspendingOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISuspendingOperation: ...
    def get_deferral(self) -> typing.Optional[SuspendingDeferral]: ...
    @_property
    def deadline(self) -> datetime.datetime: ...
