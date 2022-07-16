from DatePicker import DatePicker
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLineEdit, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.btn = QPushButton('Click')
        self.btn.clicked.connect(self.click)
        self.txt = QLineEdit()
        self.widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.txt)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def click(self):
        dlg = DatePicker(self)
        res, d = dlg.exec()
        if res == QDialog.Accepted:
            self.txt.setText(str(d))


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
