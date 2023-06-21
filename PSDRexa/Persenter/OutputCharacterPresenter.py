from Usecase.OutputCharactor import OutputCharacter


class OutputCharacterPresenter:
    def __init__(self):
        self._character_usecase = OutputCharacter()

    def output_character(self):
        self._character_usecase.execute()
