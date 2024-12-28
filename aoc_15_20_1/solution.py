input = int(open("aoc_15_20_1\\input.txt").readline())
target = int(input/10)
visits = [0] * target

for elf in range(target, 1, -1):
    for house in range(elf, target, elf):
        visits[house] += elf
        if visits[house] >= target:
            end = house
            break

print(end)