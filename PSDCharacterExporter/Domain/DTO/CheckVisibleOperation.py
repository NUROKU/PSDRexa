from typing import List


class CheckVisibleOperation:

    def __init__(self, original_check_list, update_check_list):
        self._original_check_list = original_check_list
        self._update_check_list = update_check_list
        self._diff_items = list(set(original_check_list) ^ set(update_check_list))

        self._diff_list = []
        # self._check_req_list = []

        self._modification_request_list = []

        if self._diff_items is []:
            return

        for diff in self._diff_items:
            is_checked = False if diff in self._original_check_list else True
            self._diff_list.append({"item": diff, "checked": is_checked})

    # @property
    # def check_req_list(self):
    #     return self._check_req_list

    def create_modification_request_list(self, domain_visible_layers) -> List:
        # domain側とPresenterから貰ったリストを比較して、差分があればmodificaton_listに追加
        modification_request_list = []
        diff_items = list(set(domain_visible_layers) ^ set(self._update_check_list))
        for diff in diff_items:
            is_checked = True if diff in domain_visible_layers else False
            modification_request_list.append({"item": diff, "checked": is_checked})

        return modification_request_list

    def checked_list(self):
        return [item["item"] for item in self._diff_list if item["checked"] is True]

    def unchecked_list(self):
        return [item["item"] for item in self._diff_list if item["checked"] is False]
