# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.enumeration
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.ui
import winrt.windows.ui.core
import winrt.windows.ui.popups
import winrt.windows.ui.windowmanagement

from winrt.windows.ui.viewmanagement import ApplicationViewBoundsMode, ApplicationViewMode, ApplicationViewOrientation, ApplicationViewState, ApplicationViewSwitchingOptions, ApplicationViewWindowingMode, FullScreenSystemOverlayMode, HandPreference, ScreenCaptureDisabledBehavior, UIColorType, UIElementType, UserInteractionMode, ViewSizePreference

Self = typing.TypeVar('Self')

class AccessibilitySettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AccessibilitySettings: ...
    def __new__(cls: typing.Type[AccessibilitySettings]) -> AccessibilitySettings:...
    def add_high_contrast_changed(self, handler: winrt.windows.foundation.TypedEventHandler[AccessibilitySettings, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_high_contrast_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def high_contrast(self) -> bool: ...
    @_property
    def high_contrast_scheme(self) -> str: ...

class ActivationViewSwitcher(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ActivationViewSwitcher: ...
    def is_view_presented_on_activation_virtual_desktop(self, view_id: winrt.system.Int32, /) -> bool: ...
    @typing.overload
    def show_as_standalone_async(self, view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def show_as_standalone_async(self, view_id: winrt.system.Int32, size_preference: ViewSizePreference, /) -> winrt.windows.foundation.IAsyncAction: ...

class ApplicationView_Static(type):
    def clear_all_persisted_state(cls) -> None: ...
    def clear_persisted_state(cls, key: str, /) -> None: ...
    def get_application_view_id_for_window(cls, window: typing.Optional[winrt.windows.ui.core.ICoreWindow], /) -> winrt.system.Int32: ...
    def get_for_current_view(cls) -> typing.Optional[ApplicationView]: ...
    def try_unsnap(cls) -> bool: ...
    def try_unsnap_to_fullscreen(cls) -> bool: ...
    @_property
    def value(cls) -> ApplicationViewState: ...
    @_property
    def terminate_app_on_final_view_close(cls) -> bool: ...
    @terminate_app_on_final_view_close.setter
    def terminate_app_on_final_view_close(cls, value: bool) -> None: ...
    @_property
    def preferred_launch_windowing_mode(cls) -> ApplicationViewWindowingMode: ...
    @preferred_launch_windowing_mode.setter
    def preferred_launch_windowing_mode(cls, value: ApplicationViewWindowingMode) -> None: ...
    @_property
    def preferred_launch_view_size(cls) -> winrt.windows.foundation.Size: ...
    @preferred_launch_view_size.setter
    def preferred_launch_view_size(cls, value: winrt.windows.foundation.Size) -> None: ...

class ApplicationView(winrt.system.Object, metaclass=ApplicationView_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ApplicationView: ...
    def exit_full_screen_mode(self) -> None: ...
    def get_display_regions(self) -> typing.Optional[winrt.windows.foundation.collections.IVectorView[winrt.windows.ui.windowmanagement.DisplayRegion]]: ...
    def is_view_mode_supported(self, view_mode: ApplicationViewMode, /) -> bool: ...
    def set_desired_bounds_mode(self, bounds_mode: ApplicationViewBoundsMode, /) -> bool: ...
    def set_preferred_min_size(self, min_size: winrt.windows.foundation.Size, /) -> None: ...
    def show_standard_system_overlays(self) -> None: ...
    def try_consolidate_async(self) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    def try_enter_full_screen_mode(self) -> bool: ...
    @typing.overload
    def try_enter_view_mode_async(self, view_mode: ApplicationViewMode, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_enter_view_mode_async(self, view_mode: ApplicationViewMode, view_mode_preferences: typing.Optional[ViewModePreferences], /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    def try_resize_view(self, value: winrt.windows.foundation.Size, /) -> bool: ...
    def add_consolidated(self, handler: winrt.windows.foundation.TypedEventHandler[ApplicationView, ApplicationViewConsolidatedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_consolidated(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_visible_bounds_changed(self, handler: winrt.windows.foundation.TypedEventHandler[ApplicationView, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_visible_bounds_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def is_screen_capture_enabled(self) -> bool: ...
    @is_screen_capture_enabled.setter
    def is_screen_capture_enabled(self, value: bool) -> None: ...
    @_property
    def adjacent_to_left_display_edge(self) -> bool: ...
    @_property
    def adjacent_to_right_display_edge(self) -> bool: ...
    @_property
    def id(self) -> winrt.system.Int32: ...
    @_property
    def is_full_screen(self) -> bool: ...
    @_property
    def is_on_lock_screen(self) -> bool: ...
    @_property
    def orientation(self) -> ApplicationViewOrientation: ...
    @_property
    def suppress_system_overlays(self) -> bool: ...
    @suppress_system_overlays.setter
    def suppress_system_overlays(self, value: bool) -> None: ...
    @_property
    def visible_bounds(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def desired_bounds_mode(self) -> ApplicationViewBoundsMode: ...
    @_property
    def full_screen_system_overlay_mode(self) -> FullScreenSystemOverlayMode: ...
    @full_screen_system_overlay_mode.setter
    def full_screen_system_overlay_mode(self, value: FullScreenSystemOverlayMode) -> None: ...
    @_property
    def title_bar(self) -> typing.Optional[ApplicationViewTitleBar]: ...
    @_property
    def is_full_screen_mode(self) -> bool: ...
    @_property
    def view_mode(self) -> ApplicationViewMode: ...
    @_property
    def persisted_state_id(self) -> str: ...
    @persisted_state_id.setter
    def persisted_state_id(self, value: str) -> None: ...
    @_property
    def windowing_environment(self) -> typing.Optional[winrt.windows.ui.windowmanagement.WindowingEnvironment]: ...
    @_property
    def u_i_context(self) -> typing.Optional[winrt.windows.ui.UIContext]: ...

class ApplicationViewConsolidatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ApplicationViewConsolidatedEventArgs: ...
    @_property
    def is_user_initiated(self) -> bool: ...
    @_property
    def is_app_initiated(self) -> bool: ...

class ApplicationViewScaling_Static(type):
    def try_set_disable_layout_scaling(cls, disable_layout_scaling: bool, /) -> bool: ...
    @_property
    def disable_layout_scaling(cls) -> bool: ...

class ApplicationViewScaling(winrt.system.Object, metaclass=ApplicationViewScaling_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ApplicationViewScaling: ...

class ApplicationViewSwitcher_Static(type):
    def disable_showing_main_view_on_activation(cls) -> None: ...
    def disable_system_view_activation_policy(cls) -> None: ...
    def prepare_for_custom_animated_switch_async(cls, to_view_id: winrt.system.Int32, from_view_id: winrt.system.Int32, options: ApplicationViewSwitchingOptions, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def switch_async(cls, view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def switch_async(cls, to_view_id: winrt.system.Int32, from_view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def switch_async(cls, to_view_id: winrt.system.Int32, from_view_id: winrt.system.Int32, options: ApplicationViewSwitchingOptions, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def try_show_as_standalone_async(cls, view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_show_as_standalone_async(cls, view_id: winrt.system.Int32, size_preference: ViewSizePreference, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_show_as_standalone_async(cls, view_id: winrt.system.Int32, size_preference: ViewSizePreference, anchor_view_id: winrt.system.Int32, anchor_size_preference: ViewSizePreference, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_show_as_view_mode_async(cls, view_id: winrt.system.Int32, view_mode: ApplicationViewMode, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_show_as_view_mode_async(cls, view_id: winrt.system.Int32, view_mode: ApplicationViewMode, view_mode_preferences: typing.Optional[ViewModePreferences], /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...

class ApplicationViewSwitcher(winrt.system.Object, metaclass=ApplicationViewSwitcher_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ApplicationViewSwitcher: ...

class ApplicationViewTitleBar(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ApplicationViewTitleBar: ...
    @_property
    def inactive_foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @inactive_foreground_color.setter
    def inactive_foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def inactive_background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @inactive_background_color.setter
    def inactive_background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @foreground_color.setter
    def foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_pressed_foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_pressed_foreground_color.setter
    def button_pressed_foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_pressed_background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_pressed_background_color.setter
    def button_pressed_background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_inactive_foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_inactive_foreground_color.setter
    def button_inactive_foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_inactive_background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_inactive_background_color.setter
    def button_inactive_background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_hover_foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_hover_foreground_color.setter
    def button_hover_foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_hover_background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_hover_background_color.setter
    def button_hover_background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_foreground_color.setter
    def button_foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def button_background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @button_background_color.setter
    def button_background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @background_color.setter
    def background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...

class ApplicationViewTransferContext_Static(type):
    @_property
    def data_package_format_id(cls) -> str: ...

class ApplicationViewTransferContext(winrt.system.Object, metaclass=ApplicationViewTransferContext_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ApplicationViewTransferContext: ...
    def __new__(cls: typing.Type[ApplicationViewTransferContext]) -> ApplicationViewTransferContext:...
    @_property
    def view_id(self) -> winrt.system.Int32: ...
    @view_id.setter
    def view_id(self, value: winrt.system.Int32) -> None: ...

class InputPane_Static(type):
    def get_for_current_view(cls) -> typing.Optional[InputPane]: ...
    def get_for_u_i_context(cls, context: typing.Optional[winrt.windows.ui.UIContext], /) -> typing.Optional[InputPane]: ...

class InputPane(winrt.system.Object, metaclass=InputPane_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputPane: ...
    def try_hide(self) -> bool: ...
    def try_show(self) -> bool: ...
    def add_hiding(self, handler: winrt.windows.foundation.TypedEventHandler[InputPane, InputPaneVisibilityEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_hiding(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_showing(self, handler: winrt.windows.foundation.TypedEventHandler[InputPane, InputPaneVisibilityEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_showing(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def occluded_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def visible(self) -> bool: ...
    @visible.setter
    def visible(self, value: bool) -> None: ...

class InputPaneVisibilityEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InputPaneVisibilityEventArgs: ...
    @_property
    def ensured_focused_element_in_view(self) -> bool: ...
    @ensured_focused_element_in_view.setter
    def ensured_focused_element_in_view(self, value: bool) -> None: ...
    @_property
    def occluded_rect(self) -> winrt.windows.foundation.Rect: ...

class ProjectionManager_Static(type):
    def get_device_selector(cls) -> str: ...
    @typing.overload
    def request_start_projecting_async(cls, projection_view_id: winrt.system.Int32, anchor_view_id: winrt.system.Int32, selection: winrt.windows.foundation.Rect, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def request_start_projecting_async(cls, projection_view_id: winrt.system.Int32, anchor_view_id: winrt.system.Int32, selection: winrt.windows.foundation.Rect, preffered_placement: winrt.windows.ui.popups.Placement, /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def start_projecting_async(cls, projection_view_id: winrt.system.Int32, anchor_view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def start_projecting_async(cls, projection_view_id: winrt.system.Int32, anchor_view_id: winrt.system.Int32, display_device_info: typing.Optional[winrt.windows.devices.enumeration.DeviceInformation], /) -> winrt.windows.foundation.IAsyncAction: ...
    def stop_projecting_async(cls, projection_view_id: winrt.system.Int32, anchor_view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncAction: ...
    def swap_displays_for_views_async(cls, projection_view_id: winrt.system.Int32, anchor_view_id: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncAction: ...
    def add_projection_display_available_changed(cls, handler: winrt.windows.foundation.EventHandler[winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_projection_display_available_changed(cls, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def projection_display_available(cls) -> bool: ...

class ProjectionManager(winrt.system.Object, metaclass=ProjectionManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ProjectionManager: ...

class StatusBar_Static(type):
    def get_for_current_view(cls) -> typing.Optional[StatusBar]: ...

class StatusBar(winrt.system.Object, metaclass=StatusBar_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StatusBar: ...
    def hide_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def show_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def add_hiding(self, event_handler: winrt.windows.foundation.TypedEventHandler[StatusBar, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_hiding(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_showing(self, event_handler: winrt.windows.foundation.TypedEventHandler[StatusBar, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_showing(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def foreground_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @foreground_color.setter
    def foreground_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def background_opacity(self) -> winrt.system.Double: ...
    @background_opacity.setter
    def background_opacity(self, value: winrt.system.Double) -> None: ...
    @_property
    def background_color(self) -> typing.Optional[typing.Optional[winrt.windows.ui.Color]]: ...
    @background_color.setter
    def background_color(self, value: typing.Optional[typing.Optional[winrt.windows.ui.Color]]) -> None: ...
    @_property
    def occluded_rect(self) -> winrt.windows.foundation.Rect: ...
    @_property
    def progress_indicator(self) -> typing.Optional[StatusBarProgressIndicator]: ...

class StatusBarProgressIndicator(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StatusBarProgressIndicator: ...
    def hide_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def show_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    @_property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
    @_property
    def progress_value(self) -> typing.Optional[typing.Optional[winrt.system.Double]]: ...
    @progress_value.setter
    def progress_value(self, value: typing.Optional[typing.Optional[winrt.system.Double]]) -> None: ...

class UISettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UISettings: ...
    def __new__(cls: typing.Type[UISettings]) -> UISettings:...
    def get_color_value(self, desired_color: UIColorType, /) -> winrt.windows.ui.Color: ...
    def u_i_element_color(self, desired_element: UIElementType, /) -> winrt.windows.ui.Color: ...
    def add_text_scale_factor_changed(self, handler: winrt.windows.foundation.TypedEventHandler[UISettings, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_text_scale_factor_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_color_values_changed(self, handler: winrt.windows.foundation.TypedEventHandler[UISettings, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_color_values_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_advanced_effects_enabled_changed(self, handler: winrt.windows.foundation.TypedEventHandler[UISettings, winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_advanced_effects_enabled_changed(self, cookie: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_auto_hide_scroll_bars_changed(self, handler: winrt.windows.foundation.TypedEventHandler[UISettings, UISettingsAutoHideScrollBarsChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_auto_hide_scroll_bars_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_animations_enabled_changed(self, handler: winrt.windows.foundation.TypedEventHandler[UISettings, UISettingsAnimationsEnabledChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_animations_enabled_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_message_duration_changed(self, handler: winrt.windows.foundation.TypedEventHandler[UISettings, UISettingsMessageDurationChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_message_duration_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def animations_enabled(self) -> bool: ...
    @_property
    def caret_blink_rate(self) -> winrt.system.UInt32: ...
    @_property
    def caret_browsing_enabled(self) -> bool: ...
    @_property
    def caret_width(self) -> winrt.system.UInt32: ...
    @_property
    def cursor_size(self) -> winrt.windows.foundation.Size: ...
    @_property
    def double_click_time(self) -> winrt.system.UInt32: ...
    @_property
    def hand_preference(self) -> HandPreference: ...
    @_property
    def message_duration(self) -> winrt.system.UInt32: ...
    @_property
    def mouse_hover_time(self) -> winrt.system.UInt32: ...
    @_property
    def scroll_bar_arrow_size(self) -> winrt.windows.foundation.Size: ...
    @_property
    def scroll_bar_size(self) -> winrt.windows.foundation.Size: ...
    @_property
    def scroll_bar_thumb_box_size(self) -> winrt.windows.foundation.Size: ...
    @_property
    def text_scale_factor(self) -> winrt.system.Double: ...
    @_property
    def advanced_effects_enabled(self) -> bool: ...
    @_property
    def auto_hide_scroll_bars(self) -> bool: ...

class UISettingsAnimationsEnabledChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UISettingsAnimationsEnabledChangedEventArgs: ...

class UISettingsAutoHideScrollBarsChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UISettingsAutoHideScrollBarsChangedEventArgs: ...

class UISettingsMessageDurationChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UISettingsMessageDurationChangedEventArgs: ...

class UIViewSettings_Static(type):
    def get_for_current_view(cls) -> typing.Optional[UIViewSettings]: ...

class UIViewSettings(winrt.system.Object, metaclass=UIViewSettings_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UIViewSettings: ...
    @_property
    def user_interaction_mode(self) -> UserInteractionMode: ...

class ViewModePreferences_Static(type):
    def create_default(cls, mode: ApplicationViewMode, /) -> typing.Optional[ViewModePreferences]: ...

class ViewModePreferences(winrt.system.Object, metaclass=ViewModePreferences_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ViewModePreferences: ...
    @_property
    def view_size_preference(self) -> ViewSizePreference: ...
    @view_size_preference.setter
    def view_size_preference(self, value: ViewSizePreference) -> None: ...
    @_property
    def custom_size(self) -> winrt.windows.foundation.Size: ...
    @custom_size.setter
    def custom_size(self, value: winrt.windows.foundation.Size) -> None: ...
