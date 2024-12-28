input = open("aoc_15_13_2\\input.txt").read().splitlines()
happinessDict = dict()
happiest = 0
seating = None

def evaluate_seating(seated, happiness):
    global happinessDict
    global happiest
    global seating

    if(len(seated) == len(happinessDict.keys())):
        for guest in happinessDict[seated[0]]:
            if guest[0] == seated[-1]:
                happiness += guest[1]
        for guest in happinessDict[seated[-1]]:
            if guest[0] == seated[0]:
                happiness += guest[1]
        if(happiest < happiness):
            happiest = happiness
            seating = seated
        return
    
    for guest in [guest for guest in happinessDict[seated[-1]] if guest[0] not in seated]:
        copy = seated.copy()
        copy.append(guest[0])
        change = guest[1]
        
        for person in happinessDict[guest[0]]:
            if person[0] == seated[-1]:
                change += person[1]

        evaluate_seating(copy, happiness + change)


for line in input:
    parts = line.split()
    person = parts[0]
    neighbor = parts[-1].strip('.')
    change = int(parts[3])

    if parts[2] == 'lose':
        change = -change

    if person in happinessDict.keys():
        happinessDict[person].append((neighbor, change))
    else:
        happinessDict[person] = [(neighbor, change)]

happinessDict['me'] = []

for guest in happinessDict.keys():    
    happinessDict[guest].append(('me', 0))
    happinessDict['me'].append((guest, 0))

for guest in happinessDict.keys():    
    evaluate_seating([guest], 0)
print(seating)
print(happiest)
