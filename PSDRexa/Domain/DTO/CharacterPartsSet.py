from Domain.Psd.PsdMeta import PsdMeta
from Domain.Psd.PsdTop import PsdTop


class CharacterPartsSet:
    def __init__(self, group_name):
        self._group_name = group_name

    @property
    def group_name(self):
        return self._group_name

    def get_object_from_psdtop(self, psd_top: PsdTop):
        return psd_top.find_layer_by_id(self._group_name)

    def get_child_object_list_from_psdtop(self, psd_top: PsdTop):
        image_list = psd_top.image_layer_list
        parent = self.get_object_from_psdtop(psd_top)
        ret_list = [n for n in image_list if n.parent is parent]
        return ret_list

    def get_parent_folder_path(self, psd_meta: PsdMeta):
        return f"{psd_meta.file_name}_{self._group_name}"
