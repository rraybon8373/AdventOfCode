file = open('input.txt', 'r')
data = file.readlines()

if (data[len(data)-1]!="\n"):
    data.append("\n")

max = [0,-1,-2]
count = 0
for i in data:
    if (i=="\n"):
        if (count > max[0]):
            max[2] = max[1]
            max[1] = max[0]
            max[0] = count
        elif (count > max[1]):
            max[2] = max[1]
            max[1] = count
        elif (count > max[2]):
            max[2] = count
        count = 0
    else:
        count += int(i)
print(max[0])
print(max[0]+max[1]+max[2])
