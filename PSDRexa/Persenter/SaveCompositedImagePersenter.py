from Usecase.SaveCompositedImage import SaveCompositedImage


class SaveCompositedImagePersenter:
    def __init__(self):
        self._save_composited_image_usecase = SaveCompositedImage()
        pass

    def save_composited_image_persenter(self, int_x, int_y):
        self._save_composited_image_usecase.execute(int_x, int_y)
        pass
