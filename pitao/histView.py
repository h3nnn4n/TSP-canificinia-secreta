from PyQt4              import *
from hist               import *

class viewDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_cancelar.clicked.connect(self.sair)
        self.btn_ok.clicked.connect(self.sair)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalHeaderLabels(["Tamanho", "Distância"])

        f   = open('hist.dat', 'r')

        data = []

        for i in f.readlines():
            p, q = i.split(' ')
            size = int(p)
            dist = float(q)
            data.append((size, dist))

        f.close()

        menor = 99999
        maior = 0
        media = 0

        last = 0

        for k, (size, dist) in enumerate(data):
            last = k
            menor = min(menor, dist)
            maior = max(maior, dist)
            media += dist
            self.tableWidget.insertRow(k)
            p  = QtGui.QTableWidgetItem(str(size))
            self.tableWidget.setItem(k, 0, p)
            p  = QtGui.QTableWidgetItem(str(dist))
            self.tableWidget.setItem(k, 1, p)

        last += 1

        self.tableWidget.insertRow(last)
        p  = QtGui.QTableWidgetItem("Mínimo")
        self.tableWidget.setItem(last, 0, p)
        p  = QtGui.QTableWidgetItem(str(menor))
        self.tableWidget.setItem(last, 1, p)

        last += 1

        self.tableWidget.insertRow(last)
        p  = QtGui.QTableWidgetItem("Máximo")
        self.tableWidget.setItem(last, 0, p)
        p  = QtGui.QTableWidgetItem(str(maior))
        self.tableWidget.setItem(last, 1, p)


        last += 1

        self.tableWidget.insertRow(last)
        p  = QtGui.QTableWidgetItem("Média")
        self.tableWidget.setItem(last, 0, p)
        p  = QtGui.QTableWidgetItem(str(media/len(data)))
        self.tableWidget.setItem(last, 1, p)

        self.tableWidget.resizeColumnsToContents()

    def sair(self):
        self.close()
