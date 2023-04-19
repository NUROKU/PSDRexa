from pathlib import Path

from Exception.DataStoreError import DataStoreError
from Service.ResolveService import ResolveService

# Fusionを作成してそこに画像をロードさせるやつ
# InsertFusionCompositionIntoTimelineの挙動が気に入らなくて一旦没
class CharacterFusionDataStore:
    def __init__(self):
        # self._resolve = ResolveService.get_resolve()
        # self._project_manager = self._resolve.GetProjectManager()
        # self._project = self._project_manager.GetCurrentProject()
        pass

    def put_character_fusion(self, character_image_file_path: Path):
        # Timelineにfusion追加
        project_manager = ResolveService.get_resolve().GetProjectManager()
        project = project_manager.GetCurrentProject()
        timeline = project.GetCurrentTimeline()

        timeline_item = timeline.InsertFusionCompositionIntoTimeline()
        fusion_comp = timeline_item.GetFusionCompByIndex(1)

        fusion_comp.Lock()
        loader = fusion_comp.AddTool("Loader", 0, 1)
        loader.SetAttrs({"TOOLS_Name": "PSDLoader"})
        loader.Clip = str(character_image_file_path)

        timespeed = fusion_comp.AddTool("TimeSpeed", 0, 2)
        timespeed.Speed = 0
        timespeed.ConnectInput("Input", loader)

        mediaout = fusion_comp.FindToolByID("MediaOut")
        mediaout.ConnectInput("Input", timespeed)

        fusion_comp.Unlock()

        pass

    def update_character_fusion(self, character_image_file_path: Path):
        project_manager = resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        timeline = project.GetCurrentTimeline()
        # GetCurrentVideoItemの場合、Timelineの一番上のアイテムが取得される
        timeline_item = timeline.GetCurrentVideoItem()
        fusion_list = timeline_item.GetFusionCompByIndex(1).GetToolList()

        psd_loader = None
        for f in fusion_list.values():
            if f.GetAttrs('TOOLS_Name') == "PSDLoader":
                psd_loader = f

        if psd_loader is None:
            raise DataStoreError("PSDLoader not found")

        psd_loader.Clip = str(character_image_file_path)
