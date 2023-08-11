from os.path import dirname, abspath
from pathlib import Path

from Service.ResolveService import ResolveService


class PSDRexaTemplateService:
    @staticmethod
    def init_template():
        resolve = ResolveService.get_resolve()

        project_manager = resolve.GetProjectManager()
        project = project_manager.GetCurrentProject()
        media_pool = project.GetMediaPool()

        existing_bins = media_pool.GetRootFolder().GetSubFolderList()
        existing_bin = None
        for bin in existing_bins:
            if bin.GetName() == "PSDRexa":
                existing_bin = bin
                break

        if existing_bin is None:
            media_pool = project.GetMediaPool()
            file_path = str(Path(dirname(abspath(__file__)), "PSDRexa.drb"))
            media_pool.ImportFolderFromFile(
                file_path)

