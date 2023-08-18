from typing import List

from Domain.DTO.CharacterPartsSet import CharacterPartsSet
from Usecase.InitParts import InitParts


class InitPartsPresenter:
    def __init__(self):
        self.init_parts_usecase = InitParts()
        pass

    def init_parts(self, parts_list: List):
        ret_list = []
        for n in parts_list:
            ret_list.append(CharacterPartsSet(n))

        self.init_parts_usecase.execute(ret_list)
