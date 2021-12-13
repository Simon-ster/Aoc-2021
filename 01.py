import sys

p1 = 0
p2 = 0

lines = list(map(int,sys.stdin.readlines()))

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
