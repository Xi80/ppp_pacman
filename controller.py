import sys
import termios


class InputWithoutEnter:
    """Enterキーを押さずにキーボード入力を受け取る"""

    def input_without_enter(self) -> str:
        """
        Enterキーを押さずにキーボード入力を受け取る

        Returns:
            str: 入力された文字
        """
        pass