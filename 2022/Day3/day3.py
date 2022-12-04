file = open('input.txt', 'r')
data = file.readlines()

#Part 1
'''sum = 0
for i in data:
    flag = 0
    for j in range(int(len(i)/2)):
        if(flag==1):
            break
        for k in range(int(len(i)/2)):
            if(i[j]==i[k+int(len(i)/2)]):
                a=ord(i[j]) - ord('A')+1
                if (a > 26):
                    a -= (ord('a')-ord('A'))
                else:
                    a += 26
                sum+=a
                flag = 1
                break
print(sum)

#Part2
sum=0
for i in range(int(len(data)/3)):
    flag = 0
    for j in range(int(len(data[3*i]))):
        if(flag==1):
            break
        for k in range(int(len(data[3*i+1]))):
            if(flag==1):
                break
            for l in range(int(len(data[3*i+2]))):
                if(data[3*i][j]==data[3*i+1][k] and data[3*i+1][k]==data[3*i+2][l]):
                    a=ord(data[3*i][j]) - ord('A')+1
                    if (a > 26):
                        a -= (ord('a')-ord('A'))
                    else:
                        a += 26
                    sum+=a
                    flag = 1
                    break
print(sum)
#Not the most efficient solution, but it worked for what was given'''

#The old solutions were really inefficient but I was tired and wanted to go to bed
#I was thinking over the problem after I woke up and decided to try to use an intersect method to solve it more efficienty, which ended up working

#Part 1
sum = 0
for i in data:
    c=set(i[:int(len(i)/2)]).intersection(i[int(len(i)/2):])
    a=ord(list(c)[0]) - ord('A')+1
    if (a > 26):
        a -= (ord('a')-ord('A'))
    else:
        a += 26
    sum+=a
print(sum)

#Part 2
sum = 0
for i in range(int(len(data)/3)):
    c=set(data[3*i]).intersection(data[3*i+1],data[3*i+2])
    c.remove('\n')
    a=ord(list(c)[0]) - ord('A')+1
    if (a > 26):
        a -= (ord('a')-ord('A'))
    else:
        a += 26
    sum+=a
print(sum)
#Part 2 in particular I was really unhappy with the way I left it
