# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_data_pdf

class PdfPageRotation(enum.IntEnum):
    NORMAL = 0
    ROTATE90 = 1
    ROTATE180 = 2
    ROTATE270 = 3

PdfDocument = _winrt_windows_data_pdf.PdfDocument
PdfPage = _winrt_windows_data_pdf.PdfPage
PdfPageDimensions = _winrt_windows_data_pdf.PdfPageDimensions
PdfPageRenderOptions = _winrt_windows_data_pdf.PdfPageRenderOptions