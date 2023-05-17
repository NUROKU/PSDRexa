# PSDCharacterExporter
Export PSD Character Image for DaVinci Resolve

PSD立ち絵素材をいい感じに画像出力するやつ

# 機能
- PSD画像読み込み、選択
- 画像として出力かつタイムラインに配備

# 必要動作環境
- DaVinci Resolve 18  
- Python 3.9  
PythonはインストールしてDaVinciResolve上で使えるようにしておいてください  
ワークスペース→コンソール→Py3を選択してエラーメッセージが出力されなければ使える環境になってます。  
[Python3.9のインストールはここから](https://www.python.org/downloads/release/python-3913/)

# 対応OS
- Windows  
- Mac  
Macでうまく動かない場合、セキュリティが悪さをしている場合があります。もしくはバグ

# インストール方法
ダウンロードしたzipファイルを解凍し、適切なフォルダに配備してください。

# インストール手順
ダウンロードしたzipファイルを解凍し、適切なフォルダに配置してください。

Windows向け：
1. PSDCharacterExporter（フォルダ）  
   配置先：C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules
2. PSDCharacterExporter.py  
   配置先：C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility

Mac向け：
1. PSDCharacterExporter（フォルダ）  
   配置先：/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Modules
2. PSDCharacterExporter.py  
   配置先：/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility

インストールに成功した場合、ワークスペース→スクリプトからPSDCharacterExporterが選択できるようになっています

------------------------------

※DaVinci Resolveを特定のユーザーフォルダ配下にインストールしていた場合、{ユーザ名}をインストール先のユーザ名に置き換えた上で以下のフォルダに配置してください。

Windows向け：
1. PSDCharacterExporter（フォルダ）  
   配置先：C:\Users\{ユーザ名}\AppData\Local\Blackmagic Design\DaVinci Resolve\Fusion\Modules
2. PSDCharacterExporter.py  
   配置先：C:\Users\{ユーザ名}\AppData\Local\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility

Mac向け：
1. PSDCharacterExporter（フォルダ）  
   配置先：/Users/{ユーザ名}/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Modules
2. PSDCharacterExporter.py  
   配置先：/Users/{ユーザ名}/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility

-------------
### 設定の説明
* 画像出力先：PSD画像のローカルの出力先
* 基ファイルのサイズで画像出力：ONの場合は読み込まれたPSDと同じサイズの立ち絵が出力される。OFFの場合は縦横比を維持しつつHeight,Widthで指定したサイズで出力される。
* 基ファイルのサイズでプレビュー：本ツールのプレビュー用の立ち絵画像のサイズ
* psdtoolkitの機能を使用：ONの場合ラジオボタンや!に対応してPSDを読み込む。OFFの場合は全部チェックボックスで読み込む

### Python3.9以外を使いたい
下記コマンドを実行して、同梱物のmoduleフォルダを置き換えてください

pip install -r requirements.txt -t module

# ライセンス
このプロジェクトは、GNU General Public License v3.0 (GPL-3.0) ライセンスの下でライセンスされています。

# 連絡バグ報告等
Twitter: @nu_ro_ku
