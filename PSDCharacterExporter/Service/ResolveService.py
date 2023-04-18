from Exception.ServiceError import ServiceError


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
            raise ServiceError("DaVinci Resolveの読み込みに失敗しました")
        return ResolveService.resolve
