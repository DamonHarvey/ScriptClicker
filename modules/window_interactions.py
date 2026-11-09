import win32api
import win32con
import win32gui
from enum import Enum


class Hwnd:
    """Windows handle."""

    def __init__(self, window_title: str) -> None:

        self.window_title = self._get_window_name_from_parital_name(window_title)

        self.hwnd = win32gui.FindWindow(None, self.window_title)

        if not self.hwnd:
            raise ValueError("Window not found")

    def _get_window_name_from_parital_name(self, partial_title) -> str:
        found_hwnd: int | None = None

        def callback(hwnd, extra):
            nonlocal found_hwnd
            if win32gui.IsWindowVisible(hwnd):
                window_text = win32gui.GetWindowText(hwnd)
                if partial_title.lower() in window_text.lower():
                    found_hwnd = hwnd
                    return False
            return True

        win32gui.EnumWindows(callback, None)

        if found_hwnd is None:
            raise TypeError("Window name not found.")

        return win32gui.GetWindowText(found_hwnd)


class VK(Enum):

    R = 0x52
    M = 0x4D


def send_click_to_window(hwnd: Hwnd, coords: tuple[int, int]):
    """Sends a left mouse click and release to client coordinates of window."""
    # Combine X and Y into a single lParam value
    lParam = win32api.MAKELONG(coords[0], coords[1])

    win32api.PostMessage(
        hwnd.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam
    )
    win32api.PostMessage(hwnd.hwnd, win32con.WM_LBUTTONUP, 0, lParam)


def send_keypress_to_window(hwnd: Hwnd, key_code: int):
    """Sends a key press and release to the window."""

    win32gui.PostMessage(hwnd.hwnd, win32con.WM_KEYDOWN, key_code, 0)
    win32gui.PostMessage(hwnd.hwnd, win32con.WM_KEYUP, key_code, 0)


def screen_coords_to_client_coords(hwnd: Hwnd, screen_xy: tuple[int, int]):
    """Converts the coordinates of the screen to the client coordinates of the window."""

    window_xy: tuple[int, int] = win32gui.ScreenToClient(
        hwnd.hwnd, (screen_xy[0], screen_xy[1])
    )

    return window_xy


def main():

    COORDS = (1971, -449)

    game_handle = Hwnd("Antim")

    window_coords = screen_coords_to_client_coords(game_handle, COORDS)

    send_click_to_window(game_handle, window_coords)


if __name__ == "__main__":
    main()
