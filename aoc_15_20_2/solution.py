input = int(open("aoc_15_20_2\\input.txt").readline())
target = int(input)
visits = [0] * target

for elf in range(target, 1, -1):
    for house in range(elf, target, elf):
        if house / elf <= 50:            
            visits[house] += elf * 11
            if visits[house] >= target:
                end = house
                break

print(end)