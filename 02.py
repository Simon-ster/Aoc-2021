p1 = 0
p2 = 0
horiz = 0
depth = 0
aim = 0
with open('input/2.txt') as f:
    for line in f.readlines():
        line = line.split()
        if line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
        else:
            horiz += int(line[1])
            depth += aim*int(line[1])

print(horiz * aim)
print(horiz * depth)
