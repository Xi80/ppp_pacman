from item import Item


class Food(Item):
    """
    Foodクラス
        得点アイテムの座標とアイコン，状態を管理
        アイテムは動かない

    Attributes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        status (bool): アイテムの状態
        icon (str): 表示アイコン

    Examples:
        >>> food = Food(6, 7)
        >>> food.now_x
        6
        >>> food.now_y
        7
        >>> food.icon
        '🍒'
        >>> food.status
        True
        >>> isinstance(food, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = '🍒'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
