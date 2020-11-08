# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from ScoreWindow import Ui_ScoreWindow

import sqlite3
myteams=sqlite3.connect("FantacyCricket.db")
cur=myteams.cursor()
myteams.commit()

class Ui_EvaluateWindow(object):


    def __init__(self):
        self.scoreDialog=QtWidgets.QMainWindow()
        self.score_t=Ui_ScoreWindow()
        self.score_t.setupUi(self.scoreDialog)
        
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(699, 509)
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 140, 521, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.playerList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.playerList.setObjectName("playerList")
        self.horizontalLayout.addWidget(self.playerList)

        spacerItem = QtWidgets.QSpacerItem(120, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.ScoreList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.ScoreList.setObjectName("ScoreList")
        self.horizontalLayout.addWidget(self.ScoreList)

        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(300, 440, 75, 23))
        self.Calculate.setObjectName("Calculate")

        self.SelectTeam = QtWidgets.QComboBox(self.centralwidget)
        self.SelectTeam.setGeometry(QtCore.QRect(130, 40, 111, 22))
        self.SelectTeam.setObjectName("SelectTeam")
        self.SelectTeam.addItem("")

        self.SelectMatch = QtWidgets.QComboBox(self.centralwidget)
        self.SelectMatch.setGeometry(QtCore.QRect(410, 40, 121, 22))
        self.SelectMatch.setObjectName("SelectMatch")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 84, 531, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setObjectName("line")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 100, 561, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.players = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.players.setFont(font)
        self.players.setIndent(25)
        self.players.setObjectName("players")
        self.horizontalLayout_2.addWidget(self.players)

        self.points = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.points.setFont(font)
        self.points.setIndent(25)
        self.points.setObjectName("points")
        self.horizontalLayout_2.addWidget(self.points)

        EvaluateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EvaluateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 21))
        self.menubar.setObjectName("menubar")
        EvaluateWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EvaluateWindow)
        self.statusbar.setObjectName("statusbar")
        EvaluateWindow.setStatusBar(self.statusbar)

        #cur.execute("SELECT Team from team;")
        #teams=cur.fetchall()
        #teamlist=[]
        
        #for i in teams:
        #    teamlist.append(i[0])
    
        #for name in set(teamlist):
        #    self.SelectTeam.addItem(name)

        self.SelectTeam.currentTextChanged.connect(self.combox)
        self.Calculate.clicked.connect(self.score)
        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

    def combox(self):
        
        self.playerList.clear()
        self.ScoreList.clear()
        item=self.SelectTeam.currentText()
        sql='''SELECT player from team WHERE Team=('%s')'''%(item)    
        cur.execute(sql)
        self.current_players=cur.fetchall()
        for i in self.current_players:
            self.playerList.addItem(i[0])
            
        
    def score(self):
        points=[]
        self.ScoreList.clear()
        for i in range(self.playerList.count()):
            player=self.playerList.item(i).text()
            sq_1='''SELECT scored from match WHERE player=('%s')'''%(player)
            sq_2='''SELECT faced from match WHERE player=('%s') '''%(player)
            sq_3='''SELECT fours from match WHERE player=('%s') '''%(player)
            sq_4='''SELECT sixes from match WHERE player=('%s') '''%(player)
            sq_5='''SELECT catches from match WHERE player=('%s') '''%(player)
            sq_6='''SELECT stumping from match WHERE player=('%s') '''%(player)
            sq_7='''SELECT RO from match WHERE player=('%s') '''%(player)
            sq_8='''SELECT wkts from match WHERE player=('%s') '''%(player)
            sq_9='''SELECT bowled from match WHERE player=('%s') '''%(player)
            sq_10='''SELECT given from match WHERE player=('%s') '''%(player)
            point=0
            cur.execute(sq_1)
            runs=cur.fetchone()
            point+=runs[0]//2
            
            if(50<=runs[0]<100):
                point+=5
            elif(runs[0]>100):
                point+=10
            cur.execute(sq_2)
            balls=cur.fetchone()
            if(balls[0]!=0):
                if(80<=(runs[0]/balls[0])*100<=100):
                    point+=2
                elif((runs[0]/balls[0])*100>100):
                    point+=4
            cur.execute(sq_3)
            four=cur.fetchone()
            point+=four[0]
            
            cur.execute(sq_4)
            six=cur.fetchone()
            point+=(2*six[0])
            
            cur.execute(sq_5)
            catch=cur.fetchone()
            point+=(catch[0]*10)
            
            cur.execute(sq_6)
            stump=cur.fetchone()
            point+=(stump[0]*10)
            
            cur.execute(sq_7)
            runout=cur.fetchone()
            point+=(runout[0]*10)
            
            cur.execute(sq_8)
            wicket=cur.fetchone()
            point+=(wicket[0]*10)
        
            if(wicket[0]==3):
                point+=5
            
            if(wicket[0]>5):
                point+=10
            
            
            cur.execute(sq_9)
            ballsbowled=cur.fetchone()
            overs=ballsbowled[0]//6
            
            cur.execute(sq_10)
            runsgiven=cur.fetchone()
            
            if(overs!=0):
                if(runsgiven[0]/overs<=2):
                    point+=10
                elif(2<runsgiven[0]/overs<=3.5):
                    point+=7
                elif(3.5<runsgiven[0]/overs<=4.5):
                    point+=4
                
           
            points.append(point)
            
        self.TEAM_SCORE=0
        for i in points:
            self.ScoreList.addItem(str(i))
            self.TEAM_SCORE+=i
            
        self.scoreDialog.show()
        self.score_t.Score.setText(str(self.TEAM_SCORE))


    
            


    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "MainWindow"))
        self.Calculate.setText(_translate("EvaluateWindow", "Calculate"))
        self.SelectTeam.setItemText(0, _translate("EvaluateWindow", "--SELECT TEAM--"))
        self.SelectMatch.setItemText(0, _translate("EvaluateWindow", "--SELECT MATCH--"))
        self.SelectMatch.setItemText(1, _translate("EvaluateWindow", "MATCH 1"))
        self.SelectMatch.setItemText(2, _translate("EvaluateWindow", "MATCH 2"))
        self.SelectMatch.setItemText(3, _translate("EvaluateWindow", "MATCH 3"))
        self.SelectMatch.setItemText(4, _translate("EvaluateWindow", "MATCH 4"))
        self.players.setText(_translate("EvaluateWindow", "Players"))
        self.points.setText(_translate("EvaluateWindow", "Points"))

    
        

            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())
