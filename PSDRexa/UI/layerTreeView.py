import os
from pathlib import Path
from tkinter import ttk, filedialog, messagebox

from PIL import Image
from Persenter.CheckVisibleOperationPresenter import CheckVisibleOperationPresenter
from Persenter.LayerListPersenter import LayerListPresenter
from Service.OutputSettingFile.OutputSettingFileService import OutputSettingFileService
from UI.CompositedImageCanvas import CompositedImageCanvas
from module.PIL import ImageTk
from ttkwidgets import CheckboxTreeview
from ttkwidgets.checkboxtreeview import IM_CHECKED, IM_UNCHECKED, IM_TRISTATE


class LayerTreeview(CheckboxTreeview):
    # https://github.com/TkinterEP/ttkwidgets/blob/master/ttkwidgets/checkboxtreeview.py
    # checkTreeViewはGPLライセンスなので、必然的にこのソースコードもGPLライセンスになる。
    # 多分このあたりのGUIをMITとかで配布されてる別のライブラリに置き換えたらライセンス変えれる。

    def __init__(self, master=None, canvas: CompositedImageCanvas = None, **kw):
        ttk.Treeview.__init__(self, master, style='Checkbox.Treeview', **kw)
        # style (make a noticeable disabled style)
        style = ttk.Style(self)
        style.map("Checkbox.Treeview",
                  fieldbackground=[("disabled", '#E6E6E6')],
                  foreground=[("disabled", 'gray40')],
                  background=[("disabled", '#E6E6E6')])
        # checkboxes are implemented with pictures
        self.im_checkbox_on = ImageTk.PhotoImage(Image.open(IM_CHECKED), master=self)
        self.im_checkbox_off = ImageTk.PhotoImage(Image.open(IM_UNCHECKED), master=self)
        self.im_radiobutton_on = ImageTk.PhotoImage(
            Image.open(os.path.join(self._get_assets_directory(), "Radio_on.png")), master=self)
        self.im_radiobutton_off = ImageTk.PhotoImage(
            Image.open(os.path.join(self._get_assets_directory(), "Radio_off.png")), master=self)
        self.im_visible = ImageTk.PhotoImage(Image.open(IM_TRISTATE), master=self)
        self._get_assets_directory()

        self.tag_configure("checkbox_on", image=self.im_checkbox_on)
        self.tag_configure("checkbox_off", image=self.im_checkbox_off)
        self.tag_configure("radiobutton_on", image=self.im_radiobutton_on)
        self.tag_configure("radiobutton_off", image=self.im_radiobutton_off)
        self.tag_configure("visible_on", image=self.im_visible)
        self.tag_configure("visible_off", image=self.im_checkbox_off)

        # check / uncheck boxes on click
        self.bind("<Button-1>", self._box_click, True)

        self._canvas = canvas
        self._layer_list_presenter = LayerListPresenter()

        try:
            file_path = Path(filedialog.askopenfilename(title="PSDファイルを選択してください", filetypes=[('psdファイル', '*.psd')]))
            OutputSettingFileService.init_output_setting(os.path.splitext(os.path.basename(file_path))[0])
            tree_list = self._layer_list_presenter.get_layer_list(file_path)

            for tree_item in tree_list:
                self.insert(tree_item[0], 0, tree_item[1], text=tree_item[2])
                if tree_item[3] is True:
                    if tree_item[4] in ["GroupLayer", "ImageLayer"]:
                        self.change_state(tree_item[1], 'checkbox_on')
                    elif tree_item[4] in ["OneSelectGroupLayer", "OneSelectImageLayer"]:
                        self.change_state(tree_item[1], 'radiobutton_on')
                    elif tree_item[4] == "VisibleGroupLayer":
                        self.change_state(tree_item[1], 'visible_on')
                else:
                    if tree_item[4] in ["GroupLayer", "ImageLayer"]:
                        self.change_state(tree_item[1], 'checkbox_off')
                    elif tree_item[4] in ["OneSelectGroupLayer", "OneSelectImageLayer"]:
                        self.change_state(tree_item[1], 'radiobutton_off')
                    elif tree_item[4] == "VisibleGroupLayer":
                        self.change_state(tree_item[1], 'visible_off')
            self._check_visible_operation_presenter = CheckVisibleOperationPresenter([])
            self._update_canvas()
        except Exception as e:
            messagebox.showerror("error", f"{e.__str__()}アプリケーションを終了します。")
            exit()
        # self._update_canvas()

    def _get_assets_directory(self):
        return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Resources"))

    def _update_canvas(self):
        mod_req = self._check_visible_operation_presenter.check_visible_layer(self.get_checked())
        for req in mod_req:
            if req["checked"]:
                self._turn_on(req["item"])
            else:
                self._turn_off(req["item"])
        self._canvas.update_compositedImage()

    def _turn_on(self, item):
        if self.tag_has("checkbox_off", item):
            self.change_state(item, "checkbox_on")
        elif self.tag_has("radiobutton_off", item):
            self.change_state(item, "radiobutton_on")
        elif self.tag_has("visible_off", item):
            self.change_state(item, "visible_on")

    def _turn_off(self, item):
        if self.tag_has("checkbox_on", item):
            self.change_state(item, "checkbox_off")
        elif self.tag_has("radiobutton_on", item):
            self.change_state(item, "radiobutton_off")
        elif self.tag_has("visible_on", item):
            self.change_state(item, "visible_off")

    def _is_turned_on(self, item) -> bool:
        return self.tag_has("checkbox_on", item) or self.tag_has("radiobutton_on", item) or self.tag_has("visible_on",
                                                                                                         item)

    def get_checked(self):
        """Return the list of checked items that do not have any child."""
        checked = []

        def get_checked_children(item):
            if self._is_turned_on(item):
                checked.append(item)

            ch = self.get_children(item)
            for c in ch:
                get_checked_children(c)

        ch = self.get_children("")
        for c in ch:
            get_checked_children(c)
        return checked

    def change_state(self, item, state):
        """
        Replace the current state of the item.
        i.e. replace the current state tag but keeps the other tags.

        :param item: item id
        :type item: str
        :param state: "checked", "unchecked" or "tristate": new state of the item
        :type state: str
        """
        tags = self.item(item, "tags")
        states = ["checkbox_on", "checkbox_off", "radiobutton_on", "radiobutton_off", "visible_on", "visible_off"]
        new_tags = [t for t in tags if t not in states]
        new_tags.append(state)
        self.item(item, tags=tuple(new_tags))

    def insert(self, parent, index, iid=None, **kw):
        """
        Creates a new item and return the item identifier of the newly created item.

        :param parent: identifier of the parent item
        :type parent: str
        :param index: where in the list of parent's children to insert the new item
        :type index: int or "end"
        :param iid: item identifier, iid must not already exist in the tree. If iid is None a new unique identifier is generated.
        :type iid: None or str
        :param kw: other options to be passed on to the :meth:`ttk.Treeview.insert` method

        :return: the item identifier of the newly created item
        :rtype: str
        .. note:: Same method as for the standard :class:`ttk.Treeview` but
                  add the tag for the box state accordingly to the parent
                  state if no tag among
                  ('checked', 'unchecked', 'tristate') is given.
        """
        tag = "tmp"
        if "tags" not in kw:
            kw["tags"] = (tag,)
        elif not (
                ["checkbox_on", "checkbox_off", "radiobutton_on", "radiobutton_off", "visible_on", "visible_off"] in kw[
            "tags"]):
            kw["tags"] += (tag,)

        return ttk.Treeview.insert(self, parent, index, iid, **kw)

    def _box_click(self, event):
        """Check or uncheck box when clicked."""
        x, y, widget = event.x, event.y, event.widget
        elem = widget.identify("element", x, y)
        if "image" in elem:
            # a box was clicked
            item = self.identify_row(y)
            if self._is_turned_on(item):
                self._turn_off(item)
            else:
                self._turn_on(item)

            self._update_canvas()

    def get_all_item(self, only_group=False):
        items = []

        def get_childrens(item):
            ch = self.get_children(item)
            if not (ch is () and only_group):
                items.append(item)
            for c in ch:
                get_childrens(c)

        ch = self.get_children("")
        for c in ch:
            get_childrens(c)

        return items

    def get_all_item_viewer_name(self, only_group=False):
        items = []

        def get_childrens(item):
            ch = self.get_children(item)
            if not (ch is () and only_group):
                items.append(self.item(item)["text"])
            for c in ch:
                get_childrens(c)

        ch = self.get_children("")
        for c in ch:
            get_childrens(c)
        return items
