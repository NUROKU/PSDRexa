from typing import List

from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.DTO.CheckVisibleOperation import CheckVisibleOperation
from Domain.ImageLayer.ImageLayer import ImageLayer
from Exception.DomainError import DomainError
from Common import Logger

logger = Logger.get_logger(__name__)


class PsdTopGroupLayer:
    def __init__(self, base_layer_properties: BaseLayerProperties, layer_list: List):
        self._layer_list = layer_list
        self._base_layer_properties = base_layer_properties

    @property
    def layer_list(self):
        return self._layer_list

    @property
    def image_layer_list(self):
        return [layer for layer in self._layer_list if isinstance(layer, ImageLayer)]

    @property
    def size(self):
        return self._base_layer_properties.size

    def dump_list_for_tree(self) -> List:
        # parent iid text visible
        ret_list = []

        for layer in self._layer_list:
            layer_parent_id = layer.parent.id_name if layer.parent is not None else ""
            ret_list.append(
                [layer_parent_id, layer.id_name, layer.viewer_name, layer.is_visible, layer.layer_type_name])

        return ret_list

    def select_layers_by_operation(self, check_visible_operation: CheckVisibleOperation):
        for check in check_visible_operation.checked_list():
            layer = self._find_layer(check)
            layer.selected_on()

        for check in check_visible_operation.unchecked_list():
            layer = self._find_layer(check)
            layer.selected_off()

    def dump_visible_layer_id_names(self):
        return [layer.id_name for layer in self._layer_list if layer.is_visible]

    def _find_layer(self, id_name: str):
        for layer in self._layer_list:
            if layer.id_name == id_name:
                return layer
        raise DomainError(f"Layer {id_name} not found")
