# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_networking_servicediscovery_dnssd

class DnssdRegistrationStatus(enum.IntEnum):
    SUCCESS = 0
    INVALID_SERVICE_NAME = 1
    SERVER_ERROR = 2
    SECURITY_ERROR = 3

class DnssdServiceWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

DnssdRegistrationResult = _winrt_windows_networking_servicediscovery_dnssd.DnssdRegistrationResult
DnssdServiceInstance = _winrt_windows_networking_servicediscovery_dnssd.DnssdServiceInstance
DnssdServiceInstanceCollection = _winrt_windows_networking_servicediscovery_dnssd.DnssdServiceInstanceCollection
winrt.system._mixin_sequence(DnssdServiceInstanceCollection)
DnssdServiceWatcher = _winrt_windows_networking_servicediscovery_dnssd.DnssdServiceWatcher