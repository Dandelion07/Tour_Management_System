from PyQt5.QtCore import QObject, QEvent
from Models.Tour import Tour, TourStatus
from Forms.SearchTourDialog import SearchTourDialog
from UI.Ui_ConfirmTourDialog import Ui_ConfirmTourDialog
from PyQt5.QtWidgets import QDialog, QMainWindow
from Forms.YesNoDialog import YesNoDialog


class ConfirmTourDialog(Ui_ConfirmTourDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(ConfirmTourDialog, self).__init__(parent)
        self.setupUi(self)
        self.grpConfirm.setEnabled(False)
        self.checkboxes = [self.chbDestination, self.chbInsurance, self.chbConfirm]
        self.lblError.setVisible(False)
        self.txtTourId.installEventFilter(self)

        self.btnReturn.clicked.connect(self.reject)
        self.btnConfirm.clicked.connect(self.OnConfirmClicked)
        self.btnSearchId.clicked.connect(self.OnSearchIdClicked)
        self.tours = list()

        for chb in self.checkboxes:
            chb.stateChanged.connect(self.OnCheckedChanged)
        self.chbSelectAll.clicked.connect(self.OnSelectAllCheckedChanged)

    def OnCheckedChanged(self, checked: bool):
        if all([chb.isChecked() for chb in self.checkboxes]):
            self.chbSelectAll.setChecked(True)
        else:
            self.chbSelectAll.setChecked(False)

    def OnSelectAllCheckedChanged(self, checked: bool):
        for chb in self.checkboxes:
            chb.setChecked(checked)

    def OnConfirmClicked(self) -> None:
        self.lblError.setVisible(False)
        if any(not chb.isChecked() for chb in self.checkboxes):
            self.lblError.setVisible(True)
            self.lblError.setText('تمام موارد چک لیست را تایید کنید')
            return
        if YesNoDialog('آیا از تایید اردوهای انتخاب‌شده مطمئن هستید؟', 'حذف اردو', self).exec() == QDialog.Rejected:
            return
        res = Tour.ConfirmTour(int(self.txtTourId.text().strip()))
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در تایید اردو به وجود آمده است')
            return
        self.accept()

    def OnSearchIdClicked(self):
        res, self.tours = SearchTourDialog(self, [TourStatus.NotConfirmed], False, False).exec()
        if res == QDialog.Accepted:
            self.txtTourId.setText('-'.join(str(t.id) for t in self.tours))
            self.grpConfirm.setEnabled(len(self.tours) > 0)
            for chb in self.checkboxes:
                chb.setChecked(False)
            self.chbSelectAll.setChecked(False)
            self.lblError.setVisible(False)

    def ValidateInput(self) -> bool:
        self.lblError.setVisible(False)
        if self.txtTourId.text().strip() == '':
            self.grpConfirm.setEnabled(False)
            for chb in self.checkboxes:
                chb.setChecked(False)
            self.chbSelectAll.setChecked(False)
            return False
        if not self.txtTourId.text().strip().isdigit():
            self.grpConfirm.setEnabled(False)
            for chb in self.checkboxes:
                chb.setChecked(False)
            self.chbSelectAll.setChecked(False)
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد اردو نادرست است')
            return False
        tour = Tour.SearchTourById(int(self.txtTourId.text().strip()))
        if not tour:
            self.grpConfirm.setEnabled(False)
            for chb in self.checkboxes:
                chb.setChecked(False)
            self.chbSelectAll.setChecked(False)
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این کد وجود ندارد')
            return False
        if tour.status != TourStatus.NotConfirmed:
            self.grpConfirm.setEnabled(False)
            for chb in self.checkboxes:
                chb.setChecked(False)
            self.chbSelectAll.setChecked(False)
            self.lblError.setVisible(True)
            self.lblError.setText('اردوی انتخاب شده در وضعیت «تایید نشده» نیست')
            return False
        self.grpConfirm.setEnabled(True)
        for chb in self.checkboxes:
            chb.setChecked(False)
        self.chbSelectAll.setChecked(False)
        return True

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if source is self.txtTourId and event.type() == QEvent.FocusOut:
            self.ValidateInput()
        return super(ConfirmTourDialog, self).eventFilter(source, event)
