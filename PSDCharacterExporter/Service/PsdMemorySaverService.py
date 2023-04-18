from Domain.Psd.Psd import Psd
from Exception.ServiceError import ServiceError


class PsdMemorySaverService:
    psd = None

    @staticmethod
    def set_psd(psd: Psd):
        PsdMemorySaverService.psd = psd

    @staticmethod
    def get_psd() -> Psd:
        if PsdMemorySaverService.psd is None:
            raise ServiceError("psdの再読み込みに失敗しました")
        return PsdMemorySaverService.psd

    # NOTE psdをリスト型に持たせたら複数個扱えるようになるのかな、なりたいな
