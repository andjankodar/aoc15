import re
input = open("aoc_15_06_2\\input.txt").read().split("\n")
lit = dict()

regex = re.compile("(\\d+)")
for instruction in input:
    sc,sr,ec,er = map(int, regex.findall(instruction))
    if(instruction.startswith("turn on")):
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if (i,j) in lit:
                    lit[(i,j)] += 1
                else:
                   lit[(i,j)] = 1
    elif(instruction.startswith("turn off")):
         for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if (i,j) in lit:
                    lit[(i,j)] = max(0, lit[(i,j)] -1)        
    elif(instruction.startswith("toggle")):
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if (i,j) in lit:
                    lit[(i,j)] += 2
                else:
                   lit[(i,j)] = 2              
print(sum(lit.values()))

