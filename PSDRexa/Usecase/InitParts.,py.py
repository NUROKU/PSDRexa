from Service.PsdMemorySaverService import PsdMemorySaverService


class InitParts:
    def __init__(self):
        init_parts_repo = ""

        pass
    def execute(self):
        psd = PsdMemorySaverService.get_psd()

        self.init_parts_repo.save_composited_image(composited_image)