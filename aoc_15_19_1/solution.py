import re
input = open("aoc_15_19_1\\input.txt").readlines()
medicine = input[-1]
replacements = {}

for i in range(0, len(input) - 2):
    parts = input[i].split()
    
    if parts[0] in replacements.keys():
        replacements[parts[0]].append(parts[2])
    else:
        replacements[parts[0]] = [parts[2]]
        

matches = re.findall("([A-Z][a-z]?|e?)", medicine)
molecules = set()

for i in range(0, len(matches)):
    match = matches[i]
    
    if match not in replacements.keys():
        continue     

    for replacement in replacements[match]:
        copy = matches.copy()
        copy[i] = replacement
        molecules.add(''.join(copy))

print(len(molecules))