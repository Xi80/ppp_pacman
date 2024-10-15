from item import Item
import doctest


class Block(Item):
    """Blockクラス
        壁の座標とアイコン，状態を管理
        壁は動かない

    Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン

    Examples:
        >>> block = Block(1, 1)
        >>> block.now_x
        1
        >>> block.now_y
        1
        >>> block.icon
        '🌴'
        >>> isinstance(block, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = '🌴'


if __name__ == "__main__":
    doctest.testmod()
