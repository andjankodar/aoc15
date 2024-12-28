import re
input = open("aoc_15_12_1\\input.txt").read()

print(sum([int(val) for val in re.findall("(-*\d+)", input)]))