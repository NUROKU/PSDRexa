# DaVinciResolveへのPython導入方法の推敲

## DaVinciResolveへのPython3.9の導入方法

1. Python3.9のインストール
   - [Python公式ウェブサイト](https://www.python.org/downloads/release/python-3913/)からPython3.9をダウンロードします。
   - インストーラを起動し、「Add Python 3.9 to PATH」にチェックを入れてインストールします。

2. DaVinciResolveでPython3.9を有効化する
   - DaVinciResolveを起動し、適当なプロジェクトを開きます。
   - 「ワークスペース」→「コンソール」を開きます。
   - 「Py3」をクリックします。
   - もし何もメッセージが表示されなければ、Python3.9が正常にDaVinciResolveで使用できるようになっています。

## DaVinciResolveがPython3.9を認識しない場合の対処方法

DaVinciResolveがPython3.9を認識しない場合は、PCの環境変数に以下の設定を追加してください。

- 変数名：PYTHONHOME
- 変数値：Python3.9のインストールされたディレクトリのパス

Windowsの場合、ディレクトリのパスはおそらく以下になります。

C:\Users\{ユーザ名}\AppData\Local\Programs\Python\Python39\

## Python3.9以外の特定のPythonバージョンを使用したい場合

もしPython3.9以外のバージョンを使用したい場合は、以下の手順で同梱物の"module"フォルダを置き換えてください。

1. 特定のPythonバージョンをインストールします。
2. コマンドプロンプトまたはターミナルで以下のコマンドを実行します。

```
pip install -r requirements.txt -t module
```

このコマンドで出力されたmoduleフォルダを同梱物のに置き換えてください。

(Mac版やりぞりぷと版はmoduleフォルダの中身を各OSおよび対応バージョンに合わせてインストールしてあるだけだったり…)
