# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.foundation.numerics
import winrt.windows.storage.streams
import winrt.windows.ui
import winrt.windows.ui.core
import winrt.windows.ui.input

from . import HandwritingLineHeight, InkDrawingAttributesKind, InkHighContrastAdjustment, InkInputProcessingMode, InkInputRightDragAction, InkManipulationMode, InkPersistenceFormat, InkPresenterPredefinedConfiguration, InkPresenterStencilKind, InkRecognitionTarget, PenHandedness, PenTipShape

Self = typing.TypeVar('Self')

class InkDrawingAttributes(winrt.system.Object):
    size: winrt.windows.foundation.Size
    pen_tip: PenTipShape
    ignore_pressure: winrt.system.Boolean
    fit_to_curve: winrt.system.Boolean
    color: winrt.windows.ui.Color
    pen_tip_transform: winrt.windows.foundation.numerics.Matrix3x2
    draw_as_highlighter: winrt.system.Boolean
    kind: InkDrawingAttributesKind
    pencil_properties: typing.Optional[InkDrawingAttributesPencilProperties]
    ignore_tilt: winrt.system.Boolean
    modeler_attributes: typing.Optional[InkModelerAttributes]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkDrawingAttributes: ...
    def __new__(cls: typing.Type[InkDrawingAttributes]) -> InkDrawingAttributes:...
    @staticmethod
    def create_for_pencil() -> typing.Optional[InkDrawingAttributes]: ...

class InkDrawingAttributesPencilProperties(winrt.system.Object):
    opacity: winrt.system.Double
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkDrawingAttributesPencilProperties: ...

class InkInputConfiguration(winrt.system.Object):
    is_primary_barrel_button_input_enabled: winrt.system.Boolean
    is_eraser_input_enabled: winrt.system.Boolean
    is_pen_haptic_feedback_enabled: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkInputConfiguration: ...

class InkInputProcessingConfiguration(winrt.system.Object):
    right_drag_action: InkInputRightDragAction
    mode: InkInputProcessingMode
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkInputProcessingConfiguration: ...

