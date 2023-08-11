from pathlib import Path

from Domain.Psd.PsdTop import PsdTop
from Repository.PsdRepository import PsdRepository
from Service.PsdMemorySaverService import PsdMemorySaverService


class BuildLayerList:
    def __init__(self):
        self._psd_repo = PsdRepository()

    def execute(self, psd_file_path: Path) -> PsdTop:
        psd = self._psd_repo.get_psd(psd_file_path)
        PsdMemorySaverService.set_psd(psd)

        return psd.top
