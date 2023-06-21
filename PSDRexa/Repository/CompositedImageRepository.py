from pathlib import Path

from DataStore.CompositedImageDataStore import CompositedImageDataStore
from Domain.DTO.CompositedImage import CompositedImage
from Service.SettingFileService import SettingKeys, SettingFileService


class CompositedImageRepository:
    def __init__(self):
        self._composited_image_datastore = CompositedImageDataStore()

    def save_composited_image(self, composited_image: CompositedImage):
        save_path_folder = Path(SettingFileService.read_config(SettingKeys.image_output_folder))
        save_path = save_path_folder.joinpath(composited_image.id_with_extension(extension="png"))

        is_original = SettingFileService.read_config(SettingKeys.is_image_size_original)
        image = composited_image.image
        if not is_original:
            image = composited_image.resized_image(SettingFileService.read_config(SettingKeys.image_output_size_x),
                                                   SettingFileService.read_config(SettingKeys.image_output_size_y))

        self._composited_image_datastore.output_composited_image(image, save_path)
