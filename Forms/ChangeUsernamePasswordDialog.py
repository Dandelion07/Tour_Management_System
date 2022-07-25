from typing import List, Union
from PyQt5.QtWidgets import QDialog
from Models.Account import Account
from UI.Ui_ChangeUsernamePasswordDialog import Ui_ChangeUsernamePasswordDialog
from Forms.YesNoDialog import YesNoDialog


class ChangeUsernamePasswordDialog(Ui_ChangeUsernamePasswordDialog, QDialog):
    def __init__(self, signedInUsername: str, parent=None) -> None:
        super(ChangeUsernamePasswordDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnBack.clicked.connect(self.reject)
        self.btnEdit.clicked.connect(self.OnEditClicked)

        self.username = None
        self.password = None
        self.newUsername = None
        self.newPassword = None
        self.newPasswordRepeat = None
        self.signedInUsername = signedInUsername

    def ValidateInputs(self) -> bool:
        self.username = None
        self.password = None
        self.newUsername = None
        self.newPassword = None
        self.newPasswordRepeat = None
        if self.txtUsername.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری کنونی را وارد کنید')
            return False
        self.username = self.txtUsername.text().strip()
        if self.txtPassword.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('رمز عبور کنونی را وارد کنید')
            return False
        self.password = self.txtPassword.text().strip()
        if self.signedInUsername != self.username:
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری نادرست است')
            return False
        if self.txtUsernameNew.text().strip() == '' and self.txtPasswordNew.text().strip() == '' and self.txtPasswordNewRepeat.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام کاربری یا رمز عبور جدید را وارد کنید')
            return False
        if self.txtUsernameNew.text().strip() != '':
            self.newUsername = self.txtUsernameNew.text().strip()
        if self.txtPasswordNew.text().strip() == '' and self.txtPasswordNewRepeat.text().strip() != '':
            self.lblError.setVisible(True)
            self.lblError.setText('رمز عبور جدید را وارد کنید')
            return False
        if self.txtPasswordNew.text().strip() != '' and self.txtPasswordNewRepeat.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('تکرار رمز عبور جدید را وارد کنید')
            return False
        if self.txtPasswordNew.text().strip() != '' and self.txtPasswordNewRepeat.text().strip() != '':
            self.newPassword = self.txtPasswordNew.text().strip()
            self.newPasswordRepeat = self.txtPasswordNewRepeat.text().strip()
        if self.newPassword and self.newPasswordRepeat and self.newPassword != self.newPasswordRepeat:
            self.lblError.setVisible(True)
            self.lblError.setText('تکرار رمز عبور جدید باید با رمز عبور جدید یکسان باشد')
            return False
        return True

    def OnEditClicked(self) -> None:
        if not self.ValidateInputs():
            return
        if YesNoDialog('آیا از تغییر اطلاعات مطمئن هستید؟', 'حذف کارشناس', self).exec() == QDialog.Rejected:
            return
        res = Account.EditUser(self.username, self.password, self.newUsername, self.newPassword)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('رمز عبور فعلی ناردست است')
            return
        self.accept()

    def exec(self) -> List[Union[int, str]]:
        res = super(ChangeUsernamePasswordDialog, self).exec()
        if res == QDialog.Accepted:
            return [res, self.newUsername]
        return [res, None]
