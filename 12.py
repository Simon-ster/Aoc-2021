import sys
p1 = 0
p2 = 0

caves = {}
f = sys.stdin.readlines()

for l in f:
    l = l[:-1].split('-')

    if l[0] in caves:
        caves[l[0]].append(l[1])
    else:
        caves[l[0]] = [l[1]]

    if l[1] in caves:
        caves[l[1]].append(l[0])
    else:
        caves[l[1]] = [l[0]]


p1 = 0
def search(c,visited):
    if c == 'end':
        return 1
    if (c.islower() or c == 'start') and c in set(visited):
        return 0

    total = 0
    #visited.append(c) doesn't work. j
    v = visited.copy()
    v.append(c)
    for i in caves[c]:
        total += search(i,v)
    return total

def search_small(c,visited,flag):
    if c == 'end':
        return 1
    if c == 'start' and c in set(visited):
        return 0
    if c.islower() and c in set(visited):
        if flag == 0:
            flag = 1
        else:
            return 0

    total = 0
    #visited.append(c) doesn't work. j
    v = visited.copy()
    v.append(c)
    for i in caves[c]:
        total += search_small(i,v,flag)
    return total

p1 = search('start',[])
p2 = search_small('start',[],0)

print(p1)
print(p2)
