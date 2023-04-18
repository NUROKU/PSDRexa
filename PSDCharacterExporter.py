import sys
import os

# Windows用のパス
windows_path_base = "C:\\ProgramData\\Blackmagic Design\\DaVinci Resolve\\Fusion\\Modules\\PSDCharacterExporter"

# Mac用のパス
mac_path_base = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Modules/PSDCharacterExporter"

# 使用するパスの選択
path_base = windows_path_base if os.name == 'nt' else mac_path_base

# パスの追加
sys.path.append(path_base)
sys.path.append(os.path.join(path_base, "module"))

from UI.main_ui import MainUI

ui = MainUI(resolve)
ui.execute_ui()
