import os
from pathlib import Path

from Service.PsdMemorySaverService import PsdMemorySaverService
from module.PIL.Image import Image


class PartsDataStore:
    def __init__(self):
        pass

    def save_parts(self, folder_path: Path, file_name: str, image: Image):
        folder_path.mkdir(parents=True, exist_ok=True)
        filepath = folder_path / file_name
        image.save(filepath)
