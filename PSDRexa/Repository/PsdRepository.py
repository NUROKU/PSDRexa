from pathlib import Path

import Domain.BaseLayerProperties
from PIL import Image
from psd_tools.api import layers

from Common import Logger
from Domain.BaseLayerProperties import BaseLayerProperties
from Domain.GroupLayer.OneSelectGroupLayer import OneSelectGroupLayer
from Domain.GroupLayer.VisibleGroupLayer import GroupLayer, VisibleGroupLayer
from Domain.Image.LayerImage import LayerImage
from Domain.ImageLayer.ImageLayer import ImageLayer
from Domain.ImageLayer.OneSelectImageLayer import OneSelectImageLayer
from Domain.Psd.Psd import Psd
from Domain.Psd.PsdMeta import PsdMeta
from Domain.Psd.PsdTop import PsdTop
from DataStore.PsdDataStore import PsdDataStore
from Exception.DataStoreError import DataStoreError
from Exception.RepositoryError import RepositoryError
from Service.SettingFileService import SettingFileService, SettingKeys

logger = Logger.get_logger(__name__)


class PsdRepository:
    def __init__(self):
        # TODO 気が向いたらクリーンアーキテクチャっぽくInterfaceとか作っておいてほしい
        self._psd_datastore = PsdDataStore()
        pass

    def get_psd(self, psd_file_path: Path) -> Psd:
        # TODO Flipのやつ対応できてない、あれgroupにもあるらしい
        try:
            psd_file = self._psd_datastore.get_psd(psd_file_path=psd_file_path)
            psd_meta = PsdMeta(file_path=psd_file_path)

            psdtool_layer_list = list(psd_file.descendants(include_clip=False))
            domain_layer_list = []
            BaseLayerProperties.set_id_counter(len(psdtool_layer_list))

            ratio = min(SettingFileService.read_config(SettingKeys.image_preview_size_x) / psd_file.size[0],
                        SettingFileService.read_config(SettingKeys.image_preview_size_y) / psd_file.size[1])

            # TODO *がTOPの場合の応急処置下に入れたけど、これ汚いやだ
            for layer in psdtool_layer_list:
                if layer.parent.name == "Root" and layer.name.startswith("*"):
                    root_base_property = BaseLayerProperties(name="Root", size=(0, 0), offset=(0, 0),
                                                             visible=True, layer_image=None)
                    domain_layer_list.append(GroupLayer(root_base_property, parent_group=None, child_layers=None))
                    break

            for layer in psdtool_layer_list:
                logger.debug(f"psd: {layer} size: {layer.size} opacity: {layer.opacity}")
                logger.debug(f"parent: {layer.parent.name}")
                # if ":flip" in layer.name:
                #     continue

                if layer.is_group():
                    group = define_group_domain(layer, domain_layer_list)
                    logger.debug(f"{layer.name} - {layer.blend_mode}")
                    domain_layer_list.append(group)
                    # logger.debug(group.parent)
                else:
                    layer_obj = define_image_layer_domain(layer, domain_layer_list, ratio)
                    domain_layer_list.append(layer_obj)
                    # logger.debug(layer_obj)

            add_childs_for_group(domain_layer_list)
            top_base_properties = BaseLayerProperties(name="top", size=psd_file.size, offset=psd_file.offset,
                                                      visible=True, layer_image=None)
            top_layer_groups = PsdTop(base_layer_properties=top_base_properties, layer_list=domain_layer_list)

            return Psd(psd_meta=psd_meta, psd_top_layer_group=top_layer_groups)
        except DataStoreError as e:
            raise RepositoryError("PSDファイルの読み込みに失敗しました。")
        except Exception as e:
            logger.exception(e)
            raise RepositoryError("PSDファイルの読み込みに失敗しました。")


def define_group_domain(group_obj, domain_layer_list):
    parent_group = None
    if type(group_obj.parent) is layers.Group:
        try:
            reversed_domain_layer_list = list(reversed(domain_layer_list))
            parent_group = next(filter(lambda obj: obj.name == group_obj.parent.name, reversed_domain_layer_list))
        except StopIteration:
            raise Exception(f"Parent Not Found  :{group_obj}")

    # imageは暫定、サムネ対応とかすることになったら入れるのかな・・・
    base_property = BaseLayerProperties(name=group_obj.name, size=group_obj.size, offset=group_obj.offset,
                                        visible=group_obj.is_visible(), layer_image=None)
    if SettingFileService.read_config(SettingKeys.use_psdtool_func) is True:
        if group_obj.name.startswith("!"):
            return VisibleGroupLayer(base_property, parent_group=parent_group)
        if group_obj.name.startswith("*"):
            if parent_group is None and group_obj.parent.name == "Root":
                reversed_domain_layer_list = list(reversed(domain_layer_list))
                parent_group = next(filter(lambda obj: obj.name == group_obj.parent.name, reversed_domain_layer_list))
            return OneSelectGroupLayer(base_property, parent_group=parent_group)
    return GroupLayer(base_property, parent_group=parent_group, child_layers=None)


def define_image_layer_domain(layer_obj, domain_layer_list, ratio):
    parent_group = None
    flip_list = []

    if type(layer_obj.parent) is layers.Group:
        try:
            reversed_domain_layer_list = list(reversed(domain_layer_list))
            parent_group = next(filter(lambda obj: obj.name == layer_obj.parent.name, reversed_domain_layer_list))
        except StopIteration:
            raise Exception(f"Parent Not Found  :{layer_obj}")
        # Flip_Layer_image
        # tmp_list = list(layer_obj.parent.descendants(include_clip=True))
        # for flip_layer in tmp_list:
        #     if flip_layer.parent is not layer_obj.parent:
        #         continue
        #     if flip_layer.name.startswith(f"{layer_obj.name}:flip"):
        #         layer_image = LayerImage(flip_layer.topil())
        #         flip_layer_image = FlipLayerImage(FlipType.value_from_name(flip_layer.name), layer_image)
        #         flip_list.append(flip_layer_image)

    img = layer_obj.topil()
    if layer_obj.opacity != 255 and layer_obj.opacity != 0:
        # 透明度調整
        back_img = Image.new("RGBA", layer_obj.size, (255, 255, 255, 0))
        img = Image.blend(back_img,layer_obj.topil(), layer_obj.opacity / 255)

    base_property = BaseLayerProperties(name=layer_obj.name, size=layer_obj.size, offset=layer_obj.offset,
                                        visible=layer_obj.is_visible(),
                                        layer_image=LayerImage(img, preview_ratio=ratio, opacity=layer_obj.opacity, blend_mode=str(layer_obj.blend_mode)))

    if SettingFileService.read_config(SettingKeys.use_psdtool_func) is True:
        if layer_obj.name.startswith("*"):
            return OneSelectImageLayer(base_property, parent_group, flip_list)

    return ImageLayer(base_property, parent_group, flip_list)


def add_childs_for_group(domain_layer_list):
    for group_layer in [layer for layer in domain_layer_list if isinstance(layer, GroupLayer)]:
        group_layer.set_child_layers([layer for layer in domain_layer_list if layer.parent is group_layer])
