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
import winrt.windows.foundation.numerics

from winrt.windows.gaming.input.forcefeedback import ConditionForceEffectKind, ForceFeedbackEffectAxes, ForceFeedbackEffectState, ForceFeedbackLoadEffectResult, PeriodicForceEffectKind

Self = typing.TypeVar('Self')

class ConditionForceEffect(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ConditionForceEffect: ...
    def __new__(cls: typing.Type[ConditionForceEffect], effect_kind: ConditionForceEffectKind) -> ConditionForceEffect:...
    def set_parameters(self, direction: winrt.windows.foundation.numerics.Vector3, positive_coefficient: winrt.system.Single, negative_coefficient: winrt.system.Single, max_positive_magnitude: winrt.system.Single, max_negative_magnitude: winrt.system.Single, dead_zone: winrt.system.Single, bias: winrt.system.Single, /) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @_property
    def kind(self) -> ConditionForceEffectKind: ...
    @_property
    def gain(self) -> winrt.system.Double: ...
    @gain.setter
    def gain(self, value: winrt.system.Double) -> None: ...
    @_property
    def state(self) -> ForceFeedbackEffectState: ...

class ConstantForceEffect(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ConstantForceEffect: ...
    def __new__(cls: typing.Type[ConstantForceEffect]) -> ConstantForceEffect:...
    def set_parameters(self, vector: winrt.windows.foundation.numerics.Vector3, duration: datetime.timedelta, /) -> None: ...
    def set_parameters_with_envelope(self, vector: winrt.windows.foundation.numerics.Vector3, attack_gain: winrt.system.Single, sustain_gain: winrt.system.Single, release_gain: winrt.system.Single, start_delay: datetime.timedelta, attack_duration: datetime.timedelta, sustain_duration: datetime.timedelta, release_duration: datetime.timedelta, repeat_count: winrt.system.UInt32, /) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @_property
    def gain(self) -> winrt.system.Double: ...
    @gain.setter
    def gain(self, value: winrt.system.Double) -> None: ...
    @_property
    def state(self) -> ForceFeedbackEffectState: ...

class ForceFeedbackMotor(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ForceFeedbackMotor: ...
    def load_effect_async(self, effect: typing.Optional[IForceFeedbackEffect], /) -> winrt.windows.foundation.IAsyncOperation[ForceFeedbackLoadEffectResult]: ...
    def pause_all_effects(self) -> None: ...
    def resume_all_effects(self) -> None: ...
    def stop_all_effects(self) -> None: ...
    def try_disable_async(self) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    def try_enable_async(self) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    def try_reset_async(self) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    def try_unload_effect_async(self, effect: typing.Optional[IForceFeedbackEffect], /) -> winrt.windows.foundation.IAsyncOperation[bool]: ...
    @_property
    def master_gain(self) -> winrt.system.Double: ...
    @master_gain.setter
    def master_gain(self, value: winrt.system.Double) -> None: ...
    @_property
    def are_effects_paused(self) -> bool: ...
    @_property
    def is_enabled(self) -> bool: ...
    @_property
    def supported_axes(self) -> ForceFeedbackEffectAxes: ...

class PeriodicForceEffect(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PeriodicForceEffect: ...
    def __new__(cls: typing.Type[PeriodicForceEffect], effect_kind: PeriodicForceEffectKind) -> PeriodicForceEffect:...
    def set_parameters(self, vector: winrt.windows.foundation.numerics.Vector3, frequency: winrt.system.Single, phase: winrt.system.Single, bias: winrt.system.Single, duration: datetime.timedelta, /) -> None: ...
    def set_parameters_with_envelope(self, vector: winrt.windows.foundation.numerics.Vector3, frequency: winrt.system.Single, phase: winrt.system.Single, bias: winrt.system.Single, attack_gain: winrt.system.Single, sustain_gain: winrt.system.Single, release_gain: winrt.system.Single, start_delay: datetime.timedelta, attack_duration: datetime.timedelta, sustain_duration: datetime.timedelta, release_duration: datetime.timedelta, repeat_count: winrt.system.UInt32, /) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @_property
    def gain(self) -> winrt.system.Double: ...
    @gain.setter
    def gain(self, value: winrt.system.Double) -> None: ...
    @_property
    def state(self) -> ForceFeedbackEffectState: ...
    @_property
    def kind(self) -> PeriodicForceEffectKind: ...

class RampForceEffect(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RampForceEffect: ...
    def __new__(cls: typing.Type[RampForceEffect]) -> RampForceEffect:...
    def set_parameters(self, start_vector: winrt.windows.foundation.numerics.Vector3, end_vector: winrt.windows.foundation.numerics.Vector3, duration: datetime.timedelta, /) -> None: ...
    def set_parameters_with_envelope(self, start_vector: winrt.windows.foundation.numerics.Vector3, end_vector: winrt.windows.foundation.numerics.Vector3, attack_gain: winrt.system.Single, sustain_gain: winrt.system.Single, release_gain: winrt.system.Single, start_delay: datetime.timedelta, attack_duration: datetime.timedelta, sustain_duration: datetime.timedelta, release_duration: datetime.timedelta, repeat_count: winrt.system.UInt32, /) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @_property
    def gain(self) -> winrt.system.Double: ...
    @gain.setter
    def gain(self, value: winrt.system.Double) -> None: ...
    @_property
    def state(self) -> ForceFeedbackEffectState: ...

class IForceFeedbackEffect(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IForceFeedbackEffect: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @_property
    def gain(self) -> winrt.system.Double: ...
    @gain.setter
    def gain(self, value: winrt.system.Double) -> None: ...
    @_property
    def state(self) -> ForceFeedbackEffectState: ...
