from typing import Union, List
import jdatetime
from PyQt5.QtWidgets import QDialog, QPushButton
from UI.Ui_DatePicker import Ui_DatePicker


class DatePicker(Ui_DatePicker, QDialog):
    def __init__(self, parent=None) -> None:
        super(Ui_DatePicker, self).__init__()
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.btn = [[self.findChildren(QPushButton, f'btn{i}{j}')[0] for j in range(7)] for i in range(6)]
        self.selected_day = 0
        self.selected_btn = None
        self.SelectToday()

        # Signals and Slots
        self.btnCancel.clicked.connect(self.OnCancelClicked)
        self.btnToday.clicked.connect(self.SelectToday)
        for i in range(len(self.btn)):
            for j in range(len(self.btn[0])):
                self.btn[i][j].clicked.connect(lambda checked, i=i, j=j: self.OnButtonClicked(i, j, checked))
        self.btnOk.clicked.connect(self.OnOkClicked)
        self.spnYear.valueChanged.connect(
            lambda value: self.SetGridButtons(value, self.cmbMonth.currentIndex() + 1, self.selected_day))
        self.cmbMonth.currentIndexChanged.connect(
            lambda index: self.SetGridButtons(self.spnYear.value(), index + 1, self.selected_day))
        self.btnNextMonth.clicked.connect(lambda: self.StepMonth(1))
        self.btnPrevMonth.clicked.connect(lambda: self.StepMonth(-1))

    def SetGridButtons(self, year: int, month: int, day: int) -> None:
        date = jdatetime.date(year, month, 1)
        for i in range(len(self.btn)):
            for j in range(len(self.btn[0])):
                self.btn[i][j].show()
                self.btn[i][j].setText('')
                self.btn[i][j].setChecked(False)

        for j in range(date.isoweekday() - 1):
            self.btn[0][j].hide()

        i = 0
        j = date.isoweekday() - 1
        self.selected_day = day
        day = date.day
        maxDay = self.GetMaxDayOfMonth(date)
        if self.selected_day > maxDay:
            self.selected_day = maxDay

        while True:
            self.btn[i][j].setText(str(day))
            if self.selected_day != 0 and self.selected_day == day:
                if self.selected_btn is not None:
                    self.selected_btn.setChecked(False)
                self.btn[i][j].setChecked(True)
                self.selected_btn = self.btn[i][j]
            day += 1
            j += 1
            if j == len(self.btn[i]):
                j = 0
                i += 1
            if day > maxDay:
                break

        while True:
            self.btn[i][j].hide()
            j += 1
            if j == len(self.btn[i]):
                j = 0
                i += 1
                if i == len(self.btn):
                    break

    @staticmethod
    def GetMaxDayOfMonth(date: jdatetime.date) -> int:
        d = date
        while True:
            tomorrow = d + jdatetime.timedelta(days=1)
            if tomorrow.month != d.month:
                break
            d = tomorrow
        return d.day

    def SelectToday(self) -> None:
        today = jdatetime.date.today()
        self.spnYear.setValue(today.year)
        self.cmbMonth.setCurrentIndex(today.month - 1)
        self.SetGridButtons(today.year, today.month, today.day)

    def OnCancelClicked(self) -> None:
        self.reject()

    def OnButtonClicked(self, i: int, j: int, checked: bool) -> None:
        if checked:
            self.selected_btn.setChecked(False)
            self.selected_btn = self.btn[i][j]
            self.selected_day = int(self.selected_btn.text())
        else:
            self.selected_btn.setChecked(True)

    def OnOkClicked(self) -> None:
        if self.selected_day != 0:
            self.accept()

    def StepMonth(self, step: int) -> None:
        index = (self.cmbMonth.currentIndex() + step)
        self.cmbMonth.setCurrentIndex(index % self.cmbMonth.count())
        self.spnYear.setValue(self.spnYear.value() + (index // self.cmbMonth.count()))

    def exec(self) -> List[Union[int, jdatetime.date]]:
        res = super(DatePicker, self).exec()
        if res == QDialog.Accepted:
            return [res, jdatetime.date(int(self.spnYear.value()), self.cmbMonth.currentIndex() + 1, self.selected_day)]
        else:
            return [res, None]
