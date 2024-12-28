input = open("aoc_15_09_1\\input.txt").read().splitlines()
locations = set()
distances = dict()
shortest = None

def measure(destination, visited, total):
    global shortest
    if shortest != None and total > shortest:
        return
    
    if visited == locations:
        shortest = total

    for destination in distances[destination]:
        location = destination[0]
        distance = destination[1]
        if location in visited:
            continue
        copy = visited.copy()
        copy.add(location)
        measure(location, copy, total + int(distance))


for line in input:
    parts = line.split()
    locOne = parts[0]
    locTwo = parts[2]
    distance = parts[4]
    
    locations.add(locOne)
    locations.add(locTwo)

    if locOne in distances.keys():
        distances[locOne].add((locTwo, distance))
    else:
        distances[locOne] = {(locTwo, distance)}

    if locTwo in distances.keys():
        distances[locTwo].add((locOne, distance))
    else:
        distances[locTwo] = {(locOne, distance)}

    



for start in locations:
    measure(start, {start}, 0)

print(shortest)