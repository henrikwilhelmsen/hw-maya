# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Match translation and rotation."""

from maya import cmds


def main() -> None:
    selection = cmds.ls(selection=True)
    cmds.matchTransform(*selection, position=True, rotation=True, scale=False)


if __name__ == "__main__":
    main()
