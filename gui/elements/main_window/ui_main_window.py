# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtGui import (
    QBrush,
    QColor,
    QPalette,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 580)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1120, 580))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(32, 32, 32, 32)
        self.algoLayout = QVBoxLayout()
        self.algoLayout.setSpacing(12)
        self.algoLayout.setObjectName("algoLayout")
        self.algoOptsLabel = QLabel(self.centralwidget)
        self.algoOptsLabel.setObjectName("algoOptsLabel")

        self.algoLayout.addWidget(self.algoOptsLabel)

        self.algoArgsWidget = QWidget(self.centralwidget)
        self.algoArgsWidget.setObjectName("algoArgsWidget")
        self.verticalLayout_3 = QVBoxLayout(self.algoArgsWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.algoPreviewLabel = QLabel(self.algoArgsWidget)
        self.algoPreviewLabel.setObjectName("algoPreviewLabel")
        self.algoPreviewLabel.setStyleSheet(
            "QLabel {\n	color: rgba(0, 0, 0, 128);\n}"
        )

        self.verticalLayout_3.addWidget(self.algoPreviewLabel)

        self.algoLayout.addWidget(self.algoArgsWidget)

        self.trainBtn = QPushButton(self.centralwidget)
        self.trainBtn.setObjectName("trainBtn")
        self.trainBtn.setStyleSheet(
            "QPushButton {\n"
            "    min-height: 23px;\n"
            "    min-width: 100px;\n"
            "    padding: 6px 6px;\n"
            "    border-radius: 19px;\n"
            "    qproperty-icon: none;\n"
            "    font-size: 12px;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #888888;\n"
            "    color: #EEEEEE;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #9E9E9E;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            "QDialogButtonBox QPushButton:pressed {\n"
            "    background-color: #555555;\n"
            "    border: 2px solid transparent;\n"
            "}"
        )

        self.algoLayout.addWidget(self.trainBtn)

        self.algoLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.algoLayout, 0, 2, 1, 1)

        self.envLayout = QVBoxLayout()
        self.envLayout.setSpacing(12)
        self.envLayout.setObjectName("envLayout")
        self.envOptsLabel = QLabel(self.centralwidget)
        self.envOptsLabel.setObjectName("envOptsLabel")

        self.envLayout.addWidget(self.envOptsLabel)

        self.envBtn = QPushButton(self.centralwidget)
        self.envBtn.setObjectName("envBtn")
        self.envBtn.setStyleSheet(
            "QPushButton {\n"
            "    min-height: 23px;\n"
            "    min-width: 100px;\n"
            "    padding: 6px 6px;\n"
            "    border-radius: 19px;\n"
            "    qproperty-icon: none;\n"
            "    font-size: 12px;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #888888;\n"
            "    color: #EEEEEE;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #9E9E9E;\n"
            "    border: 2px solid transparent;\n"
            "}\n"
            "\n"
            "QDialogButtonBox QPushButton:pressed {\n"
            "    background-color: #555555;\n"
            "    border: 2px solid transparent;\n"
            "}"
        )

        self.envLayout.addWidget(self.envBtn)

        self.envArgsWidget = QWidget(self.centralwidget)
        self.envArgsWidget.setObjectName("envArgsWidget")
        self.verticalLayout_2 = QVBoxLayout(self.envArgsWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.envArgsPreviewLabel = QLabel(self.envArgsWidget)
        self.envArgsPreviewLabel.setObjectName("envArgsPreviewLabel")
        self.envArgsPreviewLabel.setStyleSheet(
            "QLabel {\n	color: rgba(0,0, 0, 128);\n	margin-bottom: 96px;\n}"
        )

        self.verticalLayout_2.addWidget(self.envArgsPreviewLabel)

        self.envLayout.addWidget(self.envArgsWidget)

        self.envLayout.setStretch(2, 1)

        self.gridLayout.addLayout(self.envLayout, 0, 0, 1, 1)

        self.algoScrollArea = QScrollArea(self.centralwidget)
        self.algoScrollArea.setObjectName("algoScrollArea")
        self.algoScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 529, 514))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.algoScrollAreaPreviewLabel = QLabel(self.scrollAreaWidgetContents)
        self.algoScrollAreaPreviewLabel.setObjectName("algoScrollAreaPreviewLabel")
        self.algoScrollAreaPreviewLabel.setStyleSheet(
            "QLabel {\n	color: rgba(0, 0, 0, 128);\n}"
        )

        self.verticalLayout.addWidget(self.algoScrollAreaPreviewLabel)

        self.algoScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.algoScrollArea, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "RLGUI", None)
        )
        self.algoOptsLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                """<html><head/><body><p align="center"><span style=" font-size:12pt;">algorithm options</span></p></body></html>""",
                None,
            )
        )
        self.algoPreviewLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt;">Argument options</span></p><p align="center"><span style=" font-size:10pt;">allows you to customize</span></p><p align="center"><span style=" font-size:10pt;">how an algortihm works</span></p></body></html>',
                None,
            )
        )
        self.trainBtn.setText(
            QCoreApplication.translate("MainWindow", "train an algorithm", None)
        )
        self.envOptsLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt;">environment options</span></p></body></html>',
                None,
            )
        )
        self.envBtn.setText(
            QCoreApplication.translate("MainWindow", "select an environment", None)
        )
        self.envArgsPreviewLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt;">select an environment</span></p><p align="center"><span style=" font-size:10pt;">to view its arguments</span></p></body></html>',
                None,
            )
        )
        self.algoScrollAreaPreviewLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:16pt;">No Reinforcement Learning Algorithm</span></p><p align="center"><span style=" font-size:16pt;"> has been selected</span></p></body></html>',
                None,
            )
        )

    # retranslateUi
