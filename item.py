"""親クラス
block,player,enemy,foodの親クラス
"""


class Item:
    """block,player,enemy,foodの親クラス

    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       next_x(int) : 次の時刻でのx座標
       next_y(int) : 次の時刻でのy座標
       status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
       icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x, y) -> None:
        """
        Itemクラスのコンストラクタ
        引数にx座標とy座標を受け取り、それぞれの座標を初期化する

        Args:
            x(int): x座標
            y(int): y座標

        Returns:
            None

        Examples:
            >>> item = Item(5, 6)
            >>> item.now_x
            5
            >>> item.now_y
            6
            >>> item.next_x
            5
            >>> item.next_y
            6
            >>> item.icon
            ''
            >>> item.status
            True
        """
        self.now_x = x
        self.now_y = y
        self.next_x = x
        self.next_y = y
        self.icon = ''
        self.status = True

    def get_next_pos(self) -> tuple[int, int]:
        """
        次に移動したい座標を取得する
        オーバーライドを想定

        Returns:
            tuple[int, int]: 次の時刻の座標

        Examples:
            >>> item = Item(5, 6)
            >>> item.get_next_pos()
            (5, 6)
        """
        return self.next_x, self.next_y

    def get_pos(self) -> tuple[int, int]:
        """
        現在の座標を返す

        Returns:
            tuple[int, int]: 現在の座標

        Examples:
            >>> item = Item(5, 6)
            >>> item.get_pos()
            (5, 6)
        """
        return self.now_x, self.now_y

    def update_pos(self, stuck: bool = False) -> None:
        """
        座標を更新する

        Args:
            stuck(bool): 移動したい先に他のオブジェクトが存在し，動けない場合にTrue

        Returns:
            None

        Examples:
            >>> item = Item(5, 6)
            >>> item.next_x = 5
            >>> item.next_y = 7
            >>> item.get_pos()
            (5, 6)
            >>> item.update_pos(False)
            >>> item.get_pos()
            (5, 7)
        """

        if stuck:
            self.next_x = self.now_x
            self.next_y = self.now_y
            pass

        self.now_x = self.next_x
        self.now_y = self.next_y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
