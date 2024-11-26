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
        self.f_size = 10  # フィールドのサイズ
        self.e_num = 5
        self.f_num = 5
        self.b_num = 10
        # フィールドの初期化
        self.players = [Player(1, 1)]
        self.occupied_positions = {(1, 1)}  # 既に占有されている位置を追跡
        self.enemies = [
            self.create_unique_object(Enemy) for _ in range(self.e_num)
        ]
        self.foods = [
            self.create_unique_object(Food) for _ in range(self.f_num)
        ]

        if self.f_size < 4:
            raise ValueError("field_size must be greater than 4")
        self.blocks = [
            Block(x, y)
            for x in range(self.f_size)
            for y in range(self.f_size)
            if x == 0 or x == self.f_size - 1 or y == 0 or y == self.f_size - 1
        ]
        for b in range(self.b_num):
            self.blocks.append(self.create_unique_object(Block))
        self.field = Field(
            self.players,
            self.enemies,
            self.foods,
            self.blocks,
            self.f_size)

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
            print(self.create_score_text())

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)

            for player in self.players:
                # 敵との衝突判定
                bumped_item = self.field.check_bump(player, list(self.enemies))
                if bumped_item is not None:
                    if player.get_invincible() is True:
                        bumped_item.status = False
                        player.update_pos(stuck=False)
                        player.add_score(100)
                    else:
                        self.field._update_field()
                        os.system("cls" if os.name == "nt" else "clear")
                        # ターミナルをクリア
                        self.field._display_field()
                        score = self.players[0].get_score()
                        logger.info(f"GameOver! Score:{score}")
                        return f"GameOver! Score:{score}"

            # 敵の移動を決定
            for enemy in [e for e in self.enemies if e.status]:
                enemy.get_next_pos()

            for item in self.players:
                # ブロックとの衝突判定
                bumped_item = self.field.check_bump(item, list(self.blocks))
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            for item in self.enemies:
                # 敵の衝突判定
                other_enemies = [e for e in self.enemies if e is not item]
                bump_targets = list(self.foods + self.blocks + other_enemies)
                bumped_item = self.field.check_bump(
                    item, bump_targets)
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            for player in self.players:
                # プレイヤーとフードとの衝突判定
                bumped_item = self.field.check_bump(player, list(self.foods))
                if bumped_item is not None:
                    bumped_item.status = False
                    player.set_invincible(True)
                    player.add_score(10)
                player.update_pos()

            active_food = list(filter(lambda x: x.status is True, self.foods))
            if len(active_food) == 0:
                self.field._update_field()
                os.system("cls" if os.name == "nt" else "clear")
                # ターミナルをクリア
                self.field._display_field()
                score = self.players[0].get_score()
                logger.info(f"Game Clear! Score:{score}")
                return f"Game Clear! Score:{score}"

            self.field._update_field()

            time.sleep(0.2)

    def create_unique_object(self, obj_type):
        """
        指定されたクラスのオブジェクトを重複のない位置で生成する。
        """
        while True:
            x = randint(1, self.f_size - 2)
            y = randint(1, self.f_size - 2)
            if (x, y) not in self.occupied_positions:
                self.occupied_positions.add((x, y))
                return obj_type(x, y)

    def create_score_text(self) -> str:
        """
        スコア表示用テキストを作成
        """
        remaining_enemies = [e for e in self.enemies if e.status]
        remaining_foods = [e for e in self.foods if e.status]
        ret = f"Enemy:{len(remaining_enemies)} "
        ret += f"Foods:{len(remaining_foods)} "
        for player in self.players:
            ret += f"Score:{player.get_score()} "
        return ret
