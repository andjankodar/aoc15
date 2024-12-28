input = open("aoc_15_05_1\input.txt").readlines()
nice = 0
for line in input:
    vowels = 0
    doubles = 0
    naughty = False

    for n in {"ab", "cd", "pq", "xy"}:
        if(n in line):
            naughty = True

    if naughty:
        continue             

    for i in range(0, len(line)-1):
        if(i > 0 and line[i] == line[i-1]):
            doubles += 1
        if(line[i] in "aeiou"):
            vowels += 1 
        if(vowels >= 3 and doubles >= 1):
            nice +=1
            break

print(nice) 
