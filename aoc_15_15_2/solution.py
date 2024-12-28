import re
input = open("aoc_15_15_2\\input.txt").readlines()
ingredients = list()

for line in input:
    name = line.split()[0]
    capacity, durability, flavor, texture, calories = map(int, re.findall("(-*\\d+)", line))
    ingredients.append((capacity, durability, flavor, texture, calories))

score = 0

for i in range(0, 101):
    for j in range(0, 101-i):
        for k in range(0, 101-i-j):
            l = 100 - i - j - k
            capacity = max(0,ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k + ingredients[3][0] * l)
            durability = max(0,ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k + ingredients[3][1] * l)
            flavor = max(0,ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k + ingredients[3][2] * l)
            texture = max(0,ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k + ingredients[3][3] * l)
            calories = max(0,ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k + ingredients[3][4] * l)

            if calories != 500:
                continue
            
            total = capacity * durability * flavor * texture

            if total > score:
                score = total

print(score)




