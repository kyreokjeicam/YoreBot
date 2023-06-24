import os
from collections import namedtuple

from screeninfo import get_monitors

YORE_LOGIN_0 = 'kyre'
YORE_LOGIN_1 = 'camre'
YORE_LOGIN_2 = 'recam'
YORE_LOGIN_3 = 'okjeicam'

YORE_WINDOW_NAME = 'Tales'

PYTHON_COMMAND_KEYWORD = 'python3'

UBUNTU_LEFT_BAR_WIDTH = 74
UBUNTU_TOP_BAR_HEIGHT = 27

YORE_EXE_NAME = "talesofyore"
HOME_PATH = os.path.expanduser("~")
YORE_BINARIES_PATH = os.path.join(HOME_PATH, "TalesOfYore-1.0.30-linux")
YORE_EXEC_PATH = os.path.join(YORE_BINARIES_PATH, YORE_EXE_NAME)

Coord = namedtuple("Coord", "x y")
Position = namedtuple("Position", "x y")
Resolution = namedtuple("Resolution", "width height")
Size = namedtuple("Size", "width height")

DEFAULT_DISPLAY_RESOLUTION = Resolution(1920, 1080)
WINDOW_INSTANCE_WIDTH = 920
WINDOW_INSTANCE_HEIGHT = 480
WINDOW_BAR_HEIGHT = 36

WINDOWS_POSITIONS = (
    Position(x=UBUNTU_LEFT_BAR_WIDTH, y=UBUNTU_TOP_BAR_HEIGHT),
    Position(x=UBUNTU_LEFT_BAR_WIDTH + WINDOW_INSTANCE_WIDTH, y=UBUNTU_TOP_BAR_HEIGHT),

    Position(x=UBUNTU_LEFT_BAR_WIDTH, y=UBUNTU_TOP_BAR_HEIGHT + WINDOW_INSTANCE_HEIGHT + WINDOW_BAR_HEIGHT),
    Position(x=UBUNTU_LEFT_BAR_WIDTH + WINDOW_INSTANCE_WIDTH, y=UBUNTU_TOP_BAR_HEIGHT + WINDOW_INSTANCE_HEIGHT + WINDOW_BAR_HEIGHT)
)


class YoreCoord:
    skip_welcome_popup_coord = Coord(x=175, y=150)


def get_primary_monitor_position() -> Position:
    monitors = get_monitors()

    for monitor in monitors:
        if monitor.is_primary:
            return monitor.x, monitor.y
