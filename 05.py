p1 = 0
p2 = 0

vents = {}
def add_val(x,y):
    if (x,y) not in vents:
        vents[(x,y)] = 0
    else:
        vents[(x,y)] += 1

with open('input/test.txt') as f:
#with open('input/5.txt') as f:
    lines = f.readlines()
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
                add_val(x1,y)
        elif y1 == y2:
            start = min(x1,x2)
            end = max(x1,x2)
            for x in range(start,end + 1):
                add_val(x,y1)
        else:
            x, y = x1, y1
            xstep = (x2-x1)//abs(x2-x1)
            ystep = (y2-y1)//abs(y2-y1)
            add_val(x,y)
            while x != x2:
                x += xstep
                y += ystep
                add_val(x,y)

p1 = sum([1 for number in vents.values() if number > 0])

print(p1)
print(p2)
