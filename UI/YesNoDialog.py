from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog

from UI.Ui_YesNoDialog import Ui_YesNoDialog


class YesNoDialog(Ui_YesNoDialog, QDialog):
    def __init__(self, message: str, title: str, parent=None) -> None:
        super(YesNoDialog, self).__init__(parent)
        self.setupUi(self)
        self.CustomizeUiWithMessage(message, title)

        # Signals and Slots
        self.btnYes.clicked.connect(lambda: self.accept())
        self.btnNo.clicked.connect(lambda: self.reject())

    def CustomizeUiWithMessage(self, message: str, title: str) -> None:
        self.setWindowTitle(title)
        self.lblMessage.setText(message)
        self.lblMessage.adjustSize()
        lblW, lblH = max(self.lblMessage.width(), 160), self.lblMessage.height()
        self.lblMessage.setFixedSize(lblW, lblH)
        self.setFixedSize(max(90 + lblW, 250), 120)

        self.lblMessage.move(10, 40 - lblH // 2)
        self.lblIcon.setFixedSize(60, 60)
        self.lblIcon.move(20 + lblW, 10)
        self.btnNo.setFixedSize(100, 30)
        self.btnNo.move((lblW - 140) // 2, 80)
        self.btnYes.setFixedSize(100, 30)
        self.btnYes.move((lblW + 120) // 2, 80)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.reject()
