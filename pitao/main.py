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
        self.actionSair.triggered.connect       ( self.sair                              )
        self.actionAbrir_Mapa.triggered.connect ( lambda x: self.fPicker ( fname = None ))
        self.btn_calcular.clicked.connect       ( self.calculate_tsp                     )
        self.btn_limpar.clicked.connect         ( self.limpar                            )

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
        self.mapView = drawingMachine ( self.mapView                     )
        self.mapView.setGeometry      ( QtCore.QRect   ( 0, 0, 631, 541 ))
        self.mapView.setObjectName    ( "mapView"                        )
        self.mapView.loadMap          ( self.mapMagic                    )
        self.mapView.update           (                                  )
        ###############################################

    def limpar(self):
        self.mapView.reset()

    def calculate_tsp(self):
        points = self.mapView.getClicked()

        g = generateCompleteGraph(self.mapMagic, points)

        path, cost = simmulatedAnnealing(g, self.mapMagic, points)
        self.mapView.tspSolution(path, g)

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
