from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.ImageLayer.ImageLayer import ImageLayer
from Domain.Layer import Layer


class GroupLayer(Layer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group, child_layers=None):
        super().__init__(base_properties)
        self._parent_group = parent_group
        self._child_layers = child_layers

    def set_child_layers(self, child_layers):
        if self._child_layers is None:
            self._child_layers = child_layers
        else:
            raise ValueError("child_layers can set only 1 time")

    @property
    def child_layers(self):
        return self._child_layers

    @property
    def child_image_layers(self):
        return [layer for layer in self._child_layers if isinstance(layer, ImageLayer)]

    @property
    def child_group_layers(self):
        return [layer for layer in self._child_layers if isinstance(layer, GroupLayer)]

    @property
    def parent(self):
        return self._parent_group

    @property
    def layer_type_name(self):
        return "GroupLayer"

    def selected_on(self, child_affect: bool = True):
        if self.is_visible is True:
            return

        if self.parent is not None and self.parent.is_visible is False:
            self.parent.selected_on(child_affect=False)
        if self.parent is not None and self.parent.is_visible is False:
            return
        self.set_visible(True)

        if child_affect:
            self.fix_child_layer_check_selected_on()

    def selected_off(self, child_affect: bool = True):
        if self.is_visible is False:
            return

        self.set_visible(False)
        if child_affect:
            self.fix_child_layer_check_selected_off()

    def fix_child_layer_check_selected_on(self):
        # if self._parent_group is not None and self._parent_group.is_visible is False:
        #     self._parent_group.selected_on()
        # ↓のこれもうちょっと賢くできなかったの？
        for layer in self.child_layers:
            if layer.layer_type_name == "VisibleGroupLayer":
                layer.selected_on()

        for layer in self.child_layers:
            if layer.is_visible is True:
                return

        if len(self.child_image_layers) > 0:
            self.child_image_layers[len(self.child_image_layers) - 1].selected_on()

    def fix_child_layer_check_selected_off(self):
        for layer in self.child_layers:
            layer.selected_off()
