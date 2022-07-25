from PyQt5.QtWidgets import QDialog
from Models.Account import Account, AccessLevel
from UI.Ui_AddUserDialog import Ui_AddUserDialog


class AddUserDialog(Ui_AddUserDialog, QDialog):
    def __init__(self, parent=None) -> None:
        super(AddUserDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnAddUser.clicked.connect(self.OnAddUserClicked)
        self.btnBack.clicked.connect(self.reject)

        self.username = None
        self.password = None
        self.passwordRepeat = None

    def ValidateInputs(self) -> bool:
        self.username = None
        self.password = None
        self.passwordRepeat = None
        if self.txtUsername.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری را وارد کنید')
            return False
        self.username = self.txtUsername.text().strip()
        if self.txtPassword.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('رمز عبور را وارد کنید')
            return False
        self.password = self.txtPassword.text().strip()
        if self.txtPasswordRepeat.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('تکرار رمز عبور را وارد کنید')
            return False
        self.passwordRepeat = self.txtPasswordRepeat.text().strip()
        if self.password != self.passwordRepeat:
            self.lblError.setVisible(True)
            self.lblError.setText('تکرار رمز عبور باید با رمز عبور یکسان باشد')
            return False
        return True

    def OnAddUserClicked(self) -> None:
        if not self.ValidateInputs():
            return
        res = Account.SignUp(self.username, self.password, AccessLevel.USER)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری تکراری است')
            return
        self.accept()
