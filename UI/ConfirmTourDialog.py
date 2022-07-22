import datetime
import re
import jdatetime
from Models.Tour import Tour, TourStatus
from UI.DatePicker import DatePicker
from UI.Ui_ConfirmTourDialog import Ui_ConfirmTourDialog
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem

from UI.YesNoDialog import YesNoDialog


class ConfirmTourDialog(Ui_ConfirmTourDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(ConfirmTourDialog, self).__init__(parent)
        self.setupUi(self)
        self.grpConfirm.setEnabled(False)
        self.checkboxes = [self.chbDestination, self.chbInsurance, self.chbConfirm]
        self.lblError.setVisible(False)

        self.cmbOrigin.addItems(Tour.GetOrigins())
        self.cmbDestination.addItems(Tour.GetDestinations())

        self.btnReturn.clicked.connect(lambda: self.reject())
        self.btnConfirm.clicked.connect(self.OnConfirmClicked)
        self.btnSearch.clicked.connect(self.OnSearchClicked)
        self.btnFromDatePicker.clicked.connect(self.OnFromDatePickerClicked)
        self.btnToDatePicker.clicked.connect(self.OnToDatePickerClicked)
        self.tblTours.itemSelectionChanged.connect(self.OnSelectionChanged)

        self.origin: str = None
        self.destination: str = None
        self.fromDate: jdatetime.datetime = None
        self.toDate: jdatetime.datetime = None

    def OnSelectionChanged(self):
        self.grpConfirm.setEnabled(len(self.tblTours.selectionModel().selectedRows()) > 0)

    def ValidateInputs(self) -> bool:
        self.origin = self.cmbOrigin.currentText().strip() or None
        self.destination = self.cmbDestination.currentText().strip() or None
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

    def OnFromDatePickerClicked(self):
        res, date = DatePicker(self).exec()
        if res == QDialog.Accepted:
            self.txtFromDate.setText(str(date))

    def OnToDatePickerClicked(self):
        res, date = DatePicker(self).exec()
        if res == QDialog.Accepted:
            self.txtToDate.setText(str(date))

    def OnSearchClicked(self) -> None:
        self.tblTours.setRowCount(0)
        self.lblError.setVisible(False)
        if not self.ValidateInputs():
            return
        tours = Tour.SearchTours(self.destination, self.origin, None, self.fromDate.togregorian() if self.fromDate else None, self.toDate.togregorian() if self.toDate else None, TourStatus.NotConfirmed, False, False)
        if len(tours) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این مشخصات یافت نشد.')
            return

        for row in tours:
            rowCount = self.tblTours.rowCount()
            self.tblTours.setRowCount(rowCount + 1)
            self.tblTours.setItem(rowCount, 0, QTableWidgetItem(str(row["Id"])))
            self.tblTours.setItem(rowCount, 1, QTableWidgetItem(row["Origin"]))
            self.tblTours.setItem(rowCount, 2, QTableWidgetItem(row["Destination"]))
            self.tblTours.setItem(rowCount, 3, QTableWidgetItem(str(row["Capacity"])))
            self.tblTours.setItem(rowCount, 4, QTableWidgetItem(jdatetime.datetime.fromgregorian(datetime=datetime.datetime.fromisoformat(row["DepartTime"])).isoformat(' ', 'minutes')))
            self.tblTours.setItem(rowCount, 5, QTableWidgetItem(jdatetime.datetime.fromgregorian(datetime=datetime.datetime.fromisoformat(row["ReturnTime"])).isoformat(' ', 'minutes')))
            self.tblTours.setItem(rowCount, 6, QTableWidgetItem(row["Status"]))

    def OnConfirmClicked(self) -> None:
        self.lblError.setVisible(False)
        rows = self.tblTours.selectionModel().selectedRows()
        if len(rows) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ اردویی انتخاب نشده است.')
            return
        if any(not chb.isChecked() for chb in self.checkboxes):
            self.lblError.setVisible(True)
            self.lblError.setText('تمام موارد چک لیست را تایید کنید')
            return
        if YesNoDialog('آیا از تایید اردوهای انتخاب‌شده مطمئن هستید؟', 'حذف اردو', self).exec() == QDialog.Rejected:
            return
        row = rows[0]
        res = Tour.ConfirmTour(int(self.tblTours.item(row.row(), 0).text()))
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در حذف تایید اردو به وجود آمده است.')
            return
        self.accept()
