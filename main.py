import subprocess
import time

from utils import Coord
from windows_handler import WindowsHandler


def main():
    instances = 4

    windows_handler = WindowsHandler(instances)
    windows_handler.check_windows()
    windows_handler.close_all_windows()
    windows_handler.run_yore_instances()
    time.sleep(2.5)
    windows_handler.check_windows()
    windows_handler.print_windows()
    windows_handler.set_windows_position_and_size()
    time.sleep(10)
    windows_handler.check_windows()
    windows_handler.click_all_instances(Coord(100, 100))


if __name__ == '__main__':
    main()
