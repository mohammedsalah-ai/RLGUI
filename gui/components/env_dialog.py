from elements.env_dialog.ui_env_dialog import Ui_EnvDialog
from models.envs import EnvListModel
from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QDialog

from components.env_widget import EnvWidget


class EnvDialog(QDialog, Ui_EnvDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.env_widget = None
        self.selectedEnv = None

        self.envModel = EnvListModel()
        self.envSelectionListView.setModel(self.envModel)

        self.envSelectionListView.clicked.connect(self.on_selector_click)

    def on_selector_click(self, index: QModelIndex) -> None:
        env = self.envModel.envs[index.row()]

        self.selectedEnv = env

        self.env_widget = EnvWidget(env, self)
        self.envDescriptionScrollArea.setWidget(self.env_widget)
