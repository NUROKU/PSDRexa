import tkinter

from Common import Logger
from PIL import Image
from Persenter.CombineLayerPresenter import CombineLayerPresenter
from module.PIL import ImageTk

logger = Logger.get_logger(__name__)


class CompositedImageCanvas(tkinter.Canvas):
    def __init__(self, master=None, **kw):
        super().__init__(master)
        self._combine_layer = CombineLayerPresenter()
        self._photo_image = ImageTk.PhotoImage(Image.new("RGB", (1, 1), (0, 0, 0)))
        self._item = self.create_image(0, 0, image=self._photo_image, anchor=tkinter.NW)

        self.bind("<Configure>", self.on_resize)
        self.width = self.winfo_width()
        self.height = self.winfo_height()

    def update_compositedImage(self):
        img = self._combine_layer.get_combine_layer(self.winfo_width(), self.winfo_height())
        self._photo_image = ImageTk.PhotoImage(img)
        self.itemconfig(self._item, image=self._photo_image)

    def on_resize(self, event):
        # 高さが変わってなかったら無視。
        if event.height == self.height:
            return
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.update_compositedImage()
