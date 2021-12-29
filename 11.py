import sys
p1 = 0
p2 = 0

def neighbors(i,j,arr):
     surround = []
     l = (i != 0)
     r = (i != len(arr) -1)
     u = (j != 0)
     d = (j != len(arr[0])-1)

     if l:
         surround.append((i-1,j))
     if r:
         surround.append((i+1,j))
     if u:
         surround.append((i,j-1))
     if d:
         surround.append((i,j+1))
     if l and u:
         surround.append((i-1,j-1))
     if l and d:
         surround.append((i-1,j+1))
     if r and u:
         surround.append((i+1,j-1))
     if r and d:
         surround.append((i+1,j+1))
     return surround

f = sys.stdin.readlines()
arr = [[int(z) for z in x[:-1]] for x in f]
def flash(pair,arr,flashes):
    i,j = pair
    if arr[i][j] > 9:
        if not flashes[i][j]:
            flashes[i][j] = 1
            ns = neighbors(i,j,arr)
            for a,b in ns:
                arr[a][b] += 1
                flash((a,b),arr,flashes)

p2 = 1
while True:
    flashes = [[0 for col in range(len(arr[0]))] for row in range(len(arr))]
    #energy increase
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += 1

    #flashing
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            flash((i,j),arr,flashes)

    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if flashes[i][j] == 1:
                count += 1
                if p2 <= 100:
                    p1 += 1
                arr[i][j] = 0
    if count == len(arr[0])*len(arr):
        break
    p2 += 1

print(p1)
print(p2)
