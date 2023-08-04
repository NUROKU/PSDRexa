from Domain.DTO.CharacterPartsSet import CharacterPartsSet


class PartsRepository:
    def __init__(self):
        self._parts_datastore = PartsDataStore()

    def save_parts(self, parts:CharacterPartsSet):
        pass
