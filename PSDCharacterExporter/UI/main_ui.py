import tkinter
import tkinter as tk
from tkinter import messagebox

from Persenter.OutputCharacterPresenter import OutputCharacterPresenter
from Persenter.SaveCompositedImagePersenter import SaveCompositedImagePersenter
from Service.ResolveService import ResolveService
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

        def settings():
            self.setting_window.execute()

        root = tk.Tk()
        root.title("PSDCharacterImageExporter")
        root.geometry("800x600")

        # 右半分にチェックボックス付きのツリーを配置
        canvas = CompositedImageCanvas(root, width=400, height=300)
        canvas.pack(side="right", fill="both", expand=True)

        # 左半分
        btn3 = tkinter.Button(root, text='設定', command=settings, width=5)
        btn3.pack(side="top", padx=5, pady=5, anchor=tk.W)
        tree = LayerTreeview(root, canvas=canvas, show='tree')
        tree.pack(fill="both", expand=True)

        btn1 = tkinter.Button(root, text='出力', command=save, width=5)
        btn1.pack(side="left", padx=5, pady=5, anchor=tk.N)
        # btn2 = tkinter.Button(root, text='更新', command=save, width = 5)
        # btn2.pack(side="left", padx=5, pady=5, anchor = tk.N)

        root.mainloop()
