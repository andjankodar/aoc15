import hashlib
input = open("aoc_15_04_2\input.txt").read()
seed = 0
while not hashlib.md5((input+str(seed)).encode('utf-8')).hexdigest().startswith('000000'):
    seed += 1

print(input+str(seed))