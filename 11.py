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


#with open('input/11.txt') as f:
with open('input/test.txt') as f:
    arr = [[int(z) for z in x[:-1]] for x in f]
    for s in range(100):
        flashes = [[0 for col in range(len(arr[0]))] for row in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                ns = neighbors(i,j,arr)
                if arr[i][j] > 9:
                    flashes[i][j] = 1


print(p1)
print(p2)
