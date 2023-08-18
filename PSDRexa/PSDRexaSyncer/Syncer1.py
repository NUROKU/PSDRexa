import random

from PSDRexaSyncer.BaseSyncer import BaseSyncer
from PSDRexaSyncer.SyncTask import SyncTask


class Syncer1(BaseSyncer):
    def _sync(self, task: SyncTask):
        video_len = task.video_item.GetDuration()
        fusion_obj = task.video_item.GetFusionCompByIndex(1).FindTool("CustomTool1")
        fusion_obj.CurrentTime = 0
        index = 0
        for _ in range(0, video_len):
            fusion_obj.NumberIn1[index] = random.uniform(0.0, 100.0)
            index += 1
        fusion_obj.NumberIn1[video_len + 1] = 0
