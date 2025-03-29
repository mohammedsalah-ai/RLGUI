from elements.md_widget.ui_md_widget import Ui_MDWidget
from PySide6.QtCore import QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QWidget

from components.utils.document import Document
from components.utils.qrc_page import QRCPage


class MDWidget(QWidget, Ui_MDWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.content = Document()
        self.page = QRCPage(self.preview)
        self.channel = QWebChannel(self)

        self.channel.registerObject("content", self.content)
        self.page.setWebChannel(self.channel)
        self.preview.setPage(self.page)
        self.preview.setUrl(QUrl("qrc:/md_widget/md_widget_resources/index.html"))

    def setMD(self, text: str) -> None:
        self.content.setText(text)
