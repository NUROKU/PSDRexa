from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.GroupLayer.GroupLayer import GroupLayer


class OneSelectGroupLayer(GroupLayer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group: GroupLayer):
        super().__init__(base_properties, parent_group)

    def selected_on(self, child_affect: bool = True):
        self.set_visible(True)

        try:
            for layer in self.parent.child_layers:
                if layer is not self and layer.layer_type_name.startswith("OneSelect"):
                    layer.selected_off()
                    if child_affect and layer.layer_type_name.endswith("GroupLayer"):
                        layer.fix_child_layer_check_selected_off()
            if child_affect:
                self.fix_child_layer_check_selected_on()
        except Exception as e:
            print(e)
            pass

    def selected_off(self, child_affect: bool = True):
        self.set_visible(False)
        try:
            if self.parent is not None and self.parent.is_visible is True:
                for layer in self.parent.child_layers:
                    if layer.is_visible is True and layer.layer_type_name.startswith("OneSelect"):
                        if child_affect:
                            self.fix_child_layer_check_selected_off()
                        return
                self.set_visible(True)
                return

            if child_affect:
                self.fix_child_layer_check_selected_off()
        except Exception as e:
            print(e)
            pass
    @property
    def layer_type_name(self):
        return "OneSelectGroupLayer"
