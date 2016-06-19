from PyQt4              import *
from mainWindow         import *
from drawingMachine     import *
from mapHandler         import *
from graph              import *
from tsp                import *

import sys

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionSair.triggered.connect(self.sair)
        self.actionAbrir_Mapa.triggered.connect(self.fPicker)
        self.btn_calcular.clicked.connect(self.calculate_tsp)

        ################## MAP MAGIC ##################
        self.mapPath = None
        self.mapMagic = mapHandler()
        #self.fPicker(fname = 'map_smaller.osm')
        #self.fPicker(fname = 'map_small.osm')
        self.fPicker(fname = 'map_america.osm')
        #self.fPicker(fname = 'map_iririu_aventureiro.osm')
        #self.fPicker(fname = 'map_bucarein.osm')
        #self.fPicker(fname = 'map_jarivatuba.osm')
        #self.fPicker(fname = 'map_espinheiros.osm')
        #self.fPicker(fname = 'map_boa_vista.osm')
        #self.fPicker(fname = 'map_morro_boa_vista.osm')
        self.mapMagic.print()
        ###############################################

        ################ DRAWING MAGIC ################
        self.mapView = drawingMachine(self.mapView)
        self.mapView.setGeometry(QtCore.QRect(0, 0, 631, 541))
        self.mapView.setObjectName("mapView")
        self.mapView.loadMap(self.mapMagic)
        self.mapView.update()
        ###############################################

    def calculate_tsp(self):
        points = self.mapView.getClicked()
        g      = {}

        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                else:
                    w       = dijkstra(self.mapMagic, p1, p2)
                    g[(p1[3], p2[3])] = w

        #print(g)

        simmulatedAnnealing(g, self.mapMagic, points)

        # STUB
        pass

    def sair(self):
        self.close()

    def fPicker(self, fname=None):
        if fname is None:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')

        if fname:
            self.mapPath = fname
            print("Opening: " + self.mapPath)
            self.mapMagic.apply_file(self.mapPath)
        else:
            pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
