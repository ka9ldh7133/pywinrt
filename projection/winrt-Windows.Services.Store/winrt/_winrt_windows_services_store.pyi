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
import winrt.windows.system as windows_system
import winrt.windows.web.http as windows_web_http

from winrt.windows.services.store import StoreCanLicenseStatus, StoreConsumableStatus, StoreDurationUnit, StorePackageUpdateState, StorePurchaseStatus, StoreQueueItemExtendedState, StoreQueueItemKind, StoreQueueItemState, StoreRateAndReviewStatus, StoreUninstallStorePackageStatus

Self = typing.TypeVar('Self')

@typing.final
class StorePackageUpdateStatus:
    package_family_name: str
    package_download_size_in_bytes: winrt.system.UInt64
    package_bytes_downloaded: winrt.system.UInt64
    package_download_progress: winrt.system.Double
    total_download_progress: winrt.system.Double
    package_update_state: StorePackageUpdateState
    def __init__(self, package_family_name: str = "", package_download_size_in_bytes: winrt.system.UInt64 = 0, package_bytes_downloaded: winrt.system.UInt64 = 0, package_download_progress: winrt.system.Double = 0, total_download_progress: winrt.system.Double = 0, package_update_state: StorePackageUpdateState = StorePackageUpdateState(0)) -> None: ...

@typing.final
class StoreAcquireLicenseResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreAcquireLicenseResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def store_package_license(self) -> StorePackageLicense: ...

