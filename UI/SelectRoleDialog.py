from typing import Union, List
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog
from UI.Ui_SelectRoleDialog import Ui_SelectRoleDialog
from Models.Account import AccessLevel


class SelectRoleDialog(Ui_SelectRoleDialog, QDialog):
    def __init__(self):
        super(SelectRoleDialog, self).__init__()
        self.setupUi(self)
        self.role = None

        self.btnManager.clicked.connect(lambda: self.OnSelectRole(AccessLevel.MANAGER))
        self.btnUser.clicked.connect(lambda: self.OnSelectRole(AccessLevel.USER))

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.reject()

    def OnSelectRole(self, role: int) -> None:
        self.role = role
        self.accept()

    def exec(self) -> List[Union[int, int]]:
        res = super(SelectRoleDialog, self).exec()
        return [res, self.role]
