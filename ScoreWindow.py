# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScoreWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScoreWindow(object):
    def setupUi(self, ScoreWindow):
        ScoreWindow.setObjectName("ScoreWindow")
        ScoreWindow.resize(440, 339)
        self.centralwidget = QtWidgets.QWidget(ScoreWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.teamscore = QtWidgets.QLabel(self.centralwidget)
        self.teamscore.setGeometry(QtCore.QRect(160, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teamscore.setFont(font)
        self.teamscore.setObjectName("teamscore")
        self.Score = QtWidgets.QLineEdit(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(160, 140, 113, 20))
        self.Score.setObjectName("Score")
        ScoreWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ScoreWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        ScoreWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ScoreWindow)
        self.statusbar.setObjectName("statusbar")
        ScoreWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ScoreWindow)
        QtCore.QMetaObject.connectSlotsByName(ScoreWindow)

    def retranslateUi(self, ScoreWindow):
        _translate = QtCore.QCoreApplication.translate
        ScoreWindow.setWindowTitle(_translate("ScoreWindow", "MainWindow"))
        self.teamscore.setText(_translate("ScoreWindow", "Your Team Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScoreWindow = QtWidgets.QMainWindow()
    ui = Ui_ScoreWindow()
    ui.setupUi(ScoreWindow)
    ScoreWindow.show()
    sys.exit(app.exec_())
