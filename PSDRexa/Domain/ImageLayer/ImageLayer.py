from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.Layer import Layer


class ImageLayer(Layer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group, flip_layer_images=None):
        super().__init__(base_properties)
        self._flip_layers = flip_layer_images
        self._parent_group = parent_group

    @property
    def parent(self):
        return self._parent_group

    def selected_on(self):
        self.set_visible(True)
        if self.parent is not None and self.parent.is_visible is False:
            self.parent.selected_on()

    def selected_off(self):
        self.set_visible(False)

    @property
    def layer_type_name(self):
        return "ImageLayer"

    def image_with_background(self, size_x, size_y):
        offset = self.offset
        return self.layer_image.image_with_background(size_x, size_y, offset[0], offset[1])
