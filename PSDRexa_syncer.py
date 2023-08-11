import wave
import struct
import os
import tkinter as tk

def gui(fu, bmd, resolve):
    ui = fu.UIManager
    dispatcher = bmd.UIDispatcher(ui)

    def OnClose(ev):
        dispatcher.ExitLoop()

    def CopyFolderPath(ev):
        folder_path = fu.RequestDir("", "",
                    {"FReqB_SeqGather":True,
                     "FReqS_Title":"Choose Folder"})
        window.Find('AudioFolderPath').Clear()
        window.Find('AudioFolderPath').Insert(folder_path)
        pass

    def StartSync(ev):
        def init(video_tracks):
            # PSDRexaの初期化
            for video in video_tracks:
                if video.GetName() == "PSDRexa":
                    video_len = video.GetDuration() 
                    fusion_obj = video.GetFusionCompByIndex(1).FindTool("CustomTool1")
                    fusion_obj.CurrentTime = 0
                    index = 0
                    for _ in range(0,video_len):
                        fusion_obj.NumberIn2[index] = 0
                        index += 1

        def create_tasks(video_tracks, audio_tracks):
            # 効率悪いけど動けばまあ。うん
            tasks = []
            for video in video_tracks:
                overlaps_for_item = []
                for audio in audio_tracks:
                    if max(video.GetStart(), audio.GetStart()) < min(video.GetEnd(), audio.GetEnd()):
                        start_diff = audio.GetStart() - video.GetStart()
                        overlap = (audio.GetName(),start_diff)
                        overlaps_for_item.append(overlap)
                if overlaps_for_item:
                    tasks.append((video,overlaps_for_item))
            return tasks

        def sync_mouse(task, framerate):
            if task[0].GetName() != "PSDRexa":
                return
            
            audio_wav = [0.0] * task[0].GetDuration() 
            for audio in task[1]:
                with wave.open(os.path.join(audio_file_path, audio[0]), 'rb') as wav_file:
                    params = wav_file.getparams()

                    # このあたり某人工知能に聞いた
                    frames = wav_file.readframes(params.nframes)
                    unpacked_frames = struct.unpack('<' + 'h' * params.nframes, frames)
                    volumes = [abs(amplitude) for amplitude in unpacked_frames]

                    frame_length = params.framerate // framerate
                    frames_volumes = [sum(volumes[i:i+frame_length]) / frame_length for i in range(0, len(volumes), frame_length)]
                    
                    index = audio[1]
                    if audio[1] < 0:
                        del frames_volumes[:abs(audio[1])]
                        index = 0
                    audio_wav[index:len(frames_volumes)] = frames_volumes

            fusion_obj = task[0].GetFusionCompByIndex(1).FindTool("CustomTool1")
            fusion_obj.CurrentTime = 0
            index = 0
            for _ in range(0,len(audio_wav)):
                fusion_obj.NumberIn2[index] = audio_wav[index]
                index += 1

        audio_file_path = window.Find('AudioFolderPath').Text 
        video_index = window.Find('VideoTrackInput').Value
        audio_index = window.Find('AudioTrackInput').Value

        if audio_file_path == "":
            window.Find('ResuktLabel').Text = f"Please set audio_file_path"
            return

        projectManager = resolve.GetProjectManager()
        project = projectManager.GetCurrentProject()
        timeline = project.GetCurrentTimeline()
        video_tracks = timeline.GetItemListInTrack("video",video_index)
        audio_tracks = timeline.GetItemListInTrack("audio",audio_index)

        init(video_tracks)
        tasks = create_tasks(video_tracks,audio_tracks)
        framerate = int(timeline.GetSetting('timelineFrameRate'))

        succeed = 0
        failed = 0
        for task in tasks:
            try:
                sync_mouse(task, framerate)
                succeed = succeed + 1
            except Exception as e:
                failed = failed + 1
                continue

        if failed == 0:
            window.Find('ResuktLabel').Text = f"{succeed} file succeed."
        else:
            window.Find('ResuktLabel').Text = f"{succeed} file succeed. {failed} file failed"
            
    elements = [ 
        ui.Label({ 'Text': ""}),
        
        ui.Label({"ID": "VideoTrackLabel", "Text": "Video Track", "Geometry": [10, 10, 150, 30]}),
        ui.SpinBox({"ID": "VideoTrackInput", "Text": "",'Value': 1 ,"Geometry": [120, 10, 170, 30]}),
        ui.Label({"ID": "AudioTrackLabel", "Text": "Audio Track", "Geometry": [10, 50, 150, 30]}),
        ui.SpinBox({"ID": "AudioTrackInput", "Text": "",'Value': 1 , "Geometry": [120, 50, 170, 30]}),
        ui.Label({"ID": "AudioFolderPathLabel", "Text": "Audio Folder Path", "Geometry": [10, 90, 100, 30]}),
        ui.Button({"ID": "AudioFolderPathButton", "Text": "Select Folder", "Geometry": [120, 90, 100, 30]}),
        ui.LineEdit({ 'ID': 'AudioFolderPath',  'Text': "" , "Geometry": [10, 130, 350, 30]}),
        ui.Button({"ID": "SyncButton", "Text": "Start Sync", "Geometry": [10, 170, 100, 30]}),
        ui.Label({"ID": "ResuktLabel", "Text": "-", "Geometry": [120, 170, 150, 30]}),

    ]

    window = dispatcher.AddWindow({'ID': 'MyWindow', 'WindowTitle': 'PSDRexa mouse sync', "Geometry": [400, 200, 400, 220]},elements)

    window.On.AudioFolderPathButton.Clicked = CopyFolderPath
    window.On.SyncButton.Clicked = StartSync
    window.On.MyWindow.Close = OnClose
    window.Show()
    dispatcher.RunLoop()
    window.Hide()

gui(fu, bmd, resolve)

