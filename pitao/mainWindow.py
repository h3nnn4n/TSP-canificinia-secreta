# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 799, 558))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(639, 437))
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 141, 541))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.groupBox = QtGui.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 120, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btn_calcular = QtGui.QPushButton(self.groupBox)
        self.btn_calcular.setGeometry(QtCore.QRect(10, 30, 101, 23))
        self.btn_calcular.setObjectName(_fromUtf8("btn_calcular"))
        self.btn_limpar = QtGui.QPushButton(self.groupBox)
        self.btn_limpar.setGeometry(QtCore.QRect(10, 60, 101, 23))
        self.btn_limpar.setObjectName(_fromUtf8("btn_limpar"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 101, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.mapView = QtGui.QFrame(self.frame)
        self.mapView.setGeometry(QtCore.QRect(160, 10, 631, 541))
        self.mapView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mapView.setFrameShadow(QtGui.QFrame.Raised)
        self.mapView.setObjectName(_fromUtf8("mapView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionAbrir_Mapa = QtGui.QAction(MainWindow)
        self.actionAbrir_Mapa.setObjectName(_fromUtf8("actionAbrir_Mapa"))
        self.menuArquivo.addAction(self.actionAbrir_Mapa)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Botões", None))
        self.btn_calcular.setText(_translate("MainWindow", "Calcular", None))
        self.btn_limpar.setText(_translate("MainWindow", "Limpar", None))
        self.pushButton_3.setText(_translate("MainWindow", "Mostrar Rota", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionAbrir_Mapa.setText(_translate("MainWindow", "Abrir Mapa", None))

