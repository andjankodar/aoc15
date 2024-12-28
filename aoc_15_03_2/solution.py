input = open("input.txt").read()
visited = set()
cr, cc = 0, 0
visited.add((cr, cc))
for i in range(0, len(input)-1, 2):
    if input[i] == '^':
        cr = cr-1
    elif input[i] == '>':
        cc = cc+1
    elif input[i] == 'v':
        cr = cr+1
    elif input[i] == '<':
        cc = cc-1    
    visited.add((cr, cc))

cr, cc = 0, 0
for i in range(1, len(input)-1, 2):
    if input[i] == '^':
        cr = cr-1
    elif input[i] == '>':
        cc = cc+1
    elif input[i] == 'v':
        cr = cr+1
    elif input[i] == '<':
        cc = cc-1    
    visited.add((cr, cc))

print(len(visited))
