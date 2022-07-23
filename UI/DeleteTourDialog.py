from PyQt5.QtWidgets import QDialog, QMainWindow
from Models.Tour import TourStatus, Tour
from UI.SearchTourDialog import SearchTourDialog
from UI.Ui_DeleteTourDialog import Ui_DeleteTourDialog
from UI.YesNoDialog import YesNoDialog


class DeleteTourDialog(Ui_DeleteTourDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(DeleteTourDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnReturn.clicked.connect(lambda: self.reject())
        self.btnDelete.clicked.connect(self.OnDeleteClicked)
        self.btnSearchId.clicked.connect(self.OnSearchIdClicked)
        self.tours = list()

    def OnDeleteClicked(self) -> None:
        self.lblError.setVisible(False)
        try:
            IDs = list(map(int, self.txtTourId.text().replace(' ', '').split('-')))
        except:
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد اردوها نادرست است')
            return
        if len(IDs) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ اردویی انتخاب نشده است.')
            return
        if YesNoDialog('آیا از حذف اردوهای انتخاب‌شده مطمئن هستید؟', 'حذف اردو', self).exec() == QDialog.Rejected:
            return
        res = Tour.DeleteTours(IDs)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در حذف اردوها به وجود آمده است.')
            return
        self.accept()

    def OnSearchIdClicked(self):
        res, self.tours = SearchTourDialog(self, [TourStatus.NotConfirmed, TourStatus.Registering, TourStatus.FullCapacity], True, False).exec()
        if res == QDialog.Accepted:
            self.txtTourId.setText('-'.join(str(t.id) for t in self.tours))
