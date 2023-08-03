class InitPartsPresenter:
    def __init__(self):
        pass

    def init_parts(self, psd_file_path: Path) -> List:
        build_layer_list = BuildLayerList()
        top_layer_group = build_layer_list.execute(psd_file_path)

        return top_layer_group.dump_list_for_tree()