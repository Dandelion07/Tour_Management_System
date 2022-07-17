import sys
from PyQt5.QtWidgets import QApplication, QDialog
from typing import List, Optional
from UI.LoginDialog import LoginDialog
from UI.SelectRoleDialog import SelectRoleDialog


class Application(QApplication):
    def __init__(self, argv: List[str]) -> None:
        super(Application, self).__init__(argv)
        self.role: Optional[int] = None
        self.username: Optional[str] = None

    def exec(self) -> int:
        while True:
            res, self.role = SelectRoleDialog().exec()
            if res == QDialog.Rejected:
                return 0
            res, self.username = LoginDialog(self.role).exec()
            if res == QDialog.Accepted:
                break
        # TODO Show main window here then run the event loop (i.e. execute the application)
        return super(Application, self).exec()


if __name__ == "__main__":
    app = Application(sys.argv)
    app.exec()
