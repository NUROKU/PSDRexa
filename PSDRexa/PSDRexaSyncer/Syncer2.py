import os
import struct
import wave

from PSDRexaSyncer.BaseSyncer import BaseSyncer
from PSDRexaSyncer.SyncTask import SyncTask


class Syncer2(BaseSyncer):
    def _sync(self, task: SyncTask):
        audio_wav = [0.0] * task.video_item.GetDuration()
        for audio in task.sync_audio_clip_list:
            with wave.open(audio.audio_item.GetMediaPoolItem().GetClipProperty('File Path'), 'rb') as wav_file:
                params = wav_file.getparams()

                # このあたり某人工知能に聞いた
                frames = wav_file.readframes(params.nframes)
                unpacked_frames = struct.unpack('<' + 'h' * params.nframes, frames)
                volumes = [abs(amplitude) for amplitude in unpacked_frames]

                frame_length = params.framerate // self.frame_rate
                frames_volumes = [sum(volumes[i:i + frame_length]) / frame_length for i in
                                  range(0, len(volumes), frame_length)]

                index = audio.start_diff
                if audio.start_diff < 0:
                    del frames_volumes[:abs(audio.start_diff)]
                    index = 0
                audio_wav[index:len(frames_volumes)] = frames_volumes

        fusion_obj = task.video_item.GetFusionCompByIndex(1).FindTool("CustomTool1")
        fusion_obj.CurrentTime = 0
        index = 0

        for _ in range(0, len(audio_wav)):
            fusion_obj.NumberIn2[index] = audio_wav[index]
            index += 1
