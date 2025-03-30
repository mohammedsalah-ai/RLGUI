import json

import models.rc_models  # noqa
from PySide6.QtCore import (
    QAbstractListModel,
    QFile,
    QModelIndex,
    QModelRoleData,
    QPersistentModelIndex,
    Qt,
)


class EnvListModel(QAbstractListModel):
    def __init__(self, envs: list[dict] | None = None) -> None:
        super().__init__()

        self.envsResourcePath = ":/models/models_resources/envs.json"

        if envs is None:
            self.envs = self.loadEnvsData()

    def data(
        self,
        index: QModelIndex,
        role: QModelRoleData,
    ) -> None | str:
        if role == Qt.DisplayRole:
            envName = self.envs[index.row()]["envName"]
            return envName

    def rowCount(
        self,
        parent: QModelIndex | QPersistentModelIndex | None = None,
    ) -> int:
        if parent is None:
            parent = QModelIndex()

        return len(self.envs)

    def loadEnvsData(self) -> list:
        envsFile = QFile(self.envsResourcePath)
        if not envsFile.open(QFile.ReadOnly):
            print("I Don't Know :)")
            return []

        data = envsFile.readAll()
        envsFile.close()

        jsonStr = bytes(data).decode("utf-8")

        try:
            envsData = json.loads(jsonStr)
            return envsData
        except json.JSONDecodeError:
            return []
