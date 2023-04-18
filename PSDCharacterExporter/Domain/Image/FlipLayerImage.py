from enum import Enum

from Domain.Image.LayerImage import LayerImage


class FlipType(Enum):
    x = ":flipx"
    y = ":flipy"
    xy = ":flipxy"

    @classmethod
    def value_of(cls, flip_str):
        for e in FlipType:
            if e.value == flip_str:
                return e
        raise ValueError(f'{flip_str} は有効なFlipTypeではありません')

    @classmethod
    def value_from_name(cls, flip_str):
        if flip_str.endswith(":flipx"):
            return FlipType.x
        if flip_str.endswith(":flipy"):
            return FlipType.y
        if flip_str.endswith(":flipxy"):
            return FlipType.xy
        raise ValueError(f'{flip_str} に有効なFlipTypeではありません')


class FlipLayerImage:
    def __init__(self, flip_type: FlipType, layer_image: LayerImage):
        self._flip_type = flip_type
        self._layer_image = layer_image
