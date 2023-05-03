from pathlib import Path

from Exception.DataStoreError import DataStoreError
from module.PIL.Image import Image


class CompositedImageDataStore:
    def __init__(self):
        pass

    def output_composited_image(self, composted_image: Image, save_path: Path):
        try:
            composted_image.save(save_path)
        except Exception:
            # 雑だね
            raise DataStoreError("立ち絵画像の保存に失敗しました。出力先フォルダ指定が正しいか確認してください")
