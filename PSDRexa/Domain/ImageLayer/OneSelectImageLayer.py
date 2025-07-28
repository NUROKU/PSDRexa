from typing import List

from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.GroupLayer.GroupLayer import GroupLayer
from Domain.Image.FlipLayerImage import FlipLayerImage
from Domain.ImageLayer.ImageLayer import ImageLayer


class OneSelectImageLayer(ImageLayer):
    def __init__(self, base_properties: BaseLayerProperties, parent_group: GroupLayer,
                 flip_layer_images: List[FlipLayerImage]):
        super().__init__(base_properties, parent_group, flip_layer_images)

    def selected_on(self):
        self.set_visible(True)

        # 同じグループの他のImageLayerを全部OFFにする
        try:
            for layer in self.parent.child_layers:
                if layer is not self and layer.layer_type_name.startswith("OneSelect"):
                    layer.selected_off()
            if self.parent is not None and self.parent.is_visible is False:
                self.parent.selected_on()
        except Exception as e:
            print(e)
            pass


    def selected_off(self):
        self.set_visible(False)

        try:
            if self.parent is not None and self.parent.is_visible is True:
                for layer in self.parent.child_layers:
                    if layer.is_visible is True and layer.layer_type_name.startswith("OneSelect"):
                        return
                self.set_visible(True)
        except Exception as e:
            print(e)
            pass

    # def _get_oneselect_layers(self):
    #     # oneselectGroupも対象に含めないといけなかったので没
    #     return self._parent_group.child_image_layers

    @property
    def layer_type_name(self):
        return "OneSelectImageLayer"
