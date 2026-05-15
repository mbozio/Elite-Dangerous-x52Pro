from edx52mapper.binds import BindsProfile
from edx52mapper.quick_assign import LOOK_AROUND_ACTIONS, apply_hat_assignment, preview_hat_assignment


EMPTY_BINDS = """<Root PresetName="Empty X52" MajorVersion="4" MinorVersion="0" />"""


def test_preview_hat_assignment_maps_four_directions() -> None:
    preview = preview_hat_assignment("hat_1", LOOK_AROUND_ACTIONS)

    assert [item.direction for item in preview] == ["up", "right", "down", "left"]
    assert [item.key for item in preview] == ["Joy_POV1Up", "Joy_POV1Right", "Joy_POV1Down", "Joy_POV1Left"]


def test_apply_hat_assignment_updates_profile() -> None:
    profile = BindsProfile.from_xml(EMPTY_BINDS)

    apply_hat_assignment(profile, "hat_1", LOOK_AROUND_ACTIONS)

    bindings = {binding.action: binding for binding in profile.bindings()}
    assert bindings["HeadLookPitchUp"].slots[0].key == "Joy_POV1Up"
    assert bindings["HeadLookYawLeft"].slots[0].key == "Joy_POV1Left"
