from pynput import mouse


class ClickWatcher:

    def __init__(self) -> None:
        self._listener = None
        self.x = 0
        self.y = 0

    def _on_click(self, x, y, button, pressed):
        if pressed:
            self.x: int = x
            self.y: int = y
            return False

    def wait_for_click(self):

        with mouse.Listener(on_click=self._on_click) as listener:
            listener.join()


def main():
    watcher = ClickWatcher()
    watcher.wait_for_click()

    print(f"x:{watcher.x} y:{watcher.y}")


if __name__ == "__main__":
    main()
