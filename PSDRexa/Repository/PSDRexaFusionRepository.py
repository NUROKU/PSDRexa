import os
from pathlib import Path

from DataStore.CharacterFusionDataStore import CharacterFusionDataStore
from DataStore.ResolveBinDatastore import ResolveBinDatastore
from Domain.DTO.CharacterPartsSet import CharacterPartsSet
from Domain.DTO.CompositedImage import CompositedImage
from Domain.Psd.PsdMeta import PsdMeta
from Service.SettingFileService import SettingFileService, SettingKeys


class PSDRexaFusionRepository:
    def __init__(self):
        self._character_datastore = CharacterFusionDataStore()
        self._resolve_bin_datastore = ResolveBinDatastore()

    def output_fusion(self, composited_image:CompositedImage,eye_parts:CharacterPartsSet,mouse_parts:CharacterPartsSet,psdmeta: PsdMeta):

        sotai = ""
        mepachi_open = ""
        mepachi_close = ""
        kuchipaku_open = ""
        kuchipaku_close = ""

        save_path_folder = Path(SettingFileService.read_config(SettingKeys.image_output_folder))
        sotai = save_path_folder.joinpath(composited_image.id_with_extension(extension="png"))

        # TODO アルゴリズムもへったくれもないけど私は絶体に凝らない
        save_path_folder = Path(SettingFileService.read_config(SettingKeys.image_output_folder))
        sotai = save_path_folder.joinpath(composited_image.id_with_extension(extension="png"))
        for ignore in composited_image.ignored_list:
            ignore_id = ignore["id"]
            ignore_parent_id = ignore["parent"]
            if ignore_parent_id == SettingFileService.read_config(SettingKeys.pachi_group_1):
                mepachi_open = save_path_folder / eye_parts.get_parent_folder_path(psdmeta) / f"{ignore_id}.png"
                mepachi_close = save_path_folder / eye_parts.get_parent_folder_path(psdmeta) / f"{SettingFileService.read_config(SettingKeys.pachi_image_close_1)}.png"
            if ignore_parent_id == SettingFileService.read_config(SettingKeys.pachi_group_2):
                kuchipaku_open = save_path_folder / mouse_parts.get_parent_folder_path(psdmeta) / f"{ignore_id}.png"
                kuchipaku_close = save_path_folder / mouse_parts.get_parent_folder_path(psdmeta) / f"{SettingFileService.read_config(SettingKeys.pachi_image_close_2)}.png"

        for ignore in composited_image.not_ignored_list:
            ignore_id = ignore["id"]
            ignore_parent_id = ignore["parent"]
            if ignore_parent_id == SettingFileService.read_config(SettingKeys.pachi_group_1):
                mepachi_open = save_path_folder / eye_parts.get_parent_folder_path(psdmeta) / f"{ignore_id}.png"
                mepachi_close = save_path_folder / eye_parts.get_parent_folder_path(psdmeta) / f"{ignore_id}.png"
            if ignore_parent_id == SettingFileService.read_config(SettingKeys.pachi_group_2):
                kuchipaku_open = save_path_folder / mouse_parts.get_parent_folder_path(psdmeta) / f"{ignore_id}.png"
                kuchipaku_close = save_path_folder / mouse_parts.get_parent_folder_path(psdmeta) / f"{ignore_id}.png"

        if mepachi_open == "":
            mepachi_open = SettingFileService.get_dummy_path()
        if mepachi_close == "":
            mepachi_close = SettingFileService.get_dummy_path()
        if kuchipaku_open == "":
            kuchipaku_open = SettingFileService.get_dummy_path()
        if kuchipaku_close == "":
            kuchipaku_close = SettingFileService.get_dummy_path()
        self._character_datastore.put_character_fusion(sotai=sotai,mepachi_open=mepachi_open,mepachi_close=mepachi_close,kuchipaku_open=kuchipaku_open,kuchipaku_close=kuchipaku_close)