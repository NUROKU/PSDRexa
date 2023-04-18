from dataclasses import dataclass

from Domain.Image.LayerImage import LayerImage


@dataclass
class BaseLayerProperties:
    name: str
    size: tuple
    offset: tuple
    visible: bool
    layer_image: LayerImage
    id_name = ""
    viewer_name = ""

    def __post_init__(self):
        self.id_name = f"{self.name}_{id(self)}"
        v_name = self.name.removeprefix('!')
        v_name = v_name.removeprefix('*')
        self.viewer_name = v_name
