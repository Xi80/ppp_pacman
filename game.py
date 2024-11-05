import time
from player import Player
from enemy import Enemy
from food import Food
from block import Block
from field import Field
from user_input import UserInput
from config import Parameters
from random import randint
import logging
import os


logger = logging.getLogger(__name__)


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]): 食べ物のリスト
        blocks (list[Block]): ブロックのリスト
        field (Field): フィールドのインスタンス
    """

    def __init__(self, params: Parameters) -> None:
        """ゲームクラスの初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        self.players = []
        self.enemies = []
        self.foods = []
        self.blocks = []
        self.field = None
        self.setup(params)  # ゲームの初期設定
        self.start()  # ゲームのメインループ

    def setup(self, params: Parameters) -> None:
        """ゲームの初期設定
        ゲームの初期設定を行うメソッド．

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        f_size = 6  # フィールドのサイズ
        e_num = 0
        f_num = 0
        # フィールドの初期化
        self.players = [Player(1, 1)]
        self.enemies = [
            Enemy(randint(1, f_size - 2), randint(1, f_size - 2))
            for _ in range(e_num)]
        self.foods = [
            Food(randint(1, f_size - 2), randint(1, f_size - 2))
            for _ in range(f_num)
            ]
        if f_size < 4:
            raise ValueError("field_size must be greater than 4")
        self.blocks = [
            Block(x, y)
            for x in range(f_size)
            for y in range(f_size)
            if x == 0 or x == f_size - 1 or y == 0 or y == f_size - 1
        ]
        self.field = Field(
            self.players,
            self.enemies,
            self.foods,
            self.blocks,
            f_size)

    def start(self) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド．
        キー入力を受け取り，プレイヤーと敵の移動を行い，フィールドを更新する．
        ゲーム終了条件を満たした場合は終了する．

        Returns:
            str: ゲーム終了時のメッセージ (例: "Game Over!", "Game Clear!")
        """
        # ゲームのメインループ
        while True:
            #  フィールドを表示
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            self.field._display_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)


            # プレイヤーと敵の移動
            for item in self.players:
                item.update_pos()

            self.field._update_field()

            time.sleep(0.1)


