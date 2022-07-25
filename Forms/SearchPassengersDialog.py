from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from Models.Passenger import Passenger
from UI.Ui_SearchPassengersDialog import Ui_SearchPassengersDialog


class SearchPassengersDialog(Ui_SearchPassengersDialog, QDialog):
    def __init__(self, parent=None) -> None:
        super(SearchPassengersDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.iconSearch = QIcon()
        self.iconSearch.addPixmap(QPixmap(":/icons/resources/icons/searchPassenger.png"), QIcon.Normal, QIcon.Off)
        self.iconReset = QIcon()
        self.iconReset.addPixmap(QPixmap(":/icons/resources/icons/reset.png"), QIcon.Normal, QIcon.Off)

        self.reset()
        self.passengerId = None
        self.name = None
        self.family = None
        self.father = None
        self.phone = None

        self.btnSearchId.clicked.connect(self.OnSearchIdClicked)
        self.btnReturn.clicked.connect(self.reject)
        self.btnSearch.clicked.connect(self.OnSearchClicked)

    def reset(self) -> None:
        self.lblError.setVisible(False)
        self.txtId.setText('')
        self.txtId.setEnabled(True)
        self.txtId.setFocus()
        self.btnSearchId.setIcon(self.iconSearch)
        self.txtName.setText('')
        self.txtFamily.setText('')
        self.txtFather.setText('')
        self.txtPhone.setText('')
        self.tblTours.setRowCount(0)

    def ValidateInputs(self) -> bool:
        self.name = None
        self.family = None
        self.father = None
        self.phone = None
        self.passengerId = self.txtId.text().strip()
        if self.passengerId == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد ملی را وارد کنید')
            self.passengerId = None
            return False
        if not (self.passengerId.isdigit() and len(self.passengerId) == 10):
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد ملی صحیح نیست')
            self.passengerId = None
            return False
        passenger = Passenger.GetPassengerById(self.passengerId)
        if not passenger:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ مسافری با این کد ملی تاکنون ثبت نام نکرده است')
            self.passengerId = None
            return False
        self.name = passenger.name
        self.family = passenger.family
        self.father = passenger.father
        self.phone = passenger.phone
        return True

    def OnSearchIdClicked(self) -> None:
        if not self.txtId.isEnabled():
            self.reset()
            return
        if not self.ValidateInputs():
            return
        self.txtId.setEnabled(False)
        self.btnSearchId.setIcon(self.iconReset)
        self.txtName.setText(self.name)
        self.txtFamily.setText(self.family)
        self.txtFather.setText(self.father)
        self.txtPhone.setText(self.phone)

    def OnSearchClicked(self) -> None:
        if self.txtName.text().strip() == '':
            self.OnSearchIdClicked()
            if self.lblError.isVisible():
                return
        tours = Passenger.SearchPassengerHistory(self.passengerId)
        if not tours:
            self.lblError.setVisible(True)
            self.lblError.setText('مسافر با این کد ملی تاکنون در هیچ سفری ثبت نام نکرده است یا از سفرهای خود انصراف داده است')
            return
        for tour in tours:
            rowCount = self.tblTours.rowCount()
            self.tblTours.setRowCount(rowCount + 1)
            self.tblTours.setItem(rowCount, 0, QTableWidgetItem(str(tour.id)))
            self.tblTours.setItem(rowCount, 1, QTableWidgetItem(tour.origin))
            self.tblTours.setItem(rowCount, 2, QTableWidgetItem(tour.destination))
            self.tblTours.setItem(rowCount, 3, QTableWidgetItem(str(tour.capacity)))
            self.tblTours.setItem(rowCount, 4, QTableWidgetItem(tour.departTime.isoformat(' ', 'minutes')))
            self.tblTours.setItem(rowCount, 5, QTableWidgetItem(tour.returnTime.isoformat(' ', 'minutes')))
            self.tblTours.setItem(rowCount, 6, QTableWidgetItem(tour.status))
            self.tblTours.setItem(rowCount, 7, QTableWidgetItem(str(len(tour.passengers))))
