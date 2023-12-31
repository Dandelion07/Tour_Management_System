# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchCarsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchCarsDialog(object):
    def setupUi(self, SearchCarsDialog):
        SearchCarsDialog.setObjectName("SearchCarsDialog")
        SearchCarsDialog.resize(723, 547)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        SearchCarsDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icons/searchService.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchCarsDialog.setWindowIcon(icon)
        SearchCarsDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        SearchCarsDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchCarsDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FLayoutSearchFields = QtWidgets.QFormLayout()
        self.FLayoutSearchFields.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.FLayoutSearchFields.setObjectName("FLayoutSearchFields")
        self.lblType = QtWidgets.QLabel(SearchCarsDialog)
        self.lblType.setObjectName("lblType")
        self.FLayoutSearchFields.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblType)
        self.lblTag = QtWidgets.QLabel(SearchCarsDialog)
        self.lblTag.setObjectName("lblTag")
        self.FLayoutSearchFields.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTag)
        self.lblDriverName = QtWidgets.QLabel(SearchCarsDialog)
        self.lblDriverName.setObjectName("lblDriverName")
        self.FLayoutSearchFields.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDriverName)
        self.lblDriverId = QtWidgets.QLabel(SearchCarsDialog)
        self.lblDriverId.setObjectName("lblDriverId")
        self.FLayoutSearchFields.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblDriverId)
        self.lblDriverPhone = QtWidgets.QLabel(SearchCarsDialog)
        self.lblDriverPhone.setObjectName("lblDriverPhone")
        self.FLayoutSearchFields.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblDriverPhone)
        self.lblCapacity_2 = QtWidgets.QLabel(SearchCarsDialog)
        self.lblCapacity_2.setObjectName("lblCapacity_2")
        self.FLayoutSearchFields.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCapacity_2)
        self.txtDriverName = QtWidgets.QLineEdit(SearchCarsDialog)
        self.txtDriverName.setEnabled(False)
        self.txtDriverName.setObjectName("txtDriverName")
        self.FLayoutSearchFields.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtDriverName)
        self.txtDriverId = QtWidgets.QLineEdit(SearchCarsDialog)
        self.txtDriverId.setEnabled(False)
        self.txtDriverId.setObjectName("txtDriverId")
        self.FLayoutSearchFields.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtDriverId)
        self.txtDriverPhone = QtWidgets.QLineEdit(SearchCarsDialog)
        self.txtDriverPhone.setEnabled(False)
        self.txtDriverPhone.setObjectName("txtDriverPhone")
        self.FLayoutSearchFields.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtDriverPhone)
        self.txtType = QtWidgets.QLineEdit(SearchCarsDialog)
        self.txtType.setEnabled(False)
        self.txtType.setObjectName("txtType")
        self.FLayoutSearchFields.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtType)
        self.spnCapacity = QtWidgets.QSpinBox(SearchCarsDialog)
        self.spnCapacity.setMinimum(1)
        self.spnCapacity.setObjectName("spnCapacity")
        self.FLayoutSearchFields.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spnCapacity)
        self.HLayoutTag = QtWidgets.QHBoxLayout()
        self.HLayoutTag.setSpacing(5)
        self.HLayoutTag.setObjectName("HLayoutTag")
        self.spnTagCity = QtWidgets.QSpinBox(SearchCarsDialog)
        self.spnTagCity.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spnTagCity.setMinimum(10)
        self.spnTagCity.setObjectName("spnTagCity")
        self.HLayoutTag.addWidget(self.spnTagCity)
        self.lblIran = QtWidgets.QLabel(SearchCarsDialog)
        self.lblIran.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIran.setObjectName("lblIran")
        self.HLayoutTag.addWidget(self.lblIran)
        self.spnTagNum2 = QtWidgets.QSpinBox(SearchCarsDialog)
        self.spnTagNum2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spnTagNum2.setMinimum(100)
        self.spnTagNum2.setMaximum(999)
        self.spnTagNum2.setObjectName("spnTagNum2")
        self.HLayoutTag.addWidget(self.spnTagNum2)
        self.cmbTagLetter = QtWidgets.QComboBox(SearchCarsDialog)
        self.cmbTagLetter.setEditable(True)
        self.cmbTagLetter.setObjectName("cmbTagLetter")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.cmbTagLetter.addItem("")
        self.HLayoutTag.addWidget(self.cmbTagLetter)
        self.spnTagNum1 = QtWidgets.QSpinBox(SearchCarsDialog)
        self.spnTagNum1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spnTagNum1.setMinimum(10)
        self.spnTagNum1.setProperty("value", 10)
        self.spnTagNum1.setObjectName("spnTagNum1")
        self.HLayoutTag.addWidget(self.spnTagNum1)
        self.FLayoutSearchFields.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.HLayoutTag)
        self.verticalLayout.addLayout(self.FLayoutSearchFields)
        self.btnSearch = QtWidgets.QPushButton(SearchCarsDialog)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QtCore.QSize(40, 40))
        self.btnSearch.setObjectName("btnSearch")
        self.verticalLayout.addWidget(self.btnSearch)
        self.tblCars = QtWidgets.QTableWidget(SearchCarsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblCars.sizePolicy().hasHeightForWidth())
        self.tblCars.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.tblCars.setFont(font)
        self.tblCars.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tblCars.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tblCars.setAlternatingRowColors(True)
        self.tblCars.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tblCars.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCars.setObjectName("tblCars")
        self.tblCars.setColumnCount(7)
        self.tblCars.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCars.setHorizontalHeaderItem(6, item)
        self.tblCars.horizontalHeader().setVisible(True)
        self.tblCars.horizontalHeader().setCascadingSectionResizes(True)
        self.tblCars.horizontalHeader().setMinimumSectionSize(50)
        self.tblCars.horizontalHeader().setSortIndicatorShown(False)
        self.tblCars.horizontalHeader().setStretchLastSection(True)
        self.tblCars.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblCars)
        self.lblError = QtWidgets.QLabel(SearchCarsDialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblError.setPalette(palette)
        self.lblError.setObjectName("lblError")
        self.verticalLayout.addWidget(self.lblError)
        self.HLayoutButtons = QtWidgets.QHBoxLayout()
        self.HLayoutButtons.setObjectName("HLayoutButtons")
        self.btnSelect = QtWidgets.QPushButton(SearchCarsDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/icons/addService.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelect.setIcon(icon1)
        self.btnSelect.setIconSize(QtCore.QSize(40, 40))
        self.btnSelect.setObjectName("btnSelect")
        self.HLayoutButtons.addWidget(self.btnSelect)
        self.btnReturn = QtWidgets.QPushButton(SearchCarsDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/icons/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReturn.setIcon(icon2)
        self.btnReturn.setIconSize(QtCore.QSize(40, 40))
        self.btnReturn.setObjectName("btnReturn")
        self.HLayoutButtons.addWidget(self.btnReturn)
        self.verticalLayout.addLayout(self.HLayoutButtons)

        self.retranslateUi(SearchCarsDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchCarsDialog)

    def retranslateUi(self, SearchCarsDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchCarsDialog.setWindowTitle(_translate("SearchCarsDialog", "جست‌وجوی سرویس‌ها"))
        self.lblType.setText(_translate("SearchCarsDialog", "نوع ماشین"))
        self.lblTag.setText(_translate("SearchCarsDialog", "پلاک"))
        self.lblDriverName.setText(_translate("SearchCarsDialog", "نام راننده"))
        self.lblDriverId.setText(_translate("SearchCarsDialog", "کد ملی راننده"))
        self.lblDriverPhone.setText(_translate("SearchCarsDialog", "موبایل راننده"))
        self.lblCapacity_2.setText(_translate("SearchCarsDialog", "ظرفیت"))
        self.lblIran.setText(_translate("SearchCarsDialog", "ایران"))
        self.cmbTagLetter.setItemText(0, _translate("SearchCarsDialog", "ب"))
        self.cmbTagLetter.setItemText(1, _translate("SearchCarsDialog", "ج"))
        self.cmbTagLetter.setItemText(2, _translate("SearchCarsDialog", "چ"))
        self.cmbTagLetter.setItemText(3, _translate("SearchCarsDialog", "د"))
        self.cmbTagLetter.setItemText(4, _translate("SearchCarsDialog", "ذ"))
        self.cmbTagLetter.setItemText(5, _translate("SearchCarsDialog", "ر"))
        self.cmbTagLetter.setItemText(6, _translate("SearchCarsDialog", "ز"))
        self.cmbTagLetter.setItemText(7, _translate("SearchCarsDialog", "س"))
        self.cmbTagLetter.setItemText(8, _translate("SearchCarsDialog", "ش"))
        self.cmbTagLetter.setItemText(9, _translate("SearchCarsDialog", "ص"))
        self.cmbTagLetter.setItemText(10, _translate("SearchCarsDialog", "ط"))
        self.cmbTagLetter.setItemText(11, _translate("SearchCarsDialog", "ع"))
        self.cmbTagLetter.setItemText(12, _translate("SearchCarsDialog", "ف"))
        self.cmbTagLetter.setItemText(13, _translate("SearchCarsDialog", "ق"))
        self.cmbTagLetter.setItemText(14, _translate("SearchCarsDialog", "ک"))
        self.cmbTagLetter.setItemText(15, _translate("SearchCarsDialog", "ل"))
        self.cmbTagLetter.setItemText(16, _translate("SearchCarsDialog", "م"))
        self.cmbTagLetter.setItemText(17, _translate("SearchCarsDialog", "ن"))
        self.cmbTagLetter.setItemText(18, _translate("SearchCarsDialog", "و"))
        self.cmbTagLetter.setItemText(19, _translate("SearchCarsDialog", "ه"))
        self.cmbTagLetter.setItemText(20, _translate("SearchCarsDialog", "ی"))
        self.btnSearch.setText(_translate("SearchCarsDialog", "جست‌وجوی سرویس‌ها"))
        item = self.tblCars.horizontalHeaderItem(0)
        item.setText(_translate("SearchCarsDialog", "کد سرویس"))
        item = self.tblCars.horizontalHeaderItem(1)
        item.setText(_translate("SearchCarsDialog", "نوع ماشین"))
        item = self.tblCars.horizontalHeaderItem(2)
        item.setText(_translate("SearchCarsDialog", "ظرفیت"))
        item = self.tblCars.horizontalHeaderItem(3)
        item.setText(_translate("SearchCarsDialog", "پلاک"))
        item = self.tblCars.horizontalHeaderItem(4)
        item.setText(_translate("SearchCarsDialog", "نام راننده"))
        item = self.tblCars.horizontalHeaderItem(5)
        item.setText(_translate("SearchCarsDialog", "کد ملی راننده"))
        item = self.tblCars.horizontalHeaderItem(6)
        item.setText(_translate("SearchCarsDialog", "موبایل راننده"))
        self.lblError.setText(_translate("SearchCarsDialog", "خطا"))
        self.btnSelect.setText(_translate("SearchCarsDialog", "انتخاب سرویس‌ها"))
        self.btnReturn.setText(_translate("SearchCarsDialog", "بازگشت"))
        self.btnReturn.setShortcut(_translate("SearchCarsDialog", "Ctrl+S"))
import resource_rc
