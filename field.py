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

    def _init_(
            self,
            players: list[Player],
            f_size: int = 6) -> None:
        """
        Fieldの初期化を行う関数

        Args:
            player(list[Player]):プレイヤーのリスト
            f_size (int): フィールドのサイズ


        """
        pass

    def update_field(self) -> list[list[str]]:
        """
        プレイヤーの位置の変数を参照し、Fieldを更新する関数

        Returns:
            list[list[str]]: 更新されたFieldの情報

        Example:
            >>> p =[Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p,3)
            >>> field.update_field()[0]
            ['p1', ' ', ' ']
        """
        return [[]]

    # Fieldを表示する関数
    def _display_field(self) -> None:
        """
        Fieldをディスプレイに表示する関数

        Example:
        >>> p=[Player(1,0)]
        >>> p[0].icon = "p1"
        >>> field = Field(p,3)
        >>> field.display_field()

        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
