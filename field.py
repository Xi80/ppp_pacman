from player import Player


class Field:
    """
    Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    アイテムの位置を更新する際に移動先の位置を参照して衝突判定を行います。

    Attributes:
        player (list[Player]): プレイヤーのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    def __init__(
            self,
            players: list[Player],
            f_size: int = 6) -> None:
        """
        Fieldの初期化を行う関数

        Args:
            player(list[Player]):プレイヤーのリスト
            f_size (int): フィールドのサイズ


        """
        self.f_size = f_size
        self.field = [[" "for _ in range(f_size)] for _ in range(f_size)]
        self.players = players
        pass

    def _update_field(self) -> list[list[str]]:
        """
        プレイヤーの位置の変数を参照し、Fieldを更新する関数

        Returns:
            list[list[str]]: 更新されたFieldの情報

        Example:
            >>> p =[Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p,3)
            >>> field._update_field()[0]
            ['p1', ' ', ' ']
        """
        # fieldを初期化して空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = " "
        # playerの更新処理
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        return [[]]

    # Fieldを表示する関数
    def _display_field(self) -> None:
        """
        Fieldをディスプレイに表示する関数

        Example:
        >>> p=[Player(1,0)]
        >>> p[0].icon = "p"
        >>> field = Field(p,3)
        >>> field._display_field()
             p 
                
                
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
