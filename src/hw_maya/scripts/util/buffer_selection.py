# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Create a buffer group for selected objects."""

from maya import cmds


def main() -> None:
    selection = cmds.ls(selection=True)

    for obj in selection:
        buffer = f"{obj}_buffer"
        obj_parent: list[str] | None = cmds.listRelatives(obj, parent=True)

        # stubs are wrong, listRelatives returns None if it can't find a parent...
        if obj_parent is not None:  # pyright: ignore[reportUnnecessaryComparison]
            cmds.group(empty=True, name=buffer, parent=obj_parent[0])
        else:
            cmds.group(empty=True, name=buffer)  # pyright: ignore[reportUnreachable]

        cmds.matchTransform(buffer, obj, position=True, rotation=True, scale=False)
        cmds.parent(obj, buffer)


if __name__ == "__main__":
    main()
