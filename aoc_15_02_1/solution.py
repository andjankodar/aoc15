presents = open('input.txt').read().split('\n')
totalPaper = 0

for present in presents:
    l, w, h = map(int, present.split('x'))
    sides = [l*w, w*h, h*l]
    totalPaper += 2*sum(sides) + min(sides)

print(totalPaper)
