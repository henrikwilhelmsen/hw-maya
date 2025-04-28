# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

from maya import cmds
from maya.api import OpenMaya as om  # noqa: N813


def get_dag_path(obj: str) -> om.MDagPath:
    """Get the dag path from an object name."""
    selection_list = om.MSelectionList()

    try:
        selection_list.add(obj)
        dag_path: om.MDagPath = selection_list.getDagPath(0)
    except RuntimeError:
        cmds.error(f"Failed to get dag path for object with name: '{obj}'")

    #                  pyright doesn't know that cmds.error will terminate
    return dag_path  # pyright:ignore[reportPossiblyUnboundVariable]
