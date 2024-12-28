import hashlib
input = open("aoc_15_04_1\input.txt").read()
seed = 0
while not hashlib.md5((input+str(seed)).encode('utf-8')).hexdigest().startswith('00000'):
    seed += 1

print(input+str(seed))