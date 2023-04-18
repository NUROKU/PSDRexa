"""
Psdのメタデータ、レイヤーとグループ以外の情報は一旦全部ここに
"""
from pathlib import Path


class PsdMeta:
    def __init__(self, file_path: Path):
        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path
