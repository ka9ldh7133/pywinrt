# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.data.xml.dom
import winrt.windows.foundation
import winrt.windows.foundation.collections

from winrt.windows.graphics.printing.printticket import PrintTicketFeatureSelectionType, PrintTicketParameterDataType, PrintTicketValueType

Self = typing.TypeVar('Self')

class PrintTicketCapabilities(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintTicketCapabilities: ...
    def get_feature(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketFeature]: ...
    def get_parameter_definition(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketParameterDefinition]: ...
    @_property
    def document_binding_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_collate_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_duplex_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_hole_punch_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_input_bin_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_n_up_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_staple_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def job_passcode_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def name(self) -> str: ...
    @_property
    def page_borderless_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_media_size_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_media_type_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_orientation_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_output_color_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_output_quality_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_resolution_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def xml_namespace(self) -> str: ...
    @_property
    def xml_node(self) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...

class PrintTicketFeature(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintTicketFeature: ...
    def get_option(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketOption]: ...
    def get_selected_option(self) -> typing.Optional[PrintTicketOption]: ...
    def set_selected_option(self, value: typing.Optional[PrintTicketOption], /) -> None: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def name(self) -> str: ...
    @_property
    def options(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[PrintTicketOption]]: ...
    @_property
    def selection_type(self) -> PrintTicketFeatureSelectionType: ...
    @_property
    def xml_namespace(self) -> str: ...
    @_property
    def xml_node(self) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...

class PrintTicketOption(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintTicketOption: ...
    def get_property_node(self, name: str, xml_namespace: str, /) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...
    def get_property_value(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketValue]: ...
    def get_scored_property_node(self, name: str, xml_namespace: str, /) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...
    def get_scored_property_value(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketValue]: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def name(self) -> str: ...
    @_property
    def xml_namespace(self) -> str: ...
    @_property
    def xml_node(self) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...

class PrintTicketParameterDefinition(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintTicketParameterDefinition: ...
    @_property
    def data_type(self) -> PrintTicketParameterDataType: ...
    @_property
    def name(self) -> str: ...
    @_property
    def range_max(self) -> winrt.system.Int32: ...
    @_property
    def range_min(self) -> winrt.system.Int32: ...
    @_property
    def unit_type(self) -> str: ...
    @_property
    def xml_namespace(self) -> str: ...
    @_property
    def xml_node(self) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...

class PrintTicketParameterInitializer(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintTicketParameterInitializer: ...
    @_property
    def value(self) -> typing.Optional[PrintTicketValue]: ...
    @value.setter
    def value(self, value: typing.Optional[PrintTicketValue]) -> None: ...
    @_property
    def name(self) -> str: ...
    @_property
    def xml_namespace(self) -> str: ...
    @_property
    def xml_node(self) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...

class PrintTicketValue(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintTicketValue: ...
    def get_value_as_integer(self) -> winrt.system.Int32: ...
    def get_value_as_string(self) -> str: ...
    @_property
    def type(self) -> PrintTicketValueType: ...

class WorkflowPrintTicket(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WorkflowPrintTicket: ...
    def get_capabilities(self) -> typing.Optional[PrintTicketCapabilities]: ...
    def get_feature(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketFeature]: ...
    def get_parameter_initializer(self, name: str, xml_namespace: str, /) -> typing.Optional[PrintTicketParameterInitializer]: ...
    def merge_and_validate_ticket(self, delta_shema_ticket: typing.Optional[WorkflowPrintTicket], /) -> typing.Optional[WorkflowPrintTicket]: ...
    def notify_xml_changed_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def set_parameter_initializer_as_integer(self, name: str, xml_namespace: str, integer_value: winrt.system.Int32, /) -> typing.Optional[PrintTicketParameterInitializer]: ...
    def set_parameter_initializer_as_string(self, name: str, xml_namespace: str, string_value: str, /) -> typing.Optional[PrintTicketParameterInitializer]: ...
    def validate_async(self) -> winrt.windows.foundation.IAsyncOperation[WorkflowPrintTicketValidationResult]: ...
    @_property
    def document_binding_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_collate_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_duplex_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_hole_punch_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_input_bin_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_n_up_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def document_staple_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def job_passcode_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def name(self) -> str: ...
    @_property
    def page_borderless_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_media_size_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_media_type_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_orientation_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_output_color_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_output_quality_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def page_resolution_feature(self) -> typing.Optional[PrintTicketFeature]: ...
    @_property
    def xml_namespace(self) -> str: ...
    @_property
    def xml_node(self) -> typing.Optional[winrt.windows.data.xml.dom.IXmlNode]: ...

class WorkflowPrintTicketValidationResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WorkflowPrintTicketValidationResult: ...
    @_property
    def extended_error(self) -> winrt.windows.foundation.HResult: ...
    @_property
    def validated(self) -> bool: ...
