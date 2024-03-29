from Domain.DTO.CharacterPartsSet import CharacterPartsSet
from Domain.DTO.CompositedImage import CompositedImage
from Repository.CompositedImageRepository import CompositedImageRepository
from Repository.PSDRexaFusionRepository import PSDRexaFusionRepository
from Service.OutputSettingFile.OutputSettingFileService import OutputSettingFileService, OutputSettingKeys
from Service.PsdMemorySaverService import PsdMemorySaverService


class OutputCharacterFusion:
    def __init__(self):
        self._composited_image_rep = CompositedImageRepository()
        self._character_repository = PSDRexaFusionRepository()

    def execute(self):
        psd = PsdMemorySaverService.get_psd()
        composited_image = CompositedImage(psd.top, ignore_group=True)
        self._composited_image_rep.save_composited_image(composited_image)

        eye_parts = CharacterPartsSet(OutputSettingFileService.read_config(OutputSettingKeys.pachi_group_1))
        mouse_parts = CharacterPartsSet(OutputSettingFileService.read_config(OutputSettingKeys.pachi_group_2))

        self._character_repository.output_fusion(composited_image, eye_parts, mouse_parts, psd.meta)
