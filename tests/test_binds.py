from edx52mapper.binds import BindsProfile


SAMPLE_BINDS = """<Root PresetName="Test X52" MajorVersion="4" MinorVersion="0">
    <HeadLookPitchUp>
        <Primary Device="Keyboard" Key="Key_W" />
    </HeadLookPitchUp>
</Root>"""


def test_parse_existing_binding() -> None:
    profile = BindsProfile.from_xml(SAMPLE_BINDS)

    assert profile.preset_name == "Test X52"
    assert profile.bindings()[0].action == "HeadLookPitchUp"
    assert profile.bindings()[0].slots[0].key == "Key_W"


def test_set_primary_button_creates_missing_action() -> None:
    profile = BindsProfile.from_xml(SAMPLE_BINDS)

    profile.set_primary_button("HeadLookYawRight", "Logitech X52 Pro", "Joy_POV1Right")

    actions = {binding.action: binding for binding in profile.bindings()}
    assert actions["HeadLookYawRight"].slots[0].device == "Logitech X52 Pro"
    assert actions["HeadLookYawRight"].slots[0].key == "Joy_POV1Right"
