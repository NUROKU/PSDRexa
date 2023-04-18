import time

from Common import Logger
from Domain.DTO.CompositedImage import CompositedImage
from Service.PsdMemorySaverService import PsdMemorySaverService
from module.PIL.Image import Image

logger = Logger.get_logger(__name__)


class CombineLayer:
    def __init__(self):
        pass

    def execute(self, size_x: int, size_y: int) -> Image:
        logger.debug(f"CombineLayer start at {time.time()}")
        psd = PsdMemorySaverService.get_psd()
        composited_image = CompositedImage(psd.top_layer_group, is_for_preview=True)
        return composited_image.resized_image(size_x, size_y)
