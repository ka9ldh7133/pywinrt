# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.ui.input.inking

from . import InkAnalysisDrawingKind, InkAnalysisNodeKind, InkAnalysisStatus, InkAnalysisStrokeKind

Self = typing.TypeVar('Self')

class InkAnalysisInkBullet(winrt.system.Object):
    recognized_text: str
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisInkBullet: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisInkDrawing(winrt.system.Object):
    center: winrt.windows.foundation.Point
    drawing_kind: InkAnalysisDrawingKind
    points: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisInkDrawing: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisInkWord(winrt.system.Object):
    recognized_text: str
    text_alternates: typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisInkWord: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisLine(winrt.system.Object):
    indent_level: winrt.system.Int32
    recognized_text: str
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisLine: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisListItem(winrt.system.Object):
    recognized_text: str
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisListItem: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisNode(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisNode: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisParagraph(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    recognized_text: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisParagraph: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisResult(winrt.system.Object):
    status: InkAnalysisStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisResult: ...

class InkAnalysisRoot(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    recognized_text: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisRoot: ...
    def find_nodes(self, node_kind: InkAnalysisNodeKind, /) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalysisWritingRegion(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    recognized_text: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisWritingRegion: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class InkAnalyzer(winrt.system.Object):
    analysis_root: typing.Optional[InkAnalysisRoot]
    is_analyzing: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalyzer: ...
    def __new__(cls: typing.Type[InkAnalyzer]) -> InkAnalyzer:...
    def add_data_for_stroke(self, stroke: typing.Optional[winrt.windows.ui.input.inking.InkStroke], /) -> None: ...
    def add_data_for_strokes(self, strokes: typing.Iterable[winrt.windows.ui.input.inking.InkStroke], /) -> None: ...
    def analyze_async(self) -> winrt.windows.foundation.IAsyncOperation[InkAnalysisResult]: ...
    def clear_data_for_all_strokes(self) -> None: ...
    def remove_data_for_stroke(self, stroke_id: winrt.system.UInt32, /) -> None: ...
    def remove_data_for_strokes(self, stroke_ids: typing.Iterable[winrt.system.UInt32], /) -> None: ...
    def replace_data_for_stroke(self, stroke: typing.Optional[winrt.windows.ui.input.inking.InkStroke], /) -> None: ...
    def set_stroke_data_kind(self, stroke_id: winrt.system.UInt32, stroke_kind: InkAnalysisStrokeKind, /) -> None: ...

class IInkAnalysisNode(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    children: typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]
    id: winrt.system.UInt32
    kind: InkAnalysisNodeKind
    parent: typing.Optional[IInkAnalysisNode]
    rotated_bounding_rect: typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkAnalysisNode: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...

class IInkAnalyzerFactory(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkAnalyzerFactory: ...
    def create_analyzer(self) -> typing.Optional[InkAnalyzer]: ...
