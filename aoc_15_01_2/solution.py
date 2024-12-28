input = open('input.txt').read()
up, down = 0, 0
i = 1
for c in input:
    if c == '(':
        up += 1
    elif c == ')':
        down += 1
    if(down > up):
        print(i)
        break
    i += 1
