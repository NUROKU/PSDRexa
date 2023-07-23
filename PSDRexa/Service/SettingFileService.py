import json
from enum import Enum
from os.path import abspath, dirname
from pathlib import Path

from Exception.ServiceError import ServiceError


class SettingKeys(Enum):
    image_output_folder = "image_output_folder"
    is_image_size_original = "is_image_size_original"
    image_output_size_x = "image_output_size_x"
    image_output_size_y = "image_output_size_y"
    is_image_preview_size_original = "is_image_preview_size_original"
    image_preview_size_x = "image_preview_size_x"
    image_preview_size_y = "image_preview_size_y"
    index_for_output = "index_for_output"
    use_psdtool_func = "use_psdtool_func"


class SettingFileService:
    json_path = ""
    config_dict = None

    @staticmethod
    def get_json_path() -> str:
        if SettingFileService.json_path == "":
            folder = dirname(abspath(__file__))
            SettingFileService.json_path = str(Path(folder, "settings.json"))

        return SettingFileService.json_path

    @staticmethod
    def load_config():
        if SettingFileService.config_dict is None:
            try:
                with open(SettingFileService.get_json_path(), encoding="utf-8") as f:
                    SettingFileService.config_dict = json.load(f)
                    return SettingFileService.config_dict
            except FileNotFoundError:
                raise ServiceError(f"Cannot open {SettingFileService.get_json_path()}")
        else:
            return SettingFileService.config_dict

    @staticmethod
    def update_and_save_config(key: SettingKeys, value: str):
        config = SettingFileService.load_config()
        config[key.value] = value
        SettingFileService.config_dict = config
        with open(SettingFileService.json_path, 'w') as f:
            json.dump(SettingFileService.config_dict, f, indent=2)

    @staticmethod
    def update_and_save_configs(config_dict: dict):
        # if len(config_dict) != len(SettingKeys):
        #     raise ServiceError("cannot update config. might be logic error")
        config = SettingFileService.load_config()
        for k, v in config_dict.items():
            config[k.value] = v
        SettingFileService.config_dict = config
        with open(SettingFileService.get_json_path(), 'w') as f:
            json.dump(SettingFileService.config_dict, f, indent=2)

    @staticmethod
    def read_config(key: SettingKeys):
        return SettingFileService.load_config()[key.value]
