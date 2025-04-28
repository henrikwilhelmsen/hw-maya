# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Script menu that loads menu items from the live_scripts directory dynamically.

Every time the menu is shown, the folder is checked and every file is imported, reloaded
and added to the menu. The main function of each script file is what's being executed
by each menu item.
"""

import importlib
from pathlib import Path
from typing import Any

from maya import cmds, mel

SCRIPTS_PKG_NAME = "hw_maya.scripts"
MENU_TITLE = "HW Scripts"
MENU_NAME = "HWScriptsMenu"
LIVE_SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"


# need the *args, **kwargs arguments since maya expects it for the postMenuCommand
def load_live_script_menu_items(*args: list[Any], **kwargs: dict[str, Any]) -> None:  # noqa: ARG001 # pyright: ignore[reportExplicitAny,reportUnusedParameter]
    """Load the menu items from the live_scripts directory."""
    script_dirs = [
        x for x in LIVE_SCRIPTS_DIR.glob("*") if x.is_dir() and x.name != "__pycache__"
    ]

    for d in script_dirs:
        module_names = [x.stem for x in d.glob("*.py") if x.stem != "__init__"]

        # Delete the menu item if it exists
        if cmds.menuItem(d.name, exists=True, query=True):
            cmds.deleteUI(d.name, menuItem=True)

        # Create a title menu entry to use as a divider
        cmds.menuItem(
            d.name,
            parent=MENU_NAME,
            divider=True,
            dividerLabel=d.name.upper(),
        )

        # Create a menu item for every module
        for module_name in module_names:
            full_name = f"{SCRIPTS_PKG_NAME}.{d.name}.{module_name}"

            # Import and reload the module
            module = importlib.import_module(full_name)
            importlib.reload(module)

            # Delete the menu item if it exists
            if cmds.menuItem(module_name, exists=True, query=True):
                cmds.deleteUI(module_name, menuItem=True)

            # Create the menu item, using the module main function as the command
            cmds.menuItem(
                module_name,
                label=module_name.replace("_", " "),
                parent=MENU_NAME,
                command=f"import {full_name};{full_name}.main()",  # pyright:ignore[reportArgumentType]
            )


def create() -> None:
    """Create the live scripts menu and attach it to the Maya main menu bar."""
    # Get the name of the Maya main window.
    main_window: str = mel.eval("$tmp = $gMainWindow;")  # type: ignore[attr-defined]

    # Delete the menu if it already exists.
    if cmds.menu(MENU_NAME, exists=True):
        cmds.deleteUI(MENU_NAME)

    # Create the menu
    cmds.menu(
        MENU_NAME,
        tearOff=True,
        parent=main_window,
        label=MENU_TITLE,
        postMenuCommand=load_live_script_menu_items,
    )


if __name__ == "__main__":
    create()
