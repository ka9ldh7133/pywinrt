# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from . import _winrt_windows_ui_xaml_controls_primitives

class AnimationDirection(enum.IntEnum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3

class ComponentResourceLocation(enum.IntEnum):
    APPLICATION = 0
    NESTED = 1

class EdgeTransitionLocation(enum.IntEnum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3

class FlyoutPlacementMode(enum.IntEnum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3
    FULL = 4
    TOP_EDGE_ALIGNED_LEFT = 5
    TOP_EDGE_ALIGNED_RIGHT = 6
    BOTTOM_EDGE_ALIGNED_LEFT = 7
    BOTTOM_EDGE_ALIGNED_RIGHT = 8
    LEFT_EDGE_ALIGNED_TOP = 9
    LEFT_EDGE_ALIGNED_BOTTOM = 10
    RIGHT_EDGE_ALIGNED_TOP = 11
    RIGHT_EDGE_ALIGNED_BOTTOM = 12
    AUTO = 13

class FlyoutShowMode(enum.IntEnum):
    AUTO = 0
    STANDARD = 1
    TRANSIENT = 2
    TRANSIENT_WITH_DISMISS_ON_POINTER_MOVE_AWAY = 3

class GeneratorDirection(enum.IntEnum):
    FORWARD = 0
    BACKWARD = 1

class GroupHeaderPlacement(enum.IntEnum):
    TOP = 0
    LEFT = 1

class ListViewItemPresenterCheckMode(enum.IntEnum):
    INLINE = 0
    OVERLAY = 1

class ListViewItemPresenterSelectionIndicatorMode(enum.IntEnum):
    INLINE = 0
    OVERLAY = 1

class PlacementMode(enum.IntEnum):
    BOTTOM = 2
    LEFT = 9
    MOUSE = 7
    RIGHT = 4
    TOP = 10

class PopupPlacementMode(enum.IntEnum):
    AUTO = 0
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4
    TOP_EDGE_ALIGNED_LEFT = 5
    TOP_EDGE_ALIGNED_RIGHT = 6
    BOTTOM_EDGE_ALIGNED_LEFT = 7
    BOTTOM_EDGE_ALIGNED_RIGHT = 8
    LEFT_EDGE_ALIGNED_TOP = 9
    LEFT_EDGE_ALIGNED_BOTTOM = 10
    RIGHT_EDGE_ALIGNED_TOP = 11
    RIGHT_EDGE_ALIGNED_BOTTOM = 12

class ScrollEventType(enum.IntEnum):
    SMALL_DECREMENT = 0
    SMALL_INCREMENT = 1
    LARGE_DECREMENT = 2
    LARGE_INCREMENT = 3
    THUMB_POSITION = 4
    THUMB_TRACK = 5
    FIRST = 6
    LAST = 7
    END_SCROLL = 8

class ScrollingIndicatorMode(enum.IntEnum):
    NONE = 0
    TOUCH_INDICATOR = 1
    MOUSE_INDICATOR = 2

class SliderSnapsTo(enum.IntEnum):
    STEP_VALUES = 0
    TICKS = 1

class SnapPointsAlignment(enum.IntEnum):
    NEAR = 0
    CENTER = 1
    FAR = 2

class TickPlacement(enum.IntEnum):
    NONE = 0
    TOP_LEFT = 1
    BOTTOM_RIGHT = 2
    OUTSIDE = 3
    INLINE = 4

GeneratorPosition = _winrt_windows_ui_xaml_controls_primitives.GeneratorPosition
AppBarButtonTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.AppBarButtonTemplateSettings
AppBarTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.AppBarTemplateSettings
AppBarToggleButtonTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.AppBarToggleButtonTemplateSettings
ButtonBase = _winrt_windows_ui_xaml_controls_primitives.ButtonBase
CalendarPanel = _winrt_windows_ui_xaml_controls_primitives.CalendarPanel
CalendarViewTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.CalendarViewTemplateSettings
CarouselPanel = _winrt_windows_ui_xaml_controls_primitives.CarouselPanel
ColorPickerSlider = _winrt_windows_ui_xaml_controls_primitives.ColorPickerSlider
ColorSpectrum = _winrt_windows_ui_xaml_controls_primitives.ColorSpectrum
ComboBoxTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.ComboBoxTemplateSettings
CommandBarFlyoutCommandBar = _winrt_windows_ui_xaml_controls_primitives.CommandBarFlyoutCommandBar
CommandBarFlyoutCommandBarTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.CommandBarFlyoutCommandBarTemplateSettings
CommandBarTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.CommandBarTemplateSettings
DragCompletedEventArgs = _winrt_windows_ui_xaml_controls_primitives.DragCompletedEventArgs
DragDeltaEventArgs = _winrt_windows_ui_xaml_controls_primitives.DragDeltaEventArgs
DragStartedEventArgs = _winrt_windows_ui_xaml_controls_primitives.DragStartedEventArgs
FlyoutBase = _winrt_windows_ui_xaml_controls_primitives.FlyoutBase
FlyoutBaseClosingEventArgs = _winrt_windows_ui_xaml_controls_primitives.FlyoutBaseClosingEventArgs
FlyoutShowOptions = _winrt_windows_ui_xaml_controls_primitives.FlyoutShowOptions
GeneratorPositionHelper = _winrt_windows_ui_xaml_controls_primitives.GeneratorPositionHelper
GridViewItemPresenter = _winrt_windows_ui_xaml_controls_primitives.GridViewItemPresenter
GridViewItemTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.GridViewItemTemplateSettings
ItemsChangedEventArgs = _winrt_windows_ui_xaml_controls_primitives.ItemsChangedEventArgs
JumpListItemBackgroundConverter = _winrt_windows_ui_xaml_controls_primitives.JumpListItemBackgroundConverter
JumpListItemForegroundConverter = _winrt_windows_ui_xaml_controls_primitives.JumpListItemForegroundConverter
LayoutInformation = _winrt_windows_ui_xaml_controls_primitives.LayoutInformation
ListViewItemPresenter = _winrt_windows_ui_xaml_controls_primitives.ListViewItemPresenter
ListViewItemTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.ListViewItemTemplateSettings
LoopingSelector = _winrt_windows_ui_xaml_controls_primitives.LoopingSelector
LoopingSelectorItem = _winrt_windows_ui_xaml_controls_primitives.LoopingSelectorItem
LoopingSelectorPanel = _winrt_windows_ui_xaml_controls_primitives.LoopingSelectorPanel
MenuFlyoutItemTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.MenuFlyoutItemTemplateSettings
MenuFlyoutPresenterTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.MenuFlyoutPresenterTemplateSettings
NavigationViewItemPresenter = _winrt_windows_ui_xaml_controls_primitives.NavigationViewItemPresenter
OrientedVirtualizingPanel = _winrt_windows_ui_xaml_controls_primitives.OrientedVirtualizingPanel
PickerFlyoutBase = _winrt_windows_ui_xaml_controls_primitives.PickerFlyoutBase
PivotHeaderItem = _winrt_windows_ui_xaml_controls_primitives.PivotHeaderItem
PivotHeaderPanel = _winrt_windows_ui_xaml_controls_primitives.PivotHeaderPanel
PivotPanel = _winrt_windows_ui_xaml_controls_primitives.PivotPanel
Popup = _winrt_windows_ui_xaml_controls_primitives.Popup
ProgressBarTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.ProgressBarTemplateSettings
ProgressRingTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.ProgressRingTemplateSettings
RangeBase = _winrt_windows_ui_xaml_controls_primitives.RangeBase
RangeBaseValueChangedEventArgs = _winrt_windows_ui_xaml_controls_primitives.RangeBaseValueChangedEventArgs
RepeatButton = _winrt_windows_ui_xaml_controls_primitives.RepeatButton
ScrollBar = _winrt_windows_ui_xaml_controls_primitives.ScrollBar
ScrollEventArgs = _winrt_windows_ui_xaml_controls_primitives.ScrollEventArgs
Selector = _winrt_windows_ui_xaml_controls_primitives.Selector
SelectorItem = _winrt_windows_ui_xaml_controls_primitives.SelectorItem
SettingsFlyoutTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.SettingsFlyoutTemplateSettings
SplitViewTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.SplitViewTemplateSettings
Thumb = _winrt_windows_ui_xaml_controls_primitives.Thumb
TickBar = _winrt_windows_ui_xaml_controls_primitives.TickBar
ToggleButton = _winrt_windows_ui_xaml_controls_primitives.ToggleButton
ToggleSwitchTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.ToggleSwitchTemplateSettings
ToolTipTemplateSettings = _winrt_windows_ui_xaml_controls_primitives.ToolTipTemplateSettings
IScrollSnapPointsInfo = _winrt_windows_ui_xaml_controls_primitives.IScrollSnapPointsInfo