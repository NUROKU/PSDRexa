from PSDRexaSyncer.SyncTask import SyncerAudioClip, SyncTask


class BaseSyncer:
    def __init__(self, audio_folder_path:str, frame_rate: int):
        self._audio_folder_path = audio_folder_path
        self._frame_rate = frame_rate

    @property
    def audio_folder_path(self):
        return self._audio_folder_path

    @property
    def frame_rate(self):
        return self._frame_rate

    def sync_tasks(self, tasks):
        for task in tasks:
            self._sync(task)

    def _sync(self, task):
        raise NotImplementedError()

    @staticmethod
    def init_video_items(video_items):
        for video in video_items:
            if video.GetName() == "PSDRexa":
                video_len = video.GetDuration()
                fusion_obj = video.GetFusionCompByIndex(1).FindTool("CustomTool1")
                fusion_obj.CurrentTime = 0
                index = 0
                for _ in range(0, video_len):
                    fusion_obj.NumberIn1[index] = 0
                    fusion_obj.NumberIn2[index] = 0
                    fusion_obj.NumberIn3[index] = 0
                    fusion_obj.NumberIn4[index] = 0
                    index += 1

    @staticmethod
    def create_tasks(video_items, audio_items):
        # 効率悪いけど動けばまあ。うん
        tasks = []
        for video in video_items:
            if video.GetName() != "PSDRexa":
                continue

            clip_list = []
            for audio in audio_items:
                if max(video.GetStart(), audio.GetStart()) < min(video.GetEnd(), audio.GetEnd()):
                    start_diff = audio.GetStart() - video.GetStart()
                    audio_clip = SyncerAudioClip(audio, audio.GetDuration(), start_diff)
                    clip_list.append(audio_clip)

            tasks.append(SyncTask(video, clip_list))
        return tasks

