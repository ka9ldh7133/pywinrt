# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.microsoft.ui.composition
import winrt.microsoft.ui.xaml
import winrt.microsoft.ui.xaml.media

Self = typing.TypeVar('Self')

@typing.final
class Ellipse(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Ellipse: ...
    def __new__(cls: typing.Type[Ellipse]) -> Ellipse:...

@typing.final
class Line_Static(type):
    @_property
    def x1_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def x2_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def y1_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def y2_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class Line(winrt.system.Object, metaclass=Line_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Line: ...
    def __new__(cls: typing.Type[Line]) -> Line:...
    @_property
    def y2(self) -> winrt.system.Double: ...
    @y2.setter
    def y2(self, value: winrt.system.Double) -> None: ...
    @_property
    def y1(self) -> winrt.system.Double: ...
    @y1.setter
    def y1(self, value: winrt.system.Double) -> None: ...
    @_property
    def x2(self) -> winrt.system.Double: ...
    @x2.setter
    def x2(self, value: winrt.system.Double) -> None: ...
    @_property
    def x1(self) -> winrt.system.Double: ...
    @x1.setter
    def x1(self, value: winrt.system.Double) -> None: ...

@typing.final
class Path_Static(type):
    @_property
    def data_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class Path(winrt.system.Object, metaclass=Path_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Path: ...
    def __new__(cls: typing.Type[Path]) -> Path:...
    @_property
    def data(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.Geometry]: ...
    @data.setter
    def data(self, value: typing.Optional[winrt.microsoft.ui.xaml.media.Geometry]) -> None: ...

@typing.final
class Polygon_Static(type):
    @_property
    def fill_rule_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def points_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class Polygon(winrt.system.Object, metaclass=Polygon_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Polygon: ...
    def __new__(cls: typing.Type[Polygon]) -> Polygon:...
    @_property
    def points(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.PointCollection]: ...
    @points.setter
    def points(self, value: typing.Optional[winrt.microsoft.ui.xaml.media.PointCollection]) -> None: ...
    @_property
    def fill_rule(self) -> winrt.microsoft.ui.xaml.media.FillRule: ...
    @fill_rule.setter
    def fill_rule(self, value: winrt.microsoft.ui.xaml.media.FillRule) -> None: ...

@typing.final
class Polyline_Static(type):
    @_property
    def fill_rule_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def points_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class Polyline(winrt.system.Object, metaclass=Polyline_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Polyline: ...
    def __new__(cls: typing.Type[Polyline]) -> Polyline:...
    @_property
    def points(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.PointCollection]: ...
    @points.setter
    def points(self, value: typing.Optional[winrt.microsoft.ui.xaml.media.PointCollection]) -> None: ...
    @_property
    def fill_rule(self) -> winrt.microsoft.ui.xaml.media.FillRule: ...
    @fill_rule.setter
    def fill_rule(self, value: winrt.microsoft.ui.xaml.media.FillRule) -> None: ...

@typing.final
class Rectangle_Static(type):
    @_property
    def radius_x_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def radius_y_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class Rectangle(winrt.system.Object, metaclass=Rectangle_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Rectangle: ...
    def __new__(cls: typing.Type[Rectangle]) -> Rectangle:...
    @_property
    def radius_y(self) -> winrt.system.Double: ...
    @radius_y.setter
    def radius_y(self, value: winrt.system.Double) -> None: ...
    @_property
    def radius_x(self) -> winrt.system.Double: ...
    @radius_x.setter
    def radius_x(self, value: winrt.system.Double) -> None: ...

@typing.final
class Shape_Static(type):
    @_property
    def fill_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stretch_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_dash_array_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_dash_cap_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_dash_offset_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_end_line_cap_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_line_join_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_miter_limit_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_start_line_cap_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...
    @_property
    def stroke_thickness_property(cls) -> typing.Optional[winrt.microsoft.ui.xaml.DependencyProperty]: ...

@typing.final
class Shape(winrt.system.Object, metaclass=Shape_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Shape: ...
    def get_alpha_mask(self) -> typing.Optional[winrt.microsoft.ui.composition.CompositionBrush]: ...
    @_property
    def stroke_thickness(self) -> winrt.system.Double: ...
    @stroke_thickness.setter
    def stroke_thickness(self, value: winrt.system.Double) -> None: ...
    @_property
    def stroke_start_line_cap(self) -> winrt.microsoft.ui.xaml.media.PenLineCap: ...
    @stroke_start_line_cap.setter
    def stroke_start_line_cap(self, value: winrt.microsoft.ui.xaml.media.PenLineCap) -> None: ...
    @_property
    def stroke_miter_limit(self) -> winrt.system.Double: ...
    @stroke_miter_limit.setter
    def stroke_miter_limit(self, value: winrt.system.Double) -> None: ...
    @_property
    def stroke_line_join(self) -> winrt.microsoft.ui.xaml.media.PenLineJoin: ...
    @stroke_line_join.setter
    def stroke_line_join(self, value: winrt.microsoft.ui.xaml.media.PenLineJoin) -> None: ...
    @_property
    def stroke_end_line_cap(self) -> winrt.microsoft.ui.xaml.media.PenLineCap: ...
    @stroke_end_line_cap.setter
    def stroke_end_line_cap(self, value: winrt.microsoft.ui.xaml.media.PenLineCap) -> None: ...
    @_property
    def stroke_dash_offset(self) -> winrt.system.Double: ...
    @stroke_dash_offset.setter
    def stroke_dash_offset(self, value: winrt.system.Double) -> None: ...
    @_property
    def stroke_dash_cap(self) -> winrt.microsoft.ui.xaml.media.PenLineCap: ...
    @stroke_dash_cap.setter
    def stroke_dash_cap(self, value: winrt.microsoft.ui.xaml.media.PenLineCap) -> None: ...
    @_property
    def stroke_dash_array(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.DoubleCollection]: ...
    @stroke_dash_array.setter
    def stroke_dash_array(self, value: typing.Optional[winrt.microsoft.ui.xaml.media.DoubleCollection]) -> None: ...
    @_property
    def stroke(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.Brush]: ...
    @stroke.setter
    def stroke(self, value: typing.Optional[winrt.microsoft.ui.xaml.media.Brush]) -> None: ...
    @_property
    def stretch(self) -> winrt.microsoft.ui.xaml.media.Stretch: ...
    @stretch.setter
    def stretch(self, value: winrt.microsoft.ui.xaml.media.Stretch) -> None: ...
    @_property
    def fill(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.Brush]: ...
    @fill.setter
    def fill(self, value: typing.Optional[winrt.microsoft.ui.xaml.media.Brush]) -> None: ...
    @_property
    def geometry_transform(self) -> typing.Optional[winrt.microsoft.ui.xaml.media.Transform]: ...
