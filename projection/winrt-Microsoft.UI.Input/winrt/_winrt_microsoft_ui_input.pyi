# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.microsoft.ui
import winrt.microsoft.ui.content
import winrt.microsoft.ui.dispatching
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.graphics
import winrt.windows.system
import winrt.windows.ui.core

from winrt.microsoft.ui.input import CrossSlidingState, DraggingState, FocusNavigationReason, FocusNavigationResult, GestureSettings, HoldingState, InputActivationState, InputPointerSourceDeviceKinds, InputSystemCursorShape, NonClientRegionKind, PointerDeviceType, PointerUpdateKind, VirtualKeyStates

Self = typing.TypeVar('Self')

@typing.final
class CrossSlideThresholds:
    selection_start: winrt.system.Single
    speed_bump_start: winrt.system.Single
    speed_bump_end: winrt.system.Single
    rearrange_start: winrt.system.Single
    def __init__(self, selection_start: winrt.system.Single, speed_bump_start: winrt.system.Single, speed_bump_end: winrt.system.Single, rearrange_start: winrt.system.Single) -> None: ...

@typing.final
class ManipulationDelta:
    translation: winrt.windows.foundation.Point
    scale: winrt.system.Single
    rotation: winrt.system.Single
    expansion: winrt.system.Single
    def __init__(self, translation: winrt.windows.foundation.Point, scale: winrt.system.Single, rotation: winrt.system.Single, expansion: winrt.system.Single) -> None: ...

@typing.final
class ManipulationVelocities:
    linear: winrt.windows.foundation.Point
    angular: winrt.system.Single
    expansion: winrt.system.Single
    def __init__(self, linear: winrt.windows.foundation.Point, angular: winrt.system.Single, expansion: winrt.system.Single) -> None: ...

@typing.final
class PhysicalKeyStatus:
    repeat_count: winrt.system.UInt32
    scan_code: winrt.system.UInt32
    is_extended_key: bool
    is_menu_key_down: bool
    was_key_down: bool
    is_key_released: bool
    def __init__(self, repeat_count: winrt.system.UInt32, scan_code: winrt.system.UInt32, is_extended_key: bool, is_menu_key_down: bool, was_key_down: bool, is_key_released: bool) -> None: ...

@typing.final
class CharacterReceivedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CharacterReceivedEventArgs: ...
    @_property
    def handled(self) -> bool: ...
    @handled.setter
    def handled(self, value: bool) -> None: ...
    @_property
    def key_code(self) -> winrt.system.UInt32: ...
    @_property
    def key_status(self) -> PhysicalKeyStatus: ...

@typing.final
class ContextMenuKeyEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ContextMenuKeyEventArgs: ...
    @_property
    def handled(self) -> bool: ...
    @handled.setter
    def handled(self, value: bool) -> None: ...

@typing.final
class CrossSlidingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CrossSlidingEventArgs: ...
    @_property
    def cross_sliding_state(self) -> CrossSlidingState: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...

@typing.final
class DraggingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DraggingEventArgs: ...
    @_property
    def dragging_state(self) -> DraggingState: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...

@typing.final
class FocusChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FocusChangedEventArgs: ...
    @_property
    def handled(self) -> bool: ...
    @handled.setter
    def handled(self, value: bool) -> None: ...

@typing.final
class FocusNavigationRequest_Static(type):
    @typing.overload
    def create(cls, reason: FocusNavigationReason, /) -> typing.Optional[FocusNavigationRequest]: ...
    @typing.overload
    def create(cls, reason: FocusNavigationReason, hint_rect: winrt.windows.foundation.Rect, /) -> typing.Optional[FocusNavigationRequest]: ...
    @typing.overload
    def create(cls, reason: FocusNavigationReason, hint_rect: winrt.windows.foundation.Rect, correlation_id: _uuid.UUID, /) -> typing.Optional[FocusNavigationRequest]: ...

