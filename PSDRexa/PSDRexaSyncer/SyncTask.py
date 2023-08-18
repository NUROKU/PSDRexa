from typing import List


class SyncerAudioClip:
    def __init__(self, audio_item, start_diff, duration):
        self._audio_item = audio_item
        self._start_diff = start_diff
        self._duration = duration

    @property
    def audio_item(self):
        return self._audio_item

    @property
    def start_diff(self):
        return self._start_diff

    @property
    def duration(self):
        return self._duration


class SyncTask:
    def __init__(self, video_item, sync_audio_clip_list: List):
        self._video_item = video_item  # timelineitemをそのまま入れる
        self._sync_audio_clip_list = sync_audio_clip_list

    @property
    def video_item(self):
        return self._video_item

    @property
    def sync_audio_clip_list(self):
        return self._sync_audio_clip_list
