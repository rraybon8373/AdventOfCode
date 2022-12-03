file = open('input.txt', 'r')
data = file.readlines()

#Part 1
sum = 0
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
