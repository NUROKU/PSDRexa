import wave
import struct
import os
import tkinter as tk

from PSDRexaSyncer.BaseSyncer import BaseSyncer
from PSDRexaSyncer.Syncer2 import Syncer2


class PSDRexaSyncerUI:
    def __init__(self,fu,bmd,resolve):
        self._resolve = resolve
        self._fu = fu
        self._bmd = bmd
        self._ui = fu.UIManager
        self._dispatcher = bmd.UIDispatcher(self._ui)

        elements = [
            self._ui.Label({'Text': ""}),

            self._ui.Label({"ID": "VideoTrackLabel", "Text": "Video Track", "Geometry": [10, 10, 150, 30]}),
            self._ui.SpinBox({"ID": "VideoTrackInput", "Text": "", 'Value': 1, "Geometry": [120, 10, 170, 30]}),
            self._ui.Label({"ID": "AudioTrackLabel", "Text": "Audio Track", "Geometry": [10, 50, 150, 30]}),
            self._ui.SpinBox({"ID": "AudioTrackInput", "Text": "", 'Value': 1, "Geometry": [120, 50, 170, 30]}),
            self._ui.Label({"ID": "AudioFolderPathLabel", "Text": "Audio Folder Path", "Geometry": [10, 90, 100, 30]}),
            self._ui.Button({"ID": "AudioFolderPathButton", "Text": "Select Folder", "Geometry": [120, 90, 100, 30]}),
            self._ui.LineEdit({'ID': 'AudioFolderPath', 'Text': "", "Geometry": [10, 130, 350, 30]}),
            self._ui.Button({"ID": "SyncButton", "Text": "Start Sync", "Geometry": [10, 170, 100, 30]}),
            self._ui.Label({"ID": "ResultLabel", "Text": "-", "Geometry": [120, 170, 150, 30]}),

        ]

        self._window = self._dispatcher.AddWindow(
            {'ID': 'MyWindow', 'WindowTitle': 'PSDRexa mouse sync', "Geometry": [400, 200, 400, 220]}, elements)

        self._window.On.AudioFolderPathButton.Clicked = self.CopyFolderPath
        self._window.On.SyncButton.Clicked = self.StartSync
        self._window.On.MyWindow.Close = self.OnClose
        self._window.Show()
        self._dispatcher.RunLoop()
        self._window.Hide()

    def OnClose(self,ev):
        self._dispatcher.ExitLoop()

    def CopyFolderPath(self,ev):
        folder_path = self._fu.RequestDir("", "",
                                    {"FReqB_SeqGather": True,
                                     "FReqS_Title": "Choose Folder"})
        self._window.Find('AudioFolderPath').Clear()
        self._window.Find('AudioFolderPath').Insert(folder_path)
        pass

    def StartSync(self,ev):

        audio_folder_path = self._window.Find('AudioFolderPath').Text
        video_index = self._window.Find('VideoTrackInput').Value
        audio_index = self._window.Find('AudioTrackInput').Value

        if audio_folder_path == "":
            self._window.Find('ResultLabel').Text = f"Please set audio_file_path"
            return

        project_manager = self._resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        timeline = project.GetCurrentTimeline()
        video_tracks = timeline.GetItemListInTrack("video", video_index)
        audio_tracks = timeline.GetItemListInTrack("audio", audio_index)

        tasks = BaseSyncer.create_tasks(video_tracks, audio_tracks)
        frame_rate = int(timeline.GetSetting('timelineFrameRate'))
        syncer = Syncer2(audio_folder_path=audio_folder_path, frame_rate=frame_rate)

        BaseSyncer.init_video_items(video_tracks)
        syncer.sync_tasks(tasks)

        self._window.Find('ResultLabel').Text = f"Done"





