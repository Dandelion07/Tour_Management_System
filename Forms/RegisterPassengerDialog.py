import re
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QMainWindow
from Models.Passenger import Passenger
from Models.Tour import TourStatus, Tour
from Forms.SearchTourDialog import SearchTourDialog
from UI.Ui_RegisterPassengerDialog import Ui_RegisterPassengerDialog


class RegisterPassengerDialog(Ui_RegisterPassengerDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(RegisterPassengerDialog, self).__init__(parent)
        self.setupUi(self)

        self.iconSearch = QIcon()
        self.iconSearch.addPixmap(QPixmap(":/icons/resources/icons/searchPassenger.png"), QIcon.Normal, QIcon.Off)
        self.iconReset = QIcon()
        self.iconReset.addPixmap(QPixmap(":/icons/resources/icons/reset.png"), QIcon.Normal, QIcon.Off)

        self.reset()
        self.btnSelectTour.clicked.connect(self.OnSelectTourClicked)
        self.btnSearchId.clicked.connect(self.OnSearchIdClicked)
        self.btnRegister.clicked.connect(self.OnRegisterClicked)
        self.btnReturn.clicked.connect(self.reject)

        self.tour = None
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

    def OnSelectTourClicked(self) -> None:
        (res, tours) = SearchTourDialog(self, [TourStatus.Registering], False, False).exec()
        if res == QDialog.Accepted:
            self.txtTourId.setText(str(tours[0].id))

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
                self.txtName.setEnabled(True)
                self.txtFamily.setEnabled(True)
                self.txtFather.setEnabled(True)
                self.txtPhone.setEnabled(True)
                self.txtName.setFocus()
            else:
                self.txtName.setText(passenger.name)
                self.txtFamily.setText(passenger.family)
                self.txtFather.setText(passenger.father)
                self.txtPhone.setText(passenger.phone)
        else:
            self.reset()

    def ValidateInputs(self) -> bool:
        self.tour = None
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
        if self.txtTourId.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد اردو را وارد کنید')
            return False
        if not self.txtTourId.text().strip().isdigit():
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد اردو نادرست است')
            return False
        self.tour = Tour.SearchTourById(int(self.txtTourId.text().strip()))
        if not self.tour:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این کد وجود ندارد')
            return False
        if self.tour.status == TourStatus.FullCapacity:
            self.lblError.setVisible(True)
            self.lblError.setText('ظرفیت این اردو تکمیل است')
            return False
        if self.tour.status != TourStatus.Registering:
            self.lblError.setVisible(True)
            self.lblError.setText('اردوی انتخاب شده در وضعیت «در حال ثبت نام» نیست')
            return False
        return True

    def OnRegisterClicked(self) -> None:
        if not self.ValidateInputs():
            return
        if self.id in self.tour.passengers:
            self.lblError.setVisible(True)
            self.lblError.setText('مسافری با این کد ملی قبلا در این اردو ثبت نام کرده است')
            return
        if not Passenger.CheckExists(self.id):
            res = Passenger.CreatePassenger(self.id, self.name, self.family, self.father, self.phone)
            if not res:
                self.lblError.setVisible(True)
                self.lblError.setText('مشکلی در ثبت اطلاعات مسافر به وجود آمده است')
                return
        res = Tour.RegisterPassenger(self.tour, self.id)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در ثبت اطلاعات مسافر به وجود آمده است')
            return
        self.accept()
