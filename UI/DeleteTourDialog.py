import re
import jdatetime
import pyodbc
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem
from Models.Tour import TourStatus, Tour
from UI.Ui_DeleteTourDialog import Ui_DeleteTourDialog


class DeleteTourDialog(Ui_DeleteTourDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(DeleteTourDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.cmbStatus.addItems([TourStatus.NotConfirmed, TourStatus.Registering, TourStatus.FullCapacity])

        self.cmbOrigin.addItems([row.Origin for row in Tour.GetOrigins()])
        self.cmbDestination.addItems([row.Destination for row in Tour.GetDestinations()])

        self.btnReturn.clicked.connect(lambda: self.reject())
        self.btnDelete.clicked.connect(self.OnDeleteClicked)
        self.btnSearch.clicked.connect(self.OnSearchClicked)

        self.origin: str = None
        self.destination: str = None
        self.status: str = None
        self.fromDate: jdatetime.datetime = None
        self.toDate: jdatetime.datetime = None

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
        return True

    def OnSearchClicked(self) -> None:
        self.lblError.setVisible(False)
        if not self.ValidateInputs():
            return
        tours = Tour.SearchTours(self.destination, self.origin, None, self.fromDate, self.toDate, self.status)
        if len(tours) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این مشخصات یافت نشد.')
            return

        self.tblTours.setRowCount(0)
        for row in tours:
            rowCount = self.tblTours.rowCount()
            self.tblTours.setRowCount(rowCount + 1)
            self.tblTours.setItem(rowCount, 0, QTableWidgetItem(row.Id))
            self.tblTours.setItem(rowCount, 1, QTableWidgetItem(row.Origin))
            self.tblTours.setItem(rowCount, 2, QTableWidgetItem(row.Destination))
            self.tblTours.setItem(rowCount, 3, QTableWidgetItem(row.Capacity))
            self.tblTours.setItem(rowCount, 4, QTableWidgetItem(row.DepartTime))
            self.tblTours.setItem(rowCount, 5, QTableWidgetItem(row.ReturnTime))
            self.tblTours.setItem(rowCount, 6, QTableWidgetItem(row.Status))
            self.tblTours.setItem(rowCount, 7, QTableWidgetItem(len(row.Passengers.split('-'))))

    def OnDeleteClicked(self) -> None:
        self.lblError.setVisible(False)
        rows = self.tblTours.selectionModel().selectedRows()
        if len(rows) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ اردویی انتخاب نشده است.')
            return
        res = Tour.DeleteTours([row.model().itemData(0) for row in rows])
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در حذف اردوها به وجود آمده است.')
            return
        self.accept()
