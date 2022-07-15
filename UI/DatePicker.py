from UI.Ui_DatePicker import Ui_DatePicker
from PyQt5.QtWidgets import QDialog

class DatePicker(Ui_DatePicker, QDialog):
    def __init__(self, parent):
        super().__init__(parent)
