def generateCompleteGraph(mapMagic, points):
    g = {}
    for start in points:
        g2 = dijkstra(mapMagic, start, points)
        g.update(g2)

    return g

def dijkstra(mapMagic, source, dests):
    dist = {}

    source_id = source[3]
    dest_id   = list(map(lambda x: x[3], dests))

    dist      = {i: 99999 for i in mapMagic.points}
    prev      = {i: -1    for i in mapMagic.points}
    stop      = {i: True  for i in dest_id        }
    unvisited = set([i for i in mapMagic.points])

    stop[source_id] = False
    dist[source_id] = 0
    alive           = True

    while len(unvisited) > 0 and alive:
        u, q = getMin(unvisited, dist)
        unvisited.remove(u)

        if u in dest_id:
            stop[u] == False

        for v, w in getNeighbor(mapMagic, u):
            if v in unvisited:
                alt = dist[u] + w

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

        alive = False
        for k in stop:
            if stop[k]:
                alive = True

    for dest in dest_id:
        path = []
        u    = dest
        while prev[u] != -1:
            path.append((u, prev[u]))
            u = prev[u]
        dist[(source_id, dest)] = (path, dist[dest])

    return dist

def getNeighbor(mapMagic, u):
    neighbor = set()

    for (t1, t2), name, w in mapMagic.named_roads:
        if t1 == u:
            neighbor.add((t2, w))
        elif t2 == u:
            neighbor.add((t1, w))

    return neighbor

def getMin(unvisited, dist):
    k1, v1 = -1, 999999
    for k in unvisited:
        if dist[k] < v1:
            k1 = k
            v1 = dist[k]
    return k1, v1
