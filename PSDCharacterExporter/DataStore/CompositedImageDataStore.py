from pathlib import Path

from module.PIL.Image import Image


class CompositedImageDataStore:
    def __init__(self):
        pass

    def output_composited_image(self, composted_image: Image, save_path: Path):
        composted_image.save(save_path)
