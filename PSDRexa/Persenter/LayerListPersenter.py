from pathlib import Path
from typing import List

from Usecase.BuildLayerList import BuildLayerList


class LayerListPresenter:
    def __init__(self):
        pass

    def get_layer_list(self, psd_file_path: Path) -> List:
        build_layer_list = BuildLayerList()
        top_layer_group = build_layer_list.execute(psd_file_path)

        return top_layer_group.dump_list_for_tree()
