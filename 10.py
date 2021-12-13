p1 = 0
p2 = 0

matches = {'(':')', '[':']', '{':'}', '<':'>'}
points = {')':3, ']':57,'}':1197, '>':25137}
points2 = {')':1, ']':2,'}':3, '>':4}

#with open('input/test.txt') as f:
with open('input/10.txt') as f:
    lines = f.readlines()
    scores = []
    for line in lines:
        corrupted = False
        line = line[:-1]
        stack = []
        for i in line:
            if i in matches:
                stack.append(i)
            else:
                if matches[stack[-1]] == i:
                    stack.pop()
                else:
                    p1 += points[i]
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            for i in list(reversed(stack)):
                score *= 5
                score += points2[matches[i]]
            scores.append(score)
    scores = sorted(scores)
    p2 = scores[(len(scores)-1)//2]


print(p1)
print(p2)
