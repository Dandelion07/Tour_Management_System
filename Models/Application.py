import sys
from PyQt5.QtWidgets import QApplication, QDialog
from typing import List, Optional

from Models.Account import AccessLevel
from UI.LoginDialog import LoginDialog
from UI.SelectRoleDialog import SelectRoleDialog
from UI.MainWindow import MainWindow, Status


class Application(QApplication):
    def __init__(self, argv: List[str]) -> None:
        super(Application, self).__init__(argv)
        self.role: Optional[int] = None
        self.username: Optional[str] = None
        self.accessLevel: Optional[AccessLevel] = None

    def exec(self) -> int:
        while True:
            while True:
                res, self.role = SelectRoleDialog().exec()
                if res == QDialog.Rejected:
                    return 0
                res, self.username, self.accessLevel = LoginDialog(self.role).exec()
                if res == QDialog.Accepted:
                    break
            mainWindow = MainWindow(self.username, self.accessLevel, self.role)
            mainWindow.show()
            res = super(Application, self).exec()
            if mainWindow.status == Status.CLOSED:
                return res


if __name__ == "__main__":
    app = Application(sys.argv)
    app.exec()
