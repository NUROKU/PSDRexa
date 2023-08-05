from pathlib import Path

from DataStore.PartsDataStore import PartsDataStore
from Domain.DTO.CharacterPartsSet import CharacterPartsSet
from Service.PsdMemorySaverService import PsdMemorySaverService
from Service.SettingFileService import SettingFileService, SettingKeys


class PartsRepository:
    def __init__(self):
        self._parts_datastore = PartsDataStore()

    def save_parts(self, parts: CharacterPartsSet):
        psd = PsdMemorySaverService.get_psd()
        childs = parts.get_child_object_list_from_psdtop(psd.top)

        base_path = Path(SettingFileService.read_config(SettingKeys.image_output_folder))
        folder_path = base_path / f"{psd.meta.file_name}_{parts.group_name}"

        for child in childs:
            self._parts_datastore.save_parts(folder_path=folder_path,file_name=f"{child.id_name}.png",image=child.layer_image.image)

