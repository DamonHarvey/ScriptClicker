from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import QPoint, Qt
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


class Clicker(QWidget):

    def __init__(self):
        super().__init__()

        self.init_coordinates_widget()

        self.setLayout(self.coordinates_widget)

    def init_coordinates_widget(self):
        layout = QGridLayout()

        self.coordinates_widget = layout

        watcher = ClickWatcher()

        self.click_position = QPoint()

        x_label = QLabel("x:")
        x_label.setFixedWidth(40)
        y_label = QLabel("y:")
        y_label.setFixedWidth(40)

        def on_click():
            watcher.wait_for_click()

            self.click_position.setX(watcher.x)
            self.click_position.setY(watcher.y)

            x_label.setText(f"x:{watcher.x}")
            y_label.setText(f"y:{watcher.y}")

        widget_label = QLabel("Click Position")
        a = widget_label.font()
        a.setUnderline(True)
        a.setBold(True)
        widget_label.setFont(a)

        button = QPushButton("Set")
        button.setFixedWidth(32)
        button.clicked.connect(on_click)

        # layout.addWidget(widget_label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button, 0, 0)
        layout.addWidget(x_label, 0, 1)
        layout.addWidget(y_label, 0, 2)


def main():
    app = QApplication([])

    window = Clicker()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
