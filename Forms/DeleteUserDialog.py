from PyQt5.QtWidgets import QDialog
from Models.Account import Account
from UI.Ui_DeleteUserDialog import Ui_DeleteUserDialog
from Forms.YesNoDialog import YesNoDialog


class DeleteUserDialog(Ui_DeleteUserDialog, QDialog):
    def __init__(self, adminUser: str, parent=None) -> None:
        super(DeleteUserDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnBack.clicked.connect(self.reject)
        self.btnDeleteUser.clicked.connect(self.OnDeleteUserClicked)

        self.username = None
        self.adminUsername = adminUser

    def ValidateInputs(self) -> bool:
        self.username = None
        if self.txtUsername.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری را وارد کنید')
            return False
        if self.txtUsername.text().strip() == self.adminUsername:
            self.lblError.setVisible(True)
            self.lblError.setText('مدیر فنی نمی تواند حساب خود را حذف کند')
            return False
        self.username = self.txtUsername.text().strip()
        return True

    def OnDeleteUserClicked(self) -> None:
        if not self.ValidateInputs():
            return
        if YesNoDialog('آیا از حذف این کارشناس مطمئن هستید؟', 'حذف کارشناس', self).exec() == QDialog.Rejected:
            return
        res = Account.DeleteUser(self.username, self.adminUsername)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('کارشناسی با این نام کاربری وجود ندارد')
            return
        self.accept()
