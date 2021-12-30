import sys
from math import sqrt

p1 = 0
p2 = 0

f = sys.stdin.readlines()[0]
x_end = f.split()[2][2:-1].split('..')
y_end = f.split()[3][2:].split('..')

x_rang = list(range(int(x_end[0]), int(x_end[1])+1))
y_rang = list(range(int(y_end[0]), int(y_end[1])+1))


def within(pos):
    [a,b] = pos
    return a >= int(x_end[0]) and a <= int(x_end[1]) and b >= int(y_end[0]) and b <= int(y_end[1])

def test(vel):
    pos = [0,0]

    while pos[0] <= int(x_end[1]) and pos[1] >= int(y_end[0]):

        pos[0] += vel[0]
        pos[1] += vel[1]
        if vel[0] > 0:
            vel[0] -= 1
        if vel[0] < 0:
            vel[0] += 1
        vel[1] -= 1
        if within(pos):
            return True
    return False

#'''
    # dist = n*(n+1)/2
    # 0 = n^2/2 + n/2 - dist
    # x = -1/2 +/- sqrt((1/2)^2) - 4*(1/2 * dist) all over 1
    '''
    x = -0.5 + sqrt(.25 + 2*dist)
    if x.is_integer() and x >= 0:
        print(x)
    print((x_rang[-1]*(x_rang[-1] + 1)/2))
    '''
#any higher y_vel will cause overshoot entirely*
# goes up up up
# till max
# at which point we have vel = 0
# since completely overshoot, will be initial y + 1
# 0 - y_init is total distance
# can solve with triangle number
y_0 = y_rang[0]*(-1) - 1
p1 = int(y_0*(y_0 + 1)/2)

#'''

p2 = sum([1 for x in range(1, x_rang[-1]+1) for y in range(y_0, y_rang[0]-1,-1) if test([x,y])])



print(p1)
print(p2)
