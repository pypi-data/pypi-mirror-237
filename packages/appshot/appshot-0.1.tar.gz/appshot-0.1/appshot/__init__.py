import difflib
import time
from typing import Tuple

import cv2 as cv
import numpy as np
import win32con
import win32gui
import win32ui

ID_WIN_FRONT = -1  # 窗口处于最前方, 此时可以不传参数
ID_WIN_HANDLE = 0  # 直接窗口句柄, 不再查找, 此时需要传入参数int
ID_WIN_TITLE = 1  # 根据窗口标题查找, 此时需要传入参数str
ID_WIN_CLSNAME = 2  # 根据窗口类名查找, 此时需要传入参数str


class AppShot:
    MIN_SIMILAR_THRESHOLD = 0.5

    @staticmethod
    def _get_window_by_title(name) -> int:
        hwnd = None
        max_ratio = 0
        windows = []
        win32gui.EnumWindows(lambda hwnd, windows: windows.append(hwnd), windows)
        for window in windows:
            title = win32gui.GetWindowText(window)
            ratio = difflib.SequenceMatcher(None, name, title).ratio()
            if ratio >= AppShot.MIN_SIMILAR_THRESHOLD and ratio > max_ratio:
                max_ratio = ratio
                hwnd = window
        return hwnd

    @staticmethod
    def _get_window_by_clsname(clsname) -> int:
        hwnd = None
        max_ratio = 0
        windows = []
        win32gui.EnumWindows(lambda hwnd, windows: windows.append(hwnd), windows)
        for window in windows:
            clsname = win32gui.GetClassName(window)
            ratio = difflib.SequenceMatcher(None, clsname, clsname).ratio()
            if ratio >= AppShot.MIN_SIMILAR_THRESHOLD and ratio > max_ratio:
                max_ratio = ratio
                hwnd = window
        return hwnd

    @staticmethod
    def _get_window_front() -> int:
        return win32gui.GetForegroundWindow()

    @staticmethod
    def _get_window_size(hwnd) -> Tuple[int, int]:
        rect = win32gui.GetWindowRect(hwnd)
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        return width, height

    @staticmethod
    def _get_window_pos(hwnd) -> Tuple[int, int]:
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        return x, y

    @staticmethod
    def _get_window_rect(hwnd) -> Tuple[int, int, int, int]:
        rect = win32gui.GetWindowRect(hwnd)
        return rect

    @staticmethod
    def _check_hwnd_valid(hwnd) -> bool:
        # Check if the window with handle `hwnd` is valid
        return win32gui.IsWindow(hwnd)

    @staticmethod
    def _get_window_title(hwnd) -> str:
        return win32gui.GetWindowText(hwnd)

    @staticmethod
    def _get_window_clsname(hwnd) -> str:
        return win32gui.GetClassName(hwnd)

    def __init__(self, identy: object = None, identy_type: int = ID_WIN_FRONT):
        # 要是>python3.10, 可以升级为match写法
        if identy_type == ID_WIN_FRONT:
            self.hwnd = self._get_window_front()
        elif identy_type == ID_WIN_HANDLE:
            self.hwnd = identy
            assert self._check_hwnd_valid(self.hwnd), f"hwnd:{self.hwnd} is not valid"
        elif identy_type == ID_WIN_TITLE:
            self.hwnd = self._get_window_by_title(identy)
            assert self._check_hwnd_valid(self.hwnd), f"title:{identy} is not found"
        elif identy_type == ID_WIN_CLSNAME:
            self.hwnd = self._get_window_by_clsname(identy)
            assert self._check_hwnd_valid(self.hwnd), f"clsname:{identy} is not found"
        else:
            raise ValueError(f"identy_type:{identy_type} error")

        # step2 create dc
        self.width, self.height = self._get_window_size(self.hwnd)
        self.window_dc = None  # win32gui.GetWindowDC(self.hwnd)
        self.img_dc = None  # win32ui.CreateDCFromHandle(self.window_dc)
        self.mem_dc = None  # self.img_dc.CreateCompatibleDC()
        self.screenshot = None  # win32ui.CreateBitmap()

        self._recreate_dc()

    def _recreate_dc(self):
        """重新创建dc. 常用在更改了窗口尺寸时"""
        self.width, self.height = self._get_window_size(self.hwnd)
        if self.mem_dc is not None:
            self.mem_dc.DeleteDC()

        self.window_dc = win32gui.GetWindowDC(self.hwnd)
        self.img_dc = win32ui.CreateDCFromHandle(self.window_dc)
        self.mem_dc = self.img_dc.CreateCompatibleDC()
        self.screenshot = win32ui.CreateBitmap()

        self.screenshot.CreateCompatibleBitmap(self.img_dc, self.width, self.height)
        self.mem_dc.SelectObject(self.screenshot)

    def shot(self) -> np.ndarray:
        # 1. 检查尺寸变化
        _size = self._get_window_size(self.hwnd)
        if _size != (self.width, self.height):
            print("recreateDC")
            self._recreate_dc()

        # 2. 截图
        # 截图至内存设备描述表
        self.mem_dc.BitBlt((0, 0), (self.width, self.height), self.img_dc, (0, 0), win32con.SRCCOPY)

        # 将截图转换为NumPy数组
        screenshot_array = np.frombuffer(self.screenshot.GetBitmapBits(True), dtype='uint8')
        screenshot_array.shape = (self.height, self.width, 4)

        return screenshot_array


if __name__ == '__main__':
    shoter = AppShot()
    for i in range(5):
        img = shoter.shot()
        cv.imwrite(f'img{i}.jpg', img)
        cv.imwrite(f'img{i}.png', img)
        time.sleep(1)

