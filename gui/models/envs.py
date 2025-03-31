import json

import models.rc_models  # noqa
from PySide6.QtCore import (
    QAbstractListModel,
    QFile,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)
from PySide6.QtGui import QIcon


class EnvListModel(QAbstractListModel):
    def __init__(self, envs: list[dict] | None = None) -> None:
        super().__init__()

        self.envsResourcePath = ":/models/models_resources/envs.json"

        if envs is None:
            self.envs = self.loadEnvsData()

    def data(
        self,
        index: QModelIndex,
        role: Qt.ItemDataRole,
    ) -> None | QIcon | str:
        env = self.envs[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return env["display_name"]

        if role == Qt.ItemDataRole.DecorationRole:
            if (
                env["action_space"]["type"] == "Discrete"
                and env["observation_space"]["type"] == "Discrete"
            ):
                return QIcon(":/models/models_resources/env_icons/dado.png")
            elif (
                env["action_space"]["type"] == "Discrete"
                and env["observation_space"]["type"] == "Box"
            ):
                return QIcon(":/models/models_resources/env_icons/dabo.png")
            elif (
                env["action_space"]["type"] == "Box"
                and env["observation_space"]["type"] == "Discrete"
            ):
                return QIcon(":/models/models_resources/env_icons/bado.png")
            elif (
                env["action_space"]["type"] == "Box"
                and env["observation_space"]["type"] == "Box"
            ):
                return QIcon(":/models/models_resources/env_icons/babo.png")

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
            return []

        data = envsFile.readAll()
        envsFile.close()

        jsonStr = bytes(data).decode("utf-8")

        try:
            envsData = json.loads(jsonStr)
            return envsData
        except json.JSONDecodeError:
            return []
