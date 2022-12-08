file = open('input.txt', 'r')
data = file.readlines()

treesHorz = []
treesVert = []
for i in range(len(data[0])-1):
    treesVert.append([])
for i in data:
    line = i.strip()
    treesHorz.append([int(x) for x in line])
    for x in range(len(line)):
        treesVert[x].append(int(i[x]))
length = len(treesHorz)-1   #subtract 1 because every tree on the edges are visible
count = 4*length
scenicScore = 4
for height in range(1,length):
    for width in range(1,length):
        flag = 0
        tree = treesHorz[height][width]
        if tree == 0:
            continue
            #Trees of the lowest height will never be seen from the outside, and will always have a scenic score of 4, which is the default
        sCount = [0, 0, 0, 0]
        
        x = treesHorz[height][:width]
        x.reverse()
        flag2 = 1
        for i in x:
            if flag2:
                sCount[0] += 1
            if (i >= tree):
                flag2 = 0
                continue
            flag = 1
        
        x = treesHorz[height][width+1:]
        flag2 = 1
        for i in x:
            if flag2:
                sCount[1] += 1
            if (i >= tree):
                flag2 = 0
                continue
            flag = 1
        
        x = treesVert[width][:height]
        x.reverse()
        flag2 = 1
        for i in x:
            if flag2:
                sCount[2] += 1
            if (i >= tree):
                flag2 = 0
                continue
            flag = 1
        
        x = treesVert[width][height+1:]
        flag2 = 1
        for i in x:
            if flag2:
                sCount[3] += 1
            if (i >= tree):
                flag2 = 0
                continue
            flag = 1
        
        if flag:
            count += 1
        
        score = sCount[0] * sCount[1] * sCount[2] * sCount[3]
        if score > scenicScore:
            scenicScore = score
print(count)
print(scenicScore)
#For part 1 I initially used a lambda function for each direction (up down left right) instead of the 4 separate for loops above, but changed it once I saw part 2
#When I saw part 2 I didn't read the problem correctly and thought that trees lower than the treehouse could still block other trees from view
#For instance, if the treehouse had a height of 5 and looked at the trees in the following order (2, 3, 2, 2, 5), it would only see 3 trees as the tree in the second position would be blocking the next two
#Upon eventually rereading the problem I realized that all of the trees in that example are visible and I deleted a lot of very bad code that wasn't really working and left the really simple for loops
#My only complaint is that I really don't like using for loops 3 nests deep and that there's for sure a way more efficient strategy of solving this that I can't come up with right now
#I wanna go to bed
