from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.GroupLayer.GroupLayer import GroupLayer


class VisibleGroupLayer(GroupLayer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group: GroupLayer):
        super().__init__(base_properties, parent_group)

    def selected_on(self):
        if self.parent is not None and self.parent.is_visible is False:
            return
        self.set_visible(True)
        self.fix_child_layer_check_selected_on()

    def selected_off(self):
        if self.parent is not None and self.parent.is_visible is False:
            self.set_visible(False)
            self.fix_child_layer_check_selected_off()
        else:
            self.set_visible(True)
            self.fix_child_layer_check_selected_on()

    @property
    def layer_type_name(self):
        return "VisibleGroupLayer"
