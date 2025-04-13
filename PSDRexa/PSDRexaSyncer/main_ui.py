import tkinter as tk
from tkinter import messagebox
from PSDRexaSyncer.BaseSyncer import BaseSyncer
from PSDRexaSyncer.Syncer1 import Syncer1
from PSDRexaSyncer.Syncer2 import Syncer2

class PSDRexaSyncerUI:
    def __init__(self, fu, bmd, resolve):
        self._resolve = resolve

        self.root = tk.Tk()
        self.root.title("PSDRexa mouse sync")
        self.root.geometry("400x200")

        # UIパーツ
        tk.Label(self.root, text="Video Track").place(x=10, y=10)
        self.video_track_input = tk.Spinbox(self.root, from_=1, to=10, width=5)
        self.video_track_input.place(x=120, y=10)

        tk.Label(self.root, text="Audio Track").place(x=10, y=50)
        self.audio_track_input = tk.Spinbox(self.root, from_=1, to=10, width=5)
        self.audio_track_input.place(x=120, y=50)

        self.result2_label = tk.Label(self.root, text="-")
        tk.Button(self.root, text="口パクSync", command=self.start_sync2).place(x=10, y=90)
        self.result2_label.place(x=120, y=90)

        self.result1_label = tk.Label(self.root, text="-")
        tk.Button(self.root, text="目パチのキーフレームを再構築", command=self.start_sync1).place(x=10, y=130)
        self.result1_label.place(x=170, y=130)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def on_close(self):
        self.root.destroy()

    def start_sync2(self):
        try:
            self.result2_label.config(text="Processing...")
            video_index = int(self.video_track_input.get())
            audio_index = int(self.audio_track_input.get())

            project_manager = self._resolve.GetProjectManager()
            project = project_manager.GetCurrentProject()
            timeline = project.GetCurrentTimeline()
            video_tracks = timeline.GetItemListInTrack("video", video_index)
            audio_tracks = timeline.GetItemListInTrack("audio", audio_index)

            tasks = BaseSyncer.create_tasks(video_tracks, audio_tracks)
            frame_rate = int(timeline.GetSetting('timelineFrameRate'))
            syncer = Syncer2(frame_rate=frame_rate)

            BaseSyncer.init_video_items(video_tracks)
            result = syncer.sync_tasks(tasks)

            if result:
                message = "口パク設定が完了しました"
            else:
                message = "口パク設定が完了しましたが、一部のwavファイルの読み込みでエラーが発生しました。\n詳しくはDaVinci Resolveのコンソールを確認してください"

            messagebox.showinfo("PSDRexa_Syncer", message)
            self.result2_label.config(text="-")
        except Exception as e:
            messagebox.showerror("PSDRexa_Syncer", f"ERROR: {str(e)}")
            self.result2_label.config(text="-")

    def start_sync1(self):
        try:
            self.result1_label.config(text="Processing...")
            video_index = int(self.video_track_input.get())

            project_manager = self._resolve.GetProjectManager()
            project = project_manager.GetCurrentProject()
            timeline = project.GetCurrentTimeline()
            video_tracks = timeline.GetItemListInTrack("video", video_index)

            tasks = BaseSyncer.create_tasks(video_tracks, [])
            syncer = Syncer1(frame_rate=0)

            BaseSyncer.init_video_items(video_tracks)
            result = syncer.sync_tasks(tasks)

            if result:
                message = "目パチ設定が完了しました"
            else:
                message = "目パチ設定が完了しましたが、一部のwavファイルの読み込みでエラーが発生しました。\n詳しくはDaVinci Resolveのコンソールを確認してください"

            messagebox.showinfo("PSDRexa_Syncer", message)
            self.result1_label.config(text="-")
        except Exception as e:
            messagebox.showerror("PSDRexa_Syncer", f"ERROR: {str(e)}")
            self.result1_label.config(text="-")