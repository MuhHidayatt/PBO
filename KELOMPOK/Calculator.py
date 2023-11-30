from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 397)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 320, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.p9 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("9") )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p9.sizePolicy().hasHeightForWidth())
        self.p9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p9.setFont(font)
        self.p9.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p9.setObjectName("p9")
        self.gridLayout.addWidget(self.p9, 2, 2, 1, 1)
        self.mod = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("%") )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.mod.sizePolicy().hasHeightForWidth())
        self.mod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mod.setFont(font)
        self.mod.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(94, 255, 250);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.mod.setObjectName("mod")
        self.gridLayout.addWidget(self.mod, 1, 0, 1, 1)
        self.p1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("1") )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p1.sizePolicy().hasHeightForWidth())
        self.p1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p1.setFont(font)
        self.p1.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 4, 0, 1, 1)
        self.delete_2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.remove_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.delete_2.sizePolicy().hasHeightForWidth())
        self.delete_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(94, 255, 250);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.delete_2.setObjectName("delete_2")
        self.gridLayout.addWidget(self.delete_2, 1, 2, 1, 1)
        self.C = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("C"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.C.sizePolicy().hasHeightForWidth())
        self.C.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C.setFont(font)
        self.C.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(94, 255, 250);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.C.setObjectName("C")
        self.gridLayout.addWidget(self.C, 1, 1, 1, 1)
        self.kurang = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("-"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.kurang.sizePolicy().hasHeightForWidth())
        self.kurang.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kurang.setFont(font)
        self.kurang.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(255, 130, 232);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.kurang.setObjectName("kurang")
        self.gridLayout.addWidget(self.kurang, 2, 3, 1, 1)
        self.tambah = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("+"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.tambah.sizePolicy().hasHeightForWidth())
        self.tambah.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tambah.setFont(font)
        self.tambah.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(94, 255, 250);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.tambah.setObjectName("tambah")
        self.gridLayout.addWidget(self.tambah, 1, 3, 1, 1)
        self.koma = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.dot_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.koma.sizePolicy().hasHeightForWidth())
        self.koma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.koma.setFont(font)
        self.koma.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.koma.setObjectName("koma")
        self.gridLayout.addWidget(self.koma, 5, 2, 1, 1)
        self.bagi = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("/"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.bagi.sizePolicy().hasHeightForWidth())
        self.bagi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bagi.setFont(font)
        self.bagi.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(255, 130, 232);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bagi.setObjectName("bagi")
        self.gridLayout.addWidget(self.bagi, 4, 3, 1, 1)
        self.p7 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("7"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p7.sizePolicy().hasHeightForWidth())
        self.p7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p7.setFont(font)
        self.p7.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p7.setObjectName("p7")
        self.gridLayout.addWidget(self.p7, 2, 0, 1, 1)
        self.p0 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("0"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p0.sizePolicy().hasHeightForWidth())
        self.p0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p0.setFont(font)
        self.p0.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.p0.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p0.setObjectName("p0")
        self.gridLayout.addWidget(self.p0, 5, 0, 1, 2)
        self.p4 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("4"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p4.sizePolicy().hasHeightForWidth())
        self.p4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p4.setFont(font)
        self.p4.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p4.setObjectName("p4")
        self.gridLayout.addWidget(self.p4, 3, 0, 1, 1)
        self.p3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("3"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p3.sizePolicy().hasHeightForWidth())
        self.p3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p3.setFont(font)
        self.p3.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p3.setObjectName("p3")
        self.gridLayout.addWidget(self.p3, 4, 2, 1, 1)
        self.p6 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("6"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p6.sizePolicy().hasHeightForWidth())
        self.p6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p6.setFont(font)
        self.p6.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p6.setObjectName("p6")
        self.gridLayout.addWidget(self.p6, 3, 2, 1, 1)
        self.p2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("2"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p2.sizePolicy().hasHeightForWidth())
        self.p2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p2.setFont(font)
        self.p2.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p2.setObjectName("p2")
        self.gridLayout.addWidget(self.p2, 4, 1, 1, 1)
        self.p5 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("5"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p5.sizePolicy().hasHeightForWidth())
        self.p5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p5.setFont(font)
        self.p5.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p5.setObjectName("p5")
        self.gridLayout.addWidget(self.p5, 3, 1, 1, 1)
        self.p8 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("8"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.p8.sizePolicy().hasHeightForWidth())
        self.p8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.p8.setFont(font)
        self.p8.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    background-color : rgb(166, 166, 166);\n"
