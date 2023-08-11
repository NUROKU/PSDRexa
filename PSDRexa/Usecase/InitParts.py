from Repository.PartsRepository import PartsRepository
from Service.PsdMemorySaverService import PsdMemorySaverService
from Domain.DTO.CharacterPartsSet import CharacterPartsSet


class InitParts:
    def __init__(self):
        self.init_parts_repo = PartsRepository()

    def execute(self, parts_list):

        for part in parts_list:
            self.init_parts_repo.save_parts(part)
