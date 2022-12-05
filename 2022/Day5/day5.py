file = open('input.txt', 'r')
data = file.readlines()

part1stacks = []
iters = len(data[0])//4
for i in range(iters):
    part1stacks.append([])
flag = 0
for i in data:
    if (len(i)>1):
        if (i[1].isnumeric()):
            flag = 1
            part2stacks = [x[:] for x in part1stacks]
    if (i[0]=="\n"):
        flag = 1
    if (i[0]=="m"):
        flag = 2
    for r in range(iters):
        if (flag==0):
            c = i[4*r+1]
            if (c!=" "):
                part1stacks[r].append(c)
    if(flag==2):
        ins = i.replace("move ","").replace(" from","").replace(" to","").replace("\n","").split(" ")
        for count in range(int(ins[0])):
            part1stacks[int(ins[2])-1].insert(0,part1stacks[int(ins[1])-1].pop(0))
        for count in range(int(ins[0]),0,-1):
            part2stacks[int(ins[2])-1].insert(0,part2stacks[int(ins[1])-1].pop(count-1))
for i in range(iters):
    print(part1stacks[i][0], end = "")
print()
for i in range(iters):
    print(part2stacks[i][0], end = "")
