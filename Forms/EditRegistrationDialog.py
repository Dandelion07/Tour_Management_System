import re
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog
from Models.Passenger import Passenger
from UI.Ui_EditRegistrationDialog import Ui_EditRegistrationDialog
from Forms.YesNoDialog import YesNoDialog


class EditRegistrationDialog(Ui_EditRegistrationDialog, QDialog):
    def __init__(self, parent=None):
        super(EditRegistrationDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.iconSearch = QIcon()
        self.iconSearch.addPixmap(QPixmap(":/icons/resources/icons/searchPassenger.png"), QIcon.Normal, QIcon.Off)
        self.iconReset = QIcon()
        self.iconReset.addPixmap(QPixmap(":/icons/resources/icons/reset.png"), QIcon.Normal, QIcon.Off)

        self.reset()
        self.btnSearchId.clicked.connect(self.OnSearchIdClicked)
        self.btnEdit.clicked.connect(self.OnEditClicked)
        self.btnReturn.clicked.connect(self.reject)

        self.id = None
        self.name = None
        self.family = None
        self.father = None
        self.phone = None

    def reset(self):
        self.lblError.setVisible(False)
        self.txtId.setEnabled(True)
        self.txtId.setText('')
        self.btnSearchId.setIcon(self.iconSearch)
        self.txtName.setEnabled(False)
        self.txtName.setText('')
        self.txtFamily.setEnabled(False)
        self.txtFamily.setText('')
        self.txtFather.setEnabled(False)
        self.txtFather.setText('')
        self.txtPhone.setEnabled(False)
        self.txtPhone.setText('')

    def OnSearchIdClicked(self) -> None:
        self.lblError.setVisible(False)
        if self.txtId.isEnabled():
            IdPattern = r'^\d{10}$'
            match = re.match(IdPattern, self.txtId.text().strip())
            if not match:
                self.lblError.setVisible(True)
                self.lblError.setText('فرمت کد ملی صحیح نیست')
                return
            passenger = Passenger.GetPassengerById(self.txtId.text().strip())
            self.btnSearchId.setIcon(self.iconReset)
            self.txtId.setEnabled(False)
            if not passenger:
                self.lblError.setVisible(True)
                self.lblError.setText('مسافری با این کد ملی تاکنون ثبت نام نکرده است')
                return
            else:
                self.txtName.setText(passenger.name)
                self.txtFamily.setText(passenger.family)
                self.txtFather.setText(passenger.father)
                self.txtPhone.setText(passenger.phone)

                self.txtName.setEnabled(True)
                self.txtFamily.setEnabled(True)
                self.txtFather.setEnabled(True)
                self.txtPhone.setEnabled(True)

        else:
            self.reset()

    def ValidateInputs(self) -> bool:
        self.id = None
        self.name = None
        self.family = None
        self.father = None
        self.phone = None

        self.lblError.setVisible(False)

        if self.txtId.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد ملی مسافر را وارد کنید')
            return False
        self.id = self.txtId.text().strip()
        if self.txtName.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام مسافر را وارد کنید')
            return False
        self.name = self.txtName.text().strip()
        if self.txtFamily.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام خانوادگی مسافر را وارد کنید')
            return False
        self.family = self.txtFamily.text().strip()
        if self.txtFather.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('نام پدر را وارد کنید')
            return False
        self.father = self.txtFather.text().strip()
        if self.txtPhone.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('شماره موبایل مسافر را وارد کنید')
            return False
        self.phone = self.txtPhone.text().strip()
        return True

    def OnEditClicked(self):
        if not self.ValidateInputs():
            return
        res = YesNoDialog('آیا از ویرایش اطلاعات وارد شده مطمئن هستید؟', 'ویرایش اطلاعات', self).exec()
        if res == QDialog.Rejected:
            return
        res = Passenger.ModifyPassenger(self.id, self.name, self.family, self.father, self.phone)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در ویرایش اطلاعات به وجود آمده است')
            return
        self.accept()
