from PySide6.QtCore import Property, QObject, Signal
from PySide6.QtWidgets import QWidget


class Document(QObject):
    textChanged = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._text = ""

    def text(self) -> str:
        return self._text

    def setText(self, t: str) -> None:
        if t != self._text:
            self._text = t
            self.textChanged.emit(t)

    text = Property(str, text, setText, notify=textChanged)
