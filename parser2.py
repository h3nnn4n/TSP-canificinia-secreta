from osmread import parse_file, Way

highway_count = 0
for entity in parse_file('map_small.osm'):
    if isinstance(entity, Way) and 'highway' in entity.tags:
        highway_count += 1

print(highway_count)
