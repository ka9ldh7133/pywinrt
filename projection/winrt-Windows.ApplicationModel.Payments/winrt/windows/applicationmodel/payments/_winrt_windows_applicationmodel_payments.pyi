# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections

from . import PaymentCanMakePaymentResultStatus, PaymentOptionPresence, PaymentRequestChangeKind, PaymentRequestCompletionStatus, PaymentRequestStatus, PaymentShippingType
from . import PaymentRequestChangedHandler

Self = typing.TypeVar('Self')

class PaymentAddress(winrt.system.Object):
    sorting_code: str
    region: str
    recipient: str
    postal_code: str
    phone_number: str
    organization: str
    language_code: str
    dependent_locality: str
    country: str
    city: str
    address_lines: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    properties: typing.Optional[winrt.windows.foundation.collections.ValueSet]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentAddress: ...
    def __new__(cls: typing.Type[PaymentAddress]) -> PaymentAddress:...

class PaymentCanMakePaymentResult(winrt.system.Object):
    status: PaymentCanMakePaymentResultStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentCanMakePaymentResult: ...
    def __new__(cls: typing.Type[PaymentCanMakePaymentResult], value: PaymentCanMakePaymentResultStatus) -> PaymentCanMakePaymentResult:...

class PaymentCurrencyAmount(winrt.system.Object):
    value: str
    currency_system: str
    currency: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentCurrencyAmount: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentCurrencyAmount], value: str, currency: str) -> PaymentCurrencyAmount:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentCurrencyAmount], value: str, currency: str, currency_system: str) -> PaymentCurrencyAmount:...

class PaymentDetails(winrt.system.Object):
    total: typing.Optional[PaymentItem]
    shipping_options: typing.Optional[winrt.windows.foundation.collections.IVectorView[PaymentShippingOption]]
    modifiers: typing.Optional[winrt.windows.foundation.collections.IVectorView[PaymentDetailsModifier]]
    display_items: typing.Optional[winrt.windows.foundation.collections.IVectorView[PaymentItem]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentDetails: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetails], total: typing.Optional[PaymentItem]) -> PaymentDetails:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetails], total: typing.Optional[PaymentItem], display_items: typing.Iterable[PaymentItem]) -> PaymentDetails:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetails]) -> PaymentDetails:...

class PaymentDetailsModifier(winrt.system.Object):
    additional_display_items: typing.Optional[winrt.windows.foundation.collections.IVectorView[PaymentItem]]
    json_data: str
    supported_method_ids: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    total: typing.Optional[PaymentItem]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentDetailsModifier: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetailsModifier], supported_method_ids: typing.Iterable[str], total: typing.Optional[PaymentItem]) -> PaymentDetailsModifier:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetailsModifier], supported_method_ids: typing.Iterable[str], total: typing.Optional[PaymentItem], additional_display_items: typing.Iterable[PaymentItem]) -> PaymentDetailsModifier:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetailsModifier], supported_method_ids: typing.Iterable[str], total: typing.Optional[PaymentItem], additional_display_items: typing.Iterable[PaymentItem], json_data: str) -> PaymentDetailsModifier:...

class PaymentItem(winrt.system.Object):
    pending: winrt.system.Boolean
    label: str
    amount: typing.Optional[PaymentCurrencyAmount]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentItem: ...
    def __new__(cls: typing.Type[PaymentItem], label: str, amount: typing.Optional[PaymentCurrencyAmount]) -> PaymentItem:...

class PaymentMediator(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentMediator: ...
    def __new__(cls: typing.Type[PaymentMediator]) -> PaymentMediator:...
    def can_make_payment_async(self, payment_request: typing.Optional[PaymentRequest], /) -> winrt.windows.foundation.IAsyncOperation[PaymentCanMakePaymentResult]: ...
    def get_supported_method_ids_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[str]]: ...
    @typing.overload
    def submit_payment_request_async(self, payment_request: typing.Optional[PaymentRequest], /) -> winrt.windows.foundation.IAsyncOperation[PaymentRequestSubmitResult]: ...
    @typing.overload
    def submit_payment_request_async(self, payment_request: typing.Optional[PaymentRequest], change_handler: typing.Optional[PaymentRequestChangedHandler], /) -> winrt.windows.foundation.IAsyncOperation[PaymentRequestSubmitResult]: ...

