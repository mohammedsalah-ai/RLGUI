from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QWidget


class QRCPage(QWebEnginePage):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def acceptNavigationRequest(
        self,
        url: QUrl,
        type: QWebEnginePage.NavigationType,
        isMainFrame: bool,
    ) -> bool:
        if url.scheme() == "qrc":
            return True

        QDesktopServices.openUrl(url)
        return False
