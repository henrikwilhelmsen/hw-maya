# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Print out the name and type of every object in selection."""

from maya import cmds


def main() -> None:
    objects_and_types = cmds.ls(selection=True, showType=True)
    objects = objects_and_types[::2]
    types = objects_and_types[1::2]

    for n in range(len(objects)):
        print(f"{objects[n]}: {types[n]}")


if __name__ == "__main__":
    main()
