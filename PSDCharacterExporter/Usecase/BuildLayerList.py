from pathlib import Path

from Domain.Psd.PsdTopGroupLayer import PsdTopGroupLayer
from Repository.PsdRepository import PsdRepository
from Service.PsdMemorySaverService import PsdMemorySaverService


class BuildLayerList:
    def __init__(self):
        self._psd_repo = PsdRepository()

    def execute(self, psd_file_path: Path) -> PsdTopGroupLayer:
        psd = self._psd_repo.get_psd(psd_file_path)
        PsdMemorySaverService.set_psd(psd)

        return psd.top_layer_group
