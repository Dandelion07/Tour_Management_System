from PyQt5.QtWidgets import QDialog, QMainWindow
from Models.Tour import TourStatus, Tour
from UI.SearchTourDialog import SearchTourDialog
from UI.Ui_RegisterPassengerDialog import Ui_RegisterPassengerDialog


class RegisterPassengerDialog(Ui_RegisterPassengerDialog, QDialog):
    def __init__(self, parent: QMainWindow = None):
        super(RegisterPassengerDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)
        self.tour = None

        self.btnSelectTour.clicked.connect(self.OnSelectTourClicked)

    def OnSelectTourClicked(self):
        (res, tours) = SearchTourDialog(self, [TourStatus.Registering], False, False).exec()
        if res == QDialog.Accepted:
            self.txtTourId.setText(str(tours[0].id))
