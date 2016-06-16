from PyQt4              import *

import sys
import random
from math import sqrt

class drawingMachine(QtGui.QWidget):
    def __init__(self, parent = None):
        super(drawingMachine, self).__init__(parent)
        self.mapMagic = None
        self.clicked = set()

    def getClicked(self):
        return self.clicked

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x, y  = event.pos().x(), event.pos().y()

            nearest = None
            for obj in sorted(
                    map (lambda w: (sqrt(((self.getPoint(self.mapMagic.points[w]))[0]-x)**2 +
                                         ((self.getPoint(self.mapMagic.points[w]))[1]-y)**2),
                                          (self.getPoint(self.mapMagic.points[w])),
                                           self.mapMagic.points_used[w]
                                        ), self.mapMagic.points)):
                if obj[2] and nearest is None:
                    nearest = obj
                    break

            if nearest is not None:
                self.clicked.add(nearest)

            self.update()

    def loadMap(self, mapMagic):
        self.mapMagic = mapMagic

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        self.drawPoints(qp)
        self.drawClicked(qp)
        qp.end()

    def drawClicked(self, qp):
        qp.setPen(QtCore.Qt.green)
        for k, (x1, y1), p in self.clicked:
            qp.drawEllipse(x1-2, y1-2, 3, 3)

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

    def getPoint(self, i, j = None):
        if j is None:
            i, j, k = i
            size = self.size()
            y = size.height () - ( i - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.height()
            x =                  ( j - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.width()
        else:
            size = self.size()
            y = size.height () - ( i - self.mapMagic.minLat ) / ( self.mapMagic.maxLat - self.mapMagic.minLat) * size.height()
            x =                  ( j - self.mapMagic.minLon ) / ( self.mapMagic.maxLon - self.mapMagic.minLon) * size.width()

        return (x, y)
