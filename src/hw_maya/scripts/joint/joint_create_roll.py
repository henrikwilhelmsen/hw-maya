# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

from maya import cmds


def joint_create_roll() -> None:
    selected_joints = cmds.ls(selection=True, type="joint")

    for jnt in selected_joints:
        # duplicate selected joint and store it in a variable 'roll_joint'
        roll_joint = cmds.duplicate(jnt, parentOnly=True, name=f"{jnt}Roll")[0]

        # parent roll_joint to world
        cmds.parent(roll_joint, absolute=True, world=True)

        # get joint child and store it in a variable
        try:
            jnt_child = cmds.listRelatives(jnt, type="joint")[0]
        except (KeyError, TypeError):
            jnt_child = None

        target = [jnt, jnt_child] if jnt_child is not None else [jnt]

        constraint_name = f"{roll_joint}TmpPointConstraint"
        cmds.pointConstraint(
            *target,
            roll_joint,
            name=constraint_name,
            maintainOffset=False,
        )

        # delete point constraint
        cmds.delete(constraint_name)

        # parent roll joint to selected, maintaining position
        cmds.parent(roll_joint, jnt)


def main() -> None:
    joint_create_roll()


if __name__ == "__main__":
    main()
