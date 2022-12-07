file = open('input.txt', 'r')
data = file.readlines()

files = {}
directories = set()
cwd = []

for i in data:
    if i[0] == "$":
        if i[2] == "c":
            if (i[5]=="/"):
                cwd = []
            elif (i[5]=="."):
                cwd = cwd[:-1]
            else:
                cwd.append(i[5:].strip())
    else:
        data = i.strip().split(" ")
        if not (data[0] == "dir"):
            #Converts cwd (list of directories (a, b, c) to string with / as separator, plus adds filename at end
            file = "/".join(cwd + [data[1]])
            files[file] = int(data[0])
    directories.add("/".join(cwd))

totalSize = 0
dsizes = {}
for d in directories:
    dsize = 0
    for f in files:
        if f[:len(d)] == d:
            dsize += files[f]
    if dsize <= 100000:
        totalSize += dsize
    dsizes[d] = dsize
print(totalSize)
minSize = 30000000 - 70000000+dsizes['']
print(min(list(filter(lambda x: x > minSize,dsizes.values()))))
#What this does is takes the list of each directory size, filters based on if it's greater than the minimum size needed, then finds the minimum of that filtered list

#Today was a real leap in difficulty from the previous days, it scares me for what the future will bring
