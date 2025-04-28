# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

from maya import cmds


def joint_orient_to_parent() -> None:
    # get selected joint and store it in a variable
    selected = cmds.ls(selection=True, type="joint")[0]

    # get joint child and store it in a variable
    try:
        child = cmds.listRelatives(children=True, type="joint")[0]
    except (KeyError, TypeError):
        child = None

    if child is not None:
        # unparent the child joint
        cmds.parent(child, world=True, absolute=True)

    # orient selected joint to world
    cmds.joint([selected], edit=True, oj="none", ch=True, zso=True)

    # reparent the child joint
    if child is not None:
        cmds.parent(child, selected)


def main() -> None:
    joint_orient_to_parent()


if __name__ == "__main__":
    main()
