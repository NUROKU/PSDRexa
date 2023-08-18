from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.GroupLayer.GroupLayer import GroupLayer


class VisibleGroupLayer(GroupLayer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group: GroupLayer):
        super().__init__(base_properties, parent_group)

    def selected_on(self, child_affect: bool = True):
        self.set_visible(True)

        if child_affect:
            self.fix_child_layer_check_selected_on()

    def selected_off(self, child_affect: bool = True):

        if self.parent is not None and self.parent.is_visible is False:
            self.set_visible(False)
            if child_affect:
                self.fix_child_layer_check_selected_off()

    @property
    def layer_type_name(self):
        return "VisibleGroupLayer"
