from PyQt5.QtWidgets import QDialog

from UI.SearchTourPassengersDialog import SearchTourPassengersDialog
from UI.Ui_CancelRegistrationDialog import Ui_CancelRegistrationDialog


class CancelRegistrationDialog(Ui_CancelRegistrationDialog, QDialog):
    def __init__(self, parent=None):
        super(CancelRegistrationDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)

        self.btnSearchPassengerId.clicked.connect(self.OnSearchPassengerIdClicked)
        self.btnReturn.clicked.connect(self.reject)

    def OnSearchPassengerIdClicked(self):
        SearchTourPassengersDialog(self, True, False).exec()
