import re
import json
input = open("aoc_15_12_2\\input.txt").read()
data = json.loads(input)

def sumValues(obj):
    global all
    
    if isinstance(obj, dict):
        if "red" in obj.values():
            return
        for val in obj.values():
            sumValues(val)
    elif isinstance(obj, list):
        for val in obj:
            sumValues(val)
    else:
        all += sum([int(val) for val in re.findall("(-*\d+)", str(obj))])

all = 0

for item in data:
    sumValues(item)

print(all)