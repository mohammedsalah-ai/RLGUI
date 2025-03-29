from elements.env_dialog.ui_env_dialog import Ui_EnvDialog
from PySide6.QtWidgets import QDialog


class EnvDialog(QDialog, Ui_EnvDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
