"""Logical model of the Logitech/Saitek X52 Pro HOTAS."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class ControlKind(StrEnum):
    """Supported physical control families."""

    AXIS = "axis"
    BUTTON = "button"
    HAT = "hat"
    MODE = "mode"


@dataclass(frozen=True)
class HotasControl:
    """A physical control exposed by the X52 Pro."""

    identifier: str
    label: str
    kind: ControlKind
    device_token: str
    directions: tuple[str, ...] = ()


HAT_DIRECTIONS: tuple[str, str, str, str] = ("up", "right", "down", "left")


X52_PRO_CONTROLS: tuple[HotasControl, ...] = (
    HotasControl("stick_x", "Joystick X", ControlKind.AXIS, "Joy_XAxis"),
    HotasControl("stick_y", "Joystick Y", ControlKind.AXIS, "Joy_YAxis"),
    HotasControl("twist", "Palonnier twist", ControlKind.AXIS, "Joy_RZAxis"),
    HotasControl("throttle", "Manette des gaz", ControlKind.AXIS, "Joy_ZAxis"),
    HotasControl("rotary_1", "Rotatif 1", ControlKind.AXIS, "Joy_RXAxis"),
    HotasControl("rotary_2", "Rotatif 2", ControlKind.AXIS, "Joy_RYAxis"),
    HotasControl("slider", "Slider", ControlKind.AXIS, "Joy_SliderAxis"),
    HotasControl("trigger", "Gâchette", ControlKind.BUTTON, "Joy_1"),
    HotasControl("fire", "Bouton feu", ControlKind.BUTTON, "Joy_2"),
    HotasControl("pinkie", "Pinkie switch", ControlKind.BUTTON, "Joy_6"),
    HotasControl("clutch", "Bouton clutch", ControlKind.BUTTON, "Joy_31"),
    HotasControl("hat_1", "Hat 1 joystick", ControlKind.HAT, "Joy_POV1", HAT_DIRECTIONS),
    HotasControl("hat_2", "Hat 2 throttle", ControlKind.HAT, "Joy_POV2", HAT_DIRECTIONS),
    HotasControl("hat_3", "Mini hat", ControlKind.HAT, "Joy_POV3", HAT_DIRECTIONS),
    HotasControl("mode_1", "Mode 1", ControlKind.MODE, "Mode_1"),
    HotasControl("mode_2", "Mode 2", ControlKind.MODE, "Mode_2"),
    HotasControl("mode_3", "Mode 3", ControlKind.MODE, "Mode_3"),
)


def controls_by_kind(kind: ControlKind) -> tuple[HotasControl, ...]:
    """Return all known controls matching *kind*."""

    return tuple(control for control in X52_PRO_CONTROLS if control.kind is kind)


def find_control(identifier: str) -> HotasControl:
    """Return a control by stable identifier."""

    for control in X52_PRO_CONTROLS:
        if control.identifier == identifier:
            return control
    raise KeyError(f"Unknown X52 Pro control: {identifier}")
