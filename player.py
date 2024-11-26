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
        self.invincible(bool) : プレイヤーの状態(Trueで無敵モード，Falseで通常モード)
        self.count(int) : 残りの無敵時間カウント
        self.score(int) : 現在のスコア
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.set_invincible(False)
        self.count = 0
        self.score = 0
        pass

    def add_score(self, score: int) -> None:
        """
        スコアを加算
        Args:
            score(int)  : 加算するスコア
        Returns:
            None
        Examples:
            >>> player = Player(4, 4)
            >>> player.add_score(10)
            >>> player.get_score()
            10
        """
        self.score += score

    def get_score(self) -> int:
        """
        現在のスコアを返す
        Args:
            None
        Returns:
            int: 現在のスコア
        """
        return self.score

    def get_next_pos(self, dir: tuple[int, int]) -> tuple[int, int]:
        """
        移動方向したい方向を受け取り，移動後の座標を返す．

        Args:
            dir(tuple[int, int]): 次に移動する量(xの移動量,yの移動量)，右下方向に正

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
        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)

    def set_invincible(self, state: bool):
        """
            無敵状態を設定

            Args:
                state(bool): 無敵状態，Trueで有効

            Returns:
                None

            Examples:
                >>> player = Player(4, 4)
                >>> player.get_invincible()
                False
                >>> player.set_invincible(True)
                >>> player.get_invincible()
                True
        """

        self.invincible = state

        if self.invincible is True:
            self.count = 20
            self.icon = "🤩"
        else:
            self.count = 0
            self.icon = "😀"

    def get_invincible(self) -> bool:
        """
            無敵状態を取得

            Args:
                None

            Returns:
                bool: 無敵状態，Trueで有効

            Examples:
                >>> player = Player(4, 4)
                >>> player.get_invincible()
                False
                >>> player.set_invincible(True)
                >>> player.get_invincible()
                True
        """
        return self.invincible

    def update_pos(self, stuck: bool = False) -> None:
        if self.invincible is True:
            if self.count > 0:
                self.count -= 1
            if self.count == 0:
                self.set_invincible(False)

        return super().update_pos(stuck)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
