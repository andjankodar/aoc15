import re
input = open("aoc_15_21_2\\input.txt").readlines()
shop = open("aoc_15_21_2\\shop.txt").readlines()
bossHP = int(input[0].split()[-1]) 
bossDmg = int(input[1].split()[-1]) 
bossAP = int(input[2].split()[-1])

categories = ["weapons", "armor", "rings"]
items = dict()
items["weapons"] = list()
items["armor"] = list()
items["armor"].append((0,0,0))
items["rings"] = list()
items["rings"].append((0,0,0))
items["rings"].append((0,0,0))

category = 0
for line in shop:
    if line == "\n":
        category += 1
    
    matches = re.findall("(\\d+)", line)

    if len(matches) == 3:
        cost, dmg, ap = map(int, matches)
        items[categories[category]].append((cost, dmg, ap))
    elif len(matches) == 4:
        name, cost, dmg, ap = map(int, matches)
        items[categories[category]].append((cost, dmg, ap))

print(items)

loser = set()

for weapon in items["weapons"]:
    for armor in items["armor"]:
        for i in range(0, len(items["rings"])):
            ring1 = items["rings"][i]           
            for j in range(0, len(items["rings"])):
                if i == j:
                    continue
                ring2 = items["rings"][j]

                cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
                dmg = weapon[1] + armor[1] + ring1[1] + ring2[1]
                ap = weapon[2] + armor[2] + ring1[2] + ring2[2]

                mHP = 100
                bHP = bossHP

                turn = 1
                while mHP > 0 and bHP > 0:
                    if turn % 2 == 0:
                        mHP -= max(1, bossDmg - ap)
                    else:
                        bHP -= max(1, dmg - bossAP)
                    turn += 1
                
                if(bHP > 0):
                    loser.add(cost)
print(max(loser))



    
    

