import enum
import os
from collections import namedtuple

from PIL import ImageGrab
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
YORE_BINARIES_PATH = os.path.join("TalesOfYore-1.0.30-linux")
SCREENSHOTS_PATH = 'images/screenshots/'
YORE_EXEC_PATH = os.path.join(YORE_BINARIES_PATH, YORE_EXE_NAME)

Color = namedtuple("Color", "r g b")
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


class HandleableKeyboardInputs(enum.Enum):
    ESCAPE_KEY = 'esc'
    BACKTICK_KEY = '`'
    COMMA_KEY = ','
    PERIOD_KEY = '.'
    NUMBER_SIX_KEY = '6'

    @staticmethod
    def get_all_handleable_keys() -> list:  # returns all handleable keyboard inputs
        return [key.value for key in HandleableKeyboardInputs]


class YoreCoord:
    skip_welcome_popup_coord = Coord(x=175, y=150)
    oak_coord_1 = Coord(x=213, y=424)
    oak_coord_2 = Coord(x=261, y=453)


def check_pixel_color(coord: Coord, color: Color) -> bool:
    pixel_box = (coord.x, coord.y, coord.x+1, coord.y+1)
    image = ImageGrab.grab(bbox=pixel_box)
    r, g, b = image.getpixel((0, 0))
    if (r, g, b) == color:
        return True

    return False


def get_primary_monitor_position() -> Position:
    monitors = get_monitors()

    for monitor in monitors:
        if monitor.is_primary:
            return monitor.x, monitor.y
