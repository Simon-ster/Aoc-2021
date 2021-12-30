import sys
from functools import reduce
from operator import mul
p1 = 0
p2 = 0

def calculate(subpackets,pid):
    if pid == 0:
        return sum(subpackets)
    elif pid == 1:
        return reduce(mul,subpackets,1)
    elif pid == 2:
        return min(subpackets)
    elif pid == 3:
        return max(subpackets)
    elif pid == 5:
        return int(subpackets[0] > subpackets[1])
    elif pid == 6:
        return int(subpackets[0] < subpackets[1])
    elif pid == 7:
        return int(subpackets[0] ==  subpackets[1])



def readpacket(binary):
    #print(f"binary {binary}")
    version = int(binary[0:3],2)
    #print(f"version {version}")
    pid = int(binary[3:6],2)
    #print(f"pid {pid}")
    length = 6

    if pid == 4:
        binary = binary[6:]
        num = ''
        while True:
            length += 5
            first = binary[0:5]
            binary = binary[5:]
            num += first[1:]
            if first[0] == '0':
                break
        num = int(num,2)
        #num = version \\ return version for part 1
        return (num,length)
    """
    elif (pid >=0 and pid <= 7 and pid != 4):
        binary = binary[6:]
        npx = len(binary) // 5
        subpackets = [int(binary[i+1:i+5],2) for i in range(0, len(binary), npx) if len(binary[i:i+5]) == 5]
    """

    lid = int(binary[6],2)
    length += 1
    binary = binary[7:]

    subpackets = []
    #sums = version \\ set to version for part 1
    sums = 0
    if not lid:
        readnext = int(binary[:15],2)
        assert(len(binary[:15]) == 15)
        length += 15
        binary = binary[15:]
        while readnext > 0:
            n,l = readpacket(binary)
            readnext -= l
            sums += n
            subpackets.append(n)
            length += l
            binary = binary[l:]
        return (calculate(subpackets,pid),length)
        #return (sums, length)

    else:
        readnext = int(binary[:11],2)
        assert(len(binary[:11]) == 11)
        length += 11
        binary = binary[11:]
        while readnext > 0 :
            n,l = readpacket(binary)
            readnext -= 1
            sums += n
            subpackets.append(n)
            length += l
            binary = binary[l:]
        return (calculate(subpackets,pid),length)
        #return (sums, length)



#with open('input/16.txt') as f:
#with open('input/test.txt') as f:
#f = 'D2FE28'
#f = '38006F45291200'
#f = 'EE00D40C823060'
#f = '8A004A801A8002F478'
#f = '620080001611562C8802118E34'
#f ='9C0141080250320F1802104A08'
#f = 'CE00C43D881120'
f = sys.stdin.readlines()[0]
#first two letters are 0b
binary = bin(int('1'+ f,16))[3:]
print(binary)
n,l = readpacket(binary)
print(n)
print(l)


print(p1)
print(p2)
