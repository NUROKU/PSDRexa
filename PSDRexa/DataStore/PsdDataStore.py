from pathlib import Path

from Exception.DataStoreError import DataStoreError
from psd_tools import PSDImage


class PsdDataStore:
    def __init__(self):
        pass

    def get_psd(self, psd_file_path: Path):

        try:
            psd = PSDImage.open(psd_file_path, encoding="cp932")
        except Exception as e:
            raise DataStoreError("Failed to load the PSD file.")
        return psd
