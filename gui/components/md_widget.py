from elements.md_widget.ui_md_widget import Ui_MDWidget
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QWidget

from components.utils.document import Document


class MDWidget(QWidget, Ui_MDWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.content = Document()
        self.channel = QWebChannel(self)
        self.channel.registerObject("content", self.content)
        self.preview.page().setWebChannel(self.channel)

    def setMD(self, text: str) -> None:
        self.content.setText(text)
