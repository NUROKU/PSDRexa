import time

from Common import Logger
from Domain.DTO.CompositedImage import CompositedImage
from Service.PsdMemorySaverService import PsdMemorySaverService
from module.PIL import Image

logger = Logger.get_logger(__name__)


class CombineLayer:
    def __init__(self):
        pass

    def execute(self, size_x: int, size_y: int) -> Image:
        logger.debug(f"CombineLayer start at {time.time()}")
        psd = PsdMemorySaverService.get_psd()

        if psd is not None:
            composited_image = CompositedImage(psd.top, is_for_preview=True)
            return composited_image.resized_image(size_x, size_y)
        else:
            # dummy
            return Image.new("RGB", (1, 1), "white")
