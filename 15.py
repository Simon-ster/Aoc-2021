import sys
from copy import deepcopy
import heapq as hq
p1 = 0
p2 = 0

f = sys.stdin.readlines()
arr = [[int(z) for z in x[:-1]] for x in f]
#print(arr)

dists = [[float('inf') for z in arr[0]] for x in arr]
dists[0][0] = 0

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

def dijkstras(arr,dists):
    unvisited = []
    final = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            final += 1
            #unvisited.add((x,y))

    unvisited.append((0,(0,0)))
    hq.heapify(unvisited)
    visited = set()
    uv = set()
    uv.add((0,0))
    inc = 0
    #while inc < 10:
    while unvisited:
        #print(unvisited)
        #print(visited)
        inc += 1
        #print(unvisited)
        #print(visited)
        (d,(i,j)) = hq.heappop(unvisited)
        uv.remove((i,j))

        #print(current)
        #print(unvisited)
        #print(len(visited) - final)
        ns = neighbors(i,j,arr)
        #print(ns)
        node = deepcopy((i,j))
        visited.add(node)
        for (a,b) in ns:
            if (a,b) not in visited:
                d = deepcopy(dists[a][b])
                if dists[a][b] > dists[i][j] + arr[a][b]:
                    dists[a][b] = dists[i][j] + arr[a][b]
                    d = deepcopy(dists[a][b])
                if (a,b) not in uv:
                    hq.heappush(unvisited,(d,(a,b)))
                    uv.add((a,b))
    return dists[-1][-1]


dists2 = [[float('inf') for x in range(len(arr)*5)] for y in range(len(arr[0])*5)]
arr2 = [[0 for x in range(len(arr)*5)] for y in range(len(arr[0])*5)]
dists2[0][0] = 0

for b in range(5):
    for a in range(5):
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                v = arr[x][y]
                nv = (v+a+b-1) % 9 + 1
                #print(x+(a*10),y+(b*10))
                arr2[x+(a*len(arr[0]))][y+(b*len(arr))] = nv

print(dijkstras(arr,dists))
print(dijkstras(arr2,dists2))
