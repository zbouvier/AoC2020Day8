
vals = {}
def rebuild():
    startingPoint = 0
    for context in open("input.txt").read().rstrip().split('\n'):
        if(context[0:3] == "jmp"):
            vals[startingPoint] = [context[0:3], int(context[4:].replace("+","")), False, "nop", False]
        else:
            vals[startingPoint] = [context[0:3], int(context[4:].replace("+","")), False, "jmp", False]
        startingPoint+=1

def part1():
    rebuild()
    accumulator = 0
    thing=0
    while vals[thing][2] == False:
        if vals[thing][0] == "nop":
            vals[thing][2] = True
            thing+=1
        elif vals[thing][0] == "acc":
            accumulator+= vals[thing][1]
            vals[thing][2] = True
            thing+=1
        elif vals[thing][0] == "jmp":
            vals[thing][2] = True
            thing+=(vals[thing][1])
    return accumulator

def part2(vals):
    #rebuild()
    accumulator = 0
    thing=0
    #print(len(vals))
    if(thing < len(vals)):
        while thing < len(vals) and vals[thing][2] == False:
            if vals[thing][0] == "nop":
                vals[thing][2] = True
                thing+=1
            elif vals[thing][0] == "acc":
                accumulator+= vals[thing][1]
                vals[thing][2] = True
                thing+=1
            elif vals[thing][0] == "jmp":
                vals[thing][2] = True
                thing+=(vals[thing][1])
        if(thing == len(vals)):
            return accumulator
        else:
            return -1
    else:
        return -1


print(part1())
x = part2(vals)
current = 0
while(x == -1):
    
    if(current == len(vals)):
        break
    if vals[current][0] == "jmp":
        rebuild()
        tempVals = vals
        tempVals[current] = ['nop', tempVals[current][1], tempVals[current][2], tempVals[current][3]]
        print(f"trying: {tempVals}")
        x = part2(tempVals)
    elif vals[current][0] == "nop":
        rebuild()
        tempVals = vals
        tempVals[current] = ['jmp', tempVals[current][1], tempVals[current][2], tempVals[current][3]]
        print(f"trying: {tempVals}")
        x = part2(tempVals)
    else:
        rebuild()
    current+=1
    print("------")
print(x)


