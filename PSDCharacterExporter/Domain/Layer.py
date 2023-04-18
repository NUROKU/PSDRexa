from Domain.BaseLayerProperties import BaseLayerProperties


class Layer:
    def __init__(self, base_properties: BaseLayerProperties):
        self._base_properties = base_properties

    @property
    def name(self):
        return self._base_properties.name

    @property
    def offset(self):
        return self._base_properties.offset

    @property
    def layer_image(self):
        return self._base_properties.layer_image

    @property
    def viewer_name(self):
        return self._base_properties.viewer_name

    @property
    def id_name(self):
        return self._base_properties.id_name

    @property
    def is_visible(self):
        return self._base_properties.visible

    @property
    def layer_type_name(self):
        return "Layer"

    def set_visible(self, visible: bool):
        self._base_properties.visible = visible

    def set_visible_force(self, visible: bool):
        self._base_properties.visible = visible
