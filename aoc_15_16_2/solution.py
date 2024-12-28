import re
input = open("aoc_15_16_2\\input.txt").readlines()

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
        if actualProps[i] == 'cats' or actualProps[i] == 'trees':
            realSue = realSue and (int(values[i+1]) > expectedProps[actualProps[i]])            
        elif (actualProps[i] == 'pomeranians' or actualProps[i] == 'goldfish'):
            realSue = realSue and (expectedProps[actualProps[i]] > int(values[i+1]))            
        elif expectedProps[actualProps[i]] != int(values[i+1]):
            realSue = realSue and False            

    if realSue:
        print(sue)