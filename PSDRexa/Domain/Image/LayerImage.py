from Common import Logger
from PIL import Image

logger = Logger.get_logger(__name__)


class LayerImage:
    def __init__(self, image: Image, preview_ratio: float, opacity: int, blend_mode: str):
        self._image = image
        self._opacity = opacity
        self._blend_mode = blend_mode
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

    @property
    def blend_mode(self):
        return self._blend_mode

    def resized_image(self, size_width: int, size_height: int) -> Image:
        if size_width <= 0 or size_height <= 0:
            return Image.new("RGBA", (1, 1), (255, 255, 255, 0))
        image = self._image
        ratio = min(size_width / image.width, size_height / image.height)
        resize_size = (round(ratio * image.width), round(ratio * image.height))
        resized_image = image.resize(resize_size)

        return resized_image

    def image_with_background(self, size_width: int, size_height: int, offset_x: int, offset_y: int):
        background_image = Image.new("RGBA", (size_width, size_height), (255, 255, 255, 0))

        c = Image.new('RGBA', (size_width, size_height), (255, 255, 255, 0))
        c.paste(self._image, (offset_x, offset_y))
        return Image.alpha_composite(background_image, c)
