input = open("aoc_15_10_1\\input.txt").read()
cache = dict()

def look_and_see(input, depth):
    if depth == 40:
        return len(input)
    
    if input in cache.keys():
        return cache[input]

    expanded = ""
    sequence = input[0]
    
    for i in range(1, len(input)):  
        if input[i] != input[i-1]:
            expanded += str(len(sequence)) + str(sequence[0])
            sequence = input[i]
        else:
            sequence += input[i]
    expanded += str(len(sequence)) + str(sequence[0])
    
    length = look_and_see(expanded, depth+1)

    cache[input] = length
    return length

length = look_and_see(input, 0)
print(length)

