# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 861)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.program_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.program_name_label.setGeometry(QtCore.QRect(450, 10, 211, 71))
        self.program_name_label.setObjectName("program_name_label")
        self.label_table = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_table.setGeometry(QtCore.QRect(590, 130, 461, 91))
        self.label_table.setObjectName("label_table")
        self.data = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.data.setGeometry(QtCore.QRect(660, 240, 301, 271))
        self.data.setObjectName("data")
        self.data.setColumnCount(2)
        self.data.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(1, item)
        self.Image = QtWidgets.QLabel(parent=self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(130, 180, 441, 461))
        self.Image.setObjectName("Image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.program_name_label.setText(_translate("MainWindow", "название программы "))
        self.label_table.setText(_translate("MainWindow", "обнаруженные деффекты "))
        item = self.data.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.data.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.data.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.data.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.data.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.data.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "название деф."))
        item = self.data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "количество "))
        self.Image.setText(_translate("MainWindow", "TextLabel"))
