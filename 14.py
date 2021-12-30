import sys
p1 = 0
p2 = 0

def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

f = sys.stdin.readlines()
template = f[0][:-1]
cpy = template
lines = f[2:]
insertion = {}
for line in lines:
    [a,b] = line.strip().replace(" ","").split('->')
    insertion[a] = b


pairs = {}
for i in range(len(cpy)-1):
    test = cpy[i]+cpy[i+1]
    if test not in pairs:
        pairs[test] = 1
    else:
        pairs[test] += 1

chars = {}
for k,v in insertion.items():
    chars[v] = 0
for c in cpy:
    chars[c] = cpy.count(c)

for s in range(40):

    #print(pairs)
    newpairs = pairs.copy()
    for p in pairs:
        if p in insertion:
            first = p[0] + insertion[p]
            second = insertion[p] + p[1]
            #print(first,second)
            if first in newpairs:
                newpairs[first] += pairs[p]
            else:
                newpairs[first] = pairs[p]

            if second in newpairs:
                newpairs[second] += pairs[p]
            else:
                newpairs[second] = pairs[p]

            newpairs[p] -= pairs[p]
            #print(chars)
            #chars[p[0]] += pairs[p]

            #chars[p[1]] += pairs[p]

            chars[insertion[p]] += pairs[p]

    pairs = newpairs
    if s == 9:
        p1 = max(chars.values()) - min(chars.values())

#print(pairs)
print(p1)
print(max(chars.values())-min(chars.values()))
