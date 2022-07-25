from PyQt5.QtWidgets import QDialog
from Models.Tour import Tour, TourStatus
from Forms.SearchTourPassengersDialog import SearchTourPassengersDialog
from UI.Ui_CancelRegistrationDialog import Ui_CancelRegistrationDialog
from Forms.YesNoDialog import YesNoDialog


class CancelRegistrationDialog(Ui_CancelRegistrationDialog, QDialog):
    def __init__(self, parent=None):
        super(CancelRegistrationDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnSearchPassengerId.clicked.connect(self.OnSearchPassengerIdClicked)
        self.btnReturn.clicked.connect(self.reject)
        self.btnCancelRegistration.clicked.connect(self.OnCancelRegistrationClicked)

    def OnSearchPassengerIdClicked(self):
        res, tourId, passengers = SearchTourPassengersDialog(self, True, False).exec()
        if res == QDialog.Accepted:
            self.txtTourId.setText(str(tourId))
            self.txtPassengerId.setText('-'.join(p.id for p in passengers))

    def OnCancelRegistrationClicked(self) -> None:
        self.lblError.setVisible(False)
        if self.txtPassengerId.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد ملی مسافر را وارد کنید')
            return
        passengers = self.txtPassengerId.text().strip().split('-')
        for p in passengers:
            if not (p.isdigit() and len(p) == 10):
                self.lblError.setVisible(True)
                self.lblError.setText('فرمت کد ملی صحیح نیست')
                return
        if self.txtTourId.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد اردو را وارد کنید')
            return
        tour = Tour.SearchTourById(int(self.txtTourId.text().strip()))
        if not tour:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این کد وجود ندارد')
            return
        if tour.status in [TourStatus.Ended, TourStatus.Canceled]:
            self.lblError.setVisible(True)
            self.lblError.setText('امکان انصراف از اردوی برگزار شده یا اردوی حذف شده وجود ندارد')
            return
        res = YesNoDialog('آیا از انصراف مسافران از این اردو مطمئن هستید؟', 'انصراف از اردو', self).exec()
        if res == QDialog.Rejected:
            return
        res = Tour.CancelRegistration(int(self.txtTourId.text().strip()), self.txtPassengerId.text().strip().split('-'))
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در انصراف مسافران از اردو ایجاد شده است')
            return
        self.accept()
