from datetime import datetime

from PIL import Image

from Common import Logger
from Domain.Psd.PsdTopGroupLayer import PsdTopGroupLayer
from Service.SettingFileService import SettingFileService, SettingKeys

logger = Logger.get_logger(__name__)


class CompositedImage:
    def __init__(self, top_group_layer: PsdTopGroupLayer, is_for_preview: bool = False, id: str = None):
        self._layer_image_size = top_group_layer.size
        self._ratio = 1.0

        if is_for_preview and SettingFileService.read_config(SettingKeys.is_image_preview_size_original) is False:
            self._layer_image_size = (SettingFileService.read_config(SettingKeys.image_preview_size_x),
                                      SettingFileService.read_config(SettingKeys.image_preview_size_y))
            self._ratio = min(self._layer_image_size[0] / top_group_layer.size[0],
                              self._layer_image_size[1] / top_group_layer.size[1])

        self._composited_image = self.create_composited_image(top_group_layer=top_group_layer,
                                                              is_for_preview=is_for_preview)

        self._id = id
        if id is None:
            self._id = datetime.now().strftime('img_%Y%m%d_%H%M%S')

    @property
    def image(self) -> Image:
        return self._composited_image

    @property
    def id(self) -> str:
        return self._id.__str__()

    def id_with_extension(self, extension: str = "png") -> str:
        return f"{self._id.__str__()}.{extension}"

    def resized_image(self, width: int, height: int) -> Image:
        image = self._composited_image

        # ratio = min(width / image.width, height / image.height)
        ratio = height / image.height
        resize_size = (round(ratio * image.width), round(ratio * image.height))
        resized_image = image.resize(resize_size)
        # resized_image = image.resize((width,height))

        return resized_image

    def create_composited_image(self, top_group_layer: PsdTopGroupLayer, is_for_preview: bool):
        composited_image = Image.new("RGBA", self._layer_image_size, (255, 255, 255, 0))

        for layer in top_group_layer.image_layer_list:
            if layer.is_visible:
                if is_for_preview and SettingFileService.read_config(SettingKeys.is_image_preview_size_original) is False:
                    resized_offset = (int(layer.offset[0] * self._ratio), int(layer.offset[1] * self._ratio))

                    c = Image.new('RGBA', self._layer_image_size, (255, 255, 255, 0))
                    c.paste(layer.layer_image.previewed_image,resized_offset)
                    composited_image = Image.alpha_composite(composited_image, c)
                else:
                    c = Image.new('RGBA', self._layer_image_size, (255, 255, 255, 0))
                    c.paste(layer.layer_image.image,layer.offset)
                    composited_image = Image.alpha_composite(composited_image, c)

        return composited_image
