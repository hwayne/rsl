from sys import argv, stdout

if len(argv) > 1:
    dump = "".join(file(argv[1]).readlines()).strip()
    command = reduce(lambda x,y: x+y, dump)
else:  
    command = raw_input()

REGLENGTH = 300
registry = [[0]*REGLENGTH]
pos = 0
regpos = [0]
nowreg = 0

jumpbacks = []

nowcommand = 0
while True:
    letter = command[nowcommand]
    if letter == "+":
        registry[nowreg][pos] += 1
    elif letter == "-":
        registry[nowreg][pos] -= 1
    elif letter == ">":
        if pos < REGLENGTH: pos += 1
        else: 
            print "Exceeding Registry Dimensions"
            #return 2
    elif letter == "<":
        if pos > 0: pos -= 1
        else: 
            print "Exceeding Registry Dimensions"
            #return 2
    elif letter == "[":
        if registry[nowreg][pos] == 0:
            nests = 1
            while nests:
                nowcommand += 1
                if command[nowcommand] == "[": nests += 1
                elif command[nowcommand] == "]": nests -= 1
        else: jumpbacks.append(nowcommand-1)
    elif letter == "]":
        nowcommand = jumpbacks.pop()
    elif letter == ".":
        stdout.write( unichr(registry[nowreg][pos]))
    elif letter == ",":
        registry[nowreg][pos] = int( raw_input())
    elif letter == "*":
        regpos.append(0)
        registry.append([0]*REGLENGTH)
    elif letter == "^":
        regpos[nowreg] = pos
        pos = regpos[(nowreg + 1)%len(registry)]
        nowreg = (nowreg + 1)%len(registry)
    elif letter == "!": #Speak your heart!
        stdout.write(str(registry[nowreg][pos]))
    nowcommand += 1
    if nowcommand >= len(command): break
