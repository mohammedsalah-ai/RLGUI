from elements.main_window.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

from components.env_dialog import EnvDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.env_dialog = EnvDialog()

        self.envBtn.pressed.connect(self.show_env_dialog)

    def show_env_dialog(self) -> None:
        self.env_dialog.exec()
