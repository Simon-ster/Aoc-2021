p1 = 0
p2 = 0


def neighbors(i,j,arr):
    surround = []
    if i != 0:
        surround.append((i-1,j))
    if i != len(arr)-1:
        surround.append((i+1,j))
    if j != 0:
        surround.append((i,j-1))
    if j != len(arr[0])-1:
        surround.append((i,j+1))
    return surround

def pathfinder(i,j,arr):
    points = []
    points.append((i,j))
    for (x,y) in neighbors(i,j,arr):
        if arr[i][j] < arr[x][y]:
            if arr[x][y] < 9:
                for b in pathfinder(x,y,arr):
                    #print(b)
                    points.append(b)
    return set(points)

#with open('input/test.txt') as f:
with open('input/9.txt') as f:
    arr = [[int(z) for z in x[:-1]] for x in f]
    lows = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            surround = neighbors(i,j,arr)
            if arr[i][j] < min([arr[a][b] for (a,b) in surround]):
                lows.append((i,j))
                p1 += arr[i][j] + 1

    szs = []
    for (x,y) in lows:
        szs.append(len(pathfinder(x,y,arr)))
    szs = sorted(szs,reverse=True)
    p2 = szs[0]*szs[1]*szs[2]

print(p1)
print(p2)
