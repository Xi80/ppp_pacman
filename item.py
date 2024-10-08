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
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()