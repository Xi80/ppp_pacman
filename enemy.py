from item import Item
import random


class Enemy(Item):
    """敵管理
    敵の座標とアイコン，状態を管理
    敵は乱数によりランダムに動く

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）

    Examples:
        >>> enemy = Enemy(6, 7)
        >>> enemy.now_x
        6
        >>> enemy.now_y
        7
        >>> enemy.icon
        '👻'
        >>> enemy.status
        True
        >>> isinstance(enemy, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = '👻'

    def get_next_pos(self) -> tuple[int, int]:
        """次に移動する座標を乱数により決定する

        Returns:
            tuple[int, int]: 次の移動で遷移したい座標

        Examples:
            >>> enemy = Enemy(5,6)
            >>> possible_moves = [(5, 6), (5, 5), (5, 7), (4, 6), (6, 6)]
            >>> next_move = enemy.get_next_pos()
            >>> next_move in possible_moves
            True

        """
        movable_dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        current_pos = self.get_pos()
        self.next_x = current_pos[0] + random.choice(movable_dirs)[0]
        self.next_y = current_pos[1] + random.choice(movable_dirs)[1]
        return self.next_x, self.next_y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
