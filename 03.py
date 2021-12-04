import numpy as np
def most_common(lst):
    counts = np.bincount(lst)
    if max(counts) == min(counts):
        return 1
    return np.argmax(counts)

def least_common(lst):
    counts = np.bincount(lst)
    if max(counts) == min(counts):
        return 0
    return np.argmin(counts)

gamma = 0
epsilon = 0
lists = []
ogen = []
cosc = []
#with open('input/test.txt') as f:
with open('input/3.txt') as f:
    for line in f.readlines():
        val = list(line)
        val = val[:-1]
        lists.append(list(map(int, val)))

    ogen = lists.copy()
    cosc = lists.copy()
    lists = np.array(lists)

    for i in range(len(lists[0])):
        gamma <<= 1
        epsilon <<=1
        gamma |= most_common(lists[:,i])
        epsilon |= least_common(lists[:,i])

        if (len(ogen) > 1):
            mc2 = most_common([ogen[k][i] for k in range(len(ogen))])

            j = 0
            while j < len(ogen):
                if ogen[j][i] == mc2:
                    if len(ogen) == 1:
                        break
                    j += 1
                else:
                    ogen.pop(j)

        if (len(cosc) > 1):
            lc2 = least_common([cosc[k][i] for k in range(len(cosc))])
            j = 0
            while j < len(cosc):
                if cosc[j][i] == lc2:
                    if len(cosc) == 1:
                        break
                    j += 1
                else:
                    cosc.pop(j)

    v1 = int(''.join([str(x) for x in ogen[0]]),2)
    v2 = int(''.join([str(x) for x in cosc[0]]),2)

print(epsilon * gamma)
print(v1 * v2)
