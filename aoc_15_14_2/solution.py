import re
input = open("aoc_15_14_2\\input.txt").read().splitlines()
seconds = 0
winner = 0
reindeerDict = dict()

while(seconds < 2503):
    seconds += 1
    maxDistance = 0
    distances = set()

    for reindeer in input:
        name = reindeer.split()[0]
        speed, time, rest = map(int, re.findall("(\\d+)", reindeer))
        distance = (seconds // (time + rest)) * speed * time + min((seconds % (time + rest)), time) * speed
        distances.add((name, distance))

        if(maxDistance < distance):
            maxDistance =  distance

    for deer in distances:
        if deer[1] == maxDistance:
            if deer[0] in reindeerDict.keys():
                reindeerDict[deer[0]] = reindeerDict[deer[0]] + 1
            else:
                reindeerDict[deer[0]] = 1       

print(max(reindeerDict.values()))