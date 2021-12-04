p1 = 0
p2 = 0
with open('input/1.txt') as f:
    lines = list(map(int,f.readlines()))

    for i in range(0,len(lines)):
        if i > 0:
            if lines[i] > lines[i-1]:
                p1 += 1
        if i > 2:
            v1 = sum(lines[i-3:i])
            v2 = sum(lines[i-4:i-1])
            if v1 > v2:
                p2 += 1

print(p1)
print(p2)
