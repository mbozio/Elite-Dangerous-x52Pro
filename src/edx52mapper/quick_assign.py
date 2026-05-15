"""Smart assignment helpers for common Elite Dangerous directional commands."""

from __future__ import annotations

from dataclasses import dataclass

from edx52mapper.binds import BindsProfile
from edx52mapper.hotas import HAT_DIRECTIONS, HotasControl, find_control


@dataclass(frozen=True)
class DirectionalAssignment:
    """One direction-to-action assignment preview item."""

    direction: str
    action: str
    device: str
    key: str


DIRECTION_TO_POV_KEY: dict[str, str] = {
    "up": "Joy_POV1Up",
    "right": "Joy_POV1Right",
    "down": "Joy_POV1Down",
    "left": "Joy_POV1Left",
}


LOOK_AROUND_ACTIONS: dict[str, str] = {
    "up": "HeadLookPitchUp",
    "right": "HeadLookYawRight",
    "down": "HeadLookPitchDown",
    "left": "HeadLookYawLeft",
}


VERTICAL_THRUST_ACTIONS: dict[str, str] = {
    "up": "VerticalThrustersButton",
    "down": "VerticalThrustersButton_Landing",
}


def preview_hat_assignment(hat_identifier: str, actions_by_direction: dict[str, str]) -> tuple[DirectionalAssignment, ...]:
    """Build a safe preview for assigning a hat to directional actions."""

    hat = find_control(hat_identifier)
    _ensure_hat(hat)
    assignments: list[DirectionalAssignment] = []
    for direction in HAT_DIRECTIONS:
        action = actions_by_direction.get(direction)
        if action:
            assignments.append(
                DirectionalAssignment(
                    direction=direction,
                    action=action,
                    device="Logitech X52 Pro",
                    key=_pov_key(hat, direction),
                )
            )
    return tuple(assignments)


def apply_hat_assignment(
    profile: BindsProfile,
    hat_identifier: str,
    actions_by_direction: dict[str, str],
) -> tuple[DirectionalAssignment, ...]:
    """Apply a directional hat assignment and return the applied preview."""

    assignments = preview_hat_assignment(hat_identifier, actions_by_direction)
    for assignment in assignments:
        profile.set_primary_button(assignment.action, assignment.device, assignment.key)
    return assignments


def _ensure_hat(control: HotasControl) -> None:
    if not control.directions:
        raise ValueError(f"{control.identifier} is not a directional hat")


def _pov_key(hat: HotasControl, direction: str) -> str:
    suffix = DIRECTION_TO_POV_KEY[direction].removeprefix("Joy_POV1")
    return f"{hat.device_token}{suffix}"
