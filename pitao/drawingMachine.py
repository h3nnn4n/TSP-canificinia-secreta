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
        self.drawLines(qp)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.blue)

        for id1, id2 in self.mapMagic.lines:
            try:
                i = self.mapMagic.points[id1]
                j = self.mapMagic.points[id2]

                x1, y1 = self.getPoint(i[0], i[1])
                x2, y2 = self.getPoint(j[0], j[1])

                qp.drawEllipse(x1-1, y1-1, 2, 2)
                qp.drawEllipse(x2-1, y2-1, 2, 2)
                qp.drawPoint(x1, y1)
                qp.drawPoint(x2, y2)
            except Exception as e :
                #print("Opps")
                #raise
                pass


    def drawLines(self, qp):
        qp.setPen(QtCore.Qt.red)

        for id1, id2 in self.mapMagic.lines:
            try:
                i = self.mapMagic.points[id1]
                x1, y1 = self.getPoint(i[0], i[1])

                i = self.mapMagic.points[id2]
                x2, y2 = self.getPoint(i[0], i[1])

                qp.drawLine(x1, y1, x2, y2)
            except:
                  pass


        #for k in self.mapMagic.points:
            #i = self.mapMagic.points[k]
            #y = ( i[0] - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.height()
            #x = ( i[1] - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.width()
            #x, y = self.getPoint(i[0], i[1])
            #qp.drawPoint(x, y)

    def getPoint(self, i, j):
        size = self.size()
        y = size.height () - ( i - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.height()
        x =                  ( j - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.width()
        return (x, y)
