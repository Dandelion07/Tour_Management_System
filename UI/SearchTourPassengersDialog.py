from PyQt5.QtWidgets import QDialog, QAbstractItemView

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
        pass

    def OnSelectClicked(self) -> None:
        pass

    def OnSearchClicked(self) -> None:
        pass

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
