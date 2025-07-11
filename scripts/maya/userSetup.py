# Copyright (C) 2025 Henrik Wilhelmsen.  # noqa: D100, INP001
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.


from maya import cmds

cmds.evalDeferred("import hw_maya.menu;hw_maya.menu.create()")  # pyright:ignore[reportArgumentType]
