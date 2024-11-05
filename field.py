from player import Player
from food import Food
from block import Block
from enemy import Enemy


class Field:
    """
    Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    アイテムの位置を更新する際に移動先の位置を参照して衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        foods (list[Food]): アイテムのリスト
        blocks (list[Block]): ブロックアイテムのリスト
        enemys (list[Enemy]): 敵のリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    def __init__(
            self,
            players: list[Player],
            foods: list[Food],
            blocks: list[Block],
            enemys: list[Enemy],
            f_size: int = 6) -> None:
        """
        Fieldの初期化を行う関数

        Args:
            players (list[Player]):プレイヤーのリスト
            foods (list[Food]): アイテムのリスト
            blocks (list[Block]): ブロックアイテムのリスト
            enemys (list[Enemy]): 敵のリスト
            f_size (int): フィールドのサイズ

        """
        self.f_size = f_size
        self.field = [[""for _ in range(f_size)] for _ in range(f_size)]
        self.players = players
        self.foods = foods
        self.blocks = blocks
        self.enemys = enemys
        self._update_field()
        pass

    def _update_field(self) -> list[list[str]]:
        """
        プレイヤーの位置の変数を参照し、Fieldを更新する関数

        Returns:
            list[list[str]]: 更新されたFieldの情報

        Example:
            >>> p =[Player(1, 0)]
            >>> p[0].icon = "p"
            >>> f =[Food(0, 1)]
            >>> f[0].icon = "f"
            >>> b =[Block(0, 2)]
            >>> b[0].icon = "b"
            >>> e =[Enemy(2, 0)]
            >>> e[0].icon = "e"
            >>> field = Field(p,f,b,e,3)
            >>> field._update_field()[0]
            [' ', 'p', 'e']
            >>> field._update_field()[1]
            ['f', ' ', ' ']
            >>> field._update_field()[2]
            ['b', ' ', ' ']
        """
        # fieldを初期化して空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = "　"
        # playerの更新処理
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        # foodの更新処理
        for food in self.foods:
            if food.status:
                self.field[food.now_y][food.now_x] = food.icon
        # blockの更新処理
        for block in self.blocks:
            if block.status:
                self.field[block.now_y][block.now_x] = block.icon
        # enemyの更新処理
        for enemy in self.enemys:
            if enemy.status:
                self.field[enemy.now_y][enemy.now_x] = enemy.icon
        return self.field

    # Fieldを表示する関数
    def _display_field(self) -> None:
        """
        Fieldをディスプレイに表示する関数

        Example:
        >>> p=[Player(1,0)]
        >>> p[0].icon = "p"
        >>> f =[Food(2, 1)]
        >>> f[0].icon = "f"
        >>> b =[Block(2, 2)]
        >>> b[0].icon = "b"
        >>> e =[Enemy(2, 0)]
        >>> e[0].icon = "e"
        >>> field = Field(p,f,b,e,3)
        >>> field._display_field()
         pe
          f
          b

        """
        # self.fieldを表示
        max_width = max(len(row) for row in self.field)
        # 文字列を作成し、空白で埋める
        for row in self.field:
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
