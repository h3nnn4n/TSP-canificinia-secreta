from PyQt4              import *

import sys
import random

class drawingMachine(QtGui.QWidget):
    def __init__(self, parent = None):
        super(drawingMachine, self).__init__(parent)
        self.mapMagic = None

    def loadMap(self, mapMagic):
        self.mapMagic = mapMagic

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        #print(self.mapMagic.ways)

        for id1, id2 in self.mapMagic.lines:
            try:
                i = self.mapMagic.points[id1]
                x1 = ( i[0] - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.width()
                y1 = ( i[1] - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.height()

                i = self.mapMagic.points[id2]
                x2 = ( i[0] - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.width()
                y2 = ( i[1] - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.height()
                qp.drawLine(x1, y1, x2, y2)
            except:
                  pass

        qp.setPen(QtCore.Qt.blue)

        #print(self.mapMagic.points)

        for x in self.mapMagic.points:
            #print(x)
            i = self.mapMagic.points[x]
            x = ( i[0] - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.width()
            y = ( i[1] - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.height()
            qp.drawPoint(x, y)
