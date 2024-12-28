import re

input = open("aoc_15_07_1\\input.txt").read().splitlines()
signals = dict()

def is_string_an_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
while(len(input) > 0):
    for i in range(0, len(input)):      
        parts = input[i].split()

        if parts[len(parts)-1] in signals.keys():
            continue

        if len(parts) == 3:
            if is_string_an_int(parts[0]):
                signals[parts[2]] = int(parts[0])
                input.remove(input[i])
                break
            elif parts[0] in signals.keys():
                signals[parts[2]] = signals[parts[0]]   
                input.remove(input[i])
                break  
        elif len(parts) == 4:
            if parts[1] in signals.keys():
                signals[parts[3]] = 65535 + ~signals[parts[1]] + 1
                input.remove(input[i])
                break
            elif is_string_an_int(parts[1]):
                signals[parts[3]] = 65535 + ~int([parts[1]]) + 1
                input.remove(input[i])
                break
        elif len(parts) == 5:
            x = None
            y = None
            if parts[0] in signals.keys():
                x = signals[parts[0]]
            elif is_string_an_int(parts[0]):
                x = int(parts[0])
            if parts[2] in signals.keys():
                y = signals[parts[2]]
            elif is_string_an_int(parts[2]):
                y = int(parts[2])
            
            if x != None and y != None:
                if parts[1] == 'OR':
                    signals[parts[4]] = x | y
                    input.remove(input[i])
                    break
                elif parts[1] == 'AND':
                    signals[parts[4]] = x & y
                    input.remove(input[i])
                    break
                elif parts[1] == 'RSHIFT':
                    signals[parts[4]] = x >> y
                    input.remove(input[i])
                    break
                elif parts[1] == 'LSHIFT':
                    signals[parts[4]] = x << y
                    input.remove(input[i])
                    break
        else:
            print("wrong length")

print(signals["a"])

        

