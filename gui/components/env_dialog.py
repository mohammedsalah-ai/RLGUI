from elements.env_dialog.ui_env_dialog import Ui_EnvDialog
from models.envs import EnvListModel
from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QDialog

from components.md_widget import MDWidget


class EnvDialog(QDialog, Ui_EnvDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.selectedEnv = None

        self.md_widget = MDWidget()
        self.envDescriptionScrollArea.setWidget(self.md_widget)

        self.envModel = EnvListModel()
        self.envSelectionListView.setModel(self.envModel)

        self.envSelectionListView.doubleClicked.connect(self.on_selector_double_click)

    def on_selector_double_click(self, index: QModelIndex) -> None:
        env = self.envModel.envs[index.row()]
        self.selectedEnv = env
        self.md_widget.setMD(env["envDescription"])
