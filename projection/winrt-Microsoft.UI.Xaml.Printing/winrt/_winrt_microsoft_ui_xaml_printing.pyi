# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.microsoft.ui.xaml
import winrt.windows.foundation
import winrt.windows.graphics.printing

from winrt.microsoft.ui.xaml.printing import PreviewPageCountType
from winrt.microsoft.ui.xaml.printing import AddPagesEventHandler, GetPreviewPageEventHandler, PaginateEventHandler

Self = typing.TypeVar('Self')

@typing.final
class AddPagesEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AddPagesEventArgs: ...
    def __new__(cls: typing.Type[AddPagesEventArgs]) -> AddPagesEventArgs:...
    @_property
    def print_task_options(self) -> typing.Optional[winrt.windows.graphics.printing.PrintTaskOptions]: ...

@typing.final
class GetPreviewPageEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GetPreviewPageEventArgs: ...
    def __new__(cls: typing.Type[GetPreviewPageEventArgs]) -> GetPreviewPageEventArgs:...
    @_property
    def page_number(self) -> winrt.system.Int32: ...

@typing.final
class PaginateEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaginateEventArgs: ...
    def __new__(cls: typing.Type[PaginateEventArgs]) -> PaginateEventArgs:...
    @_property
    def current_preview_page_number(self) -> winrt.system.Int32: ...
    @_property
    def print_task_options(self) -> typing.Optional[winrt.windows.graphics.printing.PrintTaskOptions]: ...

@typing.final
class PrintDocument_Static(type):
    @_property
    def document_source_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class PrintDocument(winrt.system.Object, metaclass=PrintDocument_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintDocument: ...
    def __new__(cls: typing.Type[PrintDocument]) -> PrintDocument:...
    def add_page(self, page_visual: typing.Optional[winrt.microsoft.ui.xaml.UIElement], /) -> None: ...
    def add_pages_complete(self) -> None: ...
    def invalidate_preview(self) -> None: ...
    def set_preview_page(self, page_number: winrt.system.Int32, page_visual: typing.Optional[winrt.microsoft.ui.xaml.UIElement], /) -> None: ...
    def set_preview_page_count(self, count: winrt.system.Int32, type: PreviewPageCountType, /) -> None: ...
    def add_add_pages(self, handler: typing.Optional[AddPagesEventHandler], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_add_pages(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_get_preview_page(self, handler: typing.Optional[GetPreviewPageEventHandler], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_get_preview_page(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_paginate(self, handler: typing.Optional[PaginateEventHandler], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_paginate(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def document_source(self) -> typing.Optional[winrt.windows.graphics.printing.IPrintDocumentSource]: ...
