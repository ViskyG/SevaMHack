import cv2
import mss
import numpy as np
from .ScreenCaptureInterface import ScreenCaptureInterface
import ctypes

class MSSScreenCapture(ScreenCaptureInterface):

    def __init__(self):
        pass

    def find_window_by_title(self, window_title):
        hwnd = self.find_window_handle(window_title)
        if hwnd:
            left, top, right, bottom = self.get_window_rect(hwnd)
            return {
                'left': left,
                'top': top,
                'width': right - left,
                'height': bottom - top
            }
        else:
            return None

    def find_window_handle(self, title):
        return ctypes.windll.user32.FindWindowW(0, title)

    def get_window_rect(self, hwnd):
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
        return rect.left, rect.top, rect.right, rect.bottom

    def capture_window(self, window_title):
        with mss.mss() as sct:
            window = self.find_window_by_title(window_title)
            if window is None:
                print(f"Window with title '{window_title}' not found.")
                return None

            screenshot = sct.grab(window)
            screenshot_np = np.array(screenshot)

            # Save the screenshot for debugging
            cv2.imwrite('screenshot_before_conversion.png', screenshot_np)

            return screenshot_np
