from Service.SettingFileService import SettingFileService, SettingKeys
from Usecase.OutputCharacterFusion import OutputCharacterFusion
from Usecase.OutputCompositedImage import OutpuCompositedImage


class OutputCharacterPresenter:
    def __init__(self):
        self._composed_usecase = OutpuCompositedImage()
        self._character_fusion_usecase = OutputCharacterFusion()

    def output_character(self):
        if SettingFileService.read_config(SettingKeys.use_fusion_template):
            self._character_fusion_usecase.execute()
        else:
            self._composed_usecase.execute()
