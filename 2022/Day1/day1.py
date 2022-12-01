file = open('input.txt', 'r')
data = file.readlines()

if (data[len(data)-1]!="\n"):
    data.append("\n")

loop = 0
max1,max2,max3 = 0,-1,-2
count = 0
for i in data:
    loop += 1
    if (i=="\n"):
        if (count > max1):
            max3 = max2
            max2 = max1
            max1 = count
        elif (count > max2):
            max3 = max2
            max2 = count
        elif (count > max3):
            max3 = count
        count = 0
    else:
        count += int(i)
print(max1)
print(max1+max2+max3)
