file = open('input.txt', 'r')
data = file.readlines()
from math import lcm

#I really need to find a better way of getting my input
#Gotta look into ways of getting my input as one big string then splitting based on \n\n
#I'm writing this after I've finished the code though so that's not getting done now
monkeys = []
tempItems = []
tempOp = 0
tempOpVal = 0
tempDivVal = 0
tempTMonk = 0
tempFMonk = 0
divs = []
for i in data:
    if i[0] in ["M","\n"]:
        continue
    elif i[2] == "S":
        tempItems = i[18:].strip().split(", ")
        tempItems = [int(item) for item in tempItems]
    elif i[2] == "O":
        tempOp = i[23]
        tempOpVal = i[25:].strip()
    elif i[2] == "T":
        tempDivVal = int(i[21:].strip())
        divs.append(int(i[21:].strip()))
    elif i[7] == "t":
        tempTMonk = int(i[29])
    elif i[7] == "f":
        tempFMonk = int(i[30])
        monkeys.append([tempItems.copy(), tempOp, tempOpVal, tempDivVal, tempTMonk, tempFMonk, 0])

#Finds LCM of all the monkey's divisors
#Absolutely necessary due to how crazy big the numbers get in part 2
mod = divs[0]
for i in divs[1:]:
    mod = lcm(mod, i)

#Set this to 1 for yes, 0 for no
Part1 = 0

rounds = 10000
if Part1:
    rounds = 20

for i in range(rounds):
    for monkey in monkeys:
        monkey[6] += len(monkey[0])
        for item in range(len(monkey[0])):
            #Determines if the value used to alter worry is a number or the worry value itself
            addVal = 0
            if monkey[2][0] == "o":
                addVal = monkey[0][item]
            else:
                addVal = int(monkey[2])
            #Adds or multiplies worry by the above
            if monkey[1] == "*":
                monkey[0][item] = (monkey[0][item] * addVal)
            else:
                monkey[0][item] = (monkey[0][item] + addVal)
            #If part 1, then floor divides worry by 3 so it doesn't get out of hand. This is not part of problem 2, however, and the numbers get so crazy big I had to use lcm of all the divisors
            if Part1:
                monkey[0][item] = monkey[0][item]//3
            else:
                monkey[0][item] = monkey[0][item] % mod
            #appends item to whichever monkey gets the item
            if (monkey[0][item] % monkey[3] == 0):
                monkeys[monkey[4]][0].append(monkey[0][item])
            else:
                monkeys[monkey[5]][0].append(monkey[0][item])
        monkey[0] = []
inspects = []
for monkey in monkeys:
    inspects.append(monkey[6])
inspects.sort(reverse = True)
print(inspects[0]*inspects[1])
