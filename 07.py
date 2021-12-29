import sys

p1 = 0
p2 = 0

def norm_t(x,l):
    return triangular_number(abs(x-l))

def norm(x,l):
    return abs(x-l)

def triangular_number(n):
    n *= (n+1)/2
    #for i in range(n):
    #   n += i
    return n


sums1 = []
sums2 = []
#terrible terrible terrible solution:
#O(n^3) lul
#fixed! use known solution for sums instead of recalculating dummy

f = list(sys.stdin.readlines())
crabs = [[int(x) for x in vals.split(',')] for vals in f][0]
for i in range(max(crabs)):
    sums1.append(0)
    sums2.append(0)
    for j in range(len(crabs)):
        sums1[i] += norm(crabs[j],i)
        sums2[i] += int(norm_t(crabs[j],i))

p1 = min(sums1)
p2 = min(sums2)






print(p1)
print(p2)
