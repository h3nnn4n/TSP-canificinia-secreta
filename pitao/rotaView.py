from PyQt4              import *
from rota               import *

import itertools

class rotaDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, mapMagic, tsp, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_cancelar.clicked.connect(self.sair)
        self.btn_ok.clicked.connect(self.sair)
        self.mapMagic = mapMagic

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()

        self.tsp   = tsp[0]
        self.graph = tsp[1]

        old = None

        names = []
        for i in range(0, len(self.tsp) - 1):
            k = self.tsp[i], self.tsp[i+1]
            lines = self.graph[k][0]
            for j in lines:
                name = self.mapMagic.road_names[j]
                names.append(name)

        for k, i in enumerate(itertools.groupby(names)):
            print(i[0])
            if len(i[0]) > 0:
                self.tableWidget.insertRow(k)
                p  = QtGui.QTableWidgetItem(str(k+1))
                self.tableWidget.setItem(k, 0, p)
                p  = QtGui.QTableWidgetItem(i[0])
                self.tableWidget.setItem(k, 1, p)

        self.tableWidget.resizeColumnsToContents()

    def sair(self):
        self.close()
