# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.security.authentication.web.core
import winrt.windows.security.credentials
import winrt.windows.storage.streams
import winrt.windows.system
import winrt.windows.ui.xaml

from . import DeliveryOptimizationDownloadMode, DeliveryOptimizationDownloadModeSource, StoreLogOptions, StorePreviewProductPurchaseStatus, StoreSystemFeature

Self = typing.TypeVar('Self')

class DeliveryOptimizationSettings(winrt.system.Object):
    download_mode: DeliveryOptimizationDownloadMode
    download_mode_source: DeliveryOptimizationDownloadModeSource
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeliveryOptimizationSettings: ...
    @staticmethod
    def get_current_settings() -> typing.Optional[DeliveryOptimizationSettings]: ...

class StoreConfiguration(winrt.system.Object):
    hardware_manufacturer_info: typing.ClassVar[typing.Optional[StoreHardwareManufacturerInfo]]
    purchase_prompting_policy: typing.ClassVar[typing.Optional[typing.Optional[winrt.system.UInt32]]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreConfiguration: ...
    @staticmethod
    def filter_unsupported_system_features_async(system_features: typing.Iterable[StoreSystemFeature], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[StoreSystemFeature]]: ...
    @staticmethod
    def get_enterprise_store_web_account_id() -> str: ...
    @staticmethod
    def get_enterprise_store_web_account_id_for_user(user: typing.Optional[winrt.windows.system.User], /) -> str: ...
    @staticmethod
    def get_purchase_prompting_policy_for_user(user: typing.Optional[winrt.windows.system.User], /) -> typing.Optional[typing.Optional[winrt.system.UInt32]]: ...
    @staticmethod
    def get_store_log_data_async(options: StoreLogOptions, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.storage.streams.IRandomAccessStreamReference]: ...
    @staticmethod
    def get_store_web_account_id() -> str: ...
    @staticmethod
    def get_store_web_account_id_for_user(user: typing.Optional[winrt.windows.system.User], /) -> str: ...
    @staticmethod
    def has_store_web_account() -> winrt.system.Boolean: ...
    @staticmethod
    def has_store_web_account_for_user(user: typing.Optional[winrt.windows.system.User], /) -> winrt.system.Boolean: ...
    @staticmethod
    def is_pin_to_desktop_supported() -> winrt.system.Boolean: ...
    @staticmethod
    def is_pin_to_start_supported() -> winrt.system.Boolean: ...
    @staticmethod
    def is_pin_to_taskbar_supported() -> winrt.system.Boolean: ...
    @staticmethod
    def is_store_web_account_id(web_account_id: str, /) -> winrt.system.Boolean: ...
    @staticmethod
    def is_store_web_account_id_for_user(user: typing.Optional[winrt.windows.system.User], web_account_id: str, /) -> winrt.system.Boolean: ...
    @staticmethod
    def pin_to_desktop(app_package_family_name: str, /) -> None: ...
    @staticmethod
    def pin_to_desktop_for_user(user: typing.Optional[winrt.windows.system.User], app_package_family_name: str, /) -> None: ...
    @staticmethod
    def set_enterprise_store_web_account_id(web_account_id: str, /) -> None: ...
    @staticmethod
    def set_enterprise_store_web_account_id_for_user(user: typing.Optional[winrt.windows.system.User], web_account_id: str, /) -> None: ...
    @staticmethod
    def set_mobile_operator_configuration(mobile_operator_id: str, app_download_limit_in_megabytes: winrt.system.UInt32, update_download_limit_in_megabytes: winrt.system.UInt32, /) -> None: ...
    @staticmethod
    def set_purchase_prompting_policy_for_user(user: typing.Optional[winrt.windows.system.User], value: typing.Optional[winrt.system.UInt32], /) -> None: ...
    @staticmethod
    def set_store_web_account_id(web_account_id: str, /) -> None: ...
    @staticmethod
    def set_store_web_account_id_for_user(user: typing.Optional[winrt.windows.system.User], web_account_id: str, /) -> None: ...
    @staticmethod
    def set_system_configuration(catalog_hardware_manufacturer_id: str, catalog_store_content_modifier_id: str, system_configuration_expiration: datetime.datetime, catalog_hardware_descriptor: str, /) -> None: ...
    @staticmethod
    def should_restrict_to_enterprise_store_only() -> winrt.system.Boolean: ...
    @staticmethod
    def should_restrict_to_enterprise_store_only_for_user(user: typing.Optional[winrt.windows.system.User], /) -> winrt.system.Boolean: ...

class StoreHardwareManufacturerInfo(winrt.system.Object):
    hardware_manufacturer_id: str
    manufacturer_name: str
    model_name: str
    store_content_modifier_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StoreHardwareManufacturerInfo: ...

class StorePreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePreview: ...
    @staticmethod
    def load_add_on_product_infos_async() -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[StorePreviewProductInfo]]: ...
    @staticmethod
    def request_product_purchase_by_product_id_and_sku_id_async(product_id: str, sku_id: str, /) -> winrt.windows.foundation.IAsyncOperation[StorePreviewPurchaseResults]: ...

class StorePreviewProductInfo(winrt.system.Object):
    description: str
    product_id: str
    product_type: str
    sku_info_list: typing.Optional[winrt.windows.foundation.collections.IVectorView[StorePreviewSkuInfo]]
    title: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePreviewProductInfo: ...

class StorePreviewPurchaseResults(winrt.system.Object):
    product_purchase_status: StorePreviewProductPurchaseStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePreviewPurchaseResults: ...

class StorePreviewSkuInfo(winrt.system.Object):
    currency_code: str
    custom_developer_data: str
    description: str
    extended_data: str
    formatted_list_price: str
    product_id: str
    sku_id: str
    sku_type: str
    title: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StorePreviewSkuInfo: ...

class WebAuthenticationCoreManagerHelper(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WebAuthenticationCoreManagerHelper: ...
    @typing.overload
    @staticmethod
    def request_token_with_u_i_element_hosting_async(request: typing.Optional[winrt.windows.security.authentication.web.core.WebTokenRequest], ui_element: typing.Optional[winrt.windows.ui.xaml.UIElement], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.authentication.web.core.WebTokenRequestResult]: ...
    @typing.overload
    @staticmethod
    def request_token_with_u_i_element_hosting_async(request: typing.Optional[winrt.windows.security.authentication.web.core.WebTokenRequest], web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], ui_element: typing.Optional[winrt.windows.ui.xaml.UIElement], /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.security.authentication.web.core.WebTokenRequestResult]: ...
