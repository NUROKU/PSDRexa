from PSDRexaSyncer.SyncTask import SyncTask
from PSDRexaSyncer.Syncer1 import Syncer1
from Service.ResolveService import ResolveService
from Service.SettingFileService import SettingFileService, SettingKeys


# Fusionを作成してそこに画像をロードさせるやつ
# InsertFusionCompositionIntoTimelineの挙動が気に入らなくて一旦没
class CharacterFusionDataStore:
    def __init__(self):
        # self._resolve = ResolveService.get_resolve()
        # self._project_manager = self._resolve.GetProjectManager()
        # self._project = self._project_manager.GetCurrentProject()
        pass

    def put_character_fusion(self, sotai, mepachi_open, mepachi_close, kuchipaku_open, kuchipaku_close):
        FOLDER_NAME = "PSDRexa"
        TEMPLATE_NAME = "PSDRexaTemplate"
        # Timelineにfusion追加
        project_manager = ResolveService.get_resolve().GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()
        timeline = project.GetCurrentTimeline()

        root_folder = media_pool.GetRootFolder()

        # Template取得
        sub_folder = root_folder.GetSubFolderList()
        psdrexa_template = None
        for folder in sub_folder:
            if folder.GetName() == FOLDER_NAME:
                clips = folder.GetClipList()
                for clip in clips:
                    if clip.GetName() == TEMPLATE_NAME:
                        psdrexa_template = clip

        index = int(SettingFileService.read_config(SettingKeys.index_for_output))
        max_right_offset = ResolveService.get_startframe()

        video_items = timeline.GetItemListInTrack("video", index)
        for video_item in video_items:
            if max_right_offset < video_item.GetEnd():
                max_right_offset = video_item.GetEnd()

        psdrexa_item = media_pool.AppendToTimeline([{
            'mediaPoolItem': psdrexa_template,
            'startFrame': 0,
            'mediaType': 1,
            'trackIndex': index,
            'recordFrame': max_right_offset
        }])
        fusion_list = psdrexa_item[0].GetFusionCompByIndex(1).GetToolList()

        for f in fusion_list.values():
            if f.GetAttrs('TOOLS_Name') == "Loader_mouseopen":
                f.Clip = str(kuchipaku_open)
            if f.GetAttrs('TOOLS_Name') == "Loader_mouseclose":
                f.Clip = str(kuchipaku_close)
            if f.GetAttrs('TOOLS_Name') == "Loader_eyeopen":
                f.Clip = str(mepachi_open)
            if f.GetAttrs('TOOLS_Name') == "Loader_eyeclose":
                f.Clip = str(mepachi_close)
            if f.GetAttrs('TOOLS_Name') == "Loader_sotai":
                f.Clip = str(sotai)

        syncer = Syncer1("", 0)
        syncer.sync_tasks(tasks=[SyncTask(video_item=psdrexa_item[0], sync_audio_clip_list=[])])
