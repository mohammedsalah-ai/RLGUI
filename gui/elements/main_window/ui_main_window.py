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
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QPalette,
)
from PySide6.QtWidgets import (
    QMenuBar,
    QPushButton,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.envBtn = QPushButton(self.centralwidget)
        self.envBtn.setObjectName("envBtn")
        self.envBtn.setGeometry(QRect(30, 30, 116, 39))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "RLGUI", None)
        )
        self.envBtn.setText(
            QCoreApplication.translate("MainWindow", "environements", None)
        )

    # retranslateUi
