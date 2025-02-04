# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt._winrt_windows_media_protection_playready import (
    NDClient,
    NDCustomData,
    NDDownloadEngineNotifier,
    NDLicenseFetchDescriptor,
    NDStorageFileHelper,
    NDStreamParserNotifier,
    NDTCPMessenger,
    PlayReadyContentHeader,
    PlayReadyContentResolver,
    PlayReadyDomain,
    PlayReadyDomainIterable,
    PlayReadyDomainIterator,
    PlayReadyDomainJoinServiceRequest,
    PlayReadyDomainLeaveServiceRequest,
    PlayReadyITADataGenerator,
    PlayReadyIndividualizationServiceRequest,
    PlayReadyLicense,
    PlayReadyLicenseAcquisitionServiceRequest,
    PlayReadyLicenseIterable,
    PlayReadyLicenseIterator,
    PlayReadyLicenseManagement,
    PlayReadyLicenseSession,
    PlayReadyMeteringReportServiceRequest,
    PlayReadyRevocationServiceRequest,
    PlayReadySecureStopIterable,
    PlayReadySecureStopIterator,
    PlayReadySecureStopServiceRequest,
    PlayReadySoapMessage,
    PlayReadyStatics,
    INDClosedCaptionDataReceivedEventArgs,
    ImplementsINDClosedCaptionDataReceivedEventArgs,
    INDCustomData,
    ImplementsINDCustomData,
    INDDownloadEngine,
    ImplementsINDDownloadEngine,
    INDDownloadEngineNotifier,
    ImplementsINDDownloadEngineNotifier,
    INDLicenseFetchCompletedEventArgs,
    ImplementsINDLicenseFetchCompletedEventArgs,
    INDLicenseFetchDescriptor,
    ImplementsINDLicenseFetchDescriptor,
    INDLicenseFetchResult,
    ImplementsINDLicenseFetchResult,
    INDMessenger,
    ImplementsINDMessenger,
    INDProximityDetectionCompletedEventArgs,
    ImplementsINDProximityDetectionCompletedEventArgs,
    INDRegistrationCompletedEventArgs,
    ImplementsINDRegistrationCompletedEventArgs,
    INDSendResult,
    ImplementsINDSendResult,
    INDStartResult,
    ImplementsINDStartResult,
    INDStorageFileHelper,
    ImplementsINDStorageFileHelper,
    INDStreamParser,
    ImplementsINDStreamParser,
    INDStreamParserNotifier,
    ImplementsINDStreamParserNotifier,
    INDTransmitterProperties,
    ImplementsINDTransmitterProperties,
    IPlayReadyDomain,
    ImplementsIPlayReadyDomain,
    IPlayReadyLicense,
    ImplementsIPlayReadyLicense,
    IPlayReadyLicenseAcquisitionServiceRequest,
    ImplementsIPlayReadyLicenseAcquisitionServiceRequest,
    IPlayReadyLicenseSession,
    ImplementsIPlayReadyLicenseSession,
    IPlayReadyLicenseSession2,
    ImplementsIPlayReadyLicenseSession2,
    IPlayReadySecureStopServiceRequest,
    ImplementsIPlayReadySecureStopServiceRequest,
    IPlayReadyServiceRequest,
    ImplementsIPlayReadyServiceRequest,
)

