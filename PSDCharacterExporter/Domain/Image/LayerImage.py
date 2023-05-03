from PIL import Image

from Common import Logger

logger = Logger.get_logger(__name__)


class LayerImage:
    def __init__(self, image: Image, preview_ratio: float, opacity: int):
        self._image = image
        self._opacity = opacity
        if self._image is None:
            pil_img = Image.new("RGBA", (1, 1), (255, 255, 255, 0))
            self._image = pil_img

        self._previewed_image = self.resized_image(int(self._image.width * preview_ratio),
                                                   int(self._image.height * preview_ratio))

    @property
    def image(self):
        return self._image

    @property
    def previewed_image(self):
        return self._previewed_image

    @property
    def opacity(self):
        return self._opacity

    def resized_image(self, size_width: int, size_height: int) -> Image:
        if size_width <= 0 or size_height <= 0:
            return Image.new("RGBA", (1, 1), (255, 255, 255, 0))
        image = self._image
        ratio = min(size_width / image.width, size_height / image.height)
        resize_size = (round(ratio * image.width), round(ratio * image.height))
        resized_image = image.resize(resize_size)

        return resized_image
