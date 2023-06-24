import threading
import time
from datetime import datetime

import keyboard
import pyautogui

from utils import SCREENSHOTS_PATH, HandleableKeyboardInputs, YoreCoord
from windows_handler import WindowsHandler


class YoreBot:
    current_keyboard_inputs = list()
    gathering_spot = True
    enable = True
    works = False

    def __init__(self, window_handler: WindowsHandler, name: str = 'Yore Bot') -> None:
        self.name = name
        self.input_thread = threading.Thread(target=self._manage_inputs)
        self.work_thread = threading.Thread(target=self._work)
        self.actions_thread = threading.Thread(target=self._actions)
        self.window_handler = window_handler

    def run(self) -> None:
        self.input_thread.start()
        self.work_thread.start()
        self.actions_thread.start()

        self.input_thread.join()
        self.work_thread.join()
        self.actions_thread.join()

    def check_keyboard_inputs(self, duration: float = 0.15) -> None:
        self.current_keyboard_inputs = list()
        timeout = time.perf_counter() + duration

        while time.perf_counter() < timeout:
            for key in HandleableKeyboardInputs.get_all_handleable_keys():
                if keyboard.is_pressed(key) and key not in self.current_keyboard_inputs:
                    self.current_keyboard_inputs.append(key)

    def handle_keyboard_inputs(self) -> None:
        if HandleableKeyboardInputs.ESCAPE_KEY.value in self.current_keyboard_inputs:
            self.disable()
            return

        if HandleableKeyboardInputs.BACKTICK_KEY.value in self.current_keyboard_inputs:
            if self.works:
                self.works = False
                time.sleep(1)
                return

            self.works = True
            time.sleep(1)
            return

    def work(self) -> None:
        self.log('Work')
        self.window_handler.check_windows()

        if self.gathering_spot:
            self.window_handler.click_all_instances(YoreCoord.oak_coord_1)
            self.gathering_spot = False

        else:
            self.window_handler.click_all_instances(YoreCoord.oak_coord_2)
            self.gathering_spot = True

        time.sleep(12)

    def actions(self) -> None:
        self.log('Actions')
        self.window_handler.check_windows()

    def _manage_inputs(self) -> None:
        while self.enable:
            self.log('Manage Input')
            self.check_keyboard_inputs(duration=1.0)
            self.handle_keyboard_inputs()

    def _work(self) -> None:
        while self.enable:
            if self.works:
                self.work()

    def _actions(self) -> None:
        while self.enable:
            if self.works:
                self.actions()

    def disable(self) -> None:
        self.works = False
        self.enable = False

    def log(self, text) -> None:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f'{current_time} - {self.name} - {text} - Idle {not self.works}')

    @staticmethod
    def screenshot(name: str) -> None:
        current_time = datetime.now().strftime("%d.%m.%Y_%H:%M:%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f'{SCREENSHOTS_PATH}{current_time}_{name}.png')