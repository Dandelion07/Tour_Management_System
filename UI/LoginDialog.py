from typing import List, Union

from PyQt5.QtGui import QCloseEvent

from UI.Ui_LoginDialog import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog
from Models.Account import AccessLevel, Account


class LoginDialog(Ui_LoginDialog, QDialog):
    def __init__(self, role: int) -> None:
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.lblError.setVisible(False)
        self.role = role
        self.username = None
        self.accessLevel = None

        self.txtUsername.textChanged.connect(self.txtUsername_textChanged)
        self.txtPassword.textChanged.connect(self.txtPassword_textChanged)
        self.btnLogin.clicked.connect(self.btnLogin_clicked)
        self.btnBack.clicked.connect(self.btnBack_clicked)

        self.txtUsername.setFocus()

    def txtUsername_textChanged(self) -> None:
        self.lblError.setVisible(False)

    def txtPassword_textChanged(self) -> None:
        self.lblError.setVisible(False)

    def btnBack_clicked(self) -> None:
        self.reject()

    def btnLogin_clicked(self) -> None:
        if self.txtUsername.text().strip() == '':
            self.lblError.setText('نام کاربري را وارد کنيد')
            self.lblError.setVisible(True)
            return
        if self.txtPassword.text().strip() == '':
            self.lblError.setText('رمز عبور را وارد کنيد')
            self.lblError.setVisible(True)
            return
        self.lblError.setVisible(False)
        # TODO: Login user
        # self.username, self.accessLevel = Account.SignIn(self.txtUsername.text().strip(), self.txtPassword.text().strip(), self.role)
        self.username, self.accessLevel = Account.TestSignIn(self.txtUsername.text().strip(), self.txtPassword.text().strip(), self.role)
        if self.username is not None:
            self.accept()
        else:
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری یا رمز عبور نادرست است')

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.reject()

    def exec(self) -> List[Union[int, str, AccessLevel]]:
        res = super(LoginDialog, self).exec()
        return [res, self.username, self.accessLevel]
