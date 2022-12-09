file = open('input.txt', 'r')
data = file.readlines()

pos = [0, 0]
dimx = [0, 0]
dimy = [0, 0]
for i in data:
    line = i.strip().split(" ")
    direction = line[0]
    steps = int(line[1])
    if (direction == "L"):
        pos[0] -= steps
        if pos[0] < dimx[0]:
            dimx[0] = pos[0]
    if (direction == "R"):
        pos[0] += steps
        if pos[0] > dimx[1]:
            dimx[1] = pos[0]
    if (direction == "U"):
        pos[1] += steps
        if pos[1] > dimy[1]:
            dimy[1] = pos[1]
    if (direction == "D"):
        pos[1] -= steps
        if pos[1] < dimy[0]:
            dimy[0] = pos[1]
xSize = dimx[1] - dimx[0] + 1
ySize = dimy[1] - dimy[0] + 1

#I don't like doing this
#I'm going to use a 2d array, with the first index being x and the second being y
#This could probably be made better by just doing something along the lines of storing the tail nodes positions in a set or something then printing the length of it
#Not sure what part 2 is yet though and that scares me so I'm going with this for now
field = []
temp = []
for a in range(ySize):
    temp.append(".")
for a in range(xSize):
    field.append(temp.copy())

#Nested for loops again.... not sure of a way around it yet, but will probably have to figure that out later
#PART 2 SUCKS AAAA

#Just change this variable to solve for part 1 or part 2 (set to 2/10, respectively)
NumNodes = 10
pos = []
for a in range(NumNodes):
    pos.append([-dimx[0],-dimy[0]])
#Originally I had headpos and tailpos, both being lists of size 2
#Because of part 2 I had to change my method to a list of those coordinate lists
for i in data:
    line = i.strip().split(" ")
    direction = line[0]
    steps = int(line[1])
    for step in range(steps):
        if (direction == "L"):
            pos[0][0] -= 1
        if (direction == "R"):
            pos[0][0] += 1
        if (direction == "U"):
            pos[0][1] += 1
        if (direction == "D"):
            pos[0][1] -= 1
        #This for loop didn't exist at first cause I only had one node movement I needed to keep track of
        #Don't feel like editing the comments below this to accomodate the new strategy I just want bed
        for node in range(NumNodes-1):
            #Head and tail within range of each other
            xDiff = pos[node][0] - pos[node+1][0]
            yDiff = pos[node][1] - pos[node+1][1]
            if abs(xDiff) <= 1 and abs(yDiff) <= 1:
                #In theory this should skip if the tail doesn't need to be moved
                continue
            #Head and tail in same x coord
            elif not yDiff:
                pos[node+1][0] += xDiff//2
            #Head and tail in same y coord
            elif not xDiff:
                pos[node+1][1] += yDiff//2
            #Head and tail in the funky position
            else:
                #Originally in this part I had an if-else based on which axis the head node was farther away from the tail node, but due to part 2 introducing the case of having a node be 2 columns and rows away simultaneously I figured out I didn't need to do it that way
                pos[node+1][0] += xDiff//abs(xDiff)
                pos[node+1][1] += yDiff//abs(yDiff)
        field[pos[NumNodes-1][0]][pos[NumNodes-1][1]] = "#"
count = 0
for a in field:
    for b in a:
        if b == "#":
            count += 1
print(count)
