input = open("aoc_15_23_1\\input.txt").read().splitlines()
a = 0
b = 0
i = 0

while i < len(input):    
    instruction = input[i].split()[0]

    if instruction == 'hlf':
        register = input[i].split()[1]
        if register == 'a':
            a = a // 2
        else:
            b = b // 2
        i += 1
    elif instruction == 'tpl':
        register = input[i].split()[1]
        if register == 'a':
            a = a * 3
        else:
            b = b * 3
        i += 1
    elif instruction == 'inc':
        register = input[i].split()[1]
        if register == 'a':
            a += 1
        else:
            b += 1
        i += 1
    elif instruction == 'jmp':
        offset = int(input[i].split()[1])
        i += offset
    elif instruction == 'jie':
        register = input[i].split()[1][0]
        offset = int(input[i].split()[2])
        
        if register == 'a' and a % 2 == 0:
            i += offset
        elif register == 'b' and b % 2 == 0:
            i += offset
        else:
            i += 1
    elif instruction == 'jio':
        register = input[i].split()[1][0]
        offset = int(input[i].split()[2])
        
        if register == 'a' and a == 1:
            i += offset
        elif register == 'b' and b == 1:
            i += offset
        else:
            i += 1

print(b)
