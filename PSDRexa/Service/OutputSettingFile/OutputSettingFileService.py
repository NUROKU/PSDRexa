import json
import os
from enum import Enum
from os.path import abspath, dirname
from pathlib import Path

from Exception.ServiceError import ServiceError


class OutputSettingKeys(Enum):
    use_fusion_template = "use_fusion_template"
    pachi_group_1 = "pachi_group_1"
    pachi_group_2 = "pachi_group_2"
    pachi_group_3 = "pachi_group_3"
    pachi_group_4 = "pachi_group_4"
    pachi_image_close_1 = "pachi_image_close_1"
    pachi_image_close_2 = "pachi_image_close_2"
    pachi_image_close_3 = "pachi_image_close_3"
    pachi_image_close_4 = "pachi_image_close_4"


class OutputSettingFileService:
    json_path = ""
    config_dict = None

    @staticmethod
    def init_output_setting(file_name):
        file_path = str(Path(dirname(abspath(__file__)), f"{file_name}.json"))
        if not os.path.isfile(file_path):
            with open(file_path, 'w', encoding="utf-8") as json_file:
                data = {
                    "use_fusion_template": False,
                    "pachi_group_1": "",
                    "pachi_group_2": "",
                    "pachi_group_3": "",
                    "pachi_group_4": "",
                    "pachi_image_close_1": "",
                    "pachi_image_close_2": "",
                    "pachi_image_close_3": "",
                    "pachi_image_close_4": "",
                }
                json.dump(data, json_file, indent=2)
                OutputSettingFileService.config_dict = data
        else:
            with open(file_path, encoding="utf-8") as f:
                OutputSettingFileService.config_dict = json.load(f)

        OutputSettingFileService.json_path = file_path

    @staticmethod
    def get_json_path() -> str:

        return OutputSettingFileService.json_path

    @staticmethod
    def load_config():
        if OutputSettingFileService.config_dict is None:
            try:
                with open(OutputSettingFileService.get_json_path(), encoding="utf-8") as f:
                    OutputSettingFileService.config_dict = json.load(f)
                    return OutputSettingFileService.config_dict
            except FileNotFoundError:
                raise ServiceError(f"Cannot open {OutputSettingFileService.get_json_path()}")
        else:
            return OutputSettingFileService.config_dict

    @staticmethod
    def update_and_save_config(key: OutputSettingKeys, value):
        config = OutputSettingFileService.load_config()
        config[key.value] = value
        OutputSettingFileService.config_dict = config
        with open(OutputSettingFileService.json_path, 'w') as f:
            json.dump(OutputSettingFileService.config_dict, f, indent=2)

    @staticmethod
    def update_and_save_configs(config_dict: dict):
        # if len(config_dict) != len(SettingKeys):
        #     raise ServiceError("cannot update config. might be logic error")
        config = OutputSettingFileService.load_config()
        for k, v in config_dict.items():
            config[k.value] = v
        OutputSettingFileService.config_dict = config
        with open(OutputSettingFileService.get_json_path(), 'w') as f:
            json.dump(OutputSettingFileService.config_dict, f, indent=2)

    @staticmethod
    def read_config(key: OutputSettingKeys):
        return OutputSettingFileService.load_config()[key.value]

    @staticmethod
    def get_dummy_path() -> str:
        folder = dirname(abspath(__file__))
        return str(Path(folder, "../dummy.png"))
