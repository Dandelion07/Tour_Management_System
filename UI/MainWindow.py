from PyQt5.QtCore import QLocale, Qt, QTimer
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog
from Models.Account import AccessLevel
from UI.DeleteTourDialog import DeleteTourDialog
from UI.Ui_MainWindow import Ui_MainWindow
from UI.MessageDialog import MessageDialog, MessageDialogType
from UI.CreateTourDialog import CreateTourDialog
import jdatetime


class Status:
    SIGNED_IN = 1
    SIGNED_OUT = -1
    CLOSED = 0


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, username: str, accessLevel: AccessLevel, role: int) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.status = Status.SIGNED_IN
        self.username = username
        self.accessLevel = accessLevel
        self.role = role
        self.CheckRole()
        self.statusBar.showMessage(jdatetime.datetime.now().isoformat(' ', 'seconds'))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.OnTimerTicked)
        self.timer.setInterval(1000)
        self.timer.start()

        self.lblRole = QLabel(self.statusBar)
        self.lblRole.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.lblRole.setAlignment(Qt.AlignCenter)
        self.lblRole.setObjectName("lblRole")
        self.statusBar.addPermanentWidget(self.lblRole)
        self.lblRole.setText('نقش: ' + ('مدیر فنی' if self.role == AccessLevel.MANAGER else 'کارشناس'))

        self.lblUsername = QLabel(self.statusBar)
        self.lblUsername.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.lblUsername.setAlignment(Qt.AlignCenter)
        self.lblUsername.setObjectName("lblUsername")
        self.statusBar.addPermanentWidget(self.lblUsername)
        self.lblUsername.setText('نام کاربری: ' + self.username)

        self.ExitAction.triggered.connect(self.OnCloseClicked)
        self.SignOutAction.triggered.connect(self.OnSignOutClicked)
        self.AboutAction.triggered.connect(self.OnAboutClicked)

        self.btnNewTour.clicked.connect(self.OnCreateNewTourClicked)
        self.btnDeleteTour.clicked.connect(self.OnDeleteTourClicked)

    def CheckRole(self) -> None:
        self.AddUserAction.setEnabled(self.accessLevel.addUser)
        self.DeleteUserAction.setEnabled(self.accessLevel.deleteUser)

        self.btnNewTour.setEnabled(self.accessLevel.createTour)
        self.btnDeleteTour.setEnabled(self.accessLevel.deleteTour)
        self.btnConfirmTour.setEnabled(self.accessLevel.confirmTour)
        self.btnAssignCars.setEnabled(self.accessLevel.reserveCars)

        self.btnRegisterPassenger.setEnabled(self.accessLevel.registerPassenger)
        self.btnEditRegistration.setEnabled(self.accessLevel.modifyPassenger)
        self.btnCancelRegistration.setEnabled(self.accessLevel.cancelRegistration)

    def closeEvent(self, a0: QCloseEvent) -> None:
        if self.status == Status.SIGNED_IN:
            self.status = Status.CLOSED

    def OnCloseClicked(self):
        self.close()

    def OnSignOutClicked(self):
        self.status = Status.SIGNED_OUT
        self.close()

    def OnAboutClicked(self):
        message = 'سیستم مدیریت اردوهای مرکز فرهنگی' + '\n' + 'تهیه کننده: پریسا سادات عمادی' + '\n' + 'سال 1401'
        MessageDialog(message, 'درباره برنامه', MessageDialogType.INFO).exec()

    def OnCreateNewTourClicked(self) -> None:
        res = CreateTourDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اردوی جدید ایجاد شد', 3000)
            MessageDialog('اردوی جدید با موفقیت ایجاد شد.', 'پیام', MessageDialogType.INFO, self).exec()

    def OnTimerTicked(self):
        try:
            self.statusBar.messageChanged.disconnect()
        except:
            pass
        self.statusBar.showMessage(jdatetime.datetime.now().isoformat(' ', 'seconds'))

    def ShowStatusBarMessage(self, message: str, msecs: int = 0):
        self.timer.stop()
        self.statusBar.showMessage(message, msecs)
        self.statusBar.messageChanged.connect(self.timer.start)

    def OnDeleteTourClicked(self) -> None:
        res = DeleteTourDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اردو با موفقیت حذف شد.', 3000)
            MessageDialog('اردو با موفقیت حذف شد.', 'پیام', MessageDialogType.INFO, self).exec()
