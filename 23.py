import sys

p1 = 0
p2 = 0

f = sys.stdin.readlines()

arr = []
for line in f:
    arr.append(list(line.strip('\n')))

for line in arr:
    print(line)


