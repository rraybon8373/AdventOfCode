import re
file = open('input.txt', 'r')
data = file.readlines()

overlaptotal = 0
overlappartial = 0
for i in data:
    nums = re.split(',|-|\n',i)
    min1 = int(nums[0])
    max1 = int(nums[1])
    min2 = int(nums[2])
    max2 = int(nums[3])
    if((min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1)):
        overlaptotal += 1
    #Took me way longer than needed to solve part two because one of these if statements below were comparing max1 and min1 instead of max1 and min2
    if ((min1 >= min2 and min1 <= max2) or (max1 >= min2 and max1 <= max2) or (min2 >= min1 and min2 <= max1) or (max2 >= min1 and max2 <= max1)):
        overlappartial += 1
print(overlaptotal)
print(overlappartial)
