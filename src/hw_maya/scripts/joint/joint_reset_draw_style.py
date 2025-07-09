# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.
"""Reset the select joints' draw style and radius."""

from maya import cmds


def main() -> None:
    """Reset the select joints' draw style and radius."""
    for jnt in cmds.ls(selection=True, type="joint"):
        cmds.setAttr(f"{jnt}.drawStyle", 0)  # pyright: ignore[reportArgumentType]
        cmds.setAttr(f"{jnt}.radius", 1.5)  # pyright: ignore[reportArgumentType]


if __name__ == "__main__":
    main()
