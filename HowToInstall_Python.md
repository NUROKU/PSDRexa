# DaVinciResolveへのPython導入方法
1. Python3.9のインストール→[ここからダウンロードできます](https://www.python.org/downloads/release/python-3913/)  
インストーラ起動時に「Add Python 3.9 to PATH」にチェックを入れてインストールしてください

2. DaVinciResolveを起動し適当なプロジェクトを開き、「ワークスペース」→「コンソール」を開き、「Py3」をクリック  
これで何もメッセージが出なかったら正常にPython3.9がDaVinciResolveで使えるという事になります。

--------------------------------

## 上記手順でDaVinciResolveがPython3.9を認識しなかった場合

PCの環境変数に下記を追加してください
>変数名：PYTHONHOME  
変数値：Python3.9が置かれているディレクトリ

変数値のディレクトリははWindowsだと恐らく下記  
C:\Users\{ユーザ名}\AppData\Local\Programs\Python\Python39\

-------------------------------

## わけあってPython3.9以外のバージョンを使いたい
下記コマンドを特定のPythonのバージョンで実行して、同梱物のmoduleフォルダを置き換えてください

pip install -r requirements.txt -t module

（Mac版やりぞりぷと対応版は、このmoduleフォルダの中身を各OS,各対応バージョンでinstallしているだけだったり…）