input = open("aoc_15_05_2\input.txt").readlines()
nice = 0

for line in input:
    repeats = False
    hasPairs = False
    pairs = dict()

    for i in range(1, len(line)-1):
        pair = str(line[i-1] + line[i])
        
        if pair in pairs:
            pairs[pair].add(i-1)
            pairs[pair].add(i)
        else:
            pairs[pair] = set()
            pairs[pair].add(i-1)
            pairs[pair].add(i)
        
        if(i > 1 and line[i] == line[i-2]):
            repeats = True
    
    for key in pairs.keys():        
        if (len(pairs[key]) >= 4):
            hasPairs = True
    
    if(hasPairs and repeats):
        nice +=1

print(nice) 
