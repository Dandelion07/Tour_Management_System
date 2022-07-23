import re
from typing import List, Optional, Union
import jdatetime
from UI.DatePicker import DatePicker
from UI.Ui_SearchTourDialog import Ui_SearchTourDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView
from Models.Tour import TourStatus, Tour


class SearchTourDialog(Ui_SearchTourDialog, QDialog):
    def __init__(self, parent = None, status: List[str] = None, multiSelection: bool = True, justForReport: bool = False) -> None:
        super(SearchTourDialog, self).__init__(parent)
        self.setupUi(self)
        self.statusList = status or [TourStatus.NotConfirmed, TourStatus.Registering, TourStatus.FullCapacity, TourStatus.Ended, TourStatus.Canceled]
        self.lblError.setVisible(False)
        self.cmbStatus.addItems(self.statusList)

        self.cmbOrigin.addItems(Tour.GetOrigins())
        self.cmbDestination.addItems(Tour.GetDestinations())

        self.btnSelect.setVisible(not justForReport)
        self.tblTours.setSelectionMode(QAbstractItemView.MultiSelection if multiSelection else QAbstractItemView.SingleSelection)

        self.btnReturn.clicked.connect(lambda: self.reject())
        self.btnSelect.clicked.connect(self.OnSelectClicked)
        self.btnSearch.clicked.connect(self.OnSearchClicked)
        self.btnFromDatePicker.clicked.connect(self.OnFromDatePickerClicked)
        self.btnToDatePicker.clicked.connect(self.OnToDatePickerClicked)
        self.tblTours.itemSelectionChanged.connect(self.OnSelectionChanged)

        self.origin: str = None
        self.destination: str = None
        self.status: str = None
        self.fromDate: jdatetime.datetime = None
        self.toDate: jdatetime.datetime = None

        self.tours = dict()
        self.selectedTours = list()

    def ValidateInputs(self) -> bool:
        self.origin = self.cmbOrigin.currentText().strip() or None
        self.destination = self.cmbDestination.currentText().strip() or None
        self.status = self.cmbStatus.currentText()
        self.fromDate = None
        self.toDate = None

        datePattern = r'^([1-9]\d{3})-(\d{1,2})-(\d{1,2})$'
        match = re.match(datePattern, self.txtFromDate.text())
        if self.txtFromDate.text().strip() != '':
            if not match:
                self.lblError.setVisible(True)
                self.lblError.setText('فرمت تاریخ صحیح نیست')
                return False
            try:
                self.fromDate = jdatetime.datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            except ValueError:
                self.lblError.setVisible(True)
                self.lblError.setText('تاریخ صحیح نیست')
                return False

        if self.txtToDate.text().strip() != '':
            match = re.match(datePattern, self.txtToDate.text())
            if not match:
                self.lblError.setVisible(True)
                self.lblError.setText('فرمت تاریخ صحیح نیست')
                return False
            try:
                self.toDate = jdatetime.datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            except ValueError:
                self.lblError.setVisible(True)
                self.lblError.setText('تاریخ صحیح نیست')
                return False
        if self.fromDate and self.toDate and self.toDate < self.fromDate:
            self.lblError.setVisible(True)
            self.lblError.setText('تاریخ دوم نباید زودتر از تاریخ اول باشد.')
            return False
        return True

    def OnSearchClicked(self) -> None:
        self.tours = dict()
        self.tblTours.setRowCount(0)
        self.lblError.setVisible(False)
        if not self.ValidateInputs():
            return
        tours = Tour.SearchTours(self.destination, self.origin, None, self.fromDate.togregorian() if self.fromDate else None, self.toDate.togregorian() if self.toDate else None, self.status, True, True)
        if len(tours) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این مشخصات یافت نشد.')
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
            self.tours[rowCount] = tour

    def OnSelectClicked(self):
        self.lblError.setVisible(False)
        rows = self.tblTours.selectionModel().selectedRows()
        if len(rows) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ اردویی انتخاب نشده است.')
            return
        self.accept()

    def OnFromDatePickerClicked(self):
        res, date = DatePicker(self).exec()
        if res == QDialog.Accepted:
            self.txtFromDate.setText(str(date))

    def OnToDatePickerClicked(self):
        res, date = DatePicker(self).exec()
        if res == QDialog.Accepted:
            self.txtToDate.setText(str(date))

    def OnSelectionChanged(self):
        rows = self.tblTours.selectionModel().selectedRows()
        self.selectedTours = list()
        for row in rows:
            self.selectedTours.append(self.tours[row.row()])

    def exec(self) -> List[Union[int, Optional[List[Tour]]]]:
        res = super(SearchTourDialog, self).exec()
        if res == QDialog.Accepted:
            return [res, self.selectedTours]
        return [res, None]
