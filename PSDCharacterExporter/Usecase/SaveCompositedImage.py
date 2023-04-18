from Domain.DTO.CompositedImage import CompositedImage
from Repository.CompositedImageRepository import CompositedImageRepository
from Service.PsdMemorySaverService import PsdMemorySaverService


class SaveCompositedImage:
    def __init__(self):
        self._composited_image_rep = CompositedImageRepository()

    def execute(self):
        psd = PsdMemorySaverService.get_psd()
        composited_image = CompositedImage(psd.top_layer_group, is_for_preview=False)
        self._composited_image_rep.save_composited_image(composited_image)
