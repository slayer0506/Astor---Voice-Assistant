# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ASTORGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ASTOR(object):
    def setupUi(self, ASTOR):
        ASTOR.setObjectName("ASTOR")
        ASTOR.resize(821, 542)
        self.centralwidget = QtWidgets.QWidget(ASTOR)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 821, 541))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("C:/Users/Asus/Downloads/RECO.gif"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.initating = QtWidgets.QLabel(self.centralwidget)
        self.initating.setGeometry(QtCore.QRect(0, 0, 401, 81))
        self.initating.setText("")
        self.initating.setPixmap(QtGui.QPixmap("C:/Users/Asus/Downloads/initalising.gif"))
        self.initating.setScaledContents(False)
        self.initating.setObjectName("initating")
        self.RUN = QtWidgets.QPushButton(self.centralwidget)
        self.RUN.setGeometry(QtCore.QRect(560, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RUN.setFont(font)
        self.RUN.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.RUN.setObjectName("RUN")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(690, 470, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.EXIT.setFont(font)
        self.EXIT.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.EXIT.setObjectName("EXIT")
        self.Faceid = QtWidgets.QLabel(self.centralwidget)
        self.Faceid.setGeometry(QtCore.QRect(600, 0, 221, 161))
        self.Faceid.setText("")
        self.Faceid.setPixmap(QtGui.QPixmap("C:/Users/Asus/Downloads/FACE ID.gif"))
        self.Faceid.setScaledContents(True)
        self.Faceid.setObjectName("Faceid")
        ASTOR.setCentralWidget(self.centralwidget)

        self.retranslateUi(ASTOR)
        QtCore.QMetaObject.connectSlotsByName(ASTOR)

    def retranslateUi(self, ASTOR):
        _translate = QtCore.QCoreApplication.translate
        ASTOR.setWindowTitle(_translate("ASTOR", "MainWindow"))
        self.RUN.setText(_translate("ASTOR", "RUN"))
        self.EXIT.setText(_translate("ASTOR", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ASTOR = QtWidgets.QMainWindow()
    ui = Ui_ASTOR()
    ui.setupUi(ASTOR)
    ASTOR.show()
    sys.exit(app.exec_())