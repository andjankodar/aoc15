from copy import deepcopy
import math
import sys


input = list(map(int, open("aoc_15_24_2\\input.txt").read().splitlines()))
input.reverse()
cache = set()
smallestGroup = sys.maxsize
smallestQE = sys.maxsize
total = sum(input)
groupWeight = total // 4

groups = set()

def add_to_group(group):
    global smallestGroup
    global smallestQE

    if len(group) > smallestGroup or sum(group) > groupWeight:
        return
    
    group.sort()

    if tuple(group) in cache:
        return
    else:
        cache.add(tuple(group))

    if sum(group) == groupWeight:
        if len(group) < smallestGroup:
            smallestGroup = len(group)
            smallestQE = math.prod(group)
            print(smallestQE)
            print(group)
            print()
        elif len(group) == smallestGroup and math.prod(group) < smallestQE:
            smallestGroup = len(group)
            smallestQE = math.prod(group)
            print(smallestQE)
            print(group)
            print()
        return

    for i in range(0, len(input)):
         if input[i] not in group:
            newGroup = deepcopy(group)
            newGroup.append(input[i])
            add_to_group(newGroup)

add_to_group(list())

print(smallestQE)

           