class InkManager(winrt.system.Object):
    mode: InkManipulationMode
    bounding_rect: winrt.windows.foundation.Rect
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkManager: ...
    def __new__(cls: typing.Type[InkManager]) -> InkManager:...
    def add_stroke(self, stroke: typing.Optional[InkStroke], /) -> None: ...
    def can_paste_from_clipboard(self) -> winrt.system.Boolean: ...
    def copy_selected_to_clipboard(self) -> None: ...
    def delete_selected(self) -> winrt.windows.foundation.Rect: ...
    def get_recognition_results(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    def get_recognizers(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkRecognizer]]: ...
    def get_strokes(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]: ...
    def load_async(self, input_stream: typing.Optional[winrt.windows.storage.streams.IInputStream], /) -> winrt.windows.foundation.IAsyncActionWithProgress[winrt.system.UInt64]: ...
    def move_selected(self, translation: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def paste_from_clipboard(self, position: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def process_pointer_down(self, pointer_point: typing.Optional[winrt.windows.ui.input.PointerPoint], /) -> None: ...
    def process_pointer_up(self, pointer_point: typing.Optional[winrt.windows.ui.input.PointerPoint], /) -> winrt.windows.foundation.Rect: ...
    def process_pointer_update(self, pointer_point: typing.Optional[winrt.windows.ui.input.PointerPoint], /) -> typing.Optional[winrt.system.Object]: ...
    @typing.overload
    def recognize_async(self, recognition_target: InkRecognitionTarget, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    @typing.overload
    def recognize_async(self, stroke_collection: typing.Optional[InkStrokeContainer], recognition_target: InkRecognitionTarget, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    def save_async(self, output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream], /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...
    def select_with_line(self, from_: winrt.windows.foundation.Point, to: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def select_with_poly_line(self, polyline: typing.Iterable[winrt.windows.foundation.Point], /) -> winrt.windows.foundation.Rect: ...
    def set_default_drawing_attributes(self, drawing_attributes: typing.Optional[InkDrawingAttributes], /) -> None: ...
    def set_default_recognizer(self, recognizer: typing.Optional[InkRecognizer], /) -> None: ...
    def update_recognition_results(self, recognition_results: winrt.windows.foundation.collections.IVectorView[InkRecognitionResult], /) -> None: ...

class InkModelerAttributes(winrt.system.Object):
    scaling_factor: winrt.system.Single
    prediction_time: datetime.timedelta
    use_velocity_based_pressure: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkModelerAttributes: ...

class InkPoint(winrt.system.Object):
    position: winrt.windows.foundation.Point
    pressure: winrt.system.Single
    tilt_x: winrt.system.Single
    tilt_y: winrt.system.Single
    timestamp: winrt.system.UInt64
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkPoint: ...
    @typing.overload
    def __new__(cls: typing.Type[InkPoint], position: winrt.windows.foundation.Point, pressure: winrt.system.Single, tilt_x: winrt.system.Single, tilt_y: winrt.system.Single, timestamp: winrt.system.UInt64) -> InkPoint:...
    @typing.overload
    def __new__(cls: typing.Type[InkPoint], position: winrt.windows.foundation.Point, pressure: winrt.system.Single) -> InkPoint:...

class InkPresenter(winrt.system.Object):
    stroke_container: typing.Optional[InkStrokeContainer]
    is_input_enabled: winrt.system.Boolean
    input_device_types: winrt.windows.ui.core.CoreInputDeviceTypes
    input_processing_configuration: typing.Optional[InkInputProcessingConfiguration]
    stroke_input: typing.Optional[InkStrokeInput]
    unprocessed_input: typing.Optional[InkUnprocessedInput]
    high_contrast_adjustment: InkHighContrastAdjustment
    input_configuration: typing.Optional[InkInputConfiguration]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkPresenter: ...
    def activate_custom_drying(self) -> typing.Optional[InkSynchronizer]: ...
    def copy_default_drawing_attributes(self) -> typing.Optional[InkDrawingAttributes]: ...
    def set_predefined_configuration(self, value: InkPresenterPredefinedConfiguration, /) -> None: ...
    def update_default_drawing_attributes(self, value: typing.Optional[InkDrawingAttributes], /) -> None: ...
    def add_strokes_collected(self, handler: winrt.windows.foundation.TypedEventHandler[InkPresenter, InkStrokesCollectedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_strokes_collected(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_strokes_erased(self, handler: winrt.windows.foundation.TypedEventHandler[InkPresenter, InkStrokesErasedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_strokes_erased(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class InkPresenterProtractor(winrt.system.Object):
    radius: winrt.system.Double
    is_resizable: winrt.system.Boolean
    is_center_marker_visible: winrt.system.Boolean
    is_angle_readout_visible: winrt.system.Boolean
    are_tick_marks_visible: winrt.system.Boolean
    are_rays_visible: winrt.system.Boolean
    accent_color: winrt.windows.ui.Color
    transform: winrt.windows.foundation.numerics.Matrix3x2
    is_visible: winrt.system.Boolean
    foreground_color: winrt.windows.ui.Color
    background_color: winrt.windows.ui.Color
    kind: InkPresenterStencilKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkPresenterProtractor: ...
    def __new__(cls: typing.Type[InkPresenterProtractor], ink_presenter: typing.Optional[InkPresenter]) -> InkPresenterProtractor:...

class InkPresenterRuler(winrt.system.Object):
    width: winrt.system.Double
    length: winrt.system.Double
    is_compass_visible: winrt.system.Boolean
    are_tick_marks_visible: winrt.system.Boolean
    transform: winrt.windows.foundation.numerics.Matrix3x2
    is_visible: winrt.system.Boolean
    foreground_color: winrt.windows.ui.Color
    background_color: winrt.windows.ui.Color
    kind: InkPresenterStencilKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkPresenterRuler: ...
    def __new__(cls: typing.Type[InkPresenterRuler], ink_presenter: typing.Optional[InkPresenter]) -> InkPresenterRuler:...

class InkRecognitionResult(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkRecognitionResult: ...
    def get_strokes(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]: ...
    def get_text_candidates(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[str]]: ...

class InkRecognizer(winrt.system.Object):
    name: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkRecognizer: ...

class InkRecognizerContainer(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkRecognizerContainer: ...
    def __new__(cls: typing.Type[InkRecognizerContainer]) -> InkRecognizerContainer:...
    def get_recognizers(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkRecognizer]]: ...
    def recognize_async(self, stroke_collection: typing.Optional[InkStrokeContainer], recognition_target: InkRecognitionTarget, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    def set_default_recognizer(self, recognizer: typing.Optional[InkRecognizer], /) -> None: ...

class InkStroke(winrt.system.Object):
    selected: winrt.system.Boolean
    drawing_attributes: typing.Optional[InkDrawingAttributes]
    bounding_rect: winrt.windows.foundation.Rect
    recognized: winrt.system.Boolean
    point_transform: winrt.windows.foundation.numerics.Matrix3x2
    stroke_started_time: typing.Optional[typing.Optional[datetime.datetime]]
    stroke_duration: typing.Optional[typing.Optional[datetime.timedelta]]
    id: winrt.system.UInt32
    pointer_id: winrt.system.UInt32
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStroke: ...
    def clone(self) -> typing.Optional[InkStroke]: ...
    def get_ink_points(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkPoint]]: ...
    def get_rendering_segments(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStrokeRenderingSegment]]: ...

class InkStrokeBuilder(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStrokeBuilder: ...
    def __new__(cls: typing.Type[InkStrokeBuilder]) -> InkStrokeBuilder:...
    def append_to_stroke(self, pointer_point: typing.Optional[winrt.windows.ui.input.PointerPoint], /) -> typing.Optional[winrt.windows.ui.input.PointerPoint]: ...
    def begin_stroke(self, pointer_point: typing.Optional[winrt.windows.ui.input.PointerPoint], /) -> None: ...
    def create_stroke(self, points: typing.Iterable[winrt.windows.foundation.Point], /) -> typing.Optional[InkStroke]: ...
    @typing.overload
    def create_stroke_from_ink_points(self, ink_points: typing.Iterable[InkPoint], transform: winrt.windows.foundation.numerics.Matrix3x2, /) -> typing.Optional[InkStroke]: ...
    @typing.overload
    def create_stroke_from_ink_points(self, ink_points: typing.Iterable[InkPoint], transform: winrt.windows.foundation.numerics.Matrix3x2, stroke_started_time: typing.Optional[datetime.datetime], stroke_duration: typing.Optional[datetime.timedelta], /) -> typing.Optional[InkStroke]: ...
    def end_stroke(self, pointer_point: typing.Optional[winrt.windows.ui.input.PointerPoint], /) -> typing.Optional[InkStroke]: ...
    def set_default_drawing_attributes(self, drawing_attributes: typing.Optional[InkDrawingAttributes], /) -> None: ...

class InkStrokeContainer(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStrokeContainer: ...
    def __new__(cls: typing.Type[InkStrokeContainer]) -> InkStrokeContainer:...
    def add_stroke(self, stroke: typing.Optional[InkStroke], /) -> None: ...
    def add_strokes(self, strokes: typing.Iterable[InkStroke], /) -> None: ...
    def can_paste_from_clipboard(self) -> winrt.system.Boolean: ...
    def clear(self) -> None: ...
    def copy_selected_to_clipboard(self) -> None: ...
    def delete_selected(self) -> winrt.windows.foundation.Rect: ...
    def get_recognition_results(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    def get_stroke_by_id(self, id: winrt.system.UInt32, /) -> typing.Optional[InkStroke]: ...
    def get_strokes(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]: ...
    def load_async(self, input_stream: typing.Optional[winrt.windows.storage.streams.IInputStream], /) -> winrt.windows.foundation.IAsyncActionWithProgress[winrt.system.UInt64]: ...
    def move_selected(self, translation: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def paste_from_clipboard(self, position: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    @typing.overload
    def save_async(self, output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream], /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...
    @typing.overload
    def save_async(self, output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream], ink_persistence_format: InkPersistenceFormat, /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...
    def select_with_line(self, from_: winrt.windows.foundation.Point, to: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def select_with_poly_line(self, polyline: typing.Iterable[winrt.windows.foundation.Point], /) -> winrt.windows.foundation.Rect: ...
    def update_recognition_results(self, recognition_results: winrt.windows.foundation.collections.IVectorView[InkRecognitionResult], /) -> None: ...

class InkStrokeInput(winrt.system.Object):
    ink_presenter: typing.Optional[InkPresenter]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStrokeInput: ...
    def add_stroke_canceled(self, handler: winrt.windows.foundation.TypedEventHandler[InkStrokeInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_stroke_canceled(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_stroke_continued(self, handler: winrt.windows.foundation.TypedEventHandler[InkStrokeInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_stroke_continued(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_stroke_ended(self, handler: winrt.windows.foundation.TypedEventHandler[InkStrokeInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_stroke_ended(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_stroke_started(self, handler: winrt.windows.foundation.TypedEventHandler[InkStrokeInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_stroke_started(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class InkStrokeRenderingSegment(winrt.system.Object):
    bezier_control_point1: winrt.windows.foundation.Point
    bezier_control_point2: winrt.windows.foundation.Point
    position: winrt.windows.foundation.Point
    pressure: winrt.system.Single
    tilt_x: winrt.system.Single
    tilt_y: winrt.system.Single
    twist: winrt.system.Single
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStrokeRenderingSegment: ...

class InkStrokesCollectedEventArgs(winrt.system.Object):
    strokes: typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStrokesCollectedEventArgs: ...

class InkStrokesErasedEventArgs(winrt.system.Object):
    strokes: typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkStrokesErasedEventArgs: ...

class InkSynchronizer(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkSynchronizer: ...
    def begin_dry(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]: ...
    def end_dry(self) -> None: ...

class InkUnprocessedInput(winrt.system.Object):
    ink_presenter: typing.Optional[InkPresenter]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InkUnprocessedInput: ...
    def add_pointer_entered(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_entered(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_exited(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_exited(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_hovered(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_hovered(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_lost(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_lost(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_moved(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_moved(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_pressed(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_pressed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_released(self, handler: winrt.windows.foundation.TypedEventHandler[InkUnprocessedInput, winrt.windows.ui.core.PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_released(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class PenAndInkSettings(winrt.system.Object):
    font_family_name: str
    handwriting_line_height: HandwritingLineHeight
    is_handwriting_directly_into_text_field_enabled: winrt.system.Boolean
    is_touch_handwriting_enabled: winrt.system.Boolean
    pen_handedness: PenHandedness
    user_consents_to_handwriting_telemetry_collection: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PenAndInkSettings: ...
    @staticmethod
    def get_default() -> typing.Optional[PenAndInkSettings]: ...
    def set_pen_handedness(self, value: PenHandedness, /) -> None: ...

class IInkPointFactory(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkPointFactory: ...
    def create_ink_point(self, position: winrt.windows.foundation.Point, pressure: winrt.system.Single, /) -> typing.Optional[InkPoint]: ...

class IInkPresenterRulerFactory(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkPresenterRulerFactory: ...
    def create(self, ink_presenter: typing.Optional[InkPresenter], /) -> typing.Optional[InkPresenterRuler]: ...

class IInkPresenterStencil(winrt.system.Object):
    background_color: winrt.windows.ui.Color
    foreground_color: winrt.windows.ui.Color
    is_visible: winrt.system.Boolean
    kind: InkPresenterStencilKind
    transform: winrt.windows.foundation.numerics.Matrix3x2
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkPresenterStencil: ...

class IInkRecognizerContainer(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkRecognizerContainer: ...
    def get_recognizers(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkRecognizer]]: ...
    def recognize_async(self, stroke_collection: typing.Optional[InkStrokeContainer], recognition_target: InkRecognitionTarget, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    def set_default_recognizer(self, recognizer: typing.Optional[InkRecognizer], /) -> None: ...

class IInkStrokeContainer(winrt.system.Object):
    bounding_rect: winrt.windows.foundation.Rect
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IInkStrokeContainer: ...
    def add_stroke(self, stroke: typing.Optional[InkStroke], /) -> None: ...
    def can_paste_from_clipboard(self) -> winrt.system.Boolean: ...
    def copy_selected_to_clipboard(self) -> None: ...
    def delete_selected(self) -> winrt.windows.foundation.Rect: ...
    def get_recognition_results(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkRecognitionResult]]: ...
    def get_strokes(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[InkStroke]]: ...
    def load_async(self, input_stream: typing.Optional[winrt.windows.storage.streams.IInputStream], /) -> winrt.windows.foundation.IAsyncActionWithProgress[winrt.system.UInt64]: ...
    def move_selected(self, translation: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def paste_from_clipboard(self, position: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def save_async(self, output_stream: typing.Optional[winrt.windows.storage.streams.IOutputStream], /) -> winrt.windows.foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...
    def select_with_line(self, from_: winrt.windows.foundation.Point, to: winrt.windows.foundation.Point, /) -> winrt.windows.foundation.Rect: ...
    def select_with_poly_line(self, polyline: typing.Iterable[winrt.windows.foundation.Point], /) -> winrt.windows.foundation.Rect: ...
    def update_recognition_results(self, recognition_results: winrt.windows.foundation.collections.IVectorView[InkRecognitionResult], /) -> None: ...
