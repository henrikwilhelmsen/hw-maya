# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Toggle joint axis visibility off for all selected joints."""

from maya import cmds


def main() -> None:
    selected_joints = cmds.ls(selection=True, type="joint")

    for jnt in selected_joints:
        cmds.setAttr(jnt + ".displayLocalAxis", False)  # noqa: FBT003 # pyright:ignore[reportArgumentType]


if __name__ == "__main__":
    main()
