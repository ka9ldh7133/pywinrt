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
import winrt.windows.devices.printers
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.graphics.printing.printticket
import winrt.windows.storage
import winrt.windows.storage.streams
import winrt.windows.system

from winrt.windows.graphics.printing.workflow import PdlConversionHostBasedProcessingOperations, PrintWorkflowAttributesMergePolicy, PrintWorkflowJobAbortReason, PrintWorkflowPdlConversionType, PrintWorkflowPrinterJobStatus, PrintWorkflowSessionStatus, PrintWorkflowSubmittedStatus, PrintWorkflowUICompletionStatus

Self = typing.TypeVar('Self')

class PrintWorkflowBackgroundSession(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowBackgroundSession: ...
    def start(self) -> None: ...
    def add_setup_requested(self, setup_event_handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowBackgroundSession, PrintWorkflowBackgroundSetupRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_setup_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_submitted(self, submitted_event_handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowBackgroundSession, PrintWorkflowSubmittedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_submitted(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def status(self) -> PrintWorkflowSessionStatus: ...

class PrintWorkflowBackgroundSetupRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowBackgroundSetupRequestedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    def get_user_print_ticket_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...
    def set_requires_u_i(self) -> None: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...

class PrintWorkflowConfiguration(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowConfiguration: ...
    def abort_print_flow(self, reason: PrintWorkflowJobAbortReason, /) -> None: ...
    @_property
    def job_title(self) -> str: ...
    @_property
    def session_id(self) -> str: ...
    @_property
    def source_app_display_name(self) -> str: ...

class PrintWorkflowForegroundSession(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowForegroundSession: ...
    def start(self) -> None: ...
    def add_setup_requested(self, setup_event_handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowForegroundSession, PrintWorkflowForegroundSetupRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_setup_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_xps_data_available(self, xps_data_available_event_handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowForegroundSession, PrintWorkflowXpsDataAvailableEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_xps_data_available(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def status(self) -> PrintWorkflowSessionStatus: ...

class PrintWorkflowForegroundSetupRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowForegroundSetupRequestedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    def get_user_print_ticket_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...

class PrintWorkflowJobActivatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowJobActivatedEventArgs: ...
    @_property
    def kind(self) -> winrt.windows.applicationmodel.activation.ActivationKind: ...
    @_property
    def previous_execution_state(self) -> winrt.windows.applicationmodel.activation.ApplicationExecutionState: ...
    @_property
    def splash_screen(self) -> typing.Optional[winrt.windows.applicationmodel.activation.SplashScreen]: ...
    @_property
    def user(self) -> typing.Optional[winrt.windows.system.User]: ...
    @_property
    def session(self) -> typing.Optional[PrintWorkflowJobUISession]: ...

class PrintWorkflowJobBackgroundSession(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowJobBackgroundSession: ...
    def start(self) -> None: ...
    def add_job_starting(self, handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowJobBackgroundSession, PrintWorkflowJobStartingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_job_starting(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pdl_modification_requested(self, handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowJobBackgroundSession, PrintWorkflowPdlModificationRequestedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pdl_modification_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def status(self) -> PrintWorkflowSessionStatus: ...

class PrintWorkflowJobNotificationEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowJobNotificationEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...
    @_property
    def printer_job(self) -> typing.Optional[PrintWorkflowPrinterJob]: ...

class PrintWorkflowJobStartingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowJobStartingEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    def set_skip_system_rendering(self) -> None: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...
    @_property
    def printer(self) -> typing.Optional[winrt.windows.devices.printers.IppPrintDevice]: ...

class PrintWorkflowJobTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowJobTriggerDetails: ...
    @_property
    def print_workflow_job_session(self) -> typing.Optional[PrintWorkflowJobBackgroundSession]: ...

class PrintWorkflowJobUISession(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowJobUISession: ...
    def start(self) -> None: ...
    def add_job_notification(self, handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowJobUISession, PrintWorkflowJobNotificationEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_job_notification(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pdl_data_available(self, handler: winrt.windows.foundation.TypedEventHandler[PrintWorkflowJobUISession, PrintWorkflowPdlDataAvailableEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pdl_data_available(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def status(self) -> PrintWorkflowSessionStatus: ...

class PrintWorkflowObjectModelSourceFileContent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowObjectModelSourceFileContent: ...
    def __new__(cls: typing.Type[PrintWorkflowObjectModelSourceFileContent], xps_stream: typing.Optional[winrt.windows.storage.streams.IInputStream]) -> PrintWorkflowObjectModelSourceFileContent:...

class PrintWorkflowObjectModelTargetPackage(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowObjectModelTargetPackage: ...

class PrintWorkflowPdlConverter(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowPdlConverter: ...
    @typing.overload
    def convert_pdl_async(self, print_ticket: typing.Optional[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket], input_stream: typing.Optional[winrt.windows.storage.streams.IInputStream], output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream], /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def convert_pdl_async(self, print_ticket: typing.Optional[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket], input_stream: typing.Optional[winrt.windows.storage.streams.IInputStream], output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream], host_based_processing_operations: PdlConversionHostBasedProcessingOperations, /) -> winrt.windows.foundation.IAsyncAction: ...

class PrintWorkflowPdlDataAvailableEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowPdlDataAvailableEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...
    @_property
    def printer_job(self) -> typing.Optional[PrintWorkflowPrinterJob]: ...
    @_property
    def source_content(self) -> typing.Optional[PrintWorkflowPdlSourceContent]: ...

class PrintWorkflowPdlModificationRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowPdlModificationRequestedEventArgs: ...
    def create_job_on_printer(self, target_content_type: str, /) -> typing.Optional[PrintWorkflowPdlTargetStream]: ...
    @typing.overload
    def create_job_on_printer_with_attributes(self, job_attributes: typing.Iterable[winrt.windows.foundation.collections.IKeyValuePair[str, winrt.windows.devices.printers.IppAttributeValue]], target_content_type: str, /) -> typing.Optional[PrintWorkflowPdlTargetStream]: ...
    @typing.overload
    def create_job_on_printer_with_attributes(self, job_attributes: typing.Iterable[winrt.windows.foundation.collections.IKeyValuePair[str, winrt.windows.devices.printers.IppAttributeValue]], target_content_type: str, operation_attributes: typing.Iterable[winrt.windows.foundation.collections.IKeyValuePair[str, winrt.windows.devices.printers.IppAttributeValue]], job_attributes_merge_policy: PrintWorkflowAttributesMergePolicy, operation_attributes_merge_policy: PrintWorkflowAttributesMergePolicy, /) -> typing.Optional[PrintWorkflowPdlTargetStream]: ...
    @typing.overload
    def create_job_on_printer_with_attributes_buffer(self, job_attributes_buffer: typing.Optional[winrt.windows.storage.streams.IBuffer], target_content_type: str, /) -> typing.Optional[PrintWorkflowPdlTargetStream]: ...
    @typing.overload
    def create_job_on_printer_with_attributes_buffer(self, job_attributes_buffer: typing.Optional[winrt.windows.storage.streams.IBuffer], target_content_type: str, operation_attributes_buffer: typing.Optional[winrt.windows.storage.streams.IBuffer], job_attributes_merge_policy: PrintWorkflowAttributesMergePolicy, operation_attributes_merge_policy: PrintWorkflowAttributesMergePolicy, /) -> typing.Optional[PrintWorkflowPdlTargetStream]: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    def get_pdl_converter(self, conversion_type: PrintWorkflowPdlConversionType, /) -> typing.Optional[PrintWorkflowPdlConverter]: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...
    @_property
    def printer_job(self) -> typing.Optional[PrintWorkflowPrinterJob]: ...
    @_property
    def source_content(self) -> typing.Optional[PrintWorkflowPdlSourceContent]: ...
    @_property
    def u_i_launcher(self) -> typing.Optional[PrintWorkflowUILauncher]: ...

class PrintWorkflowPdlSourceContent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowPdlSourceContent: ...
    def get_content_file_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.storage.StorageFile]: ...
    def get_input_stream(self) -> typing.Optional[winrt.windows.storage.streams.IInputStream]: ...
    @_property
    def content_type(self) -> str: ...

class PrintWorkflowPdlTargetStream(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowPdlTargetStream: ...
    def complete_stream_submission(self, status: PrintWorkflowSubmittedStatus, /) -> None: ...
    def get_output_stream(self) -> typing.Optional[winrt.windows.storage.streams.IOutputStream]: ...

class PrintWorkflowPrinterJob(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowPrinterJob: ...
    def get_job_attributes(self, attribute_names: typing.Iterable[str], /) -> typing.Optional[winrt.windows.foundation.collections.IMap[str, winrt.windows.devices.printers.IppAttributeValue]]: ...
    def get_job_attributes_as_buffer(self, attribute_names: typing.Iterable[str], /) -> typing.Optional[winrt.windows.storage.streams.IBuffer]: ...
    def get_job_print_ticket(self) -> typing.Optional[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...
    def get_job_status(self) -> PrintWorkflowPrinterJobStatus: ...
    def set_job_attributes(self, job_attributes: typing.Iterable[winrt.windows.foundation.collections.IKeyValuePair[str, winrt.windows.devices.printers.IppAttributeValue]], /) -> typing.Optional[winrt.windows.devices.printers.IppSetAttributesResult]: ...
    def set_job_attributes_from_buffer(self, job_attributes_buffer: typing.Optional[winrt.windows.storage.streams.IBuffer], /) -> typing.Optional[winrt.windows.devices.printers.IppSetAttributesResult]: ...
    @_property
    def job_id(self) -> winrt.system.Int32: ...
    @_property
    def printer(self) -> typing.Optional[winrt.windows.devices.printers.IppPrintDevice]: ...

class PrintWorkflowSourceContent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowSourceContent: ...
    def get_job_print_ticket_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket]: ...
    def get_source_spool_data_as_stream_content(self) -> typing.Optional[PrintWorkflowSpoolStreamContent]: ...
    def get_source_spool_data_as_xps_object_model(self) -> typing.Optional[PrintWorkflowObjectModelSourceFileContent]: ...

class PrintWorkflowSpoolStreamContent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowSpoolStreamContent: ...
    def get_input_stream(self) -> typing.Optional[winrt.windows.storage.streams.IInputStream]: ...

class PrintWorkflowStreamTarget(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowStreamTarget: ...
    def get_output_stream(self) -> typing.Optional[winrt.windows.storage.streams.IOutputStream]: ...

class PrintWorkflowSubmittedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowSubmittedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    def get_target(self, job_print_ticket: typing.Optional[winrt.windows.graphics.printing.printticket.WorkflowPrintTicket], /) -> typing.Optional[PrintWorkflowTarget]: ...
    @_property
    def operation(self) -> typing.Optional[PrintWorkflowSubmittedOperation]: ...

class PrintWorkflowSubmittedOperation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowSubmittedOperation: ...
    def complete(self, status: PrintWorkflowSubmittedStatus, /) -> None: ...
    @_property
    def configuration(self) -> typing.Optional[PrintWorkflowConfiguration]: ...
    @_property
    def xps_content(self) -> typing.Optional[PrintWorkflowSourceContent]: ...

class PrintWorkflowTarget(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowTarget: ...
    @_property
    def target_as_stream(self) -> typing.Optional[PrintWorkflowStreamTarget]: ...
    @_property
    def target_as_xps_object_model_package(self) -> typing.Optional[PrintWorkflowObjectModelTargetPackage]: ...

class PrintWorkflowTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowTriggerDetails: ...
    @_property
    def print_workflow_session(self) -> typing.Optional[PrintWorkflowBackgroundSession]: ...

class PrintWorkflowUIActivatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowUIActivatedEventArgs: ...
    @_property
    def kind(self) -> winrt.windows.applicationmodel.activation.ActivationKind: ...
    @_property
    def previous_execution_state(self) -> winrt.windows.applicationmodel.activation.ApplicationExecutionState: ...
    @_property
    def splash_screen(self) -> typing.Optional[winrt.windows.applicationmodel.activation.SplashScreen]: ...
    @_property
    def user(self) -> typing.Optional[winrt.windows.system.User]: ...
    @_property
    def print_workflow_session(self) -> typing.Optional[PrintWorkflowForegroundSession]: ...

class PrintWorkflowUILauncher(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowUILauncher: ...
    def is_u_i_launch_enabled(self) -> bool: ...
    def launch_and_complete_u_i_async(self) -> winrt.windows.foundation.IAsyncOperation[PrintWorkflowUICompletionStatus]: ...

class PrintWorkflowXpsDataAvailableEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintWorkflowXpsDataAvailableEventArgs: ...
    def get_deferral(self) -> typing.Optional[winrt.windows.foundation.Deferral]: ...
    @_property
    def operation(self) -> typing.Optional[PrintWorkflowSubmittedOperation]: ...
