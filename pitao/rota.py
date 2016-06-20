# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rota.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(3, 3, 632, 421))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tableWidget = QtGui.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 611, 401))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(3, 430, 632, 41))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.btn_cancelar = QtGui.QPushButton(self.frame_2)
        self.btn_cancelar.setGeometry(QtCore.QRect(540, 10, 83, 23))
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.btn_ok = QtGui.QPushButton(self.frame_2)
        self.btn_ok.setGeometry(QtCore.QRect(450, 10, 83, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_cancelar.setText(_translate("Dialog", "Cancelar", None))
        self.btn_ok.setText(_translate("Dialog", "Ok", None))

