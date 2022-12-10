file = open('input.txt', 'r')
data = file.readlines()

stops = [20, 60, 100, 140, 180, 220]

x = 1
cycle = 0
total = 0

grid = []
temp = []
for a in range(40):
    temp.append(".")
for a in range(6):
    grid.append(temp.copy())

def myFun():
    #I didn't want to write this chunk of code twice due to Part 2
    #It was fine in part when when it was just cycle++ and if cycle in stops
    global cycle, total
    
    if abs(x - cycle%40)<=1:
        grid[cycle//40][cycle%40] = "#"
    cycle += 1
    if cycle in stops:
        total += cycle * x

for i in data:
    myFun()
    if (i[0] == "n"):
        continue
    v = int(i.strip().split(" ")[1])
    myFun()
    x += v
print(total)
for i in grid:
    print(i)

#Got part 1 in 8 minutes, part 2 in 16 minutes so overall 24 minutes spent on this problem, pretty proud
#For anyone curious who doesn't want to bother running the code, the visible output was RLEZFLGE
#This was surprisingly easy and that terrifies me, what hell awaits me later in the month
