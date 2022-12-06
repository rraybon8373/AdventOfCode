file = open('input.txt', 'r')
data = file.readlines()

flag1 = 0
flag2 = 0
for i in range(len(data[0])-3):
    if(len(set(data[0][i:i+4]))==4) and not flag1:
        print(i+4)
        flag1 = 1
    if(len(set(data[0][i:i+14]))==14) and not flag2:
        print(i+14)
        flag2 = 1
    if (flag1 and flag2):
        break
    #For part 1 I initially had 4 IF statements joined by AND statements that were something along the line of
    #if data[i] in data[i+1:i+4]
    #Part 2 makes you search for 14 unique characters in a row and luckily I didn't want to bother writing 14 IF statements
    #Bless sets for only keeping unique values
