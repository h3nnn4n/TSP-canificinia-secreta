from PyQt4              import *
from mainWindow         import *
from drawingMachine     import *

import osmium as o

import sys

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionSair.triggered.connect(self.sair)
        self.actionAbrir_Mapa.triggered.connect(self.fPicker)

        ################## MAP MAGIC ##################
        self.mapPath = None
        self.mapMagic = mapHandler()
        #self.fPicker(fname = '/home/h3nnn4n/projeto_de_soft/pitao/map_small.osm')
        self.fPicker(fname = '/home/h3nnn4n/projeto_de_soft/pitao/map.osm')
        self.mapMagic.print()
        ###############################################

        ################ DRAWING MAGIC ################
        self.mapView = drawingMachine(self.mapView)
        self.mapView.setGeometry(QtCore.QRect(0, 0, 471, 421))
        self.mapView.setObjectName("mapView")
        self.mapView.loadMap(self.mapMagic)
        self.mapView.update()
        ###############################################

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
        self.nodes  = []
        self.ways   = []
        self.rels   = []
        self.points = {}
        self.lines  = []

        self.minLat =  99999
        self.maxLat = -99999
        self.minLon =  99999
        self.maxLon = -99999

    def node(self, n):
        self.nodes.append(n)

        #if 'highway' in n.tags:
            #self.points[n.id] = (n.location.lat, n.location.lon)

        self.points[n.id] = (n.location.lat, n.location.lon)

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
                #print(j)
                if f is not None:
                    f = j.ref

                if old is not None:
                    self.lines.append((old.ref, j.ref))
                    #print((old.ref, j.ref))
                old = j
            if w.is_closed():
                self.lines.append((old.ref, f))
            #print((old.ref, f), w.is_closed())

    def relation(self, r):
        self.rels.append(r)

    def print(self):
        pass
        #print(self.points)
        #print("Loaded: ")
        #print(self.nodes)
        #print(self.ways)
        #print(self.rels)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
