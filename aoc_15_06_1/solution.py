import re
input = open("aoc_15_06_1\\input.txt").read().split("\n")
lit = set()
regex = re.compile("(\\d+)")
for instruction in input:
    sc,sr,ec,er = map(int, regex.findall(instruction))
    if(instruction.startswith("turn on")):
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                lit.add((i,j))
    elif(instruction.startswith("turn off")):
         for i in range(sr, er+1):
            for j in range(sc, ec+1):
                lit.discard((i,j))
    elif(instruction.startswith("toggle")):
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if (i,j) in lit:
                    lit.discard((i,j))
                else:
                    lit.add((i,j))                
print(len(lit))
