from Domain.DTO.CompositedImage import CompositedImage
from Repository.CharacterRepository import CharacterRepository
from Repository.CompositedImageRepository import CompositedImageRepository
from Service.PsdMemorySaverService import PsdMemorySaverService


class OutputCharacter:
    def __init__(self):
        self._composited_image_rep = CompositedImageRepository()
        self._character_repository = CharacterRepository()

    def execute(self):
        psd = PsdMemorySaverService.get_psd()
        composited_image = CompositedImage(psd.top)

        self._composited_image_rep.save_composited_image(composited_image)
        self._character_repository.output_charactor(composited_image)
