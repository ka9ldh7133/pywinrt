# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.ui.text

Self = typing.TypeVar('Self')

class LanguageFont(winrt.system.Object):
    font_family: str
    font_stretch: winrt.windows.ui.text.FontStretch
    font_style: winrt.windows.ui.text.FontStyle
    font_weight: winrt.windows.ui.text.FontWeight
    scale_factor: winrt.system.Double
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LanguageFont: ...

class LanguageFontGroup(winrt.system.Object):
    document_alternate1_font: typing.Optional[LanguageFont]
    document_alternate2_font: typing.Optional[LanguageFont]
    document_heading_font: typing.Optional[LanguageFont]
    fixed_width_text_font: typing.Optional[LanguageFont]
    modern_document_font: typing.Optional[LanguageFont]
    traditional_document_font: typing.Optional[LanguageFont]
    u_i_caption_font: typing.Optional[LanguageFont]
    u_i_heading_font: typing.Optional[LanguageFont]
    u_i_notification_heading_font: typing.Optional[LanguageFont]
    u_i_text_font: typing.Optional[LanguageFont]
    u_i_title_font: typing.Optional[LanguageFont]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LanguageFontGroup: ...
    def __new__(cls: typing.Type[LanguageFontGroup], language_tag: str) -> LanguageFontGroup:...
