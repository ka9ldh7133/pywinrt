# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt._winrt_windows_system_diagnostics import (
    DiagnosticActionResult,
    DiagnosticInvoker,
    ProcessCpuUsage,
    ProcessCpuUsageReport,
    ProcessDiagnosticInfo,
    ProcessDiskUsage,
    ProcessDiskUsageReport,
    ProcessMemoryUsage,
    ProcessMemoryUsageReport,
    SystemCpuUsage,
    SystemCpuUsageReport,
    SystemDiagnosticInfo,
    SystemMemoryUsage,
    SystemMemoryUsageReport,
)

__all__ = [
    "DiagnosticActionState",
    "DiagnosticActionResult",
    "DiagnosticInvoker",
    "ProcessCpuUsage",
    "ProcessCpuUsageReport",
    "ProcessDiagnosticInfo",
    "ProcessDiskUsage",
    "ProcessDiskUsageReport",
    "ProcessMemoryUsage",
    "ProcessMemoryUsageReport",
    "SystemCpuUsage",
    "SystemCpuUsageReport",
    "SystemDiagnosticInfo",
    "SystemMemoryUsage",
    "SystemMemoryUsageReport",
]

class DiagnosticActionState(enum.IntEnum):
    INITIALIZING = 0
    DOWNLOADING = 1
    VERIFYING_TRUST = 2
    DETECTING = 3
    RESOLVING = 4
    VERIFYING_RESOLUTION = 5
    EXECUTING = 6

