# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_graphics_printing3d

class Print3DTaskCompletion(enum.IntEnum):
    ABANDONED = 0
    CANCELED = 1
    FAILED = 2
    SLICING = 3
    SUBMITTED = 4

class Print3DTaskDetail(enum.IntEnum):
    UNKNOWN = 0
    MODEL_EXCEEDS_PRINT_BED = 1
    UPLOAD_FAILED = 2
    INVALID_MATERIAL_SELECTION = 3
    INVALID_MODEL = 4
    MODEL_NOT_MANIFOLD = 5
    INVALID_PRINT_TICKET = 6

class Printing3DBufferFormat(enum.IntEnum):
    UNKNOWN = 0
    R32_G32_B32_A32_FLOAT = 2
    R32_G32_B32_A32_UINT = 3
    R32_G32_B32_FLOAT = 6
    R32_G32_B32_UINT = 7
    PRINTING3_D_DOUBLE = 500
    PRINTING3_D_UINT = 501

class Printing3DMeshVerificationMode(enum.IntEnum):
    FIND_FIRST_ERROR = 0
    FIND_ALL_ERRORS = 1

class Printing3DModelUnit(enum.IntEnum):
    METER = 0
    MICRON = 1
    MILLIMETER = 2
    CENTIMETER = 3
    INCH = 4
    FOOT = 5

class Printing3DObjectType(enum.IntEnum):
    MODEL = 0
    SUPPORT = 1
    OTHERS = 2

class Printing3DPackageCompression(enum.IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Printing3DTextureEdgeBehavior(enum.IntEnum):
    NONE = 0
    WRAP = 1
    MIRROR = 2
    CLAMP = 3

Printing3DBufferDescription = _winrt_windows_graphics_printing3d.Printing3DBufferDescription
Print3DManager = _winrt_windows_graphics_printing3d.Print3DManager
Print3DTask = _winrt_windows_graphics_printing3d.Print3DTask
Print3DTaskCompletedEventArgs = _winrt_windows_graphics_printing3d.Print3DTaskCompletedEventArgs
Print3DTaskRequest = _winrt_windows_graphics_printing3d.Print3DTaskRequest
Print3DTaskRequestedEventArgs = _winrt_windows_graphics_printing3d.Print3DTaskRequestedEventArgs
Print3DTaskSourceChangedEventArgs = _winrt_windows_graphics_printing3d.Print3DTaskSourceChangedEventArgs
Print3DTaskSourceRequestedArgs = _winrt_windows_graphics_printing3d.Print3DTaskSourceRequestedArgs
Printing3D3MFPackage = _winrt_windows_graphics_printing3d.Printing3D3MFPackage
Printing3DBaseMaterial = _winrt_windows_graphics_printing3d.Printing3DBaseMaterial
Printing3DBaseMaterialGroup = _winrt_windows_graphics_printing3d.Printing3DBaseMaterialGroup
Printing3DColorMaterial = _winrt_windows_graphics_printing3d.Printing3DColorMaterial
Printing3DColorMaterialGroup = _winrt_windows_graphics_printing3d.Printing3DColorMaterialGroup
Printing3DComponent = _winrt_windows_graphics_printing3d.Printing3DComponent
Printing3DComponentWithMatrix = _winrt_windows_graphics_printing3d.Printing3DComponentWithMatrix
Printing3DCompositeMaterial = _winrt_windows_graphics_printing3d.Printing3DCompositeMaterial
Printing3DCompositeMaterialGroup = _winrt_windows_graphics_printing3d.Printing3DCompositeMaterialGroup
Printing3DFaceReductionOptions = _winrt_windows_graphics_printing3d.Printing3DFaceReductionOptions
Printing3DMaterial = _winrt_windows_graphics_printing3d.Printing3DMaterial
Printing3DMesh = _winrt_windows_graphics_printing3d.Printing3DMesh
Printing3DMeshVerificationResult = _winrt_windows_graphics_printing3d.Printing3DMeshVerificationResult
Printing3DModel = _winrt_windows_graphics_printing3d.Printing3DModel
Printing3DModelTexture = _winrt_windows_graphics_printing3d.Printing3DModelTexture
Printing3DMultiplePropertyMaterial = _winrt_windows_graphics_printing3d.Printing3DMultiplePropertyMaterial
Printing3DMultiplePropertyMaterialGroup = _winrt_windows_graphics_printing3d.Printing3DMultiplePropertyMaterialGroup
Printing3DTexture2CoordMaterial = _winrt_windows_graphics_printing3d.Printing3DTexture2CoordMaterial
Printing3DTexture2CoordMaterialGroup = _winrt_windows_graphics_printing3d.Printing3DTexture2CoordMaterialGroup
Printing3DTextureResource = _winrt_windows_graphics_printing3d.Printing3DTextureResource