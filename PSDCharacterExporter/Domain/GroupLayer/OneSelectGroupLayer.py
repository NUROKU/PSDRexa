from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.GroupLayer.GroupLayer import GroupLayer


class OneSelectGroupLayer(GroupLayer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group: GroupLayer):
        super().__init__(base_properties, parent_group)

    def selected_on(self):
        self.set_visible(True)
        for layer in self.parent.child_layers:
            if layer is not self and isinstance(layer, (OneSelectGroupLayer, type(self))):
                layer.selected_off()
        self.fix_child_layer_check_selected_on()

    def selected_off(self):
        self.set_visible(False)
        if self.parent is not None and self.parent.is_visible is True:
            for layer in self.parent.child_layers:
                if layer.is_visible is True and isinstance(layer, (OneSelectGroupLayer, type(self))):
                    self.fix_child_layer_check_selected_off()
                    return
            self.set_visible(True)
            return
        self.fix_child_layer_check_selected_off()

    @property
    def layer_type_name(self):
        return "OneSelectGroupLayer"
