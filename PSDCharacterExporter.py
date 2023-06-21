import sys
import os

# Windows用のパス
windows_path_base = "C:\\ProgramData\\Blackmagic Design\\DaVinci Resolve\\Fusion\\Modules\\PSDRexa"
windows_user_path_base = os.path.join(os.environ.get("USERPROFILE",""), "AppData\\Local\\Blackmagic Design\\DaVinci Resolve\\Fusion\\Modules\\PSDRexa")

# Mac用のパス
mac_path_base = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Modules/PSDRexa"
mac_user_path_base = os.path.join(os.environ.get("HOME",""), "Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Modules/PSDRexa")

# 使用するパスの選択
if os.name == 'nt':
    path_base = windows_path_base
    user_path_base = windows_user_path_base
else:
    path_base = mac_path_base
    user_path_base = mac_user_path_base

# パスの追加
sys.path.append(path_base)
sys.path.append(os.path.join(path_base, "module"))

# ユーザーごとのインストールパスが存在する場合、そのパスも追加
if os.path.exists(user_path_base):
    sys.path.append(user_path_base)
    sys.path.append(os.path.join(user_path_base, "module"))

from UI.main_ui import MainUI

ui = MainUI(resolve)
ui.execute_ui()