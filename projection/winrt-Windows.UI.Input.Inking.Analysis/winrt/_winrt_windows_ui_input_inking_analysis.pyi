# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.ui.input.inking

from winrt.windows.ui.input.inking.analysis import InkAnalysisDrawingKind, InkAnalysisNodeKind, InkAnalysisStatus, InkAnalysisStrokeKind

Self = typing.TypeVar('Self')

class InkAnalysisInkBullet(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisInkBullet: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def recognized_text(self) -> str: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class InkAnalysisInkDrawing(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisInkDrawing: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def center(self) -> winrt.windows.foundation.Point: ...
    @_property
    def drawing_kind(self) -> InkAnalysisDrawingKind: ...
    @_property
    def points(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class InkAnalysisInkWord(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisInkWord: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def recognized_text(self) -> str: ...
    @_property
    def text_alternates(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class InkAnalysisLine(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisLine: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def indent_level(self) -> winrt.system.Int32: ...
    @_property
    def recognized_text(self) -> str: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class InkAnalysisListItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisListItem: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def recognized_text(self) -> str: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class InkAnalysisNode(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisNode: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class InkAnalysisParagraph(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisParagraph: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...
    @_property
    def recognized_text(self) -> str: ...

class InkAnalysisResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisResult: ...
    @_property
    def status(self) -> InkAnalysisStatus: ...

class InkAnalysisRoot(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisRoot: ...
    def find_nodes(self, node_kind: InkAnalysisNodeKind, /) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...
    @_property
    def recognized_text(self) -> str: ...

class InkAnalysisWritingRegion(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkAnalysisWritingRegion: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...
    @_property
    def recognized_text(self) -> str: ...

class InkAnalyzer(winrt.system.Object):
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
    @_property
    def analysis_root(self) -> typing.Optional[InkAnalysisRoot]: ...
    @_property
    def is_analyzing(self) -> bool: ...

class IInkAnalysisNode(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkAnalysisNode: ...
    def get_stroke_ids(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def bounding_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def children(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[IInkAnalysisNode]]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> InkAnalysisNodeKind: ...
    @_property
    def parent(self) -> typing.Optional[IInkAnalysisNode]: ...
    @_property
    def rotated_bounding_rect(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.foundation.Point]]: ...

class IInkAnalyzerFactory(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkAnalyzerFactory: ...
    def create_analyzer(self) -> typing.Optional[InkAnalyzer]: ...
