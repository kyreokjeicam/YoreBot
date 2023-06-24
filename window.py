from utils import Position, Size


class Window:
    def __init__(self, wid: str, x: int, y: int, width: int, height: int, name: str) -> None:
        self.wid = wid
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def get_window_id(self) -> str:
        return self.wid

    def get_window_position(self) -> Position:
        return Position(self.x, self.y)

    def get_window_size(self) -> Size:
        return Size(self.width, self.height)

    def __str__(self) -> str:
        return self.name
