import os
import subprocess
import time

import pyautogui

from utils import YORE_EXEC_PATH, WINDOWS_POSITIONS, WINDOW_INSTANCE_WIDTH, \
    WINDOW_INSTANCE_HEIGHT, YORE_WINDOW_NAME, Coord, UBUNTU_LEFT_BAR_WIDTH, UBUNTU_TOP_BAR_HEIGHT, Position
from window import Window


class WindowsHandler:
    coord_to_click = list()
    numeric_window_identity = None
    windows_list = list()

    def __init__(self, window_quantity: int = 1) -> None:
        """Max amount of windows = 4"""
        self.window_quantity = window_quantity
        self.enable = False

    def check_windows(self) -> None:
        current_instances_amount = 0
        self.windows_list = list()
        current_windows_list = subprocess.check_output(["wmctrl", "-G", "-l"]).decode("utf-8").splitlines()

        for window in current_windows_list:
            window_data = window.split()

            if window_data[7] == YORE_WINDOW_NAME:
                self.windows_list.append(Window(
                    wid=window_data[0],
                    x=int(window_data[2]),
                    y=int(window_data[3]),
                    width=int(window_data[4]),
                    height=int(window_data[5]),
                    name=f"yore_instance_{current_instances_amount}"
                ))

                current_instances_amount += 1

    def run_yore_instances(self) -> None:
        for _ in range(self.window_quantity):
            self.launch_window()

    def handle(self) -> None:
        self.enable = True

        while self.enable:
            pass

    def set_windows_position_and_size(self) -> None:
        if len(self.windows_list) == 0:
            return

        for n in range(self.window_quantity):
            subprocess.run([
                "wmctrl",
                "-i",
                "-r",
                f"{self.windows_list[n].get_window_id()}",
                "-b",
                "remove,fullscreen"
            ])
            time.sleep(1)
            subprocess.run([
                "wmctrl",
                "-i",
                "-r",
                f"{self.windows_list[n].get_window_id()}",
                "-b",
                "remove,maximized_vert,maximized_horz"
            ])
            time.sleep(1)
            subprocess.run([
                "wmctrl",
                "-i",
                "-r",
                f"{self.windows_list[n].get_window_id()}",
                "-e",
                f"0,{WINDOWS_POSITIONS[n].x},{WINDOWS_POSITIONS[n].y},{WINDOW_INSTANCE_WIDTH},{WINDOW_INSTANCE_HEIGHT}"
            ])

    def close_all_windows(self) -> None:
        if len(self.windows_list) == 0:
            return

        for n in range(self.window_quantity):
            subprocess.run([
                "wmctrl",
                "-ic",
                f"{self.windows_list[n].get_window_id()}",
            ])

    def click_all_instances(self, first_instance_coord: Coord) -> None:
        first_instance_game_coord = Coord(
            first_instance_coord.x - UBUNTU_LEFT_BAR_WIDTH,
            first_instance_coord.y - UBUNTU_TOP_BAR_HEIGHT
        )

        for window in self.windows_list:
            print('essa')
            window_instance_position = Position(window.x, window.y)
            click_coord = Coord(
                window_instance_position.x + first_instance_game_coord.x,
                window_instance_position.y + first_instance_game_coord.y
            )
            self.focus_window(window.get_window_id())
            pyautogui.moveTo(x=click_coord.x, y=click_coord.y)
            pyautogui.click(x=click_coord.x, y=click_coord.y, duration=0.15)
            time.sleep(1)

    @staticmethod
    def focus_window(wid: str):
        subprocess.run([
            "wmctrl",
            "-ia",
            wid,
        ])

    @staticmethod
    def launch_window() -> None:
        os.system(f"nohup {YORE_EXEC_PATH} &")

    def print_windows(self) -> None:
        for window in self.windows_list:
            print(window.name)
