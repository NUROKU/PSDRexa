import tkinter
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from Service.SettingFileService import SettingKeys, SettingFileService


class SettingWindow:
    def __init__(self):
        pass

    def execute(self):
        dlg_modal = tk.Toplevel()

        dlg_modal.title("設定")  # ウィンドウタイトル
        dlg_modal.geometry("600x200")

        def select_folder():
            folder_path = filedialog.askdirectory(
                initialdir=SettingFileService.read_config(SettingKeys.image_output_folder), title="select psd file")
            if folder_path != "":
                folder_path_label.config(text=folder_path)
            dlg_modal.lift()

        def save_settings():
            config_dict = {
                SettingKeys.image_output_folder: folder_path_label.cget("text"),
                SettingKeys.is_image_size_original: checkbox_var.get(),
                SettingKeys.image_output_size_x: int(number1_spinbox.get()),
                SettingKeys.image_output_size_y: int(number2_spinbox.get()),
                SettingKeys.is_image_preview_size_original: checkbox_var_2.get(),
                SettingKeys.image_preview_size_x: int(number3_spinbox.get()),
                SettingKeys.image_preview_size_y: int(number4_spinbox.get()),
                SettingKeys.use_psdtool_func: checkbox_var_3.get()
            }
            SettingFileService.update_and_save_configs(config_dict)
            messagebox.showinfo("Info", "設定が保存されました。アプリケーションを終了します。")
            # save_state_label.config(text="Save Done!")
            dlg_modal.quit()

        def exit():
            save_settings()
            dlg_modal.destroy()

        ### image_output_folder
        frame1 = tk.Frame(dlg_modal)
        folder_button = tk.Button(frame1, text="画像出力先", command=select_folder)
        folder_button.pack(side="left")
        folder_path_label = tk.Label(frame1, text=SettingFileService.read_config(SettingKeys.image_output_folder))
        folder_path_label.pack(side="left")
        frame1.pack(side="top", anchor=tk.W)

        sep1 = ttk.Separator(dlg_modal)
        sep1.pack(fill="both")

        ### image_size
        checkbox_var = tk.BooleanVar(value=SettingFileService.read_config(SettingKeys.is_image_size_original))
        checkbox = tk.Checkbutton(dlg_modal, text="基ファイルのサイズで画像出力", variable=checkbox_var)
        checkbox.pack(side="top", anchor=tk.W)

        image_size_frame1 = tk.Frame(dlg_modal)
        number1_label = tk.Label(image_size_frame1, text="Height:")
        number1_label.pack(side="left", anchor=tk.W)
        number1_spinbox = tk.Spinbox(image_size_frame1,
                                     from_=100, to=1920, increment=10,
                                     textvariable=tkinter.IntVar(
                                         value=SettingFileService.read_config(SettingKeys.image_output_size_x)))
        number1_spinbox.pack(side="left", anchor=tk.W)

        number2_label = tk.Label(image_size_frame1, text="Width:")
        number2_label.pack(side="left", anchor=tk.W)
        number2_spinbox = tk.Spinbox(image_size_frame1,
                                     from_=100, to=1280, increment=10,
                                     textvariable=tkinter.IntVar(
                                         value=SettingFileService.read_config(SettingKeys.image_output_size_y)))
        number2_spinbox.pack(side="left", anchor=tk.W)
        image_size_frame1.pack(side="top", anchor=tk.W)

        sep2 = ttk.Separator(dlg_modal)
        sep2.pack(fill="both")

        ### preview_image_size
        checkbox_var_2 = tk.BooleanVar(value=SettingFileService.read_config(SettingKeys.is_image_preview_size_original))
        checkbox_2 = tk.Checkbutton(dlg_modal, text="基ファイルのサイズでプレビュー", variable=checkbox_var_2)
        checkbox_2.pack(side="top", anchor=tk.W)

        image_size_frame2 = tk.Frame(dlg_modal)
        number3_label = tk.Label(image_size_frame2, text="Height:")
        number3_label.pack(side="left", anchor=tk.W)
        number3_spinbox = tk.Spinbox(image_size_frame2,
                                     from_=100, to=1920, increment=10,
                                     textvariable=tkinter.IntVar(
                                         value=SettingFileService.read_config(SettingKeys.image_preview_size_x)))
        number3_spinbox.pack(side="left", anchor=tk.W)

        # image_size_frame2 = tk.Frame(dlg_modal)
        number4_label = tk.Label(image_size_frame2, text="Width:")
        number4_label.pack(side="left", anchor=tk.W)
        number4_spinbox = tk.Spinbox(image_size_frame2,
                                     from_=100, to=1280, increment=10,
                                     textvariable=tkinter.IntVar(
                                         value=SettingFileService.read_config(SettingKeys.image_preview_size_y)))
        number4_spinbox.pack(side="left", anchor=tk.W)
        # image_size_frame2.pack(side="top", anchor=tk.W)
        image_size_frame2.pack(side="top", anchor=tk.W)

        sep3 = ttk.Separator(dlg_modal)
        sep3.pack(fill="both")
        #
        checkbox_var_3 = tk.BooleanVar(value=SettingFileService.read_config(SettingKeys.use_psdtool_func))
        checkbox_3 = tk.Checkbutton(dlg_modal, text="psdtoolkitの機能(*や!の変換)を使用", variable=checkbox_var_3)
        checkbox_3.pack(side="top", anchor=tk.W)

        # Button
        frame4 = tk.Frame(dlg_modal)
        save_button = tk.Button(frame4, text="Save_and_Exit", command=save_settings)
        save_button.pack(side="left")
        exit_button = tk.Button(frame4, text="Exit", command=exit)
        exit_button.pack(side="left")
        save_state_label = tk.Label(frame4, text="")
        save_state_label.pack(side="left")

        frame4.pack(side="top", anchor=tk.W)
