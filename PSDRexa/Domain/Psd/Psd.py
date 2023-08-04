from Domain.Psd.PsdMeta import PsdMeta
from Domain.Psd.PsdTop import PsdTop


class Psd:
    def __init__(self, psd_meta: PsdMeta, psd_top_layer_group: PsdTop):
        self._meta = psd_meta
        self._top = psd_top_layer_group

    @property
    def top(self):
        return self._top
