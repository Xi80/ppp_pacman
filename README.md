# Pacman Project

キーボード入力によってターミナル上を動くパックマンです。

## Requirement
- Python 3.12.5


## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - 
```shell
python main.py
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py           # パラメータ定義
├── main.py             # 実行ファイル
├── result              # 結果出力ディレクトリ
│   └── 20241105_170100
├── block.py            # Blockクラス
├── controller_test.py  #コントローラ入力のテスト
├── enemy.py            # Enemyクラス
├── field.py            # Fieldクラス
├── food.py             # Foodクラス
├── game.py             # Gameクラス
├── input_without_enter # エンターキーを押さずに入力を受け取るクラス
├── item.py             # block,player,enemy,foodの親クラス
├── player.py           # Playerクラス
├── userinput.py        # ユーザーの入力を受け取るクラス
└── utils.py            # 共有関数群
```
