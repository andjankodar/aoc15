input = [int(c) for c in open("aoc_15_17_1\\input.txt").readlines()]
combinations = set()
cache = set()

def tap(containers, tapped):
    global combinations
    global cache
    
    if tapped == 150 and str(containers) not in cache:
        combinations.add(str(containers))
        return
    elif tapped > 150:       
        return

    if str(containers) in cache:
        return
    else:
        cache.add(str(containers))
    
    for i in range(0, len(input)):
        if i in containers:
            continue     
        containerCopy = containers.copy()
        containerCopy.append(i)
        containerCopy.sort()
        tap(containerCopy, tapped+input[i])

for i in range(0, len(input)):
    tap([i], input[i])

print(len(combinations))