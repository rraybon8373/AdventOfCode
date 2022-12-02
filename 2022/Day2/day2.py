file = open('input.txt', 'r')
data = file.readlines()

p1Score = 0
p2Score = 0
for i in data:
    a = ord(i[0]) - ord('A')
    b = ord(i[2]) - ord('X')
    #Part1
    if (a==b):
        p1Score += 3
    elif (a==b-1 or a == b+2):
        p1Score += 6
    p1Score += b+1
    #Part2
    if (b==0):
        p2Score += (a+2)%3 + 1
    elif (b==1):
        p2Score += a+1
    elif (b==2):
        p2Score += (a+1)%3 + 1
    p2Score += b*3
print(p1Score)
print(p2Score)
