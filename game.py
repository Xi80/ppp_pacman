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
        e_num = 1
        f_num = 1
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

            # 敵の移動を決定
            for enemy in self.enemies:
                enemy.get_next_pos()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)

            for item in self.players + self.enemies:
                # ブロックとの衝突判定
                bumped_item = self.field.check_bump(item, list(self.blocks))
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            for item in self.enemies:
                # 敵とフードとの衝突判定
                bumped_item = self.field.check_bump(
                    item, list(self.foods + self.enemies))
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            for item in self.players:
                # プレイヤーとフードとの衝突判定
                bumped_item = self.field.check_bump(item, list(self.foods))
                if bumped_item is not None:
                    bumped_item.status = False
                    item.set_invincible(True)
                item.update_pos()

            for player in self.players:
                # 敵との衝突判定
                bumped_item = self.field.check_bump(player, list(self.enemies))
                if bumped_item is not None:
                    if player.get_invincible() is True:
                        bumped_item.status = False
                        item.update_pos(stuck=False)
                    else:
                        self.field._update_field()
                        os.system("cls" if os.name == "nt" else "clear")
                        # ターミナルをクリア
                        self.field._display_field()
                        logger.info("Game Over!")
                        return "Game Over!"

            active_food = list(filter(lambda x: x.status is True, self.foods))
            if len(active_food) == 0:
                self.field._update_field()
                os.system("cls" if os.name == "nt" else "clear")
                # ターミナルをクリア
                self.field._display_field()
                logger.info("Game Clear!")
                return "Game Clear!"

            self.field._update_field()

            time.sleep(0.1)
