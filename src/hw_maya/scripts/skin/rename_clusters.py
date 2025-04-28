# Copyright (C) 2025 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Rename the skin clusters of all connected meshes to match the mesh name."""

from maya import cmds, mel

from hw_maya.constants import NG_SKIN_PREFIX, SKIN_CLUSTER_SUFFIX


def main() -> None:
    meshes = cmds.ls(selection=True, exactType="transform")

    for mesh in meshes:
        new_name = f"{mesh}{SKIN_CLUSTER_SUFFIX}"

        # Get existing skinCluster
        try:
            skin_cluster: str = mel.eval(f'findRelatedSkinCluster("{mesh}");')
        except RuntimeError:
            print("No skinCluster found for mesh '{mesh}'")
            continue

        # Skip if the name is already set
        if skin_cluster == new_name:
            print(f"Skin cluster '{skin_cluster}' is already named correctly")
            continue

        # Skip if an object with the new name already exists
        if cmds.objExists(new_name):
            cmds.warning(
                f"skinCluster '{new_name}' already exists, unable to rename {skin_cluster}",  # noqa: E501
            )
            continue

        # Rename the skinCluster
        cmds.rename(skin_cluster, new_name)
        print(f"Renamed '{skin_cluster}' to {new_name}")

        # Rename ngSkinTools skinCluster if it exists
        ng_skin_cluster = f"{NG_SKIN_PREFIX}{skin_cluster}"
        ng_new_name = f"{NG_SKIN_PREFIX}{new_name}"

        if cmds.objExists(ng_skin_cluster):
            cmds.rename(ng_skin_cluster, ng_new_name)
            print(f"Renamed '{ng_skin_cluster}' to {ng_new_name}")


if __name__ == "__main__":
    main()
