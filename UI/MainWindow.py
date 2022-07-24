from PyQt5.QtCore import QLocale, Qt, QTimer
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog
from Models.Account import AccessLevel
from UI.AddUserDialog import AddUserDialog
from UI.CancelRegistrationDialog import CancelRegistrationDialog
from UI.ChangeUsernamePasswordDialog import ChangeUsernamePasswordDialog
from UI.ConfirmTourDialog import ConfirmTourDialog
from UI.DeleteTourDialog import DeleteTourDialog
from UI.DeleteUserDialog import DeleteUserDialog
from UI.EditRegistrationDialog import EditRegistrationDialog
from UI.RegisterPassengerDialog import RegisterPassengerDialog
from UI.ReserveCarsDialog import ReserveCarsDialog
from UI.SearchPassengersDialog import SearchPassengersDialog
from UI.SearchTourDialog import SearchTourDialog
from UI.SearchTourPassengersDialog import SearchTourPassengersDialog
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
        self.AddUserAction.triggered.connect(self.OnAddUserClicked)
        self.DeleteUserAction.triggered.connect(self.OnDeleteUserClicked)
        self.ChangePasswordAction.triggered.connect(self.OnChangeUsernamePasswordClicked)

        self.btnNewTour.clicked.connect(self.OnCreateNewTourClicked)
        self.btnDeleteTour.clicked.connect(self.OnDeleteTourClicked)
        self.btnConfirmTour.clicked.connect(self.OnConfirmTourClicked)
        self.btnRegisterPassenger.clicked.connect(self.OnRegisterPassengerClicked)
        self.btnEditRegistration.clicked.connect(self.OnEditRegistrationClicked)
        self.btnSearchTours.clicked.connect(self.OnSearchToursClicked)
        self.btnCancelRegistration.clicked.connect(self.OnCancelRegistrationClicked)
        self.btnSearchTourPassengers.clicked.connect(self.OnSearchTourPassengersClicked)
        self.btnSearchPassengers.clicked.connect(self.OnSearchPassengersClicked)
        self.btnAssignCars.clicked.connect(self.OnReserveCarsClicked)
        self.btnSearchTourCars.clicked.connect(self.OnSearchTourCarsClicked)

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

    def OnCloseClicked(self) -> None:
        self.close()

    def OnSignOutClicked(self) -> None:
        self.status = Status.SIGNED_OUT
        self.close()

    def OnAboutClicked(self) -> None:
        message = 'سیستم مدیریت اردوهای مرکز فرهنگی' + '\n' + 'تهیه کننده: پریسا سادات عمادی' + '\n' + 'سال 1401'
        MessageDialog(message, 'درباره برنامه', MessageDialogType.INFO).exec()

    def OnCreateNewTourClicked(self) -> None:
        res = CreateTourDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اردوی جدید ایجاد شد', 3000)
            MessageDialog('اردوی جدید با موفقیت ایجاد شد.', 'پیام', MessageDialogType.INFO, self).exec()

    def OnTimerTicked(self) -> None:
        try:
            self.statusBar.messageChanged.disconnect()
        except:
            pass
        self.statusBar.showMessage(jdatetime.datetime.now().isoformat(' ', 'seconds'))

    def ShowStatusBarMessage(self, message: str, msecs: int = 0) -> None:
        self.timer.stop()
        self.statusBar.showMessage(message, msecs)
        self.statusBar.messageChanged.connect(self.timer.start)

    def OnDeleteTourClicked(self) -> None:
        res = DeleteTourDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اردو با موفقیت حذف شد.', 3000)
            MessageDialog('اردو با موفقیت حذف شد.', 'پیام', MessageDialogType.INFO, self).exec()

    def OnConfirmTourClicked(self) -> None:
        res = ConfirmTourDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اردو با موفقیت تایید شد', 3000)
            MessageDialog('اردو با موفقیت تایید شد', 'پیام', MessageDialogType.INFO).exec()

    def OnRegisterPassengerClicked(self) -> None:
        res = RegisterPassengerDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('مسافر با موفقیت ثبت‌ نام شد', 3000)
            MessageDialog('مسافر با موفقیت ثبت نام شد.', 'پیام', MessageDialogType.INFO).exec()

    def OnEditRegistrationClicked(self) -> None:
        res = EditRegistrationDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اطلاعات مسافر با موفقیت ویرایش شد', 3000)
            MessageDialog('اطلاعات مسافر با موفقیت ویرایش شد', 'پیام', MessageDialogType.INFO).exec()

    def OnSearchToursClicked(self) -> None:
        SearchTourDialog(self, None, True, True).exec()

    def OnCancelRegistrationClicked(self) -> None:
        res = CancelRegistrationDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('انصراف مسافران با موفقیت انجام شد', 3000)
            MessageDialog('انصراف مسافران با موفقیت انجام شد', 'پیام', MessageDialogType.INFO).exec()

    def OnSearchTourPassengersClicked(self) -> None:
        SearchTourPassengersDialog(self, True, True).exec()

    def OnSearchPassengersClicked(self) -> None:
        SearchPassengersDialog(self).exec()

    def OnReserveCarsClicked(self) -> None:
        res = ReserveCarsDialog(self, False).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('سرویس های اردوی مورد نظر با موفقیت ثبت شد', 3000)
            MessageDialog('سرویس های اردوی مورد نظر با موفقیت ثبت شد', 'پیام', MessageDialogType.INFO).exec()

    def OnSearchTourCarsClicked(self) -> None:
        ReserveCarsDialog(self, True).exec()

    def OnAddUserClicked(self):
        res = AddUserDialog(self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('کارشناس جدید با موفقیت ایجاد شد', 3000)
            MessageDialog('کارشناس جدید با موفقیت ایجاد شد', 'پیام', MessageDialogType.INFO).exec()

    def OnDeleteUserClicked(self):
        res = DeleteUserDialog(self.username, self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('کارشناس با موفقیت حذف شد', 3000)
            MessageDialog('کارشناس با موفقیت حذف شد', 'پیام', MessageDialogType.INFO).exec()

    def OnChangeUsernamePasswordClicked(self):
        res, username = ChangeUsernamePasswordDialog(self.username, self).exec()
        if res == QDialog.Accepted:
            self.ShowStatusBarMessage('اطلاعات با موفقیت تغییر یافت', 3000)
            MessageDialog('اطلاعات با موفقیت تغییر یافت', 'پیام', MessageDialogType.INFO).exec()
            self.username = username
            self.lblUsername.setText('نام کاربری: ' + self.username)
