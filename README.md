# Ankier

英単語のリストが書かれたテキストファイルから [Anki](https://apps.ankiweb.net "Anki Home") 登録用データを作成する物です。
[weblio](https://www.weblio.jp) をありがたく利用させていただいています。

# Requirement
 
Python 3.8.5 で動作しています。
 
# Installation
 
ankier.py と 英単語の書かれた word.txt を同じディレクトリに配置してください。
 
# Usage
 
```bash
fuga@hoge:/# python ankier.py
```
 
# Note
 
実行すると output_for_anki.txt を出力します。
Anki で「ファイルを読み込む」から登録してください。
出力データには品詞とその単語の意味を、英単語のリストに反映させています。

 
# Author

positoro@gmail.com
 
# License
 
radioRecorder is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
