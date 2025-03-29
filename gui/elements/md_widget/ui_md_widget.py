# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'md_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import elements.md_widget.rc_md_widget  # noqa
from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
    QUrl,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QGridLayout


class Ui_MDWidget(object):
    def setupUi(self, MDWidget):
        if not MDWidget.objectName():
            MDWidget.setObjectName("MDWidget")
        MDWidget.resize(621, 508)
        self.gridLayout = QGridLayout(MDWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.preview = QWebEngineView(MDWidget)
        self.preview.setObjectName("preview")
        self.preview.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.preview.setUrl(QUrl("qrc:/md_widget/md_widget_resources/index.html"))

        self.gridLayout.addWidget(self.preview, 0, 0, 1, 1)

        self.retranslateUi(MDWidget)

        QMetaObject.connectSlotsByName(MDWidget)

    # setupUi

    def retranslateUi(self, MDWidget):
        MDWidget.setWindowTitle(
            QCoreApplication.translate("MDWidget", "MDWidget", None)
        )

    # retranslateUi
