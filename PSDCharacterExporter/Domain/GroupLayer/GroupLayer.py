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

    def selected_on(self):
        self.set_visible(True)
        self.fix_child_layer_check_selected_on()

    def selected_off(self):
        self.set_visible(False)
        self.fix_child_layer_check_selected_off()

    def fix_child_layer_check_selected_on(self):
        if self._parent_group is not None and self._parent_group.is_visible is False:
            self._parent_group.selected_on()
        # ↓のこれもうちょっと賢くできなかったの？
        for layer in self.child_layers:
            if layer.layer_type_name == "VisibleGroupLayer":
                layer.selected_on()

        for layer in self.child_layers:
            if layer.is_visible is True:
                return

        if len(self.child_image_layers) > 0:
            self.child_image_layers[len(self.child_image_layers) - 1].selected_on()
        else:
            self.child_group_layers[len(self.child_group_layers) - 1].selected_on()

    def fix_child_layer_check_selected_off(self):
        for layer in self.child_layers:
            layer.selected_off()

    # def set_visible(self, visible: bool):
    #     super().set_visible(visible)

    # 全グループ共通だからここにおいてるけど、どうなんだろうね
    # if visible:
    #     if self._parent_group is not None and self._parent_group.is_visible is False:
    #         self._parent_group.selected_on()
    #     # ↓のこれもうちょっと賢くできなかったの？
    #     for layer in self.child_layers:
    #         if layer.layer_type_name == "VisibleGroupLayer":
    #             layer.set_visible(True)
#
#     if len(self.child_image_layers) > 0:
#         self.child_image_layers[len(self.child_image_layers) - 1].set_visible(True)
#     else:
#         self.child_group_layers[len(self.child_group_layers) - 1].set_visible(True)
# else:
#     for layer in self.child_image_layers:
#         layer.set_visible(False)
#     for group in self.child_group_layers:
#         group.selected_off()
#
