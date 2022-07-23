import re
from typing import List, Optional, Union
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem
from Models.Tour import Tour, TourStatus
from Models.Passenger import Passenger
from UI.SearchTourDialog import SearchTourDialog
from UI.Ui_SearchTourPassengersDialog import Ui_SearchTourPassengersDialog


class SearchTourPassengersDialog(Ui_SearchTourPassengersDialog, QDialog):
    def __init__(self, parent=None, multiSelection: bool = True, justForReport: bool = False) -> None:
        super(SearchTourPassengersDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnSelect.setVisible(not justForReport)
        self.tblPassengers.setSelectionMode(QAbstractItemView.MultiSelection if multiSelection else QAbstractItemView.SingleSelection)

        self.btnReturn.clicked.connect(lambda: self.reject())
        self.btnSelect.clicked.connect(self.OnSelectClicked)
        self.btnSearch.clicked.connect(self.OnSearchClicked)
        self.btnSearchTourId.clicked.connect(self.OnSearchTourIdClicked)
        self.tblPassengers.itemSelectionChanged.connect(self.OnSelectionChanged)

        self.tourId = None
        self.passengerId = None
        self.name = None
        self.family = None
        self.father = None
        self.phone = None

        self.passengers = dict()
        self.selectedPassengers = list()

    def ValidateInputs(self) -> bool:
        self.tourId = None
        self.passengerId = None
        self.name = None
        self.family = None
        self.father = None
        self.phone = None
        if self.txtTourId.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد اردو را وارد کنید')
            return False
        if not self.txtTourId.text().strip().isdigit():
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد اردو صحیح نیست')
            return False
        self.tourId = int(self.txtTourId.text().strip())
        tour = Tour.SearchTourById(self.tourId)
        if not tour:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این کد وجود ندارد')
            return False
        match = re.match(r'^\d{10}$', self.txtPassengerId.text().strip())
        if self.txtPassengerId.text().strip() != '' and not match:
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد ملی صحیح نیست')
            return False
        self.passengerId = self.txtPassengerId.text().strip() or None
        self.name = self.txtName.text().strip() or None
        self.family = self.txtFamily.text().strip() or None
        self.father = self.txtFather.text().strip() or None
        self.phone = self.txtPhone.text().strip() or None
        return True

    def OnSelectClicked(self) -> None:
        self.lblError.setVisible(False)
        rows = self.tblPassengers.selectionModel().selectedRows()
        if len(rows) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ مسافری انتخاب نشده است.')
            return
        self.accept()

    def OnSearchClicked(self) -> None:
        self.passengers = dict()
        self.tblPassengers.setRowCount(0)
        self.lblError.setVisible(False)
        if not self.ValidateInputs():
            return
        tour = Tour.SearchTourById(self.tourId)
        if len(tour.passengers) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ مسافری در این اردو ثبت نام نکرده است')
            return
        passengers = Tour.SearchTourPassengers(self.tourId, self.passengerId, self.name, self.family, self.father, self.phone)
        for p in passengers:
            rowCount = self.tblPassengers.rowCount()
            self.tblPassengers.setRowCount(rowCount + 1)
            self.tblPassengers.setItem(rowCount, 0, QTableWidgetItem(str(p.id)))
            self.tblPassengers.setItem(rowCount, 1, QTableWidgetItem(str(p.name)))
            self.tblPassengers.setItem(rowCount, 2, QTableWidgetItem(str(p.family)))
            self.tblPassengers.setItem(rowCount, 3, QTableWidgetItem(str(p.father)))
            self.tblPassengers.setItem(rowCount, 4, QTableWidgetItem(str(p.phone)))

            self.passengers[rowCount] = p

    def OnSelectionChanged(self) -> None:
        rows = self.tblPassengers.selectionModel().selectedRows()
        self.selectedPassengers = list()
        for row in rows:
            self.selectedPassengers.append(self.passengers[row.row()])

    def OnSearchTourIdClicked(self) -> None:
        res, tours = SearchTourDialog(self, None, False, False).exec()
        if res == QDialog.Accepted:
            self.tourId = tours[0].id
            self.txtTourId.setText(str(self.tourId))

    def exec(self) -> List[Union[int, Optional[int], Optional[List[Passenger]]]]:
        res = super(SearchTourPassengersDialog, self).exec()
        if res == QDialog.Accepted:
            return [res, self.tourId, self.selectedPassengers]
        return [res, None, None]
