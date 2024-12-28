
input = open("aoc_15_11_2\\input.txt").read()
password = [ord(char) for char in input]
valid = False

while(not valid):
    for i in range(7, -1, -1):
        password[i] = password[i] + 1
        
        if password[i] > ord('z'):
            password[i] = ord('a')            
        else:            
            break
       
    validLetters = True
    for char in password:
        if char == ord('i') or char == ord('o') or char == ord('l'):
            validLetters = False
            break

    hasSequence = False
    for i in range(0, len(password) - 2):
        if password[i+1] == password[i] +1 and password[i+2] == password[i] + 2:
            hasSequence = True
            break

    doubles = set()
    for i in range(0, len(password) - 1):
        if password[i] == password[i+1]:
            doubles.add(password[i])
    
    valid = validLetters and hasSequence and len(doubles) >= 2

print("".join([chr(unic) for unic in password]))

        
    

            
    

    