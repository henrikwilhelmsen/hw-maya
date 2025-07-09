# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Orient the selected joint to its parent joint."""

import logging

from maya import cmds

logger = logging.getLogger(__name__)


def main() -> None:
    """Orient the selected joint to its parent."""
    # get selected joint and store it in a variable
    selection = cmds.ls(selection=True, type="joint")
    if len(selection) != 1:
        logger.error("Orient to parent only supports one selected joint at a time")
        return

    joint = selection[0]

    # get joint child and store it in a variable
    try:
        child = cmds.listRelatives(children=True, type="joint")[0]
    except (KeyError, TypeError):
        child = None

    if child is not None:
        # un-parent the child joint
        cmds.parent(child, world=True, absolute=True)

    # orient selected joint to its parent (world)
    cmds.joint(
        joint,
        edit=True,
        orientJoint="none",
        children=True,
        zeroScaleOrient=True,
    )

    # re-parent the child joint
    if child is not None:
        cmds.parent(child, joint)


if __name__ == "__main__":
    main()
