class ResolveService:
    resolve = None

    @staticmethod
    def set_resolve(resolve):
        if "GetProjectManager" in dir(resolve):
            ResolveService.resolve = resolve
        else:
            return
            # TODO 警告出せるようにしときたいけど実装面倒なんであとまわし
            # raise ServiceError("DaVinci Resolveの読み込みに失敗しました")

    @staticmethod
    def get_resolve():
        if ResolveService.resolve is None:
            # raise ServiceError("DaVinci Resolveの読み込みに失敗しました")
            return None
        return ResolveService.resolve

    @staticmethod
    def get_framerate():
        return ResolveService.get_resolve().GetProjectManager().GetCurrentProject().GetSetting('timelineFrameRate')

    @staticmethod
    def get_startframe():
        # framerate = ResolveService.get_framerate()
        # timeline = ResolveService.get_resolve().GetProjectManager().GetCurrentProject().GetCurrentTimeline()
        # start_timecode = timeline.GetStartTimecode()
        #
        # time_parts = start_timecode.split(':')
        # hours, minutes, seconds, frames = [int(part) for part in time_parts]
        # total_frames = hours * 3600 * framerate + minutes * 60 * framerate + seconds * framerate
        timeline = ResolveService.get_resolve().GetProjectManager().GetCurrentProject().GetCurrentTimeline()
        return timeline.GetStartFrame()
