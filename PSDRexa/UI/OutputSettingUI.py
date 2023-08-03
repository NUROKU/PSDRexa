import tkinter
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from Service.SettingFileService import SettingKeys, SettingFileService
from Service.PsdMemorySaverService import PsdMemorySaverService

class OutputSettingUI:
    def __init__(self):

        self.psd_layer_list = PsdMemorySaverService.get_psd().top_layer_group.dump_list()


        self.root = tk.Toplevel()
        self.root.geometry('600x300')

        frame_top = tk.Frame(self.root)
        frame_top.pack(side=tk.TOP, fill=tk.X, pady=5)

        button_output = tk.Button(frame_top, text="出力先", command=self.on_output_button_click)
        button_output.pack(side=tk.LEFT)

        self.label_output = tk.Label(frame_top, text=SettingFileService.read_config(SettingKeys.image_output_folder))
        self.label_output.pack(side=tk.LEFT)

        ttk.Separator(self.root, orient='horizontal').pack(side=tk.TOP, fill=tk.X, pady=5)

        self.check_value = tk.BooleanVar(value = SettingFileService.read_config(SettingKeys.use_fusion_template))
        self.check_box = tk.Checkbutton(self.root, text="目パチや口パクが行えるFusionTemmplateとして出力する",
                                        variable=self.check_value, anchor='w', command=self.checkbox_update)
        self.check_box.pack(side=tk.TOP, anchor='w')

        ttk.Separator(self.root, orient='horizontal').pack(side=tk.TOP, fill=tk.X, pady=5)

        frame_main = tk.Frame(self.root)
        frame_main.pack(side=tk.TOP, fill=tk.BOTH, pady=5)

        frame_left = tk.Frame(frame_main)
        frame_left.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        frame_right = tk.Frame(frame_main)
        frame_right.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        self.list_box = tk.Listbox(frame_left)
        self.list_box.pack(pady=5)

        self.list_box.bind('<<ListboxSelect>>', self.on_select)

        label_mepachi = tk.Label(frame_right, text="目パチ")
        label_mepachi.pack()

        frame_entry_mepachi_group = tk.Frame(frame_right)
        frame_entry_mepachi_group.pack(fill=tk.X)

        label_closed_eye_group = tk.Label(frame_entry_mepachi_group, text="グループ：")
        label_closed_eye_group.pack(side=tk.LEFT)

        self.entry_mepachi_group = tk.Entry(frame_entry_mepachi_group)
        self.entry_mepachi_group.pack(side=tk.LEFT)
        self.entry_mepachi_group.bind("<Button-1>", lambda event, parent_group="": self.on_entry_click(event, parent_group))

        frame_entry_mepachi = tk.Frame(frame_right)
        frame_entry_mepachi.pack(fill=tk.X)

        label_closed_eye = tk.Label(frame_entry_mepachi, text="閉じた目：")
        label_closed_eye.pack(side=tk.LEFT)

        self.entry_mepachi = tk.Entry(frame_entry_mepachi)
        self.entry_mepachi.pack(side=tk.LEFT)
        self.entry_mepachi.bind("<Button-1>",
                                        lambda event, parent_group=self.entry_mepachi_group: self.on_entry_click(event, parent_group))

        label_kuchipaku = tk.Label(frame_right, text="口パク")
        label_kuchipaku.pack()

        frame_entry_kuchipaku_group = tk.Frame(frame_right)
        frame_entry_kuchipaku_group.pack(fill=tk.X)

        label_closed_mouth_group = tk.Label(frame_entry_kuchipaku_group, text="グループ：")
        label_closed_mouth_group.pack(side=tk.LEFT)

        self.entry_kuchipaku_group = tk.Entry(frame_entry_kuchipaku_group)
        self.entry_kuchipaku_group.pack(side=tk.LEFT)
        self.entry_kuchipaku_group.bind("<Button-1>", lambda event, parent_group="": self.on_entry_click(event, parent_group))

        frame_entry_kuchipaku = tk.Frame(frame_right)
        frame_entry_kuchipaku.pack(fill=tk.X)

        label_closed_mouth = tk.Label(frame_entry_kuchipaku, text="閉じた口：")
        label_closed_mouth.pack(side=tk.LEFT)

        self.entry_kuchipaku = tk.Entry(frame_entry_kuchipaku)
        self.entry_kuchipaku.pack(side=tk.LEFT)
        self.entry_kuchipaku.bind("<Button-1>",
                                        lambda event, parent_group=self.entry_kuchipaku_group: self.on_entry_click(event, parent_group))

        frame_buttons = tk.Frame(frame_right)
        frame_buttons.pack(pady=5)

        button_init = tk.Button(frame_buttons, text="初期構築を行う", command=self.on_init_button_click)
        button_init.pack(side=tk.LEFT, padx=5)

        button_save = tk.Button(frame_buttons, text="設定を保存する", command=self.on_save_button_click)
        button_save.pack(side=tk.LEFT, padx=5)

    def on_select(self, event):
        # Get selected line index
        index = self.list_box.curselection()[0]
        # Get the line's text
        item = self.list_box.get(index)
        # Check which entry is focused and set its content to the selected item
        if self.entry_mepachi == self.root.focus_get() and self.entry_mepachi_group.get() != "":
            self.entry_mepachi.delete(0, 'end')
            self.entry_mepachi.insert(0, item)
        elif self.entry_kuchipaku == self.root.focus_get() and self.entry_kuchipaku_group.get() != "":
            self.entry_kuchipaku.delete(0, 'end')
            self.entry_kuchipaku.insert(0, item)
        elif self.entry_kuchipaku_group == self.root.focus_get():
            self.entry_kuchipaku_group.delete(0, 'end')
            self.entry_kuchipaku_group.insert(0, item)
        elif self.entry_mepachi_group == self.root.focus_get():
            self.entry_mepachi_group.delete(0, 'end')
            self.entry_mepachi_group.insert(0, item)

    def on_entry_click(self, event, parent_group):
        print(event.widget)
        self.list_box.delete(0, tkinter.END)
        if parent_group == "":
            items = [i for i in self.psd_layer_list if i[3] is False]
            for item in items:
                self.list_box.insert(tk.END, item[0])
        else:
            print(parent_group.get())
            items = [i for i in self.psd_layer_list if i[2] == parent_group.get()]
            for item in items:
                self.list_box.insert(tk.END, item[0])

    def on_output_button_click(self):
        try:
            directory_path = filedialog.askdirectory()
            if directory_path != "":
                SettingFileService.update_and_save_config(SettingKeys.image_output_folder, directory_path)
                self.label_output.config(text=directory_path)
        except Exception as e:
            messagebox.showerror("error", e.__str__())

    def on_init_button_click(self):
        print("Init button clicked")

    def on_save_button_click(self):
        print("Save button clicked")

    def checkbox_update(self):
        SettingFileService.update_and_save_config(SettingKeys.use_fusion_template, self.check_value.get())

    def run(self):
        self.root.mainloop()
