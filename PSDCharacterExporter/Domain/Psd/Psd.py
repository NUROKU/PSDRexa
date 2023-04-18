from Domain.Psd.PsdMeta import PsdMeta
from Domain.Psd.PsdTopGroupLayer import PsdTopGroupLayer


class Psd:
    def __init__(self, psd_meta: PsdMeta, psd_top_layer_group: PsdTopGroupLayer):
        self._meta = psd_meta
        self._top_layer_group = psd_top_layer_group

    @property
    def top_layer_group(self):
        return self._top_layer_group
