import re
input = open("aoc_15_14_1\\input.txt").read().splitlines()
seconds = 2503
winner = 0

for reindeer in input:
    name = reindeer.split()[0]
    speed, time, rest = map(int, re.findall("(\\d+)", reindeer))
    distance = (seconds // (time + rest)) * speed * time + min((seconds % (time + rest)), time) * speed
    if distance > winner:
        winner = distance

print(winner)