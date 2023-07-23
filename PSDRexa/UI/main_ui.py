import tkinter
import platform
import os
import tkinter as tk
from tkinter import messagebox, filedialog

from Persenter.OutputCharacterPresenter import OutputCharacterPresenter
from Persenter.SaveCompositedImagePersenter import SaveCompositedImagePersenter
from Service.ResolveService import ResolveService
from Service.SettingFileService import SettingKeys, SettingFileService
from UI.CompositedImageCanvas import CompositedImageCanvas
from UI.SettingWindow import SettingWindow
from UI.layerTreeView import LayerTreeview


class MainUI:
    def __init__(self, resolve):
        self.save_pre = SaveCompositedImagePersenter()
        self.out_pre = OutputCharacterPresenter()
        self.setting_window = SettingWindow()
        ResolveService.set_resolve(resolve)

    def execute_ui(self):
        def save():
            try:
                self.out_pre.output_character()
            except Exception as e:
                messagebox.showerror("error", e.__str__())

        def set_local_folder():
            try:
                # TODO ここ別んとこに出しときたいなあ
                directory_path = filedialog.askdirectory()
                if directory_path != "":
                    SettingFileService.update_and_save_config(SettingKeys.image_output_folder, directory_path)
                    directory_label.config(text=directory_path)
            except Exception as e:
                messagebox.showerror("error", e.__str__())
        def set_output_index(*args):
            SettingFileService.update_and_save_config(SettingKeys.index_for_output, spinbox_var.get())

        def settings():
            self.setting_window.execute()

        root = tk.Tk()
        root.title("PSDRexa")
        root.geometry("800x600")

        resource_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Resources"))
        if platform.system() == 'Windows':
            root.iconbitmap(os.path.join(resource_folder, "ico_orig.ico"))
        else:
            img = tk.PhotoImage(file=os.path.join(resource_folder, "ico_orig.gif"))
            root.tk.call('wm', 'iconphoto', root._w, img)

        # 設定とか
        settings_frame1 = tk.Frame(root)
        btn3 = tkinter.Button(settings_frame1, text='設定', command=settings, width=5)
        btn3.pack(side="left", padx=5, pady=5, anchor=tk.W)
        btn4 = tk.Button(settings_frame1, text="出力先", command=set_local_folder)
        btn4.pack(side="left", padx=5, pady=5, anchor=tk.W)
        directory_label = tk.Label(settings_frame1,
                                   text=SettingFileService.read_config(SettingKeys.image_output_folder))
        directory_label.pack(side="left", padx=5, pady=5, anchor=tk.W)
        settings_frame1.pack(side="top", anchor=tk.W)

        # 右半分立ち絵
        canvas = CompositedImageCanvas(root, width=600, height=300)
        canvas.pack(side="right", fill="both", expand=True)

        # 左半分チェックボックス付きのツリーを配置
        tree = LayerTreeview(root, canvas=canvas, show='tree')
        tree.pack(fill="both", expand=True)

        btn1 = tkinter.Button(root, text='出力', command=save, width=5)
        btn1.pack(side="left", padx=5, pady=5, anchor=tk.N)

        # SpinBoxの設定
        index_label = tk.Label(root, text="出力index:")
        index_label.pack(side="top", padx=1, pady=1, anchor=tk.N)
        spinbox_var = tk.StringVar()
        spinbox_var.trace("w", set_output_index)
        spinbox = tk.Spinbox(root, textvariable=spinbox_var, from_=1, to=100)
        spinbox.pack(side="top", padx=1, pady=1, anchor=tk.N)

        # btn2 = tkinter.Button(root, text='更新', command=save, width = 5)
        # btn2.pack(side="left", padx=5, pady=5, anchor = tk.N)

        root.mainloop()
