from pathlib import Path

from DataStore.CharacterFusionDataStore import CharacterFusionDataStore
from DataStore.ResolveBinDatastore import ResolveBinDatastore
from Domain.DTO.CompositedImage import CompositedImage
from Service.SettingFileService import SettingFileService, SettingKeys


class CompositedImageResolveRepository:
    def __init__(self):
        self._character_datastore = CharacterFusionDataStore()
        self._resolve_bin_datastore = ResolveBinDatastore()

    def output_charactor(self, composited_image: CompositedImage):
        save_path_folder = Path(SettingFileService.read_config(SettingKeys.image_output_folder))
        save_path = save_path_folder.joinpath(composited_image.id_with_extension(extension="png"))

        added_item = self._resolve_bin_datastore.add_image_to_bin(save_path)
        # self._character_datastore.put_CharactorFusion(save_path)
