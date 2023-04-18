from PIL.Image import Image

from Usecase.CombineLayer import CombineLayer


class CombineLayerPresenter:
    def __init__(self):
        self._combine_layer = CombineLayer()

    def get_combine_layer(self, size_x: int, size_y: int) -> Image:
        return self._combine_layer.execute(size_x, size_y)
