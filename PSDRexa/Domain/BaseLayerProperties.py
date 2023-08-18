from Domain.Image.LayerImage import LayerImage


class BaseLayerProperties:
    __id_counter = 0

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
        v_name = self.name.lstrip('!*')
        self.viewer_name = v_name

        name = v_name
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for char in invalid_chars:
            name = name.replace(char, '_')
        self.id_name = f"{BaseLayerProperties.__id_counter:04d}_{name}"
        BaseLayerProperties.__id_counter -= 1

    @classmethod
    def set_id_counter(cls, counter_id: int):
        BaseLayerProperties.__id_counter = counter_id
