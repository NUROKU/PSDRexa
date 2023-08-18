from PSDRexaSyncer.BaseSyncer import BaseSyncer
from PSDRexaSyncer.Syncer1 import Syncer1
from PSDRexaSyncer.Syncer2 import Syncer2


class PSDRexaSyncerUI:
    def __init__(self, fu, bmd, resolve):
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
            self._ui.Button({"ID": "Sync2Button", "Text": "口パクSync", "Geometry": [10, 170, 100, 30]}),
            self._ui.Label({"ID": "Result2Label", "Text": "-", "Geometry": [120, 170, 150, 30]}),
            self._ui.Button({"ID": "Sync1Button", "Text": "目パチのキーフレームを再構築", "Geometry": [10, 210, 150, 30]}),
            self._ui.Label({"ID": "Result1Label", "Text": "-", "Geometry": [170, 210, 150, 30]}),
        ]

        self._window = self._dispatcher.AddWindow(
            {'ID': 'MyWindow', 'WindowTitle': 'PSDRexa mouse sync', "Geometry": [400, 250, 400, 250]}, elements)

        self._window.On.AudioFolderPathButton.Clicked = self.CopyFolderPath
        self._window.On.Sync1Button.Clicked = self.StartSync1
        self._window.On.Sync2Button.Clicked = self.StartSync2
        self._window.On.MyWindow.Close = self.OnClose
        self._window.Show()
        self._dispatcher.RunLoop()
        self._window.Hide()

    def OnClose(self, ev):
        self._dispatcher.ExitLoop()

    def CopyFolderPath(self, ev):
        folder_path = self._fu.RequestDir("", "",
                                          {"FReqB_SeqGather": True,
                                           "FReqS_Title": "Choose Folder"})
        self._window.Find('AudioFolderPath').Clear()
        self._window.Find('AudioFolderPath').Insert(folder_path)
        pass

    def StartSync2(self, ev):
        audio_folder_path = self._window.Find('AudioFolderPath').Text
        video_index = self._window.Find('VideoTrackInput').Value
        audio_index = self._window.Find('AudioTrackInput').Value

        if audio_folder_path == "":
            self._window.Find('Result2Label').Text = f"Please set audio_file_path"
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

        self._window.Find('Result2Label').Text = f"Sync Done"

    def StartSync1(self, ev):
        video_index = self._window.Find('VideoTrackInput').Value
        project_manager = self._resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        timeline = project.GetCurrentTimeline()
        video_tracks = timeline.GetItemListInTrack("video", video_index)

        tasks = BaseSyncer.create_tasks(video_tracks, [])
        syncer = Syncer1(audio_folder_path="", frame_rate=0)

        BaseSyncer.init_video_items(video_tracks)
        syncer.sync_tasks(tasks)

        self._window.Find('Result1Label').Text = f"Sync Done"
