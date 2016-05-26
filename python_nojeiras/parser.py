from imposm.parser import OSMParser

class HighwayCounter(object):
    highways = 0

    def coords(self, coords):
        for i in coords:
            pass
            #print i

    def ways(self, ways):
        for osmid, tags, refs in ways:
            if 'highway' in tags:
                self.highways += 1
                #print osmid
                #print tags
                #print refs
                #print "\n"

counter = HighwayCounter()
p = OSMParser(concurrency=1, coords_callback=counter.coords, ways_callback=counter.ways)
p.parse('map_small.osm')


# done
print(counter.highways)
