# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tic-tac-toe.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

import random

import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.t10 = QtWidgets.QLineEdit(self.centralwidget)
        self.t10.setObjectName("t10")
        self.horizontalLayout.addWidget(self.t10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.t11 = QtWidgets.QLineEdit(self.centralwidget)
        self.t11.setObjectName("t11")
        self.horizontalLayout_2.addWidget(self.t11)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.verticalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.verticalLayout.addWidget(self.b2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t1.setFont(font)
        self.t1.setAlignment(QtCore.Qt.AlignCenter)
        self.t1.setObjectName("t1")
        self.gridLayout_2.addWidget(self.t1, 0, 0, 1, 1)
        self.t9 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t9.setFont(font)
        self.t9.setAlignment(QtCore.Qt.AlignCenter)
        self.t9.setObjectName("t9")
        self.gridLayout_2.addWidget(self.t9, 2, 2, 1, 1)
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t5.setFont(font)
        self.t5.setAlignment(QtCore.Qt.AlignCenter)
        self.t5.setObjectName("t5")
        self.gridLayout_2.addWidget(self.t5, 1, 1, 1, 1)
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t3.setFont(font)
        self.t3.setAlignment(QtCore.Qt.AlignCenter)
        self.t3.setObjectName("t3")
        self.gridLayout_2.addWidget(self.t3, 0, 2, 1, 1)
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t7.setFont(font)
        self.t7.setAlignment(QtCore.Qt.AlignCenter)
        self.t7.setObjectName("t7")
        self.gridLayout_2.addWidget(self.t7, 2, 0, 1, 1)
        self.t8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t8.setFont(font)
        self.t8.setAlignment(QtCore.Qt.AlignCenter)
        self.t8.setObjectName("t8")
        self.gridLayout_2.addWidget(self.t8, 2, 1, 1, 1)
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t4.setFont(font)
        self.t4.setAlignment(QtCore.Qt.AlignCenter)
        self.t4.setObjectName("t4")
        self.gridLayout_2.addWidget(self.t4, 1, 0, 1, 1)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t6.setFont(font)
        self.t6.setText("")
        self.t6.setAlignment(QtCore.Qt.AlignCenter)
        self.t6.setObjectName("t6")
        self.gridLayout_2.addWidget(self.t6, 1, 2, 1, 1)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.t2.setFont(font)
        self.t2.setAlignment(QtCore.Qt.AlignCenter)
        self.t2.setObjectName("t2")
        self.gridLayout_2.addWidget(self.t2, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.t12 = QtWidgets.QLineEdit(self.centralwidget)
        self.t12.setObjectName("t12")
        self.horizontalLayout_3.addWidget(self.t12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.t13 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t13.setFont(font)
        self.t13.setText("")
        self.t13.setAlignment(QtCore.Qt.AlignCenter)
        self.t13.setObjectName("t13")
        self.gridLayout_3.addWidget(self.t13, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionStats = QtWidgets.QAction(MainWindow)
        self.actionStats.setObjectName("actionStats")
        self.menuOptions.addAction(self.actionNew_Game)
        self.menuOptions.addAction(self.actionStats)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.triggered[QtWidgets.QAction].connect(self.popups)

        self.b2.clicked.connect(self._game)
        self.b1.clicked.connect(self.logic1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def message(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle('HEY!')
        Dialog.exec()

    def message1(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle('END')
        Dialog.exec()
     
    def player_win(self):
        MyPlayer = sqlite3.connect('Game_stats.db')
        curs = MyPlayer.cursor()
        pl = 'Player'
        curs.execute("SELECT * from stats WHERE Result = '"+pl+"';")
        rec = curs.fetchone()
        sql = "UPDATE stats SET Count = '"+str(rec[1] + 1)+"' WHERE Result = '"+pl+"';"
        try:
            curs.execute(sql)
            MyPlayer.commit()
            print('updated')
        except:
            print('error')
            MyPlayer.rollback()

    def comp_win(self):
        MyPlayer = sqlite3.connect('Game_stats.db')
        curs = MyPlayer.cursor()
        cm = 'Computer'
        curs.execute("SELECT * from stats WHERE Result = '"+cm+"';")
        rec = curs.fetchone()
        sql = "UPDATE stats SET Count = '"+str(rec[1] + 1)+"' WHERE Result = '"+cm+"';"
        try:
            curs.execute(sql)
            MyPlayer.commit()
            print('updated')
        except:
            print('error')
            MyPlayer.rollback()

    def draw(self):
        MyPlayer = sqlite3.connect('Game_stats.db')
        curs = MyPlayer.cursor()
        dw = 'Draw'
        curs.execute("SELECT * from stats WHERE Result = '"+dw+"';")
        rec = curs.fetchone()
        sql = "UPDATE stats SET Count = '"+str(rec[1] + 1)+"' WHERE Result = '"+dw+"';"
        try:
            curs.execute(sql)
            MyPlayer.commit()
            print('updated')
        except:
            print('error')
            MyPlayer.rollback()

    def clear_screen(self):
        clear = os.system('cls')

    def logic2(self):
        if self.t1.text() == self.t2.text() == self.t3.text() != '':
            if self.t11.text() == self.t1.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t1.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return        
        elif self.t4.text() == self.t5.text() == self.t6.text() != '':
            if self.t11.text() == self.t4.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t4.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return        
        elif self.t7.text() == self.t8.text() == self.t9.text() != '':
            if self.t11.text() == self.t7.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t7.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return        
        elif self.t1.text() == self.t4.text() == self.t7.text() != '':
            if self.t11.text() == self.t1.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t1.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return       
        elif self.t2.text() == self.t5.text() == self.t8.text() != '':
            if self.t11.text() == self.t2.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t2.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return   
        elif self.t3.text() == self.t6.text() == self.t9.text() != '':
            if self.t11.text() == self.t3.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t3.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return
        elif self.t1.text() == self.t5.text() == self.t9.text() != '':
            if self.t11.text() == self.t1.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t1.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return
        elif self.t3.text() == self.t5.text() == self.t7.text() != '':
            if self.t11.text() == self.t3.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t3.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return
        elif (self.t1.text() != ''
              and
              self.t2.text() != ''
              and
              self.t3.text() != ''
              and
              self.t4.text() != ''
              and
              self.t5.text() != ''
              and
              self.t6.text() != ''
              and
              self.t7.text() != ''
              and
              self.t8.text() != ''
              and
              self.t9.text() != ''):
            self.t13.setText('Draw')
            msg = 'Game Draw!'
            self.draw()
            self.message1(msg)
            return
        else:
            return self.player()

    def logic1(self):
        if self.t1.text() == self.t2.text() == self.t3.text() != '':
            if self.t11.text() == self.t1.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t1.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return        
        elif self.t4.text() == self.t5.text() == self.t6.text() != '':
            if self.t11.text() == self.t4.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t4.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return        
        elif self.t7.text() == self.t8.text() == self.t9.text() != '':
            if self.t11.text() == self.t7.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t7.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return        
        elif self.t1.text() == self.t4.text() == self.t7.text() != '':
            if self.t11.text() == self.t1.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t1.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return       
        elif self.t2.text() == self.t5.text() == self.t8.text() != '':
            if self.t11.text() == self.t2.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t2.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return   
        elif self.t3.text() == self.t6.text() == self.t9.text() != '':
            if self.t11.text() == self.t3.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t3.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return
        elif self.t1.text() == self.t5.text() == self.t9.text() != '':
            if self.t11.text() == self.t1.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t1.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return
        elif self.t3.text() == self.t5.text() == self.t7.text() != '':
            if self.t11.text() == self.t3.text():
                self.t13.setText('Congratulations! You Won.')
                msg='You Won'
                self.player_win()
                self.message1(msg)
            elif self.t12.text() == self.t3.text():
                self.t13.setText('You lose. Better luck next time!')
                msg='You lose'
                self.comp_win()
                self.message1(msg)
            return
        elif (self.t1.text() != ''
              and
              self.t2.text() != ''
              and
              self.t3.text() != ''
              and
              self.t4.text() != ''
              and
              self.t5.text() != ''
              and
              self.t6.text() != ''
              and
              self.t7.text() != ''
              and
              self.t8.text() != ''
              and
              self.t9.text() != ''):
            self.t13.setText('Draw')
            msg = 'Game Draw!'
            self.draw()
            self.message1(msg)
            return
        else:
            return self.computer()

    def _game(self):
        if self.t11.text() == 'X':
            msg = 'You are first'
            self.message(msg)
        else:
            self.computer()

    def player(self):
        print('your turn')

    def computer(self):
        print('computer turn')
        k = self.t12.text()
        list1 = [self.t1, self.t3, self.t5, self.t7, self.t9]
        list2 = [self.t2, self.t4, self.t6, self.t8]
        if (self.t1.text() == '' or
            self.t3.text() == '' or
            self.t5.text() == '' or
            self.t7.text() == '' or
            self.t9.text() == ''):
            b = int(5 * random.random())
            while(1):
                g = list1[b]
                if(g.text() == ''):
                    g.setText(k)
                    break
                else:
                    b = int(5 * random.random())
            self.logic2()
        elif (self.t2.text() == '' or
              self.t4.text() == '' or
              self.t6.text() == '' or
              self.t8.text() == ''):
            c = int(4 * random.random())
            while(1):
                h = list2[c]
                if(h.text() == ''):
                    h.setText(k)
                    break
                else:
                    c = int(4 * random.random())
            self.logic2()
        else:
            return

    def popups(self,action):
        txt = (action.text())
        if txt == 'New Game':
            name,OK=QtWidgets.QInputDialog.getText(MainWindow, "Player Name", "Enter your name:")
            if OK == True:
                nm = name
                self.t10.setText(nm)
                self.t11.clear()
                self.t12.clear()
                self.t13.clear()
                self.t1.clear()
                self.t2.clear()
                self.t3.clear()
                self.t4.clear()
                self.t5.clear()
                self.t6.clear()
                self.t7.clear()
                self.t8.clear()
                self.t9.clear()
                self.clear_screen()
            symbol,OK=QtWidgets.QInputDialog.getText(MainWindow, "Symbol", "Enter your symbol:")
            if OK == True:
                sm = symbol
                self.t11.setText(sm)
                if sm == 'X':
                    self.t12.setText('O')
                elif sm == 'O':
                    self.t12.setText('X')
                    
        elif txt == 'Stats':
            from game_stats import Ui_stats
            Dialog = QtWidgets.QDialog()
            ui = Ui_stats()
            ui.setupUi(Dialog)
            Dialog.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GAME"))
        self.label.setText(_translate("MainWindow", "Player Name:"))
        self.label_2.setText(_translate("MainWindow", "Symbol:"))
        self.b1.setText(_translate("MainWindow", "Confirm Move"))
        self.b2.setText(_translate("MainWindow", "Start Game"))
        self.label_3.setText(_translate("MainWindow", "Computer:"))
        self.label_4.setText(_translate("MainWindow", "Symbol:"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.actionNew_Game.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionStats.setText(_translate("MainWindow", "Stats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
