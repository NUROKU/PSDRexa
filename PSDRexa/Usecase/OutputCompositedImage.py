from Domain.DTO.CompositedImage import CompositedImage
from Repository.CompositedImageRepository import CompositedImageRepository
from Repository.CompositedImageResolveRepository import CompositedImageResolveRepository
from Service.PsdMemorySaverService import PsdMemorySaverService


class OutpuCompositedImage:
    def __init__(self):
        self._composited_image_rep = CompositedImageRepository()
        self._character_repository = CompositedImageResolveRepository()

    def execute(self):
        psd = PsdMemorySaverService.get_psd()
        composited_image = CompositedImage(psd.top)

        self._composited_image_rep.save_composited_image(composited_image)
        self._character_repository.output_charactor(composited_image)
