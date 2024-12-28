input = open("aoc_15_08_2\\input.txt").read().splitlines()
stringCode = 0
original = 0

for line in input:
    i = 1
    stringCode += len(line) + 4
    original += len(line)
    while i < len(line)-1:
        if line[i] == "\\" and line[i+1] == "\"":
            stringCode += 2           
            i += 2
        elif line[i] == "\\" and line[i+1] == "\\":
            stringCode += 2            
            i += 2
        elif line[i] == "\\" and line[i+1] == "x":
            stringCode += 1           
            i += 4
        else:
            i+=1

print(stringCode-original)