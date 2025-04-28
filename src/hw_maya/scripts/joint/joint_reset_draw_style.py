# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

from maya import cmds


def main() -> None:
    for jnt in cmds.ls(selection=True, type="joint"):
        cmds.setAttr(f"{jnt}.drawStyle", 0)
        cmds.setAttr(f"{jnt}.radius", 1.5)


if __name__ == "__main__":
    main()