@typing.final
class StoreAppLicense(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreAppLicense: ...
    @_property
    def add_on_licenses(self) -> typing.Mapping[str, StoreLicense]: ...
    @_property
    def expiration_date(self) -> datetime.datetime: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def is_active(self) -> bool: ...
    @_property
    def is_trial(self) -> bool: ...
    @_property
    def is_trial_owned_by_this_user(self) -> bool: ...
    @_property
    def sku_store_id(self) -> str: ...
    @_property
    def trial_time_remaining(self) -> datetime.timedelta: ...
    @_property
    def trial_unique_id(self) -> str: ...
    @_property
    def is_disc_license(self) -> bool: ...

@typing.final
class StoreAvailability(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreAvailability: ...
    def request_purchase_async(self) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    def request_purchase_with_purchase_properties_async(self, store_purchase_properties: StorePurchaseProperties, /) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    @_property
    def end_date(self) -> datetime.datetime: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def price(self) -> StorePrice: ...
    @_property
    def store_id(self) -> str: ...

@typing.final
class StoreCanAcquireLicenseResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreCanAcquireLicenseResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def licensable_sku(self) -> str: ...
    @_property
    def status(self) -> StoreCanLicenseStatus: ...

@typing.final
class StoreCollectionData(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreCollectionData: ...
    @_property
    def acquired_date(self) -> datetime.datetime: ...
    @_property
    def campaign_id(self) -> str: ...
    @_property
    def developer_offer_id(self) -> str: ...
    @_property
    def end_date(self) -> datetime.datetime: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def is_trial(self) -> bool: ...
    @_property
    def start_date(self) -> datetime.datetime: ...
    @_property
    def trial_time_remaining(self) -> datetime.timedelta: ...

@typing.final
class StoreConsumableResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreConsumableResult: ...
    @_property
    def balance_remaining(self) -> winrt.system.UInt32: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def status(self) -> StoreConsumableStatus: ...
    @_property
    def tracking_id(self) -> _uuid.UUID: ...

@typing.final
class StoreContext_Static(type):
    def get_default(cls) -> StoreContext: ...
    def get_for_user(cls, user: windows_system.User, /) -> StoreContext: ...

@typing.final
class StoreContext(winrt.system.Object, metaclass=StoreContext_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreContext: ...
    def acquire_store_license_for_optional_package_async(self, optional_package: windows_applicationmodel.Package, /) -> windows_foundation.IAsyncOperation[StoreAcquireLicenseResult]: ...
    def can_acquire_store_license_async(self, product_store_id: str, /) -> windows_foundation.IAsyncOperation[StoreCanAcquireLicenseResult]: ...
    def can_acquire_store_license_for_optional_package_async(self, optional_package: windows_applicationmodel.Package, /) -> windows_foundation.IAsyncOperation[StoreCanAcquireLicenseResult]: ...
    def download_and_install_store_packages_async(self, store_ids: typing.Iterable[str], /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def find_store_product_for_package_async(self, product_kinds: typing.Iterable[str], package: windows_applicationmodel.Package, /) -> windows_foundation.IAsyncOperation[StoreProductResult]: ...
    def get_app_and_optional_store_package_updates_async(self) -> windows_foundation.IAsyncOperation[typing.Sequence[StorePackageUpdate]]: ...
    def get_app_license_async(self) -> windows_foundation.IAsyncOperation[StoreAppLicense]: ...
    def get_associated_store_products_async(self, product_kinds: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[StoreProductQueryResult]: ...
    def get_associated_store_products_by_in_app_offer_token_async(self, in_app_offer_tokens: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[StoreProductQueryResult]: ...
    def get_associated_store_products_with_paging_async(self, product_kinds: typing.Iterable[str], max_items_to_retrieve_per_page: winrt.system.UInt32, /) -> windows_foundation.IAsyncOperation[StoreProductPagedQueryResult]: ...
    def get_associated_store_queue_items_async(self) -> windows_foundation.IAsyncOperation[typing.Sequence[StoreQueueItem]]: ...
    def get_consumable_balance_remaining_async(self, product_store_id: str, /) -> windows_foundation.IAsyncOperation[StoreConsumableResult]: ...
    def get_customer_collections_id_async(self, service_ticket: str, publisher_user_id: str, /) -> windows_foundation.IAsyncOperation[str]: ...
    def get_customer_purchase_id_async(self, service_ticket: str, publisher_user_id: str, /) -> windows_foundation.IAsyncOperation[str]: ...
    def get_store_product_for_current_app_async(self) -> windows_foundation.IAsyncOperation[StoreProductResult]: ...
    def get_store_products_async(self, product_kinds: typing.Iterable[str], store_ids: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[StoreProductQueryResult]: ...
    def get_store_products_with_options_async(self, product_kinds: typing.Iterable[str], store_ids: typing.Iterable[str], store_product_options: StoreProductOptions, /) -> windows_foundation.IAsyncOperation[StoreProductQueryResult]: ...
    def get_store_queue_items_async(self, store_ids: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[typing.Sequence[StoreQueueItem]]: ...
    def get_user_collection_async(self, product_kinds: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[StoreProductQueryResult]: ...
    def get_user_collection_with_paging_async(self, product_kinds: typing.Iterable[str], max_items_to_retrieve_per_page: winrt.system.UInt32, /) -> windows_foundation.IAsyncOperation[StoreProductPagedQueryResult]: ...
    def get_user_purchase_history_async(self, product_kinds: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[StoreProductQueryResult]: ...
    def report_consumable_fulfillment_async(self, product_store_id: str, quantity: winrt.system.UInt32, tracking_id: _uuid.UUID, /) -> windows_foundation.IAsyncOperation[StoreConsumableResult]: ...
    def request_download_and_install_store_package_updates_async(self, store_package_updates: typing.Iterable[StorePackageUpdate], /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def request_download_and_install_store_packages_async(self, store_ids: typing.Iterable[str], /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def request_download_and_install_store_packages_with_install_options_async(self, store_ids: typing.Iterable[str], store_package_install_options: StorePackageInstallOptions, /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def request_download_store_package_updates_async(self, store_package_updates: typing.Iterable[StorePackageUpdate], /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def request_purchase_async(self, store_id: str, /) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    def request_purchase_by_in_app_offer_token_async(self, in_app_offer_token: str, /) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    def request_purchase_with_purchase_properties_async(self, store_id: str, store_purchase_properties: StorePurchaseProperties, /) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    def request_rate_and_review_app_async(self) -> windows_foundation.IAsyncOperation[StoreRateAndReviewResult]: ...
    def request_uninstall_store_package_async(self, package: windows_applicationmodel.Package, /) -> windows_foundation.IAsyncOperation[StoreUninstallStorePackageResult]: ...
    def request_uninstall_store_package_by_store_id_async(self, store_id: str, /) -> windows_foundation.IAsyncOperation[StoreUninstallStorePackageResult]: ...
    def set_install_order_for_associated_store_queue_items_async(self, items: typing.Iterable[StoreQueueItem], /) -> windows_foundation.IAsyncOperation[typing.Sequence[StoreQueueItem]]: ...
    def try_silent_download_and_install_store_package_updates_async(self, store_package_updates: typing.Iterable[StorePackageUpdate], /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def try_silent_download_store_package_updates_async(self, store_package_updates: typing.Iterable[StorePackageUpdate], /) -> windows_foundation.IAsyncOperationWithProgress[StorePackageUpdateResult, StorePackageUpdateStatus]: ...
    def uninstall_store_package_async(self, package: windows_applicationmodel.Package, /) -> windows_foundation.IAsyncOperation[StoreUninstallStorePackageResult]: ...
    def uninstall_store_package_by_store_id_async(self, store_id: str, /) -> windows_foundation.IAsyncOperation[StoreUninstallStorePackageResult]: ...
    def add_offline_licenses_changed(self, handler: windows_foundation.TypedEventHandler[StoreContext, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_offline_licenses_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def user(self) -> windows_system.User: ...
    @_property
    def can_silently_download_store_package_updates(self) -> bool: ...

@typing.final
class StoreImage(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreImage: ...
    @_property
    def caption(self) -> str: ...
    @_property
    def height(self) -> winrt.system.UInt32: ...
    @_property
    def image_purpose_tag(self) -> str: ...
    @_property
    def uri(self) -> windows_foundation.Uri: ...
    @_property
    def width(self) -> winrt.system.UInt32: ...

@typing.final
class StoreLicense(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreLicense: ...
    @_property
    def expiration_date(self) -> datetime.datetime: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def in_app_offer_token(self) -> str: ...
    @_property
    def is_active(self) -> bool: ...
    @_property
    def sku_store_id(self) -> str: ...

@typing.final
class StorePackageInstallOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePackageInstallOptions: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def allow_forced_app_restart(self) -> bool: ...
    @allow_forced_app_restart.setter
    def allow_forced_app_restart(self, value: bool) -> None: ...

@typing.final
class StorePackageLicense(winrt.system.Object, windows_foundation.ImplementsIClosable):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePackageLicense: ...
    def close(self) -> None: ...
    def release_license(self) -> None: ...
    def add_license_lost(self, handler: windows_foundation.TypedEventHandler[StorePackageLicense, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_license_lost(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def is_valid(self) -> bool: ...
    @_property
    def package(self) -> windows_applicationmodel.Package: ...

@typing.final
class StorePackageUpdate(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePackageUpdate: ...
    @_property
    def mandatory(self) -> bool: ...
    @_property
    def package(self) -> windows_applicationmodel.Package: ...

@typing.final
class StorePackageUpdateResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePackageUpdateResult: ...
    @_property
    def overall_state(self) -> StorePackageUpdateState: ...
    @_property
    def store_package_update_statuses(self) -> typing.Sequence[StorePackageUpdateStatus]: ...
    @_property
    def store_queue_items(self) -> typing.Sequence[StoreQueueItem]: ...

@typing.final
class StorePrice(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePrice: ...
    @_property
    def currency_code(self) -> str: ...
    @_property
    def formatted_base_price(self) -> str: ...
    @_property
    def formatted_price(self) -> str: ...
    @_property
    def formatted_recurrence_price(self) -> str: ...
    @_property
    def is_on_sale(self) -> bool: ...
    @_property
    def sale_end_date(self) -> datetime.datetime: ...
    @_property
    def unformatted_base_price(self) -> str: ...
    @_property
    def unformatted_price(self) -> str: ...
    @_property
    def unformatted_recurrence_price(self) -> str: ...

@typing.final
class StoreProduct(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreProduct: ...
    def get_is_any_sku_installed_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def request_purchase_async(self) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    def request_purchase_with_purchase_properties_async(self, store_purchase_properties: StorePurchaseProperties, /) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    @_property
    def description(self) -> str: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def has_digital_download(self) -> bool: ...
    @_property
    def images(self) -> typing.Sequence[StoreImage]: ...
    @_property
    def in_app_offer_token(self) -> str: ...
    @_property
    def is_in_user_collection(self) -> bool: ...
    @_property
    def keywords(self) -> typing.Sequence[str]: ...
    @_property
    def language(self) -> str: ...
    @_property
    def link_uri(self) -> windows_foundation.Uri: ...
    @_property
    def price(self) -> StorePrice: ...
    @_property
    def product_kind(self) -> str: ...
    @_property
    def skus(self) -> typing.Sequence[StoreSku]: ...
    @_property
    def store_id(self) -> str: ...
    @_property
    def title(self) -> str: ...
    @_property
    def videos(self) -> typing.Sequence[StoreVideo]: ...

@typing.final
class StoreProductOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreProductOptions: ...
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def action_filters(self) -> typing.MutableSequence[str]: ...

@typing.final
class StoreProductPagedQueryResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreProductPagedQueryResult: ...
    def get_next_async(self) -> windows_foundation.IAsyncOperation[StoreProductPagedQueryResult]: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def has_more_results(self) -> bool: ...
    @_property
    def products(self) -> typing.Mapping[str, StoreProduct]: ...

@typing.final
class StoreProductQueryResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreProductQueryResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def products(self) -> typing.Mapping[str, StoreProduct]: ...

@typing.final
class StoreProductResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreProductResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def product(self) -> StoreProduct: ...

@typing.final
class StorePurchaseProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePurchaseProperties: ...
    @typing.overload
    def __new__(cls: typing.Type[Self], name: str) -> Self: ...
    @typing.overload
    def __new__(cls: typing.Type[Self]) -> Self: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @_property
    def extended_json_data(self) -> str: ...
    @extended_json_data.setter
    def extended_json_data(self, value: str) -> None: ...

@typing.final
class StorePurchaseResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePurchaseResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def status(self) -> StorePurchaseStatus: ...

@typing.final
class StoreQueueItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreQueueItem: ...
    def cancel_install_async(self) -> windows_foundation.IAsyncAction: ...
    def get_current_status(self) -> StoreQueueItemStatus: ...
    def pause_install_async(self) -> windows_foundation.IAsyncAction: ...
    def resume_install_async(self) -> windows_foundation.IAsyncAction: ...
    def add_completed(self, handler: windows_foundation.TypedEventHandler[StoreQueueItem, StoreQueueItemCompletedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_completed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_status_changed(self, handler: windows_foundation.TypedEventHandler[StoreQueueItem, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_status_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def install_kind(self) -> StoreQueueItemKind: ...
    @_property
    def package_family_name(self) -> str: ...
    @_property
    def product_id(self) -> str: ...

@typing.final
class StoreQueueItemCompletedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreQueueItemCompletedEventArgs: ...
    @_property
    def status(self) -> StoreQueueItemStatus: ...

@typing.final
class StoreQueueItemStatus(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreQueueItemStatus: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def package_install_extended_state(self) -> StoreQueueItemExtendedState: ...
    @_property
    def package_install_state(self) -> StoreQueueItemState: ...
    @_property
    def update_status(self) -> StorePackageUpdateStatus: ...

@typing.final
class StoreRateAndReviewResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreRateAndReviewResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def status(self) -> StoreRateAndReviewStatus: ...
    @_property
    def was_updated(self) -> bool: ...

@typing.final
class StoreRequestHelper_Static(type):
    def send_request_async(cls, context: StoreContext, request_kind: winrt.system.UInt32, parameters_as_json: str, /) -> windows_foundation.IAsyncOperation[StoreSendRequestResult]: ...

@typing.final
class StoreRequestHelper(winrt.system.Object, metaclass=StoreRequestHelper_Static):
    pass

@typing.final
class StoreSendRequestResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreSendRequestResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def response(self) -> str: ...
    @_property
    def http_status_code(self) -> windows_web_http.HttpStatusCode: ...

@typing.final
class StoreSku(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreSku: ...
    def get_is_installed_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def request_purchase_async(self) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    def request_purchase_with_purchase_properties_async(self, store_purchase_properties: StorePurchaseProperties, /) -> windows_foundation.IAsyncOperation[StorePurchaseResult]: ...
    @_property
    def availabilities(self) -> typing.Sequence[StoreAvailability]: ...
    @_property
    def bundled_skus(self) -> typing.Sequence[str]: ...
    @_property
    def collection_data(self) -> StoreCollectionData: ...
    @_property
    def custom_developer_data(self) -> str: ...
    @_property
    def description(self) -> str: ...
    @_property
    def extended_json_data(self) -> str: ...
    @_property
    def images(self) -> typing.Sequence[StoreImage]: ...
    @_property
    def is_in_user_collection(self) -> bool: ...
    @_property
    def is_subscription(self) -> bool: ...
    @_property
    def is_trial(self) -> bool: ...
    @_property
    def language(self) -> str: ...
    @_property
    def price(self) -> StorePrice: ...
    @_property
    def store_id(self) -> str: ...
    @_property
    def subscription_info(self) -> StoreSubscriptionInfo: ...
    @_property
    def title(self) -> str: ...
    @_property
    def videos(self) -> typing.Sequence[StoreVideo]: ...

@typing.final
class StoreSubscriptionInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreSubscriptionInfo: ...
    @_property
    def billing_period(self) -> winrt.system.UInt32: ...
    @_property
    def billing_period_unit(self) -> StoreDurationUnit: ...
    @_property
    def has_trial_period(self) -> bool: ...
    @_property
    def trial_period(self) -> winrt.system.UInt32: ...
    @_property
    def trial_period_unit(self) -> StoreDurationUnit: ...

@typing.final
class StoreUninstallStorePackageResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreUninstallStorePackageResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def status(self) -> StoreUninstallStorePackageStatus: ...

@typing.final
class StoreVideo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreVideo: ...
    @_property
    def caption(self) -> str: ...
    @_property
    def height(self) -> winrt.system.UInt32: ...
    @_property
    def preview_image(self) -> StoreImage: ...
    @_property
    def uri(self) -> windows_foundation.Uri: ...
    @_property
    def video_purpose_tag(self) -> str: ...
    @_property
    def width(self) -> winrt.system.UInt32: ...

