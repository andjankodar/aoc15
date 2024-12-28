import re
input = open("aoc_15_19_2\\input.txt").readlines()
medicine = input[-1]
replacements = dict()

def count_str(s, x):
    count = 0
    index = s.find(x)
    while index != -1:
        count += 1
        index = s.find(x, index + 1)
    return count


count = 0
for c in medicine:
    if c.isupper():
        count += 1

count -= count_str(medicine, "Rn")
count -= count_str(medicine, "Ar")
count -= 2 * count_str(medicine, "Y")
count -= 1

print(count)
