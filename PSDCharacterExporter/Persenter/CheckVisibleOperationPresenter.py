from typing import List

from Domain.DTO.CheckVisibleOperation import CheckVisibleOperation
from Usecase.CheckVisibleLayer import CheckVisibleLayer


class CheckVisibleOperationPresenter:
    def __init__(self, visible_list: List):
        self._last_list = visible_list
        self._check_layer = CheckVisibleLayer()

    def check_visible_layer(self, visible_list: List):
        check_op = CheckVisibleOperation(self._last_list, visible_list)
        self._last_list = visible_list

        req_list = self._check_layer.execute(check_op)

        # last_listのアップデート
        for req in req_list:
            if req["item"] in visible_list:
                if req["checked"] is True:
                    visible_list.append(req["item"])
                else:
                    visible_list.remove(req["item"])

        return req_list
