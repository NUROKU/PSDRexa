## DaVinciResolveへのPythonの導入方法

1. Pythonのインストール
   - [Python公式ウェブサイト](https://www.python.org/downloads/release/python-3913/)からPythonをダウンロードします。
   - インストーラを起動し、「Add Python 3.9 to PATH」にチェックを入れてインストールします。

2. DaVinciResolveでPythonを有効化する
   - DaVinciResolveを起動し、適当なプロジェクトを開きます。
   - 「ワークスペース」→「コンソール」を開きます。
   - 「Py3」をクリックします。
   - もし何もメッセージが表示されなければ、Python3.9が正常にDaVinciResolveで使用できるようになっています。

## DaVinciResolveがPythonを認識しない場合の対処方法

DaVinciResolveがPythonを認識しない場合は、PCの環境変数に以下の設定を追加してください。

- 変数名：PYTHONHOME
- 変数値：Pythonのインストールされたディレクトリのパス

Windowsの場合、ディレクトリのパスはおそらく以下になります。

C:\Users\{ユーザ名}\AppData\Local\Programs\Python\Python39\
