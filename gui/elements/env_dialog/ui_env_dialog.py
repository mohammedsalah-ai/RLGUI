# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QGridLayout,
    QHBoxLayout,
    QScrollArea,
    QTreeView,
    QWidget,
)


class Ui_EnvDialog(object):
    def setupUi(self, EnvDialog):
        if not EnvDialog.objectName():
            EnvDialog.setObjectName("EnvDialog")
        EnvDialog.resize(968, 585)
        EnvDialog.setMinimumSize(QSize(968, 585))
        EnvDialog.setStyleSheet("QDialog {\n	background-color: #FFFFFF;\n}")
        self.gridLayout = QGridLayout(EnvDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(24)
        self.gridLayout.setContentsMargins(32, 32, 32, 32)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.envSelectionTreeView = QTreeView(EnvDialog)
        self.envSelectionTreeView.setObjectName("envSelectionTreeView")

        self.horizontalLayout.addWidget(self.envSelectionTreeView)

        self.envDescriptionScrollArea = QScrollArea(EnvDialog)
        self.envDescriptionScrollArea.setObjectName("envDescriptionScrollArea")
        self.envDescriptionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 454))
        self.envDescriptionScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.envDescriptionScrollArea)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(EnvDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStyleSheet(
            "QDialogButtonBox {\n"
            "    qproperty-centerButtons: true;\n"
            "}\n"
            "\n"
            "QDialogButtonBox QPushButton {\n"
            "    min-height: 23px;\n"
            "    min-width: 75px;\n"
            "    padding: 6px 6px;\n"
            "    border-radius: 19px;\n"
            "    qproperty-icon: none;\n"
            "    font-size: 12px;\n"
            "}\n"
            "\n"
            'QDialogButtonBox QPushButton[text="OK"] {\n'
            "    background-color: #888888;\n"
            "    color: #EEEEEE;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            'QDialogButtonBox QPushButton[text="OK"]:hover {\n'
            "    background-color: #9E9E9E;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            'QDialogButtonBox QPushButton[text="OK"]:pressed {\n'
            "    background-color: #555555;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            'QDialogButtonBox QPushButton[text="Cancel"] {\n'
            "    background-color: #BBBBBB;\n"
            "    color: #EEEEEE;\n"
            "    border: 2px solid #BBBBBB;\n"
            "}\n"
            "\n"
            'QDialogButtonBox QPushButton[text="Cancel"]:hover {\n'
            "    background-color: #CCCCCC;\n"
            "    border: 2px solid #CCCCCC;\n"
            "}\n"
            "\n"
            "QDialogButto"
            'nBox QPushButton[text="Cancel"]:pressed {\n'
            "    background-color: #999999;\n"
            "    border: 2px solid #999999;\n"
            "}"
        )
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(EnvDialog)
        self.buttonBox.accepted.connect(EnvDialog.accept)
        self.buttonBox.rejected.connect(EnvDialog.reject)

        QMetaObject.connectSlotsByName(EnvDialog)

    # setupUi

    def retranslateUi(self, EnvDialog):
        EnvDialog.setWindowTitle(
            QCoreApplication.translate("EnvDialog", "Environments", None)
        )

    # retranslateUi
