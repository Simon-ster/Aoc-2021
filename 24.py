import sys

p1 = 0
p2 = 0

f = sys.stdin.readlines()


def alu(input,instructions):
    w,x,y,z = 0,0,0,0
    mapping = {'w':0,
               'x':0,
               'y':0,
               'z':0}
    ival = 0
    for line in instructions:
        #print(mapping)
        line = line.split()
        line.append(None)
        func = line[0]
        par1 = line[1]
        par2 = line[2]

        if par2 in mapping:
            par2 = int(mapping[par2])
        else:
            if par2:
                par2 = int(par2)

        if func == 'inp':
            mapping[par1] = int(input[ival])
            ival += 1

        elif func == 'add':
            mapping[par1] += par2

        elif func == 'mul':
            mapping[par1] *= par2

        elif func == 'div':
            if par2 == 0:
                print('div by zero')
                exit(1)
            mapping[par1] //= par2

        elif func == 'mod':
            if mapping[par1] < 0 or par2 <= 0:
                print('mod error')
                exit(1)
            mapping[par1] %= par2

        elif func == 'eql':
            if mapping[par1] == par2:
                mapping[par1] = 1
            else:
                mapping[par1] = 0

        else:
            print(func)
            print('problem')
            exit(1)
    return mapping['z']


#input = '99899999999999'
input =  '999119'
input =  '99911993949684'
input =  '62911941716111'
val = alu(input,f)
print(val)

# w = int(input())

#32 + w1 + w2 * 26 + 156 + w3 + 3
#191 + w1 + 26*w2 + w3

#9 +  (w1+w2)%26
#x should be 1:
    #w3 = 8

