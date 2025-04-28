# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

from maya import cmds


def main() -> None:
    cmds.select(add=True, hierarchy=True)
    selection = cmds.ls(selection=True, type="joint")
    for jnt in selection:
        rotation = (
            cmds.getAttr(f"{jnt}.rotateX", channelBox=True),
            cmds.getAttr(f"{jnt}.rotateY", channelBox=True),
            cmds.getAttr(f"{jnt}.rotateZ", channelBox=True),
        )
        if rotation != (0, 0, 0):
            cmds.warning(f"joint '{jnt}' has non-zero rotation: {rotation}")


if __name__ == "__main__":
    main()
