import random
from math import exp, cosh

def simmulatedAnnealing(g, mapMagic, points):
    t_0      = 20.0
    t_n      = 0.0
    T        = 0.1
    maxIter  = 10**2
    i        = 0
    point_id = list(map( lambda x: x[3], points))

    s0 = randomSolution(point_id)

    print(energy(s0, g))

    while i < maxIter:
        T =  (t_0 - t_n)/cosh((10.0*float(i)/float(maxIter)))
        sn = pertubate(s0.copy())
        if exp(-(energy(sn, g) - energy(s0, g))/T) > random.random():
            s0 = sn

        i += 1

        print(i, energy(s0, g), T)

def pertubate(g):
    w      = random.randint(1, len(g) - 3)
    p      = g[w]
    g[w]   = g[w+1]
    g[w+1] = p
    return g

def energy(s, g):
    c = 0
    for i in range(0, len(s)-1):
        c += g[(s[i], s[i+1])][1]

    return c

def randomSolution(g):
    g2 = g.copy()
    random.shuffle(g2)
    g2.append(g2[0])
    return g2
