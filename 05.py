import sys

p1 = 0
p2 = 0

vents = {}
vents2 = {}
def add_val(x,y,v):
    if (x,y) not in v:
        v[(x,y)] = 0
    else:
        v[(x,y)] += 1

lines = list(sys.stdin.readlines())
for line in lines:
    #line.split() gets rid of ->
    x1 = int(line.split()[0].split(",")[0])
    x2 = int(line.split()[2].split(",")[0])

    y1 = int(line.split()[0].split(",")[1])
    y2 = int(line.split()[2].split(",")[1])

    if x1 == x2:
        start = min(y1,y2)
        end = max(y1,y2)
        for y in range(start,end + 1):
            add_val(x1,y,vents)
            add_val(x1,y,vents2)
    elif y1 == y2:
        start = min(x1,x2)
        end = max(x1,x2)
        for x in range(start,end + 1):
            add_val(x,y1,vents)
            add_val(x,y1,vents2)
    else:
        x, y = x1, y1
        xstep = (x2-x1)//abs(x2-x1)
        ystep = (y2-y1)//abs(y2-y1)
        add_val(x,y,vents2)
        while x != x2:
            x += xstep
            y += ystep
            add_val(x,y,vents2)

p1 = sum([1 for number in vents.values() if number > 0])
p2 = sum([1 for number in vents2.values() if number > 0])

print(p1)
print(p2)
