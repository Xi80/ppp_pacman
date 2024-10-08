from item import Item


class Player(Item):
    """プレイヤークラス
    Itemを継承して作成したプレイヤークラス.
    入力から移動方向を受け取って移動しようとする方向を計算するメソッドと
    マップから移動して良いと許可が出た時に呼び出される座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """

    def __init__(self, x, y) -> None:
        pass

    def get_next_pos(self,dir: tuple[int, int]) -> tuple[int, int]:
        """
        移動方向したい方向を受け取り，移動後の座標を返す．

        Args:
            dir(tuple[int, int]: 次に移動する量(xの移動量,yの移動量)，右下方向に正

        Returns:
            tuple[int, int]: 移動後の座標

        Examples:
            >>> player = Player(4, 4)
            >>> player.get_next_pos((1, 0))
            (5, 4)
            >>> player = Player(4, 4)
            >>> player.get_next_pos((0, 1))
            (4, 5)
        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()