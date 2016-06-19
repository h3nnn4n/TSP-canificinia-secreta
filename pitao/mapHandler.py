import osmium as o

from math import sqrt

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
