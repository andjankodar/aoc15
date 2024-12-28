presents = open("input.txt").read().split("\n")
ribbon = 0
for present in presents:
    l, w, h = map(int, present.split('x'))
    ribbon +=  min(2*l+2*h, min(2*l + 2*w, 2*h + 2*w)) + l*w*h
print(ribbon)