@typing.final
class FocusNavigationRequest(winrt.system.Object, metaclass=FocusNavigationRequest_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FocusNavigationRequest: ...
    @_property
    def correlation_id(self) -> _uuid.UUID: ...
    @_property
    def hint_rect(self) -> typing.Optional[typing.Optional[winrt.windows.foundation.Rect]]: ...
    @_property
    def reason(self) -> FocusNavigationReason: ...

@typing.final
class FocusNavigationRequestEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FocusNavigationRequestEventArgs: ...
    @_property
    def result(self) -> FocusNavigationResult: ...
    @result.setter
    def result(self, value: FocusNavigationResult) -> None: ...
    @_property
    def request(self) -> typing.Optional[FocusNavigationRequest]: ...

@typing.final
class GestureRecognizer(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GestureRecognizer: ...
    def __new__(cls: typing.Type[GestureRecognizer]) -> GestureRecognizer:...
    def can_be_double_tap(self, value: typing.Optional[PointerPoint], /) -> bool: ...
    def complete_gesture(self) -> None: ...
    def process_down_event(self, value: typing.Optional[PointerPoint], /) -> None: ...
    def process_inertia(self) -> None: ...
    def process_mouse_wheel_event(self, value: typing.Optional[PointerPoint], is_shift_key_down: bool, is_control_key_down: bool, /) -> None: ...
    def process_move_events(self, value: winrt.windows.foundation.collections.IVector[PointerPoint], /) -> None: ...
    def process_up_event(self, value: typing.Optional[PointerPoint], /) -> None: ...
    def add_cross_sliding(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, CrossSlidingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_cross_sliding(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_dragging(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, DraggingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_dragging(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_holding(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, HoldingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_holding(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_completed(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationCompletedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_completed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_inertia_starting(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationInertiaStartingEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_inertia_starting(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_started(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationStartedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_started(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_updated(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationUpdatedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_updated(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_right_tapped(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, RightTappedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_right_tapped(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_tapped(self, handler: winrt.windows.foundation.TypedEventHandler[GestureRecognizer, TappedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_tapped(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def show_gesture_feedback(self) -> bool: ...
    @show_gesture_feedback.setter
    def show_gesture_feedback(self, value: bool) -> None: ...
    @_property
    def pivot_radius(self) -> winrt.system.Single: ...
    @pivot_radius.setter
    def pivot_radius(self, value: winrt.system.Single) -> None: ...
    @_property
    def pivot_center(self) -> winrt.windows.foundation.Point: ...
    @pivot_center.setter
    def pivot_center(self, value: winrt.windows.foundation.Point) -> None: ...
    @_property
    def manipulation_exact(self) -> bool: ...
    @manipulation_exact.setter
    def manipulation_exact(self, value: bool) -> None: ...
    @_property
    def inertia_translation_displacement(self) -> winrt.system.Single: ...
    @inertia_translation_displacement.setter
    def inertia_translation_displacement(self, value: winrt.system.Single) -> None: ...
    @_property
    def inertia_translation_deceleration(self) -> winrt.system.Single: ...
    @inertia_translation_deceleration.setter
    def inertia_translation_deceleration(self, value: winrt.system.Single) -> None: ...
    @_property
    def inertia_rotation_deceleration(self) -> winrt.system.Single: ...
    @inertia_rotation_deceleration.setter
    def inertia_rotation_deceleration(self, value: winrt.system.Single) -> None: ...
    @_property
    def inertia_rotation_angle(self) -> winrt.system.Single: ...
    @inertia_rotation_angle.setter
    def inertia_rotation_angle(self, value: winrt.system.Single) -> None: ...
    @_property
    def inertia_expansion_deceleration(self) -> winrt.system.Single: ...
    @inertia_expansion_deceleration.setter
    def inertia_expansion_deceleration(self, value: winrt.system.Single) -> None: ...
    @_property
    def inertia_expansion(self) -> winrt.system.Single: ...
    @inertia_expansion.setter
    def inertia_expansion(self, value: winrt.system.Single) -> None: ...
    @_property
    def gesture_settings(self) -> GestureSettings: ...
    @gesture_settings.setter
    def gesture_settings(self, value: GestureSettings) -> None: ...
    @_property
    def cross_slide_thresholds(self) -> CrossSlideThresholds: ...
    @cross_slide_thresholds.setter
    def cross_slide_thresholds(self, value: CrossSlideThresholds) -> None: ...
    @_property
    def cross_slide_horizontally(self) -> bool: ...
    @cross_slide_horizontally.setter
    def cross_slide_horizontally(self, value: bool) -> None: ...
    @_property
    def cross_slide_exact(self) -> bool: ...
    @cross_slide_exact.setter
    def cross_slide_exact(self, value: bool) -> None: ...
    @_property
    def auto_process_inertia(self) -> bool: ...
    @auto_process_inertia.setter
    def auto_process_inertia(self, value: bool) -> None: ...
    @_property
    def is_active(self) -> bool: ...
    @_property
    def is_inertial(self) -> bool: ...
    @_property
    def mouse_wheel_parameters(self) -> typing.Optional[MouseWheelParameters]: ...

@typing.final
class HoldingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HoldingEventArgs: ...
    @_property
    def holding_state(self) -> HoldingState: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...

@typing.final
class InputActivationListener_Static(type):
    def get_for_island(cls, island: typing.Optional[winrt.microsoft.ui.content.ContentIsland], /) -> typing.Optional[InputActivationListener]: ...
    def get_for_window_id(cls, window_id: winrt.microsoft.ui.WindowId, /) -> typing.Optional[InputActivationListener]: ...

@typing.final
class InputActivationListener(winrt.system.Object, metaclass=InputActivationListener_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputActivationListener: ...
    def add_input_activation_changed(self, handler: winrt.windows.foundation.TypedEventHandler[InputActivationListener, InputActivationListenerActivationChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_input_activation_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def state(self) -> InputActivationState: ...

@typing.final
class InputActivationListenerActivationChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputActivationListenerActivationChangedEventArgs: ...

@typing.final
class InputCursor_Static(type):
    def create_from_core_cursor(cls, cursor: typing.Optional[winrt.windows.ui.core.CoreCursor], /) -> typing.Optional[InputCursor]: ...

@typing.final
class InputCursor(winrt.system.Object, metaclass=InputCursor_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputCursor: ...
    def close(self) -> None: ...

@typing.final
class InputCustomCursor(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputCustomCursor: ...

@typing.final
class InputDesktopNamedResourceCursor_Static(type):
    def create(cls, resource_name: str, /) -> typing.Optional[InputDesktopNamedResourceCursor]: ...
    def create_from_module(cls, module_name: str, resource_name: str, /) -> typing.Optional[InputDesktopNamedResourceCursor]: ...

@typing.final
class InputDesktopNamedResourceCursor(winrt.system.Object, metaclass=InputDesktopNamedResourceCursor_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputDesktopNamedResourceCursor: ...
    @_property
    def module_name(self) -> str: ...
    @_property
    def resource_name(self) -> str: ...

@typing.final
class InputDesktopResourceCursor_Static(type):
    def create(cls, resource_id: winrt.system.UInt32, /) -> typing.Optional[InputDesktopResourceCursor]: ...
    def create_from_module(cls, module_name: str, resource_id: winrt.system.UInt32, /) -> typing.Optional[InputDesktopResourceCursor]: ...

@typing.final
class InputDesktopResourceCursor(winrt.system.Object, metaclass=InputDesktopResourceCursor_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputDesktopResourceCursor: ...
    @_property
    def module_name(self) -> str: ...
    @_property
    def resource_id(self) -> winrt.system.UInt32: ...

@typing.final
class InputFocusController_Static(type):
    def get_for_island(cls, island: typing.Optional[winrt.microsoft.ui.content.ContentIsland], /) -> typing.Optional[InputFocusController]: ...

@typing.final
class InputFocusController(winrt.system.Object, metaclass=InputFocusController_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputFocusController: ...
    def depart_focus(self, request: typing.Optional[FocusNavigationRequest], /) -> FocusNavigationResult: ...
    def try_set_focus(self) -> bool: ...
    def add_got_focus(self, handler: winrt.windows.foundation.TypedEventHandler[InputFocusController, FocusChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_got_focus(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_lost_focus(self, handler: winrt.windows.foundation.TypedEventHandler[InputFocusController, FocusChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_lost_focus(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_navigate_focus_requested(self, handler: winrt.windows.foundation.TypedEventHandler[InputFocusController, FocusNavigationRequestEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_navigate_focus_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def has_focus(self) -> bool: ...

@typing.final
class InputFocusNavigationHost_Static(type):
    def get_for_site_bridge(cls, site: typing.Optional[winrt.microsoft.ui.content.IContentSiteBridge], /) -> typing.Optional[InputFocusNavigationHost]: ...

@typing.final
class InputFocusNavigationHost(winrt.system.Object, metaclass=InputFocusNavigationHost_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputFocusNavigationHost: ...
    def navigate_focus(self, request: typing.Optional[FocusNavigationRequest], /) -> FocusNavigationResult: ...
    def add_depart_focus_requested(self, handler: winrt.windows.foundation.TypedEventHandler[InputFocusNavigationHost, FocusNavigationRequestEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_depart_focus_requested(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def contains_focus(self) -> bool: ...

@typing.final
class InputKeyboardSource_Static(type):
    def get_for_island(cls, island: typing.Optional[winrt.microsoft.ui.content.ContentIsland], /) -> typing.Optional[InputKeyboardSource]: ...
    def get_key_state_for_current_thread(cls, virtual_key: winrt.windows.system.VirtualKey, /) -> winrt.windows.ui.core.CoreVirtualKeyStates: ...

@typing.final
class InputKeyboardSource(winrt.system.Object, metaclass=InputKeyboardSource_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputKeyboardSource: ...
    def get_current_key_state(self, virtual_key: winrt.windows.system.VirtualKey, /) -> VirtualKeyStates: ...
    def get_key_state(self, virtual_key: winrt.windows.system.VirtualKey, /) -> VirtualKeyStates: ...
    def add_character_received(self, handler: winrt.windows.foundation.TypedEventHandler[InputKeyboardSource, CharacterReceivedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_character_received(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_context_menu_key(self, handler: winrt.windows.foundation.TypedEventHandler[InputKeyboardSource, ContextMenuKeyEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_context_menu_key(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_key_down(self, handler: winrt.windows.foundation.TypedEventHandler[InputKeyboardSource, KeyEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_key_down(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_key_up(self, handler: winrt.windows.foundation.TypedEventHandler[InputKeyboardSource, KeyEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_key_up(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_system_key_down(self, handler: winrt.windows.foundation.TypedEventHandler[InputKeyboardSource, KeyEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_system_key_down(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_system_key_up(self, handler: winrt.windows.foundation.TypedEventHandler[InputKeyboardSource, KeyEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_system_key_up(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class InputLightDismissAction_Static(type):
    def get_for_window_id(cls, window_id: winrt.microsoft.ui.WindowId, /) -> typing.Optional[InputLightDismissAction]: ...

@typing.final
class InputLightDismissAction(winrt.system.Object, metaclass=InputLightDismissAction_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputLightDismissAction: ...
    def add_dismissed(self, handler: winrt.windows.foundation.TypedEventHandler[InputLightDismissAction, InputLightDismissEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_dismissed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class InputLightDismissEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputLightDismissEventArgs: ...

@typing.final
class InputNonClientPointerSource_Static(type):
    def get_for_window_id(cls, window_id: winrt.microsoft.ui.WindowId, /) -> typing.Optional[InputNonClientPointerSource]: ...

@typing.final
class InputNonClientPointerSource(winrt.system.Object, metaclass=InputNonClientPointerSource_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputNonClientPointerSource: ...
    def clear_all_region_rects(self) -> None: ...
    def clear_region_rects(self, region: NonClientRegionKind, /) -> None: ...
    def get_region_rects(self, region: NonClientRegionKind, /) -> winrt.windows.graphics.RectInt32: ...
    def set_region_rects(self, region: NonClientRegionKind, rects: winrt.system.Array[winrt.windows.graphics.RectInt32], /) -> None: ...
    def add_caption_tapped(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientCaptionTappedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_caption_tapped(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_entered(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientPointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_entered(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_exited(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientPointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_exited(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_moved(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientPointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_moved(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_pressed(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientPointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_pressed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_released(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientPointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_released(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_regions_changed(self, handler: winrt.windows.foundation.TypedEventHandler[InputNonClientPointerSource, NonClientRegionsChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_regions_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def dispatcher_queue(self) -> typing.Optional[winrt.microsoft.ui.dispatching.DispatcherQueue]: ...

@typing.final
class InputObject(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputObject: ...
    @_property
    def dispatcher_queue(self) -> typing.Optional[winrt.microsoft.ui.dispatching.DispatcherQueue]: ...

@typing.final
class InputPointerSource_Static(type):
    def get_for_island(cls, island: typing.Optional[winrt.microsoft.ui.content.ContentIsland], /) -> typing.Optional[InputPointerSource]: ...

@typing.final
class InputPointerSource(winrt.system.Object, metaclass=InputPointerSource_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputPointerSource: ...
    def add_pointer_capture_lost(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_capture_lost(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_entered(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_entered(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_exited(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_exited(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_moved(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_moved(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_pressed(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_pressed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_released(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_released(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_routed_away(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_routed_away(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_routed_released(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_routed_released(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_routed_to(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_routed_to(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_pointer_wheel_changed(self, handler: winrt.windows.foundation.TypedEventHandler[InputPointerSource, PointerEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_pointer_wheel_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def cursor(self) -> typing.Optional[InputCursor]: ...
    @cursor.setter
    def cursor(self, value: typing.Optional[InputCursor]) -> None: ...
    @_property
    def device_kinds(self) -> InputPointerSourceDeviceKinds: ...

@typing.final
class InputPreTranslateKeyboardSource_Static(type):
    def get_for_island(cls, island: typing.Optional[winrt.microsoft.ui.content.ContentIsland], /) -> typing.Optional[InputPreTranslateKeyboardSource]: ...

@typing.final
class InputPreTranslateKeyboardSource(winrt.system.Object, metaclass=InputPreTranslateKeyboardSource_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputPreTranslateKeyboardSource: ...

@typing.final
class InputSystemCursor_Static(type):
    def create(cls, type: InputSystemCursorShape, /) -> typing.Optional[InputSystemCursor]: ...

@typing.final
class InputSystemCursor(winrt.system.Object, metaclass=InputSystemCursor_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputSystemCursor: ...
    @_property
    def cursor_shape(self) -> InputSystemCursorShape: ...

@typing.final
class KeyEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> KeyEventArgs: ...
    @_property
    def handled(self) -> bool: ...
    @handled.setter
    def handled(self, value: bool) -> None: ...
    @_property
    def key_status(self) -> PhysicalKeyStatus: ...
    @_property
    def timestamp(self) -> winrt.system.UInt64: ...
    @_property
    def virtual_key(self) -> winrt.windows.system.VirtualKey: ...

@typing.final
class ManipulationCompletedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ManipulationCompletedEventArgs: ...
    @_property
    def cumulative(self) -> ManipulationDelta: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...
    @_property
    def velocities(self) -> ManipulationVelocities: ...

@typing.final
class ManipulationInertiaStartingEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ManipulationInertiaStartingEventArgs: ...
    @_property
    def cumulative(self) -> ManipulationDelta: ...
    @_property
    def delta(self) -> ManipulationDelta: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...
    @_property
    def velocities(self) -> ManipulationVelocities: ...

@typing.final
class ManipulationStartedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ManipulationStartedEventArgs: ...
    @_property
    def cumulative(self) -> ManipulationDelta: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...

@typing.final
class ManipulationUpdatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ManipulationUpdatedEventArgs: ...
    @_property
    def cumulative(self) -> ManipulationDelta: ...
    @_property
    def delta(self) -> ManipulationDelta: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...
    @_property
    def velocities(self) -> ManipulationVelocities: ...

@typing.final
class MouseWheelParameters(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MouseWheelParameters: ...
    @_property
    def page_translation(self) -> winrt.windows.foundation.Point: ...
    @page_translation.setter
    def page_translation(self, value: winrt.windows.foundation.Point) -> None: ...
    @_property
    def delta_scale(self) -> winrt.system.Single: ...
    @delta_scale.setter
    def delta_scale(self, value: winrt.system.Single) -> None: ...
    @_property
    def delta_rotation_angle(self) -> winrt.system.Single: ...
    @delta_rotation_angle.setter
    def delta_rotation_angle(self, value: winrt.system.Single) -> None: ...
    @_property
    def char_translation(self) -> winrt.windows.foundation.Point: ...
    @char_translation.setter
    def char_translation(self, value: winrt.windows.foundation.Point) -> None: ...

@typing.final
class NonClientCaptionTappedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> NonClientCaptionTappedEventArgs: ...
    @_property
    def point(self) -> winrt.windows.foundation.Point: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...

@typing.final
class NonClientPointerEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> NonClientPointerEventArgs: ...
    @_property
    def is_point_in_region(self) -> bool: ...
    @_property
    def point(self) -> winrt.windows.foundation.Point: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def region_kind(self) -> NonClientRegionKind: ...

@typing.final
class NonClientRegionsChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> NonClientRegionsChangedEventArgs: ...
    @_property
    def changed_regions(self) -> NonClientRegionKind: ...

@typing.final
class PointerEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PointerEventArgs: ...
    def get_intermediate_points(self) -> typing.Optional[winrt.windows.foundation.collections.IVector[PointerPoint]]: ...
    def get_intermediate_transformed_points(self, transform: typing.Optional[IPointerPointTransform], /) -> typing.Optional[winrt.windows.foundation.collections.IVector[PointerPoint]]: ...
    @_property
    def handled(self) -> bool: ...
    @handled.setter
    def handled(self, value: bool) -> None: ...
    @_property
    def current_point(self) -> typing.Optional[PointerPoint]: ...
    @_property
    def key_modifiers(self) -> winrt.windows.system.VirtualKeyModifiers: ...

@typing.final
class PointerPoint(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PointerPoint: ...
    def get_transformed_point(self, transform: typing.Optional[IPointerPointTransform], /) -> typing.Optional[PointerPoint]: ...
    @_property
    def frame_id(self) -> winrt.system.UInt32: ...
    @_property
    def is_in_contact(self) -> bool: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def pointer_id(self) -> winrt.system.UInt32: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...
    @_property
    def properties(self) -> typing.Optional[PointerPointProperties]: ...
    @_property
    def timestamp(self) -> winrt.system.UInt64: ...

@typing.final
class PointerPointProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PointerPointProperties: ...
    @_property
    def contact_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def is_barrel_button_pressed(self) -> bool: ...
    @_property
    def is_canceled(self) -> bool: ...
    @_property
    def is_eraser(self) -> bool: ...
    @_property
    def is_horizontal_mouse_wheel(self) -> bool: ...
    @_property
    def is_in_range(self) -> bool: ...
    @_property
    def is_inverted(self) -> bool: ...
    @_property
    def is_left_button_pressed(self) -> bool: ...
    @_property
    def is_middle_button_pressed(self) -> bool: ...
    @_property
    def is_primary(self) -> bool: ...
    @_property
    def is_right_button_pressed(self) -> bool: ...
    @_property
    def is_x_button1_pressed(self) -> bool: ...
    @_property
    def is_x_button2_pressed(self) -> bool: ...
    @_property
    def mouse_wheel_delta(self) -> winrt.system.Int32: ...
    @_property
    def orientation(self) -> winrt.system.Single: ...
    @_property
    def pointer_update_kind(self) -> PointerUpdateKind: ...
    @_property
    def pressure(self) -> winrt.system.Single: ...
    @_property
    def touch_confidence(self) -> bool: ...
    @_property
    def twist(self) -> winrt.system.Single: ...
    @_property
    def x_tilt(self) -> winrt.system.Single: ...
    @_property
    def y_tilt(self) -> winrt.system.Single: ...

@typing.final
class PointerPredictor_Static(type):
    def create_for_input_pointer_source(cls, input_pointer_source: typing.Optional[InputPointerSource], /) -> typing.Optional[PointerPredictor]: ...

@typing.final
class PointerPredictor(winrt.system.Object, metaclass=PointerPredictor_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PointerPredictor: ...
    def close(self) -> None: ...
    def get_predicted_points(self, point: typing.Optional[PointerPoint], /) -> typing.Optional[PointerPoint]: ...
    @_property
    def prediction_time(self) -> datetime.timedelta: ...
    @prediction_time.setter
    def prediction_time(self, value: datetime.timedelta) -> None: ...

@typing.final
class RightTappedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RightTappedEventArgs: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...

@typing.final
class TappedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TappedEventArgs: ...
    @_property
    def pointer_device_type(self) -> PointerDeviceType: ...
    @_property
    def position(self) -> winrt.windows.foundation.Point: ...
    @_property
    def tap_count(self) -> winrt.system.UInt32: ...

@typing.final
class IPointerPointTransform(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IPointerPointTransform: ...
    def try_transform(self, in_point: winrt.windows.foundation.Point, /) -> typing.Tuple[bool, winrt.windows.foundation.Point]: ...
    def try_transform_bounds(self, in_rect: winrt.windows.foundation.Rect, /) -> typing.Tuple[bool, winrt.windows.foundation.Rect]: ...
    @_property
    def inverse(self) -> typing.Optional[IPointerPointTransform]: ...
