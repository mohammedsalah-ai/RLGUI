from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QWidget


class QRCPage(QWebEnginePage):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def acceptNavigationRequest(
        self,
        url: QUrl | str,
        type: QWebEnginePage.NavigationType,
        isMainFrame: bool,
    ) -> bool:
        if isinstance(url, QUrl) and url.scheme() == "qrc":
            return True

        return False
