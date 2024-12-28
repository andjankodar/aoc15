input = open("aoc_15_08_1\\input.txt").read().splitlines()
stringCode = 0
stringLiteral = 0

for line in input:
    stringCode += len(line)
    i = 1
    while i < len(line)-1:
        if line[i] == "\\" and line[i+1] == "\"":
            stringLiteral += 1
            i += 2
        elif line[i] == "\\" and line[i+1] == "\\":
            stringLiteral += 1
            i += 2
        elif line[i] == "\\" and line[i+1] == "x":
            stringLiteral += 1
            i += 4
        else:
            stringLiteral += 1
            i+=1

print(stringCode-stringLiteral)