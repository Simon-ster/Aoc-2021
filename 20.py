import sys
p1 = 0
p2 = 0

f = sys.stdin.readlines()

algo = f[0]

arr = [list(line.strip()) for line in f[2:]]


mapping = {'#':'1',
        '.':'0'}

def convert(inp):
    str = ""
    for i in inp:
        str += mapping[i]
    return int(str,2)

def getstr(i,j,arr):
    str = ""
    for a in range(-1,2):
        for b in range(-1,2):
            str += arr[i+a][j+b]
    return str

iterations = 50
buf = 2
ins = ''
for s in range(iterations):
    if s % 2:
        ins = '#'
    else:
        ins = '.'

    for i in range(buf):
        arr.insert(0,list(ins*(len(arr[0]))))
        arr.append(list(ins*(len(arr[0]))))
    for i in range(len(arr)):
        for j in range(buf):
            arr[i].insert(0,ins)
            arr[i].append(ins)

    newarr = []
    for i in range(len(arr)):
        newarr.append([])
        for j in range(len(arr[i])):
            newarr[i].append('.')

    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            str = getstr(i,j,arr)
            newarr[i][j] = algo[convert(str)]
    arr = newarr
    arr.pop(0)
    arr.pop(-1)
    for line in range(len(arr)):
        arr[line] = arr[line][1:-1]

    if s == 2:
        p1 = sum([1 for i in range(len(arr)) for j in range(len(arr[i])) if arr[i][j] == '#'])
p2 = sum([1 for i in range(len(arr)) for j in range(len(arr[i])) if arr[i][j] == '#'])
print(p1)
print(p2)
