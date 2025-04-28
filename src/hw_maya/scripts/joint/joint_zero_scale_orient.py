# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Zero scale orient on all selected joints."""

from maya import cmds


def joint_zero_scale_orient() -> None:
    selection = cmds.ls(selection=True, type="joint")
    cmds.joint(selection, edit=True, zeroScaleOrient=True)  # pyright: ignore[reportArgumentType]


def main() -> None:
    joint_zero_scale_orient()


if __name__ == "__main__":
    main()
