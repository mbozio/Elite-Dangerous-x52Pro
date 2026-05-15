"""Import and export helpers for Elite Dangerous `.binds` XML files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class BindingSlot:
    """Primary or secondary physical binding for one Elite Dangerous action."""

    role: str
    device: str | None
    key: str | None


@dataclass(frozen=True)
class GameBinding:
    """A parsed Elite Dangerous command binding."""

    action: str
    slots: tuple[BindingSlot, ...]
    attributes: dict[str, str]


class BindsProfile:
    """Mutable representation of a `.binds` file backed by an XML tree."""

    def __init__(self, tree: ET.ElementTree, source_path: Path | None = None) -> None:
        self.tree = tree
        self.source_path = source_path

    @classmethod
    def load(cls, path: Path | str) -> "BindsProfile":
        """Load a `.binds` XML profile from disk."""

        resolved = Path(path)
        return cls(ET.parse(resolved), resolved)

    @classmethod
    def from_xml(cls, xml_text: str) -> "BindsProfile":
        """Create a profile from an XML string, mainly for tests."""

        return cls(ET.ElementTree(ET.fromstring(xml_text)))

    @property
    def preset_name(self) -> str:
        """Return the Elite Dangerous preset name when available."""

        return self.tree.getroot().attrib.get("PresetName", "Profil sans nom")

    def bindings(self) -> tuple[GameBinding, ...]:
        """Return parsed game command bindings from the XML root children."""

        parsed: list[GameBinding] = []
        for element in self.tree.getroot():
            slots: list[BindingSlot] = []
            for role in ("Primary", "Secondary"):
                slot = element.find(role)
                if slot is not None:
                    slots.append(
                        BindingSlot(
                            role=role,
                            device=slot.attrib.get("Device"),
                            key=slot.attrib.get("Key"),
                        )
                    )
            if slots or element.attrib:
                parsed.append(
                    GameBinding(
                        action=element.tag,
                        slots=tuple(slots),
                        attributes=dict(element.attrib),
                    )
                )
        return tuple(parsed)

    def set_primary_button(self, action: str, device: str, key: str) -> None:
        """Set or create an action primary binding."""

        action_element = self._get_or_create_action(action)
        primary = action_element.find("Primary")
        if primary is None:
            primary = ET.SubElement(action_element, "Primary")
        primary.attrib["Device"] = device
        primary.attrib["Key"] = key

    def write(self, path: Path | str) -> None:
        """Write the profile as XML to *path*."""

        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        ET.indent(self.tree, space="    ")
        self.tree.write(destination, encoding="utf-8", xml_declaration=True)

    def _get_or_create_action(self, action: str) -> ET.Element:
        root = self.tree.getroot()
        existing = root.find(action)
        if existing is not None:
            return existing
        return ET.SubElement(root, action)
