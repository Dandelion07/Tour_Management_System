import sys

from UI.LoginDialog import LoginDialog
from UI.SelectRoleDialog import SelectRoleDialog
from PyQt5.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)

while True:
    selectRoleDlg = SelectRoleDialog()
    res, role = selectRoleDlg.exec()
    if res == QDialog.Rejected:
        break
    loginDlg = LoginDialog(role)
    if loginDlg.exec() == QDialog.Accepted:
        break
