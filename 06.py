p1 = 0
p2 = 0

#part 1 useless lmao
with open('input/6.txt') as f:
    fishies = [[int(x) for x in vals.split(',')] for vals in f][0]
    for i in range(80):
        #print(fishies)
        fishies = [a - 1 for a in fishies]
        for f in range(len(fishies)):
            if fishies[f] == -1:
                fishies[f] += 7
                fishies.append(8)

    p1 = len(fishies)


#with open('input/test.txt') as f:
with open('input/6.txt') as f:
    fishies = [[int(x) for x in vals.split(',')] for vals in f][0]
    counts = [fishies.count(i) for i in range(9)]
    for i in range(256):
        print(counts)
        counts.append(counts.pop(0))
        counts[6] += counts[-1]

    p2 = sum(counts)

print(p1)
print(p2)
