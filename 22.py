import sys
import numpy as np

p1 = 0
p2 = 0

f = sys.stdin.readlines()
a = np.zeros((101,101,101))

for line in f:
    line = line.strip().split()
    switch = line[0]
    line = line[1:][0].split(',')
    #print(line)
    x_l,x_h = [int(i) for i in line[0][2:].split('..')]
    y_l,y_h = [int(i) for i in line[1][2:].split('..')]
    z_l,z_h = [int(i) for i in line[2][2:].split('..')]

    '''
    if x_l < -50:
        x_l = -50
    if x_h > 50:
        x_h = 50

    if y_l < -50:
        y_l = -50
    if y_h > 50:
        y_h = 50

    if z_l < -50:
        z_l = -50
    if z_h > 50:
        z_h = 50

    print(x_l,x_h)
    print(y_l,y_h)
    print(z_l,z_h)
    '''

    if switch == 'on':
        a[x_l+50:x_h+51,y_l+50:y_h+51,z_l+50:z_h+51] = 1
    else:
        a[x_l+50:x_h+51,y_l+50:y_h+51,z_l+50:z_h+51] = 0


print(a.sum())
