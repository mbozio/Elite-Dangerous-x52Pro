"""Tkinter prototype for the Elite Dangerous X52 Pro mapper."""

from __future__ import annotations

from pathlib import Path
from tkinter import filedialog, messagebox, ttk
import tkinter as tk

from edx52mapper.binds import BindsProfile
from edx52mapper.hotas import ControlKind, controls_by_kind
from edx52mapper.quick_assign import LOOK_AROUND_ACTIONS, apply_hat_assignment, preview_hat_assignment


class MapperApp(tk.Tk):
    """Small desktop UI that visualises the X52 Pro and loaded bindings."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Elite Dangerous X52 Pro Mapper")
        self.geometry("1100x700")
        self.profile: BindsProfile | None = None
        self.status = tk.StringVar(value="Aucun profil chargé")
        self._build_layout()

    def _build_layout(self) -> None:
        toolbar = ttk.Frame(self, padding=8)
        toolbar.pack(fill=tk.X)
        ttk.Button(toolbar, text="Importer .binds", command=self.import_binds).pack(side=tk.LEFT, padx=4)
        ttk.Button(toolbar, text="Exporter .binds", command=self.export_binds).pack(side=tk.LEFT, padx=4)
        ttk.Button(toolbar, text="Auto Hat 1 → vue", command=self.auto_hat_look).pack(side=tk.LEFT, padx=4)
        ttk.Label(toolbar, textvariable=self.status).pack(side=tk.RIGHT)

        body = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        body.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.visual = HotasCanvas(body)
        body.add(self.visual, weight=2)

        side = ttk.Frame(body, padding=8)
        body.add(side, weight=1)
        ttk.Label(side, text="Commandes chargées", font=("TkDefaultFont", 12, "bold")).pack(anchor=tk.W)
        self.bindings = tk.Listbox(side, height=30)
        self.bindings.pack(fill=tk.BOTH, expand=True, pady=8)
        ttk.Label(
            side,
            text=(
                "Astuce : les assistants appliquent plusieurs directions d'un hat "
                "en une seule action pour éviter les mappings incomplets."
            ),
            wraplength=320,
        ).pack(anchor=tk.W)

    def import_binds(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("Elite Dangerous binds", "*.binds"), ("XML", "*.xml"), ("Tous", "*")])
        if not path:
            return
        self.profile = BindsProfile.load(path)
        self.status.set(f"Profil chargé : {self.profile.preset_name}")
        self._refresh_bindings()

    def export_binds(self) -> None:
        if self.profile is None:
            messagebox.showwarning("Export impossible", "Importez d'abord un fichier .binds.")
            return
        default_name = f"{self.profile.preset_name}.binds".replace(" ", "_")
        path = filedialog.asksaveasfilename(defaultextension=".binds", initialfile=default_name)
        if not path:
            return
        self.profile.write(Path(path))
        self.status.set(f"Profil exporté : {path}")

    def auto_hat_look(self) -> None:
        if self.profile is None:
            messagebox.showwarning("Assignation impossible", "Importez d'abord un fichier .binds.")
            return
        preview = preview_hat_assignment("hat_1", LOOK_AROUND_ACTIONS)
        details = "\n".join(f"{item.direction} → {item.action} ({item.key})" for item in preview)
        if messagebox.askyesno("Assigner Hat 1 à la vue ?", details):
            apply_hat_assignment(self.profile, "hat_1", LOOK_AROUND_ACTIONS)
            self._refresh_bindings()
            self.status.set("Hat 1 assigné à la direction de vue")

    def _refresh_bindings(self) -> None:
        self.bindings.delete(0, tk.END)
        if self.profile is None:
            return
        for binding in self.profile.bindings():
            slot_text = ", ".join(f"{slot.role}:{slot.key or '-'}" for slot in binding.slots)
            self.bindings.insert(tk.END, f"{binding.action} — {slot_text or 'non assigné'}")


class HotasCanvas(tk.Canvas):
    """Canvas rendering sliders, buttons and hats for a readable HOTAS overview."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, background="#111827", highlightthickness=0)
        self.bind("<Configure>", lambda _event: self.draw())

    def draw(self) -> None:
        self.delete("all")
        self._title()
        self._draw_axes()
        self._draw_buttons()
        self._draw_hats()
        self._draw_modes()

    def _title(self) -> None:
        self.create_text(28, 24, anchor=tk.W, text="Logitech X52 Pro — vue de mapping", fill="#f9fafb", font=("TkDefaultFont", 16, "bold"))

    def _draw_axes(self) -> None:
        x = 40
        y = 70
        self.create_text(x, y - 24, anchor=tk.W, text="Axes", fill="#93c5fd", font=("TkDefaultFont", 12, "bold"))
        for index, axis in enumerate(controls_by_kind(ControlKind.AXIS)):
            yy = y + index * 48
            self.create_text(x, yy, anchor=tk.W, text=axis.label, fill="#e5e7eb")
            self.create_rectangle(x + 145, yy - 8, x + 390, yy + 8, outline="#6b7280", fill="#1f2937")
            self.create_rectangle(x + 145, yy - 8, x + 268, yy + 8, outline="", fill="#2563eb")
            self.create_oval(x + 260, yy - 14, x + 276, yy + 14, outline="#bfdbfe", fill="#60a5fa")

    def _draw_buttons(self) -> None:
        x = 470
        y = 70
        self.create_text(x, y - 24, anchor=tk.W, text="Boutons", fill="#86efac", font=("TkDefaultFont", 12, "bold"))
        for index, button in enumerate(controls_by_kind(ControlKind.BUTTON)):
            col = index % 2
            row = index // 2
            cx = x + col * 150
            cy = y + row * 70
            self.create_oval(cx, cy, cx + 34, cy + 34, outline="#bbf7d0", fill="#166534")
            self.create_text(cx + 44, cy + 17, anchor=tk.W, text=button.label, fill="#e5e7eb")

    def _draw_hats(self) -> None:
        x = 470
        y = 270
        self.create_text(x, y - 24, anchor=tk.W, text="Hats directionnels", fill="#fcd34d", font=("TkDefaultFont", 12, "bold"))
        for index, hat in enumerate(controls_by_kind(ControlKind.HAT)):
            cx = x + index * 185
            cy = y + 65
            self.create_text(cx, y, anchor=tk.W, text=hat.label, fill="#e5e7eb")
            self.create_polygon(cx + 35, cy - 42, cx + 55, cy - 16, cx + 15, cy - 16, fill="#92400e", outline="#fde68a")
            self.create_polygon(cx + 35, cy + 42, cx + 55, cy + 16, cx + 15, cy + 16, fill="#92400e", outline="#fde68a")
            self.create_polygon(cx - 42, cy, cx - 16, cy - 20, cx - 16, cy + 20, fill="#92400e", outline="#fde68a")
            self.create_polygon(cx + 112, cy, cx + 86, cy - 20, cx + 86, cy + 20, fill="#92400e", outline="#fde68a")
            self.create_oval(cx + 12, cy - 22, cx + 58, cy + 22, fill="#78350f", outline="#fde68a")

    def _draw_modes(self) -> None:
        x = 40
        y = 450
        self.create_text(x, y - 24, anchor=tk.W, text="Modes", fill="#c4b5fd", font=("TkDefaultFont", 12, "bold"))
        for index, mode in enumerate(controls_by_kind(ControlKind.MODE)):
            cx = x + index * 150
            self.create_rectangle(cx, y, cx + 110, y + 42, outline="#ddd6fe", fill="#4c1d95")
            self.create_text(cx + 55, y + 21, text=mode.label, fill="#f5f3ff")


def main() -> None:
    app = MapperApp()
    app.mainloop()


if __name__ == "__main__":
    main()
