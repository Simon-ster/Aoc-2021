import sys
p1 = 0
p2 = 0

horiz = 0
depth = 0
aim = 0
lines = list(sys.stdin.readlines())

for line in lines:
    line = line.split()
    if line[0] == 'down':
        aim += int(line[1])
    elif line[0] == 'up':
        aim -= int(line[1])
    else:
        horiz += int(line[1])
        depth += aim*int(line[1])
p1 = horiz*aim
p2 = horiz*depth

print(p1)
print(p2)
