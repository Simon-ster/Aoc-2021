p1 = 0
p2 = 0

def norm(x,l):
    return triangular_number(abs(x-l))


def triangular_number(n):
    for i in range(n):
        n += i
    return n


sums = []
#terrible terrible terrible solution:
#O(n^3) lul
with open('input/7.txt') as f:
#with open('input/test.txt') as f:
    crabs = [[int(x) for x in vals.split(',')] for vals in f][0]
    for i in range(max(crabs)):
        sums.append(0)
        for j in range(len(crabs)):
            sums[i] += norm(crabs[j],i)

    print(min(sums))






print(p1)
print(p2)
