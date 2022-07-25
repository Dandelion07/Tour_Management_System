from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from Forms.SearchTourDialog import SearchTourDialog
from UI.Ui_ReserveCarsDialog import Ui_ReserveCarsDialog
from Models.Tour import Tour, TourStatus
from Forms.YesNoDialog import YesNoDialog


class ReserveCarsDialog(Ui_ReserveCarsDialog, QDialog):
    def __init__(self, parent=None, justForReport: bool = False) -> None:
        super(ReserveCarsDialog, self).__init__(parent)
        self.setupUi(self)
        self.lblError.setVisible(False)
        self.justForReport = justForReport
        self.btnSelect.setVisible(not justForReport)
        self.btnSearch.setText('نمایش لیست سرویس های اردو' if justForReport else 'نمایش لیست سرویس های قابل انتخاب')

        self.btnSearchTourId.clicked.connect(self.OnSearchTourIdClicked)
        self.btnSearch.clicked.connect(self.OnSearchClicked)
        self.btnReturn.clicked.connect(self.reject)
        self.btnSelect.clicked.connect(self.OnSelectClicked)
        self.tblCars.itemSelectionChanged.connect(self.OnSelectionChanged)

        self.tourId = None
        self.tour = None
        self.cars = dict()
        self.selectedCars = list()

    def OnSearchTourIdClicked(self) -> None:
        status = [TourStatus.Registering, TourStatus.FullCapacity, TourStatus.Ended, TourStatus.Canceled] if self.justForReport else [TourStatus.Registering, TourStatus.FullCapacity]
        res, tours = SearchTourDialog(self, status, False, False).exec()
        if res == QDialog.Accepted:
            tour: Tour = tours[0]
            self.txtTourId.setText(str(tour.id))
            self.txtOrigin.setText(tour.origin)
            self.txtDestination.setText(tour.destination)
            self.txtDepartTime.setText(tour.departTime.isoformat(' ', 'minutes'))
            self.txtReturnTime.setText(tour.returnTime.isoformat(' ', 'minutes'))
            self.txtCapacity.setText(str(tour.capacity))
            self.lblError.setVisible(False)

    def ValidateInputs(self) -> bool:
        self.tourId = None
        self.tour = None
        if self.txtTourId.text().strip() == '':
            self.lblError.setVisible(True)
            self.lblError.setText('کد اردو را وارد کنید')
            return False
        if not self.txtTourId.text().strip().isdigit():
            self.lblError.setVisible(True)
            self.lblError.setText('فرمت کد اردو صحیح نیست')
            return False
        self.tourId = int(self.txtTourId.text().strip())
        self.tour = Tour.SearchTourById(self.tourId)
        if not self.tour:
            self.lblError.setVisible(True)
            self.lblError.setText('اردویی با این کد یافت نشد')
            return False
        if not self.justForReport:
            if self.tour.status == TourStatus.NotConfirmed:
                self.lblError.setVisible(True)
                self.lblError.setText('هماهنگی سرویس ها برای اردو صرفا پس از تایید اردو توسط مدیر فنی امکان پذیر است')
                return False
            if self.tour.status in [TourStatus.Ended, TourStatus.Canceled]:
                self.lblError.setVisible(True)
                self.lblError.setText('امکان هماهنگی سرویس برای اردوهای برگزارشده یا حذف شده وجود ندارد')
                return False
            if len(self.tour.cars) > 0:
                self.lblError.setVisible(True)
                self.lblError.setText('سرویس های این اردو قبلا انتخاب شده است')
                return False
        return True

    def OnSearchClicked(self) -> None:
        self.tblCars.setRowCount(0)
        if not self.ValidateInputs():
            return
        if self.justForReport:
            self.tour = Tour.SearchTourById(self.tourId)
            if not self.tour:
                self.lblError.setVisible(True)
                self.lblError.setText('اردویی با این کد وجود ندارد')
                return
            if len(self.tour.cars) == 0:
                self.lblError.setVisible(True)
                self.lblError.setText('در حال حاضر هیچ سرویسی برای این اردو ثبت نشده است')
                return
            for car in Tour.GetTourCars(self.tour):
                rowCount = self.tblCars.rowCount()
                self.tblCars.setRowCount(rowCount + 1)
                self.tblCars.setItem(rowCount, 0, QTableWidgetItem(str(car.id)))
                self.tblCars.setItem(rowCount, 1, QTableWidgetItem(car.type))
                self.tblCars.setItem(rowCount, 2, QTableWidgetItem(str(car.capacity)))
                self.tblCars.setItem(rowCount, 3, QTableWidgetItem(str(car.tag).replace('-', ' ایران ')))
                self.tblCars.setItem(rowCount, 4, QTableWidgetItem(car.driverName))
                self.tblCars.setItem(rowCount, 5, QTableWidgetItem(car.driverId))
                self.tblCars.setItem(rowCount, 6, QTableWidgetItem(car.driverPhone))
        else:
            cars = Tour.ShowAccessibleCarsForTour(self.tour)
            self.cars = dict()
            self.selectedCars = list()
            if not cars:
                self.lblError.setVisible(True)
                self.lblError.setText('در حال حاضر هیچ سرویس آزادی در این تاریخ وجود ندارد')
                return
            for car in cars:
                rowCount = self.tblCars.rowCount()
                self.tblCars.setRowCount(rowCount + 1)
                self.tblCars.setItem(rowCount, 0, QTableWidgetItem(str(car.id)))
                self.tblCars.setItem(rowCount, 1, QTableWidgetItem(car.type))
                self.tblCars.setItem(rowCount, 2, QTableWidgetItem(str(car.capacity)))
                self.tblCars.setItem(rowCount, 3, QTableWidgetItem(str(car.tag).replace('-', ' ایران ')))
                self.tblCars.setItem(rowCount, 4, QTableWidgetItem(car.driverName))
                self.tblCars.setItem(rowCount, 5, QTableWidgetItem(car.driverId))
                self.tblCars.setItem(rowCount, 6, QTableWidgetItem(car.driverPhone))
                self.cars[rowCount] = car

    def OnSelectionChanged(self) -> None:
        self.selectedCars = list()
        rows = self.tblCars.selectionModel().selectedRows()
        for row in rows:
            self.selectedCars.append(self.cars[row.row()])

    def OnSelectClicked(self) -> None:
        if not self.ValidateInputs():
            return
        if len(self.selectedCars) == 0:
            self.lblError.setVisible(True)
            self.lblError.setText('هیچ سرویسی انتخاب نشده است')
            return
        if sum(car.capacity for car in self.selectedCars) < self.tour.capacity:
            self.lblError.setVisible(True)
            self.lblError.setText('مجموع ظرفیت سرویس های انتخاب شده از ظرفیت اردو کمتر است')
            return
        if YesNoDialog('آیا از ثبت سرویس برای این اردو مطمئن هستید؟', 'ثبت سرویس', self).exec() == QDialog.Rejected:
            return
        res = Tour.AssignCarsToTour(self.tour, self.selectedCars)
        if not res:
            self.lblError.setVisible(True)
            self.lblError.setText('مشکلی در ثبت سرویس ها به وجود آمده است')
            return
        self.accept()
