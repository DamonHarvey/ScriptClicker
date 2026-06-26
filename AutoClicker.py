import pyautogui
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QApplication,
    QPushButton,
    QGridLayout,
    QLineEdit,
)

from modules.click_util import ClickWatcher


class AutoClicker(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.init_coord_widget()
        self.place_widgets()

    def init_coord_widget(self):
        layout = QGridLayout()
        container = QWidget()
        container.setLayout(layout)
        self.set_coords_widget = container

        self.watcher = ClickWatcher()

        def on_click():
            self.watcher.wait_for_click()

            x_cord_box.setText(str(self.watcher.x))
            y_cord_box.setText(str(self.watcher.y))

        x_label = QLabel("x:")
        y_label = QLabel("y:")

        x_cord_box = QLineEdit()
        x_cord_box.setText(str(self.watcher.x))
        x_cord_box.setFixedWidth(37)

        y_cord_box = QLineEdit()
        y_cord_box.setText(str(self.watcher.y))
        y_cord_box.setFixedWidth(37)

        button = QPushButton("Set Position")
        button.clicked.connect(on_click)

        layout.addWidget(x_label, 0, 0)
        layout.addWidget(x_cord_box, 0, 1)
        layout.addWidget(y_label, 0, 2)
        layout.addWidget(y_cord_box, 0, 3)
        layout.addWidget(button, 1, 0, 1, 4)

    def place_widgets(self):

        layout = QGridLayout()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        layout.addWidget(self.set_coords_widget, 0, 0, Qt.AlignmentFlag.AlignCenter)


def main():
    app = QApplication(sys.argv)

    window = AutoClicker()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
