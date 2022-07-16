from Ui_LoginWindow import Ui_LoginWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class LoginWindow(QMainWindow, Ui_LoginWindow):
    closeSignal = pyqtSignal()
    #TODO: DELETE THIS SECTION
    loginSignal = pyqtSignal(str)
        
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.txtUsername.textChanged.connect(self.txtUsername_textChanged)
        self.txtPassword.textChanged.connect(self.txtPassword_textChanged)
        self.btnLogin.clicked.connect(self.btnLogin_clicked)
        self.btnCancel.clicked.connect(self.btnCancel_clicked)
        self.closeSignal.connect(self.on_close)

    def txtUsername_textChanged(self, text):
        self.lblError.setVisible(False)

    def txtPassword_textChanged(self, text):
        self.lblError.setVisible(False)

    def btnCancel_clicked(self, checked):
        self.close()
        self.parent.show()

    def btnLogin_clicked(self, checked):
        if self.txtUsername.text().strip() == '':
            self.lblError.setText('نام کاربري را وارد کنيد')
            self.lblError.setVisible(True)
            return
        if self.txtPassword.text().strip() == '':
            self.lblError.setText('رمز عبور را وارد کنيد')
            self.lblError.setVisible(True)
            return
        self.lblError.setVisible(False)
        #TODO: Login user
        self.loginSignal.emit(self.txtUsername.text())
        self.close()

    def closeEvent(self, event):
        self.closeSignal.emit()

    def on_close(self):
        if self.parent:
            self.parent.show()
