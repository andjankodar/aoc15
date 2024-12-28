input = open('input.txt').read()
up, down = input.count('('), input.count(')')
print(up - down)