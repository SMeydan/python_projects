# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 900)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(830, 10, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(23, 93, 255);\n"
"background-color: rgb(176, 149, 147);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 400, 911, 31))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 190, 921, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setStyleSheet("border-bottom-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(380, 130, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(230, 130, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(90, 130, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(23, 93, 255);\n"
"background-color: rgb(176, 149, 147);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 350, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(210, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(690, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(450, 210, 41, 204))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(690, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(690, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 270, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 370, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(690, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(330, 220, 131, 31))
        self.frame.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l4 = QtWidgets.QLabel(self.frame)
        self.l4.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l4.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l4.setObjectName("l4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 260, 131, 31))
        self.frame_2.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.l5 = QtWidgets.QLabel(self.frame_2)
        self.l5.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l5.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l5.setObjectName("l5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(330, 330, 131, 31))
        self.frame_3.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.l6 = QtWidgets.QLabel(self.frame_3)
        self.l6.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l6.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l6.setObjectName("l6")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(330, 370, 131, 31))
        self.frame_4.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.l7 = QtWidgets.QLabel(self.frame_4)
        self.l7.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l7.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l7.setObjectName("l7")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(800, 250, 131, 31))
        self.frame_5.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.l8 = QtWidgets.QLabel(self.frame_5)
        self.l8.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l8.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l8.setObjectName("l8")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(800, 290, 131, 31))
        self.frame_6.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.l9 = QtWidgets.QLabel(self.frame_6)
        self.l9.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l9.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l9.setObjectName("l9")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(800, 330, 131, 31))
        self.frame_7.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.l10 = QtWidgets.QLabel(self.frame_7)
        self.l10.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l10.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l10.setObjectName("l10")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(800, 370, 131, 31))
        self.frame_8.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.l11 = QtWidgets.QLabel(self.frame_8)
        self.l11.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l11.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l11.setObjectName("l11")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(40, 80, 131, 31))
        self.frame_9.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.l1 = QtWidgets.QLabel(self.frame_9)
        self.l1.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l1.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l1.setObjectName("l1")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(190, 80, 131, 31))
        self.frame_10.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.l2 = QtWidgets.QLabel(self.frame_10)
        self.l2.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l2.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l2.setObjectName("l2")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(330, 80, 131, 31))
        self.frame_11.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.l3 = QtWidgets.QLabel(self.frame_11)
        self.l3.setGeometry(QtCore.QRect(40, 10, 55, 16))
        self.l3.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.l3.setObjectName("l3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(870, 130, 41, 20))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.listWidget_hmi = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_hmi.setGeometry(QtCore.QRect(20, 460, 161, 381))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_hmi.setFont(font)
        self.listWidget_hmi.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_hmi.setObjectName("listWidget_hmi")
        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(510, 60, 131, 91))
        self.listWidget_1.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_1.setObjectName("listWidget_1")
        self.listWidget_hvalue = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_hvalue.setGeometry(QtCore.QRect(180, 460, 150, 381))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_hvalue.setFont(font)
        self.listWidget_hvalue.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_hvalue.setObjectName("listWidget_hvalue")
        self.listWidget_user = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_user.setGeometry(QtCore.QRect(330, 460, 150, 381))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_user.setFont(font)
        self.listWidget_user.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_user.setObjectName("listWidget_user")
        self.listWidget_axis = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_axis.setGeometry(QtCore.QRect(630, 460, 150, 381))
        self.listWidget_axis.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_axis.setObjectName("listWidget_axis")
        self.listWidget_uvalue = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_uvalue.setGeometry(QtCore.QRect(480, 460, 150, 381))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_uvalue.setFont(font)
        self.listWidget_uvalue.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_uvalue.setObjectName("listWidget_uvalue")
        self.listWidget_avalue = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_avalue.setGeometry(QtCore.QRect(780, 460, 150, 381))
        self.listWidget_avalue.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_avalue.setObjectName("listWidget_avalue")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(640, 60, 131, 91))
        self.listWidget_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.listWidget_2.setObjectName("listWidget_2")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(120, 420, 131, 31))
        self.frame_12.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_10 = QtWidgets.QLabel(self.frame_12)
        self.label_10.setGeometry(QtCore.QRect(40, 0, 111, 31))
        self.label_10.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_10.setObjectName("label_10")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(400, 420, 131, 31))
        self.frame_13.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_13 = QtWidgets.QLabel(self.frame_13)
        self.label_13.setGeometry(QtCore.QRect(40, 0, 111, 31))
        self.label_13.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_13.setObjectName("label_13")
        self.frame_14 = QtWidgets.QFrame(self.centralwidget)
        self.frame_14.setGeometry(QtCore.QRect(690, 420, 131, 31))
        self.frame_14.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        self.label_17.setGeometry(QtCore.QRect(40, 0, 111, 31))
        self.label_17.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_17.setObjectName("label_17")
        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setGeometry(QtCore.QRect(570, 10, 131, 31))
        self.frame_15.setStyleSheet("background-color: rgb(176, 149, 147);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_18 = QtWidgets.QLabel(self.frame_15)
        self.label_18.setGeometry(QtCore.QRect(30, 10, 111, 16))
        self.label_18.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_18.setObjectName("label_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuTrends = QtWidgets.QMenu(self.menubar)
        self.menuTrends.setObjectName("menuTrends")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuTrends.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "GUEST"))
        self.label.setText(_translate("MainWindow", "HMI           USER           AXIS"))
        self.label_2.setText(_translate("MainWindow", "AVERAGE"))
        self.pushButton_2.setText(_translate("MainWindow", "GRAPH"))
        self.label_15.setText(_translate("MainWindow", "TOTAL"))
        self.label_3.setText(_translate("MainWindow", "product"))
        self.label_5.setText(_translate("MainWindow", "boxes"))
        self.label_7.setText(_translate("MainWindow", "product"))
        self.label_11.setText(_translate("MainWindow", "boxes"))
        self.label_9.setText(_translate("MainWindow", "boxes"))
        self.label_14.setText(_translate("MainWindow", "product"))
        self.label_12.setText(_translate("MainWindow", "boxes"))
        self.label_4.setText(_translate("MainWindow", "User(per min)"))
        self.label_6.setText(_translate("MainWindow", "COUNTERS"))
        self.label_8.setText(_translate("MainWindow", "Total(per min)"))
        self.label_16.setText(_translate("MainWindow", "product"))
        self.l4.setText(_translate("MainWindow", "NONE"))
        self.l5.setText(_translate("MainWindow", "NONE"))
        self.l6.setText(_translate("MainWindow", "NONE"))
        self.l7.setText(_translate("MainWindow", "NONE"))
        self.l8.setText(_translate("MainWindow", "NONE"))
        self.l9.setText(_translate("MainWindow", "NONE"))
        self.l10.setText(_translate("MainWindow", "NONE"))
        self.l11.setText(_translate("MainWindow", "NONE"))
        self.l1.setText(_translate("MainWindow", "NONE"))
        self.l2.setText(_translate("MainWindow", "NONE"))
        self.l3.setText(_translate("MainWindow", "NONE"))
        self.label_10.setText(_translate("MainWindow", "HMI"))
        self.label_13.setText(_translate("MainWindow", "USER"))
        self.label_17.setText(_translate("MainWindow", "AXIS"))
        self.label_18.setText(_translate("MainWindow", "REAL"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuTrends.setTitle(_translate("MainWindow", "Trends"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
