from Domain.Image.LayerImage import LayerImage


class BaseLayerProperties:
    def __init__(self, name: str, size: tuple, offset: tuple, visible: bool, layer_image: LayerImage):
        self.name = name
        self.size = size
        self.offset = offset
        self.visible = visible
        self.layer_image = layer_image
        self.id_name = ""
        self.viewer_name = ""
        self.__post_init__()

    def __post_init__(self):
        self.id_name = f"{self.name}_{id(self)}"
        v_name = self.name.lstrip('!*')
        self.viewer_name = v_name