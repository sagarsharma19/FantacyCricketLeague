# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practiceForBigProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
example=sqlite3.connect("FantacyCricket.db")
curs=example.cursor()


from NewWindow import Ui_Form
from EvaluateWindow import Ui_EvaluateWindow
from OpenWindow import Ui_OpenWindow


class Ui_MainWindow(object):
    def __init__(self):
        self.newDialog=QtWidgets.QMainWindow()
        self.new_t=Ui_Form()
        self.new_t.setupUi(self.newDialog)

        self.evalDialog=QtWidgets.QMainWindow()
        self.eval_t=Ui_EvaluateWindow()
        self.eval_t.setupUi(self.evalDialog)

        self.openDialog=QtWidgets.QMainWindow()
        self.open_t=Ui_OpenWindow()
        self.open_t.setupUi(self.openDialog)

    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 150, 501, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.batsmancount=0
        self.bowlercount=0
        self.wicketkeepercount=0
        self.allroundercount=0


        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        spacerItem = QtWidgets.QSpacerItem(120, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 20, 611, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.batsman = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.batsman.setObjectName("batsman")
        self.horizontalLayout_2.addWidget(self.batsman)
        self.batsman_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.batsman_count.setGeometry(QtCore.QRect(250, 90, 47, 13))
        self.batsman_count.setObjectName("batsman_count")
        self.horizontalLayout_2.addWidget(self.batsman_count)
        self.bowler = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.bowler.setObjectName("bowler")
        self.horizontalLayout_2.addWidget(self.bowler)
        self.bowler_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.bowler_count.setGeometry(QtCore.QRect(250, 90, 47, 13))
        self.bowler_count.setObjectName("bowler_count")
        self.horizontalLayout_2.addWidget(self.bowler_count)
        self.wicketkeeper = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.wicketkeeper.setObjectName("wicketkeeper")
        self.horizontalLayout_2.addWidget(self.wicketkeeper)
        self.wicketkeeper_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.wicketkeeper_count.setGeometry(QtCore.QRect(250, 90, 47, 13))
        self.wicketkeeper_count.setObjectName("wicketkeeper_count")
        self.horizontalLayout_2.addWidget(self.wicketkeeper_count)
        self.allrounder = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.allrounder.setObjectName("allrounder")
        self.horizontalLayout_2.addWidget(self.allrounder)
        self.allrounder_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.allrounder_count.setGeometry(QtCore.QRect(250, 90, 47, 13))
        self.allrounder_count.setObjectName("allrounder_count")
        self.horizontalLayout_2.addWidget(self.allrounder_count)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 470, 501, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.available_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.available_label.setObjectName("available_label")
        self.horizontalLayout_3.addWidget(self.available_label)
        self.available_number = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.available_number.setObjectName("available_number")
        self.horizontalLayout_3.addWidget(self.available_number)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.selected_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.selected_label.setObjectName("selected_label")
        self.horizontalLayout_3.addWidget(self.selected_label)
        self.selected_number = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.selected_number.setObjectName("selected_number")
        self.horizontalLayout_3.addWidget(self.selected_number)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(430, 100, 211, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")


        self.name_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_4.addWidget(self.name_label)
        self.teamname = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_4.addWidget(self.teamname)
        MainWindow.setCentralWidget(self.centralwidget)

        self.availablepointslabel = QtWidgets.QLabel(self.centralwidget)
        self.availablepointslabel.setGeometry(QtCore.QRect(150, 90, 81, 16))
        self.availablepointslabel.setObjectName("availablepointslabel")
        self.pointsusedlabel = QtWidgets.QLabel(self.centralwidget)
        self.pointsusedlabel.setGeometry(QtCore.QRect(150, 120, 61, 16))
        self.pointsusedlabel.setObjectName("pointsusedlabel")
        self.availablepoints = QtWidgets.QLabel(self.centralwidget)
        self.availablepoints.setGeometry(QtCore.QRect(250, 90, 47, 13))
        self.availablepoints.setObjectName("availablepoints")
        self.pointsused = QtWidgets.QLabel(self.centralwidget)
        self.pointsused.setGeometry(QtCore.QRect(250, 120, 47, 13))
        self.pointsused.setObjectName("pointsused")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Save_Team = QtWidgets.QAction(MainWindow)
        self.Save_Team.setObjectName("Save_Team")
        self.Save_Team.triggered.connect(self.saving)

        self.New_Team = QtWidgets.QAction(MainWindow)
        self.New_Team.setObjectName("New_Team")
        self.New_Team.triggered.connect(self.new_team)

        self.Evaluate_Team = QtWidgets.QAction(MainWindow)
        self.Evaluate_Team.setObjectName("Evaluate_Team")
        self.Evaluate_Team.triggered.connect(self.evaluating)

        self.Open_Team=QtWidgets.QAction(MainWindow)
        self.Open_Team.setObjectName("Open_Team")
        self.Open_Team.triggered.connect(self.open_team)


        self.menuManage_Teams.addAction(self.Save_Team)
        self.menuManage_Teams.addAction(self.New_Team)
        self.menuManage_Teams.addAction(self.Evaluate_Team)
        self.menuManage_Teams.addAction(self.Open_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        ##radio buttons clicked
        self.batsman.clicked.connect(self.checkRadioButton)
        self.bowler.clicked.connect(self.checkRadioButton)
        self.wicketkeeper.clicked.connect(self.checkRadioButton)
        self.allrounder.clicked.connect(self.checkRadioButton)

        ##items in list widget double clicked
        self.listWidget.itemDoubleClicked.connect(self.removelistWidget)
        self.listWidget_2.itemDoubleClicked.connect(self.removelistWidget_2)

        self.currentteam=[]
        self.availableplayers=[]
        self.player_and_ctg=[]
        self.teamlist=[]

        curs.execute('''SELECT Team from team; ''')
        teams=curs.fetchall()
        for i in set(teams):
            self.teamlist.append(i[0])
        
        curs.execute('''SELECT player,ctg from stats ;''')
        p_and_c=curs.fetchall()
        for i in p_and_c:
            self.player_and_ctg.append(i)
            
        curs.execute('''SELECT player from stats ;''')
        self.available=curs.fetchall()
        for i in self.available:
            self.availableplayers.append(i[0])

        self.new_t.pushButton.clicked.connect(self.newteam)
        self.open_t.OpenButton.clicked.connect(self.openteam)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.batsman.setText(_translate("MainWindow", "batsman"))
        self.bowler.setText(_translate("MainWindow", "bowler"))
        self.wicketkeeper.setText(_translate("MainWindow", "wicketkeeper"))
        self.allrounder.setText(_translate("MainWindow", "allrounder"))
        self.available_label.setText(_translate("MainWindow", "availavle players"))
        self.selected_label.setText(_translate("MainWindow", "selected players"))
        self.name_label.setText(_translate("MainWindow", "Team Name"))

        self.availablepointslabel.setText(_translate("MainWindow", "Available Points:"))
        self.pointsusedlabel.setText(_translate("MainWindow", "Points Used:"))
        self.availablepoints.setText(_translate("MainWindow", "1000"))
        self.pointsused.setText(_translate("MainWindow", "0"))
        
        
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.Save_Team.setText(_translate("MainWindow", "Save Team"))
        self.New_Team.setText(_translate("MainWindow", "New Team"))
        self.Evaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.Open_Team.setText(_translate("MainWindow", "Open Team"))
        
    def new_team(self):
        self.newDialog.show()

    def newteam(self):
        self.availablepoints.setText("1000")
        self.pointsused.setText("0")
        self.T=self.new_t.lineEdit.text()
        self.listWidget_2.clear()
        self.listWidget.clear()
        self.currentteam=[]
        self.availableplayers=[]
        curs.execute('''SELECT player from stats ;''')
        self.available=curs.fetchall()
        for i in self.available:
            self.availableplayers.append(i[0])

        if(self.T in self.teamlist):
            error_dialog=QtWidgets.QErrorMessage()
            error_dialog.showMessage('Team name already exists')
            error_dialog.exec_()
                
        else:
            self.teamname.setText(self.T)
            self.newDialog.close()

    def open_team(self):
        self.openDialog.show()
        
    def openteam(self):
        self.listWidget.clear()
        self.teamname.clear()
        self.batsman_count.clear()
        self.bowler_count.clear()
        self.wicketkeeper_count.clear()
        self.allrounder_count.clear()

        self.currentteam=[]
        self.availableplayers=[]
        curs.execute('''SELECT player from stats ;''')
        self.available=curs.fetchall()
        for i in self.available:
            self.availableplayers.append(i[0])
            
        opening_team=self.open_t.NameOfTeam.text()
        if(opening_team not in self.teamlist):
            error_dialog=QtWidgets.QErrorMessage()
            error_dialog.showMessage('Team Does not exist!')
            error_dialog.exec_()
        else:
            
            curs.execute('''SELECT player from team WHERE Team=('%s')'''%(opening_team))
            t=curs.fetchall()
            
            for i in t:
                self.listWidget.addItem(i[0])
            
            self.teamname.setText(opening_team)
                    
        for i in range(self.listWidget.count()):
            self.currentteam.append(self.listWidget.item(i).text())
            self.availableplayers.remove(self.listWidget.item(i).text())

        self.selected_number.setText(str(len(self.currentteam)))
        self.available_number.setText(str(len(self.availableplayers)))
        self.openDialog.close()
    
   
        
    def evaluating(self):
        example.commit()
        self.evalDialog.show()
        for name in self.teamlist:
            self.eval_t.SelectTeam.addItem(name)
  
    def saving(self):
        if(len(self.currentteam)==11 and len(self.teamname.text())>0):
            if(int(self.availablepoints.text())>=0):
                if(self.teamname.text() not in self.teamlist):
                    for i in self.currentteam:
                        curs.execute("INSERT INTO team('Team','player')VALUES('%s','%s')" %(self.teamname.text(),i))
                            
                        example.commit()
                    
                    self.teamlist.append(self.teamname.text())
                    print(self.teamlist)
                else:
                    error_dialog=QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Team name already exists')
                    error_dialog.exec_()
                    
            else:
                error_dialog=QtWidgets.QErrorMessage()
                error_dialog.showMessage('You are exceeding the Available points limit!')
                error_dialog.exec_()
                
        else:
            error_dialog=QtWidgets.QErrorMessage()
            error_dialog.showMessage('team should have 11 players only or the Team Name is missing')
            error_dialog.exec_()
        
    def removelistWidget(self,item):
        a_p=int(self.availablepoints.text())
        p_u=int(self.pointsused.text())
        self.listWidget.takeItem(self.listWidget.row(item))
        self.listWidget_2.addItem(item.text())
        self.currentteam.remove(item.text())
        self.availableplayers.append(item.text())
        self.available_number.setText(str(len(self.availableplayers)))
        self.selected_number.setText(str(len(self.currentteam)))
        for i in self.player_and_ctg:
            if(i[0]==item.text() and i[1]=="BAT"):
                self.batsmancount-=1
                
            if(i[0]==item.text() and i[1]=="BWL"):
                self.bowlercount-=1
                
            if(i[0]==item.text() and i[1]=="AR"):
                self.allroundercount-=1
            
            if(i[0]==item.text() and i[1]=="WK"):
                self.wicketkeepercount-=1
                

        self.batsman_count.setText(str(self.batsmancount))
        self.bowler_count.setText(str(self.bowlercount))
        self.wicketkeeper_count.setText(str(self.allroundercount))
        self.allrounder_count.setText(str(self.wicketkeepercount))

        curs.execute("SELECT value from match WHERE player=('%s')"%(item.text()))
        val=curs.fetchone()
        a_p=a_p+val[0]
        p_u=p_u-val[0]
        self.availablepoints.setText(str(a_p))
        self.pointsused.setText(str(p_u))
        
        #print(self.availableplayers)
    def removelistWidget_2(self,item):
        a_p=int(self.availablepoints.text())
        p_u=int(self.pointsused.text())
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.addItem(item.text())
        self.error(item) 
        
        self.currentteam.append(item.text())
        self.availableplayers.remove(item.text())
        self.available_number.setText(str(len(self.availableplayers)))
        self.selected_number.setText(str(len(self.currentteam)))
        for i in self.player_and_ctg:
            if(i[0]==item.text() and i[1]=="BAT"):
                self.batsmancount+=1
                self.error(item)            
            if(i[0]==item.text() and i[1]=="BWL"):
                self.bowlercount+=1
                self.error(item)        
            if(i[0]==item.text() and i[1]=="AR"):
                self.allroundercount+=1
                self.error(item)
            if(i[0]==item.text() and i[1]=="WK"):
                self.wicketkeepercount+=1
                self.error(item)
        #### big note -----just see below allrounder and wicketkeeper count 
        #### are written mismatched but this only is giving correct output
        #### on output app dont change this and work accordingly.
        #####################################################################
        self.batsman_count.setText(str(self.batsmancount))
        self.bowler_count.setText(str(self.bowlercount))
        self.wicketkeeper_count.setText(str(self.allroundercount))
        self.allrounder_count.setText(str(self.wicketkeepercount))

        curs.execute("SELECT value from match WHERE player=('%s')"%(item.text()))
        val=curs.fetchone()
        a_p=a_p-val[0]
        p_u=p_u+val[0]
        if(a_p<0):
            error_dialog=QtWidgets.QErrorMessage()
            error_dialog.showMessage('oh no! not enough points undo the last pick othrtwise team would not be saved')
            error_dialog.exec_()
        
        self.availablepoints.setText(str(a_p))
        self.pointsused.setText(str(p_u))
            
        #print(self.availableplayers)

    def error(self,item):
        error_dialog=QtWidgets.QErrorMessage()
        
        if self.batsmancount>=0 and self.batsmancount<6:
            pass
            
        else:
            error_dialog.showMessage('Oh no! Only 5 batsman are allowed')
            error_dialog.exec_()
            
            

        if self.allroundercount>=0 and self.allroundercount<2:
            pass
            
        else:
            error_dialog.showMessage('Oh no! Only 1 keeper are allowed')
            error_dialog.exec_()
            
            

        if self.bowlercount>=0 and self.bowlercount<5:
            pass
            
        else:
            error_dialog.showMessage('Oh no! Only 5 bowlers are allowed')
            error_dialog.exec_()
                       

        if self.listWidget.count()<12:
            pass
            
        else:
            error_dialog.showMessage('Oh no! No more than 11 Players are allowed')
            error_dialog.exec_()
            
        
            

    def checkRadioButton(self):
        sql_1='''SELECT player from stats WHERE ctg="BAT" ;'''
        sql_2='''SELECT player from stats WHERE ctg="BWL" ;'''
        sql_3='''SELECT player from stats WHERE ctg="WK" ;'''
        sql_4='''SELECT player from stats WHERE ctg="AR"; '''

        if self.batsman.isChecked()==True :
            self.listWidget_2.clear()    
            curs.execute(sql_1)
            allbatsmans=curs.fetchall()
            for i in allbatsmans:
                if(i[0] in self.availableplayers):
                    self.listWidget_2.addItem(i[0])
            

        if self.bowler.isChecked()==True :
            self.listWidget_2.clear()
            curs.execute(sql_2)
            allbowlers=curs.fetchall()
            for i in allbowlers:
                if(i[0] in self.availableplayers):
                    self.listWidget_2.addItem(i[0])
            

        if self.allrounder.isChecked()==True :
            self.listWidget_2.clear()
            curs.execute(sql_3)
            allallrounders=curs.fetchall()
            for i in allallrounders:
                if(i[0] in self.availableplayers):
                    self.listWidget_2.addItem(i[0])
            

        if self.wicketkeeper.isChecked()==True :
            self.listWidget_2.clear()
            curs.execute(sql_4)
            allwicketkeepers=curs.fetchall()
            for i in allwicketkeepers:
                if(i[0] in self.availableplayers):
                    self.listWidget_2.addItem(i[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
