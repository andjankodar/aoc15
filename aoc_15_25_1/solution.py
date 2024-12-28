import re
input = open("aoc_15_25_1\\input.txt").read()
row, col = map(int, re.findall("(\\d+)", input))

currentValue = 20151125 
#number of repetitions of the alfgorithm. A line between ro x and col x has x items.
# To hit row, col on that line we need to start from row = target col + target row then deduct rows
iterations = sum(range(1, col + row))-row   

for i in range(0, iterations):
    currentValue = (currentValue * 252533) % 33554393
print(currentValue)
# while True:
#     i+=1
#     if cr == 0:
#         cr = cc + 1
#         cc = 0
#     else:
#         cr -= 1
#         cc += 1

#     currentValue = (currentValue * 252533) % 33554393

#     if cr == row:
#         if cc == col:
#             print(currentValue)
#             print(i)
#             break





iterations = 18168396
print(iterations)