class PaymentMerchantInfo(winrt.system.Object):
    package_full_name: str
    uri: typing.Optional[winrt.windows.foundation.Uri]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentMerchantInfo: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMerchantInfo], uri: typing.Optional[winrt.windows.foundation.Uri]) -> PaymentMerchantInfo:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMerchantInfo]) -> PaymentMerchantInfo:...

class PaymentMethodData(winrt.system.Object):
    json_data: str
    supported_method_ids: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentMethodData: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMethodData], supported_method_ids: typing.Iterable[str]) -> PaymentMethodData:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMethodData], supported_method_ids: typing.Iterable[str], json_data: str) -> PaymentMethodData:...

class PaymentOptions(winrt.system.Object):
    shipping_type: PaymentShippingType
    request_shipping: winrt.system.Boolean
    request_payer_phone_number: PaymentOptionPresence
    request_payer_name: PaymentOptionPresence
    request_payer_email: PaymentOptionPresence
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentOptions: ...
    def __new__(cls: typing.Type[PaymentOptions]) -> PaymentOptions:...

class PaymentRequest(winrt.system.Object):
    details: typing.Optional[PaymentDetails]
    merchant_info: typing.Optional[PaymentMerchantInfo]
    method_data: typing.Optional[winrt.windows.foundation.collections.IVectorView[PaymentMethodData]]
    options: typing.Optional[PaymentOptions]
    id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequest: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData], merchant_info: typing.Optional[PaymentMerchantInfo], options: typing.Optional[PaymentOptions], id: str) -> PaymentRequest:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData]) -> PaymentRequest:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData], merchant_info: typing.Optional[PaymentMerchantInfo]) -> PaymentRequest:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData], merchant_info: typing.Optional[PaymentMerchantInfo], options: typing.Optional[PaymentOptions]) -> PaymentRequest:...

class PaymentRequestChangedArgs(winrt.system.Object):
    change_kind: PaymentRequestChangeKind
    selected_shipping_option: typing.Optional[PaymentShippingOption]
    shipping_address: typing.Optional[PaymentAddress]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequestChangedArgs: ...
    def acknowledge(self, change_result: typing.Optional[PaymentRequestChangedResult], /) -> None: ...

class PaymentRequestChangedResult(winrt.system.Object):
    updated_payment_details: typing.Optional[PaymentDetails]
    message: str
    change_accepted_by_merchant: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequestChangedResult: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequestChangedResult], change_accepted_by_merchant: winrt.system.Boolean) -> PaymentRequestChangedResult:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequestChangedResult], change_accepted_by_merchant: winrt.system.Boolean, updated_payment_details: typing.Optional[PaymentDetails]) -> PaymentRequestChangedResult:...

class PaymentRequestSubmitResult(winrt.system.Object):
    response: typing.Optional[PaymentResponse]
    status: PaymentRequestStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequestSubmitResult: ...

class PaymentResponse(winrt.system.Object):
    payer_email: str
    payer_name: str
    payer_phone_number: str
    payment_token: typing.Optional[PaymentToken]
    shipping_address: typing.Optional[PaymentAddress]
    shipping_option: typing.Optional[PaymentShippingOption]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentResponse: ...
    def complete_async(self, status: PaymentRequestCompletionStatus, /) -> winrt.windows.foundation.IAsyncAction: ...

class PaymentShippingOption(winrt.system.Object):
    tag: str
    label: str
    is_selected: winrt.system.Boolean
    amount: typing.Optional[PaymentCurrencyAmount]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentShippingOption: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentShippingOption], label: str, amount: typing.Optional[PaymentCurrencyAmount]) -> PaymentShippingOption:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentShippingOption], label: str, amount: typing.Optional[PaymentCurrencyAmount], selected: winrt.system.Boolean) -> PaymentShippingOption:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentShippingOption], label: str, amount: typing.Optional[PaymentCurrencyAmount], selected: winrt.system.Boolean, tag: str) -> PaymentShippingOption:...

class PaymentToken(winrt.system.Object):
    json_details: str
    payment_method_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentToken: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentToken], payment_method_id: str) -> PaymentToken:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentToken], payment_method_id: str, json_details: str) -> PaymentToken:...
