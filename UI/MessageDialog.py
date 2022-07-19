from PyQt5.QtGui import QIcon, QPixmap, QCloseEvent
from PyQt5.QtWidgets import QDialog
from UI.Ui_MessageDialog import Ui_MessageDialog


class MessageDialogType:
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'


class MessageDialog(Ui_MessageDialog, QDialog):
    def __init__(self, message: str, title: str, dialog_type: str = 'info', parent=None) -> None:
        super(MessageDialog, self).__init__(parent)
        self.setupUi(self)
        self.CustomizeUiWithMessage(message, title, dialog_type)
        self.btnClose.clicked.connect(lambda: self.accept())

    def CustomizeUiWithMessage(self, message: str, title: str, dialog_type: str = 'info'):
        self.setWindowTitle(title)
        self.lblMessage.setText(message)
        self.lblMessage.adjustSize()
        lblW, lblH = max(self.lblMessage.width(), 160), self.lblMessage.height()
        self.lblMessage.setFixedSize(lblW, lblH)
        self.setFixedSize(max(90 + lblW, 250), 120)

        self.lblMessage.move(10, 40 - lblH // 2)
        self.lblIcon.setFixedSize(60, 60)
        self.lblIcon.move(20 + lblW, 10)
        self.btnClose.setFixedSize(100, 30)
        self.btnClose.move((lblW - 10) // 2, 80)

        pixmap = QPixmap(f":/icons/resources/icons/{dialog_type}.png")
        icon = QIcon()
        icon.addPixmap(pixmap, QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.lblIcon.setPixmap(pixmap)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.accept()