"    border-radius : 30px;\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.p8.setObjectName("p8")
        self.gridLayout.addWidget(self.p8, 2, 1, 1, 1)
        self.kali = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.press_it("*"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.kali.sizePolicy().hasHeightForWidth())
        self.kali.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kali.setFont(font)
        self.kali.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(255, 130, 232);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.kali.setObjectName("kali")
        self.gridLayout.addWidget(self.kali, 3, 3, 1, 1)
        self.sama_dengan = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.equal_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.sama_dengan.sizePolicy().hasHeightForWidth())
        self.sama_dengan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sama_dengan.setFont(font)
        self.sama_dengan.setStyleSheet("QPushButton{\n"
"    color : rgb(0, 0, 0);\n"
"    border-radius : 30px;\n"
"    background-color: rgb(255, 130, 232);\n"
"}\n"
"QPushButton:Hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.sama_dengan.setObjectName("sama_dengan")
        self.gridLayout.addWidget(self.sama_dengan, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#fungsi sama dengan
    def equal_it(self):
        screen = self.label.text()
        answer = eval(screen)
        self.label.setText(str(answer))
        
#Menghapus karakter
    def remove_it(self):
        screen = self.label.text()
        screen = screen [:-1]
        self.label.setText(screen)
                
#Membuat Decimal       
    def dot_it(self):
        screen = self.label.text()
        signs_tuple = ("/", "x", "+", "-","%")
        for i in signs_tuple:
            if i not in screen:
                if "." in screen: 
                    pass
                else:
                    self.label.setText(f"{screen}.")
            else:
                if screen[-1].isnumeric() and "." not in screen[screen.rfind(i):]:
                    self.label.setText(f"{screen}.")
                else:
                    pass
        
 #Biar bisa ditekan       
    def press_it(self, pressed):
        if pressed == "C":
                self.label.setText('0')
        else:            
                if self.label.text() == "0":
                   self.label.setText('')
                self.label.setText(f'{self.label.text()}{pressed}')
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.p9.setText(_translate("MainWindow", "9"))
        self.p9.setShortcut(_translate("MainWindow", "9"))
        self.mod.setText(_translate("MainWindow", "%"))
        self.mod.setShortcut(_translate("MainWindow", "%"))
        self.p1.setText(_translate("MainWindow", "1"))
        self.p1.setShortcut(_translate("MainWindow", "1"))
        self.delete_2.setText(_translate("MainWindow", "Del"))
        self.delete_2.setShortcut(_translate("MainWindow", "Backspace"))
        self.C.setText(_translate("MainWindow", "C"))
        self.C.setShortcut(_translate("MainWindow", "C"))
        self.kurang.setText(_translate("MainWindow", "-"))
        self.kurang.setShortcut(_translate("MainWindow", "-"))
        self.tambah.setText(_translate("MainWindow", "+"))
        self.tambah.setShortcut(_translate("MainWindow", "+"))
        self.koma.setText(_translate("MainWindow", ","))
        self.koma.setShortcut(_translate("MainWindow", ","))
        self.bagi.setText(_translate("MainWindow", "/"))
        self.bagi.setShortcut(_translate("MainWindow", "/"))
        self.p7.setText(_translate("MainWindow", "7"))
        self.p7.setShortcut(_translate("MainWindow", "7"))
        self.p0.setText(_translate("MainWindow", "0"))
        self.p0.setShortcut(_translate("MainWindow", "0"))
        self.p4.setText(_translate("MainWindow", "4"))
        self.p4.setShortcut(_translate("MainWindow", "4"))
        self.p3.setText(_translate("MainWindow", "3"))
        self.p3.setShortcut(_translate("MainWindow", "3"))
        self.p6.setText(_translate("MainWindow", "6"))
        self.p6.setShortcut(_translate("MainWindow", "6"))
        self.p2.setText(_translate("MainWindow", "2"))
        self.p2.setShortcut(_translate("MainWindow", "2"))
        self.p5.setText(_translate("MainWindow", "5"))
        self.p5.setShortcut(_translate("MainWindow", "5"))
        self.p8.setText(_translate("MainWindow", "8"))
        self.p8.setShortcut(_translate("MainWindow", "8"))
        self.kali.setText(_translate("MainWindow", "X"))
        self.kali.setShortcut(_translate("MainWindow", "*"))
        self.sama_dengan.setText(_translate("MainWindow", "="))
        self.sama_dengan.setShortcut(_translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
