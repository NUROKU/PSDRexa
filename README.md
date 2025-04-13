# PSDRexa
Export PSD Character Image for DaVinci Resolve

PSD立ち絵素材をいい感じにDaVinciResolveで使えるようにするやつ

# 機能
- PSD画像読み込み、選択
- 画像として出力かつタイムラインに配備
- 口パク目パチできるFusionとして出力してタイムラインに配備

# 必要動作環境
- DaVinci Resolve 18.5以上  
- Python 3.6以上 3.12以下
PythonはインストールしてDaVinciResolve上で使えるようにしておいてください  
ワークスペース→コンソール→Py3を選択してエラーメッセージが出力されなければ使える環境になってます。
[Pythonインストール手順はここから](./HowToInstall_Python.md)

# 対応OS
- Windows  
- Mac  
Macでうまく動かない場合、セキュリティ権限周りが悪さをしている場合があります。もしくはバグ  
また、MacのApp版を使用している場合に正常に動作しない場合があるらしいです。

# インストール手順
ダウンロードしたzipファイルを解凍し、Installerを実行してください。オンライン環境でしか動作しない点に注意してください

Windows向け：
* PSDRexa_WinInstaller.batを実行してください

Mac向け：
+ PSDRexa_MacInstaller.commandを実行してください

インストールに成功した場合、ワークスペース→スクリプトからPSDRexaとPSDRexa_syncerが選択できるようになっています

-------------
### 設定の説明
* 画像出力先：PSD画像のローカルの出力先
* 基ファイルのサイズで画像出力：ONの場合は読み込まれたPSDと同じサイズの立ち絵が出力される。OFFの場合は縦横比を維持しつつHeight,Widthで指定したサイズで出力される。
* 基ファイルのサイズでプレビュー：本ツールのプレビュー用の立ち絵画像のサイズ
* psdtoolkitの機能を使用：ONの場合ラジオボタンや!に対応してPSDを読み込む。OFFの場合は全部チェックボックスで読み込む

### 出力目パチ口パク設定の説明
* 画像出力先：PSD画像のローカルの出力先
* 目パチや口パクが行えるFusionTemplateとして出力する：ONにすると目パチ口パクできるFusionで出力される
* その他いろいろ：目パチ口パクとかの設定

### 目パチ口パク用手順

1 ~ 4の手順で目パチができます。口パクもしたい場合は5以降の手順も踏んでください
1. 目パチ口パク設定を開き、「目パチや口パクが行えるFusionTemplateとして出力する」にする
2. 目パチ口パク用のグループや閉じた状態のグループ/レイヤーを選択する。挙動としては
   * 入力するところをクリックすると左側のリストボックスに候補が現れる
   * 候補の名前の先頭に番号(レイヤーを上から並べた順)が付いています。
3. 「目パチ口パク用のパーツ出力」をクリック
   * この処理は時間がかかる場合があります
4. PSDRexaに戻って立ち絵を出力すると、DaVinciResolve上で目パチする立ち絵ができます。
5. DaVinci Resolveのワークスペース→スクリプトからPSDRexa_syncerを選択し、実行してください
   * video_track : 口パクしたい立ち絵が置かれているビデオトラック、V1なら1でV2なら2...
   * audio_track : 口パクを行う基となる音声ファイルが置かれているオーディオトラック、A1なら1でA2なら2...
   * audio_folder_path : 口パクを行う基となる音声ファイルが置かれているローカルのフォルダー
   * 口パクSync：口パクを反映させます。実行完了すると横に「Done」と表示されます
   * 目パチのキーフレームを再構築：指定されたvideo_track上にある立ち絵の目パチキーフレームを再構築します
   
--------------

# ライセンス
このプロジェクトは、GNU General Public License v3.0 (GPL-3.0) ライセンスの下でライセンスされています。

# 連絡バグ報告等
Twitter: @nu_ro_ku
