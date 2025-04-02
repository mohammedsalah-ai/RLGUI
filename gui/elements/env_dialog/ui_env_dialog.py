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
    QAbstractScrollArea,
    QDialogButtonBox,
    QGridLayout,
    QHBoxLayout,
    QListView,
    QScrollArea,
    QWidget,
)


class Ui_EnvDialog(object):
    def setupUi(self, EnvDialog):
        if not EnvDialog.objectName():
            EnvDialog.setObjectName("EnvDialog")
        EnvDialog.resize(1280, 680)
        EnvDialog.setMinimumSize(QSize(1280, 680))
        EnvDialog.setStyleSheet("QDialog {\n	background-color: #FFFFFF;\n}")
        self.gridLayout = QGridLayout(EnvDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(24)
        self.gridLayout.setContentsMargins(32, 32, 32, 32)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.envSelectionListView = QListView(EnvDialog)
        self.envSelectionListView.setObjectName("envSelectionListView")
        self.envSelectionListView.setStyleSheet(
            "QListView {\n"
            "    background-color: #ffffff;\n"
            "    border: 1px solid #e0e0e0;\n"
            "    border-radius: 8px;\n"
            "    padding: 0;\n"
            "    font-size: 14px;\n"
            "    color: #555555;\n"
            "    outline: 0;\n"
            "    alternate-background-color: #ffffff; /* Disable alternate colors */\n"
            "}\n"
            "\n"
            "QListView::item {\n"
            "    background-color: #ffffff;\n"
            "    border: none;\n"
            "    border-bottom: 1px solid #e8e8e8; /* Gray separator between items */\n"
            "    padding: 12px 15px;\n"
            "    margin: 0;\n"
            "    height: 30px;\n"
            "}\n"
            "\n"
            "QListView::item:hover {\n"
            "    background-color: #f8f8f8;\n"
            "    color: #333333;\n"
            "}\n"
            "\n"
            "QListView::item:selected {\n"
            "    background-color: #f0f0f0;\n"
            "    color: #222222;\n"
            "    border-bottom: 1px solid #e0e0e0;\n"
            "}\n"
            "\n"
            "QListView::item:selected:active {\n"
            "    background-color: #e8e8e8;\n"
            "}\n"
            "\n"
            "/* Remove the dotted focus rectangle */\n"
            "QListView::item:focus {\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "/* Custom scrollbar to match the style */\n"
            "QScrollBar:vertical {\n"
            ""
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 10px;\n"
            "    margin: 0;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: #d0d0d0;\n"
            "    min-height: 30px;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
            "    height: 0;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: none;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.envSelectionListView)

        self.envDescriptionScrollArea = QScrollArea(EnvDialog)
        self.envDescriptionScrollArea.setObjectName("envDescriptionScrollArea")
        self.envDescriptionScrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.envDescriptionScrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.envDescriptionScrollArea.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.envDescriptionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 890, 549))
        self.envDescriptionScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.envDescriptionScrollArea)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

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