__all__ = [
    "NDCertificateFeature",
    "NDCertificatePlatformID",
    "NDCertificateType",
    "NDClosedCaptionFormat",
    "NDContentIDType",
    "NDMediaStreamType",
    "NDProximityDetectionType",
    "NDStartAsyncOptions",
    "PlayReadyDecryptorSetup",
    "PlayReadyEncryptionAlgorithm",
    "PlayReadyHardwareDRMFeatures",
    "PlayReadyITADataFormat",
    "NDClient",
    "NDCustomData",
    "NDDownloadEngineNotifier",
    "NDLicenseFetchDescriptor",
    "NDStorageFileHelper",
    "NDStreamParserNotifier",
    "NDTCPMessenger",
    "PlayReadyContentHeader",
    "PlayReadyContentResolver",
    "PlayReadyDomain",
    "PlayReadyDomainIterable",
    "PlayReadyDomainIterator",
    "PlayReadyDomainJoinServiceRequest",
    "PlayReadyDomainLeaveServiceRequest",
    "PlayReadyITADataGenerator",
    "PlayReadyIndividualizationServiceRequest",
    "PlayReadyLicense",
    "PlayReadyLicenseAcquisitionServiceRequest",
    "PlayReadyLicenseIterable",
    "PlayReadyLicenseIterator",
    "PlayReadyLicenseManagement",
    "PlayReadyLicenseSession",
    "PlayReadyMeteringReportServiceRequest",
    "PlayReadyRevocationServiceRequest",
    "PlayReadySecureStopIterable",
    "PlayReadySecureStopIterator",
    "PlayReadySecureStopServiceRequest",
    "PlayReadySoapMessage",
    "PlayReadyStatics",
    "INDClosedCaptionDataReceivedEventArgs",
    "ImplementsINDClosedCaptionDataReceivedEventArgs",
    "INDCustomData",
    "ImplementsINDCustomData",
    "INDDownloadEngine",
    "ImplementsINDDownloadEngine",
    "INDDownloadEngineNotifier",
    "ImplementsINDDownloadEngineNotifier",
    "INDLicenseFetchCompletedEventArgs",
    "ImplementsINDLicenseFetchCompletedEventArgs",
    "INDLicenseFetchDescriptor",
    "ImplementsINDLicenseFetchDescriptor",
    "INDLicenseFetchResult",
    "ImplementsINDLicenseFetchResult",
    "INDMessenger",
    "ImplementsINDMessenger",
    "INDProximityDetectionCompletedEventArgs",
    "ImplementsINDProximityDetectionCompletedEventArgs",
    "INDRegistrationCompletedEventArgs",
    "ImplementsINDRegistrationCompletedEventArgs",
    "INDSendResult",
    "ImplementsINDSendResult",
    "INDStartResult",
    "ImplementsINDStartResult",
    "INDStorageFileHelper",
    "ImplementsINDStorageFileHelper",
    "INDStreamParser",
    "ImplementsINDStreamParser",
    "INDStreamParserNotifier",
    "ImplementsINDStreamParserNotifier",
    "INDTransmitterProperties",
    "ImplementsINDTransmitterProperties",
    "IPlayReadyDomain",
    "ImplementsIPlayReadyDomain",
    "IPlayReadyLicense",
    "ImplementsIPlayReadyLicense",
    "IPlayReadyLicenseAcquisitionServiceRequest",
    "ImplementsIPlayReadyLicenseAcquisitionServiceRequest",
    "IPlayReadyLicenseSession",
    "ImplementsIPlayReadyLicenseSession",
    "IPlayReadyLicenseSession2",
    "ImplementsIPlayReadyLicenseSession2",
    "IPlayReadySecureStopServiceRequest",
    "ImplementsIPlayReadySecureStopServiceRequest",
    "IPlayReadyServiceRequest",
    "ImplementsIPlayReadyServiceRequest",
]

class NDCertificateFeature(enum.IntEnum):
    TRANSMITTER = 1
    RECEIVER = 2
    SHARED_CERTIFICATE = 3
    SECURE_CLOCK = 4
    ANTI_ROLL_BACK_CLOCK = 5
    CRLS = 9
    PLAY_READY3_FEATURES = 13

class NDCertificatePlatformID(enum.IntEnum):
    WINDOWS = 0
    OSX = 1
    WINDOWS_ON_ARM = 2
    WINDOWS_MOBILE7 = 5
    IOS_ON_ARM = 6
    X_BOX_ON_PPC = 7
    WINDOWS_PHONE8_ON_ARM = 8
    WINDOWS_PHONE8_ON_X86 = 9
    XBOX_ONE = 10
    ANDROID_ON_ARM = 11
    WINDOWS_PHONE81_ON_ARM = 12
    WINDOWS_PHONE81_ON_X86 = 13

class NDCertificateType(enum.IntEnum):
    UNKNOWN = 0
    PC = 1
    DEVICE = 2
    DOMAIN = 3
    ISSUER = 4
    CRL_SIGNER = 5
    SERVICE = 6
    SILVERLIGHT = 7
    APPLICATION = 8
    METERING = 9
    KEY_FILE_SIGNER = 10
    SERVER = 11
    LICENSE_SIGNER = 12

class NDClosedCaptionFormat(enum.IntEnum):
    ATSC = 0
    SCTE20 = 1
    UNKNOWN = 2

class NDContentIDType(enum.IntEnum):
    KEY_ID = 1
    PLAY_READY_OBJECT = 2
    CUSTOM = 3

class NDMediaStreamType(enum.IntEnum):
    AUDIO = 1
    VIDEO = 2

class NDProximityDetectionType(enum.IntEnum):
    UDP = 1
    TCP = 2
    TRANSPORT_AGNOSTIC = 4

class NDStartAsyncOptions(enum.IntEnum):
    MUTUAL_AUTHENTICATION = 1
    WAIT_FOR_LICENSE_DESCRIPTOR = 2

class PlayReadyDecryptorSetup(enum.IntEnum):
    UNINITIALIZED = 0
    ON_DEMAND = 1

class PlayReadyEncryptionAlgorithm(enum.IntEnum):
    UNPROTECTED = 0
    AES128_CTR = 1
    COCKTAIL = 4
    AES128_CBC = 5
    UNSPECIFIED = 65535
    UNINITIALIZED = 2147483647

class PlayReadyHardwareDRMFeatures(enum.IntEnum):
    HARDWARE_DRM = 1
    HEVC = 2
    AES128_CBC = 3

class PlayReadyITADataFormat(enum.IntEnum):
    SERIALIZED_PROPERTIES = 0
    SERIALIZED_PROPERTIES_WITH_CONTENT_PROTECTION_WRAPPER = 1

