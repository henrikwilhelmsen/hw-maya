# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Create a locator at the selected object(s)."""

from maya import cmds


def main() -> None:
    for x in cmds.ls(selection=True):
        locator = f"{x}_locator"
        cmds.spaceLocator(name=locator)
        cmds.setAttr(f"{locator}.scale", 15, 15, 15)
        cmds.matchTransform(locator, x, position=True, rotation=True, scale=False)


if __name__ == "__main__":
    main()
