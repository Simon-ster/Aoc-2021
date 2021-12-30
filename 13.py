import sys
p1 = 0
p2 = 0

f = sys.stdin.readlines()
points = []
actions = []
p = True
for l in f:
    if l == '\n':
        p = False
        continue
    elif p:
        a,b = l.strip('\n').split(',')
        points.append([int(a),int(b)])
    else:
        l = l.split()
        l = l[2].split('=')
        actions.append([l[0],int(l[1])])


def fold(action,points):
    x_max = max([p[0] for p in points])
    y_max = max([p[1] for p in points])
    a,f = action
    if a == 'x':
        x_max = f
    else:
        y_max = f
    newpoints = []
    for [x,y] in points:
        if x > x_max:
            x = x_max - (x - x_max)
        elif y > y_max:
            y = y_max - (y - y_max)
        newpoints.append([x,y])
    return newpoints

first = True
for a in actions:
    points = fold(a,points)
    if first:
        ps = [(a,b) for [a,b] in points]
        p1 = len(set(ps))
        first = False

x_max = max([p[0] for p in points])
y_max = max([p[1] for p in points])
printme = []
points = set([(a,b) for [a,b] in points])
for j in range(y_max+1):
    printme.append([])
    for i in range(x_max+1):
        if (i,j) in points:
            printme[j].append('O')
        else:
            printme[j].append('.')

print(p1)
print(printme)
