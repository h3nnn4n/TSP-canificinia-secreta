from PyQt4              import *
from mainWindow         import *
from drawingMachine     import *

import osmium as o

from math import sqrt

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
        print(points)
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

class mapHandler(o.SimpleHandler):
    def __init__(self):
        o.SimpleHandler.__init__(self)
        self.nodes       = []
        self.ways        = []
        self.rels        = []
        self.lines       = []
        self.named_roads = []

        self.points      = {}
        self.points_used = {}

        self.minLat =  99999
        self.maxLat = -99999
        self.minLon =  99999
        self.maxLon = -99999

    def dist(self, a, b):
        x1 = self.points[a][0]
        x2 = self.points[b][0]

        y1 = self.points[a][1]
        y2 = self.points[b][1]

        return sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100.0

    def node(self, n):
        self.nodes.append(n)

        self.points[n.id]      = (n.location.lat, n.location.lon, 'highway' in n.tags)
        self.points_used[n.id] = False

        if 'highway' in n.tags: # or True:
            self.minLat = min(self.minLat, n.location.lat)
            self.minLon = min(self.minLon, n.location.lon)
            self.maxLat = max(self.maxLat, n.location.lat)
            self.maxLon = max(self.maxLon, n.location.lon)

    def way(self, w):
        self.ways.append(w)
        if 'highway' in w.tags:
            f   = None
            old = None
            for j in w.nodes:
                self.points_used[j.ref] = True
                if f is not None:
                    f = j.ref

                if old is not None:
                    self.lines.append((old.ref, j.ref))
                    self.named_roads.append(((old.ref, j.ref), w.tags['name'] if 'name' in w.tags else '', self.dist(old.ref, j.ref)))
                old = j
            if w.is_closed() and f is not None:
                self.lines.append((old.ref, f))
                self.named_roads.append(((old.ref, f), w.tags['name'] if 'name' in w.tags else '', self.dist(old.ref, f)))

    def relation(self, r):
        self.rels.append(r)

    def print(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
