from Domain.DTO.CheckVisibleOperation import CheckVisibleOperation
from Service.PsdMemorySaverService import PsdMemorySaverService


class CheckVisibleLayer:
    def __init__(self):
        pass

    def execute(self, check_visible_operation: CheckVisibleOperation) -> list:
        psd = PsdMemorySaverService.get_psd()

        psd.top_layer_group.select_layers_by_operation(check_visible_operation)

        # 気を使ってDomain側のcheck状態を入れて返してる、場合によってはいらないかもだけど
        mod_req = check_visible_operation.create_modification_request_list(
            psd.top_layer_group.dump_visible_layer_id_names())

        PsdMemorySaverService.set_psd(psd)

        return mod_req
