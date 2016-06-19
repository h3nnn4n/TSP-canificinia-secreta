
def dijkstra(mapMagic, source, dest):
    print("\nRUNNING DIJKSTRA")

    dist = {}

    source_id = source[3]
    dest_id   = dest[3]

    print("From %d to %d" % (source_id, dest_id))

    dist      = {i: 99999 for i in mapMagic.points}
    prev      = {i: -1    for i in mapMagic.points}
    unvisited = set([i for i in mapMagic.points])

    dist[source_id] = 0

    while len(unvisited) > 0:
        u, q = getMin(unvisited, dist)
        unvisited.remove(u)

        if u == dest_id:
            break

        for v, w in getNeighbor(mapMagic, u):
            if v in unvisited:
                alt = dist[u] + w

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    path = set()
    u    = dest_id
    while prev[u] != -1:
        path.add(u)
        u = prev[u]
    path.add(u)

    return path, dist[dest_id]

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
