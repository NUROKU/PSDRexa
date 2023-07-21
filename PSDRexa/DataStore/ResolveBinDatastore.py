from pathlib import Path

from Common import Logger
from Service.ResolveService import ResolveService

logger = Logger.get_logger(__name__)


class ResolveBinDatastore:
    def __init__(self):
        # Template用のはTemplate_binみたいな名前のDatastoreクラス作る
        self.image_bin_name = "RSDRexa"
        pass

    # Bin作成
    def get_image_bin(self):
        # 同じ名前の既存のBinがあるかどうかを確認
        project_manager = ResolveService.get_resolve().GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()

        existing_bins = media_pool.GetRootFolder().GetSubFolderList()
        existing_bin = None
        for bin in existing_bins:
            if bin.GetName() == self.image_bin_name:
                existing_bin = bin
                break

        # 同じ名前のBinが存在しない場合、新しいBinを作成
        if existing_bin is None:
            new_bin = media_pool.AddSubFolder(media_pool.GetRootFolder(), self.image_bin_name)
            logger.debug(f"新しいBinが作成されました: {self.image_bin_name}")
            media_pool.SetCurrentFolder(new_bin)
            return new_bin
        else:
            logger.debug(f"既に同じ名前のBinが存在するため、新しいBinを作成しませんでした: {self.image_bin_name}")
            media_pool.SetCurrentFolder(existing_bin)
            return existing_bin

    def get_image_from_bin(self, file_name):
        clips = self.get_image_bin.GetItemList()
        for clip in clips:
            clip_attrs = clip.GetAttrs()
            if clip_attrs['Name'] == file_name:
                return clip

        logger.debug(f"Failed to get image : {file_name}")
        return None

    # def add_image(self, bin):
    #    clips = bin.GetItemList()
    #    image_list = []
    #    for clip in clips:
    #        clip_attrs = clip.GetAttrs()
    #        image_list.append(clip_attrs['Name'])
    #
    #    return image_list

    def add_image_to_bin(self, image_path: Path):
        # timelineへのimage追加もしちゃってるの単純に命名詐欺では？

        media_storage = ResolveService.get_resolve().GetMediaStorage()
        self.get_image_bin()
        item = media_storage.AddItemListToMediaPool(str(image_path))

        project_manager = ResolveService.get_resolve().GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()

        res = media_pool.AppendToTimeline(item)
        # return res
