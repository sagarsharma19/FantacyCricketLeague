# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenWindow(object):
    def setupUi(self, OpenWindow):
        OpenWindow.setObjectName("OpenWindow")
        OpenWindow.resize(380, 296)
        self.centralwidget = QtWidgets.QWidget(OpenWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.OpenTeam = QtWidgets.QLabel(self.centralwidget)
        self.OpenTeam.setGeometry(QtCore.QRect(110, 60, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.OpenTeam.setFont(font)
        self.OpenTeam.setObjectName("OpenTeam")

        self.NameOfTeam = QtWidgets.QLineEdit(self.centralwidget)
        self.NameOfTeam.setGeometry(QtCore.QRect(110, 100, 131, 20))
        self.NameOfTeam.setText("")
        self.NameOfTeam.setObjectName("NameOfTeam")

        self.OpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenButton.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.OpenButton.setObjectName("OpenButton")

        OpenWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OpenWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        OpenWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OpenWindow)
        self.statusbar.setObjectName("statusbar")
        OpenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OpenWindow)
        QtCore.QMetaObject.connectSlotsByName(OpenWindow)

    def retranslateUi(self, OpenWindow):
        _translate = QtCore.QCoreApplication.translate
        OpenWindow.setWindowTitle(_translate("OpenWindow", "MainWindow"))
        self.OpenTeam.setText(_translate("OpenWindow", "Enter Team Name To Open"))
        self.OpenButton.setText(_translate("OpenWindow", "open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenWindow = QtWidgets.QMainWindow()
    ui = Ui_OpenWindow()
    ui.setupUi(OpenWindow)
    OpenWindow.show()
    sys.exit(app.exec_())
