import re
input = open("aoc_15_16_1\\input.txt").readlines()

expectedProps = dict()
expectedProps["children"] = 3
expectedProps["cats"] = 7
expectedProps["samoyeds"] = 2
expectedProps["pomeranians"] = 3
expectedProps["akitas"] = 0
expectedProps["vizslas"] = 0
expectedProps["goldfish"] = 5
expectedProps["trees"] = 3
expectedProps["cars"] = 2
expectedProps["perfumes"] = 1

for i in range(0, len(input)):
    sue = i+1
    actualProps = re.findall("([a-z]+):", input[i])
    values = re.findall("(\\d+)", input[i])
    realSue = True
    
    for i in range(0, len(actualProps)):
        if expectedProps[actualProps[i]] != int(values[i+1]):
            realSue = False
            break

    if realSue:
        print(sue)