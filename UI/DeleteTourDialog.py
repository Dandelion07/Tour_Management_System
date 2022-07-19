import re

import jdatetime
from PyQt5.QtWidgets import QDialog, QMainWindow

from Models.Tour import TourStatus, Tour
from UI.Ui_DeleteTourDialog import Ui_DeleteTourDialog


class DeleteTourDialog(Ui_DeleteTourDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(DeleteTourDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.cmbStatus.addItems([TourStatus.NotConfirmed, TourStatus.Registering, TourStatus.FullCapacity])

        self.btnReturn.clicked.connect(lambda: self.reject())
        self.btnDelete.clicked.connect(self.OnDeleteClicked)
        self.btnSearch.clicked.connect(self.OnSearchClicked)

        self.origin: str = None
        self.destination: str = None
        self.status: TourStatus = None
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
        tours = Tour.SearchTours()
        if len(tours) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این مشخصات یافت نشد.')
            return
        model = self.tblTours.model()
        for row in tours:
            model.insertRow(model.rowCount())



    def OnDeleteClicked(self) -> None:
        pass
