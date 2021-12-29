import sys
p1 = 0
p2 = 0

lets = 'abcdefg'
ls = [7,7,4,8,9,8,6]
dic = {
    0:set(['a','b','c','e','f','g']),
    1:set(['c','f']),
    2:set(['a','c','d','e','g']),
    3:set(['a','c','d','f','g']),
    4:set(['b','c','d','f']),
    5:set(['a','b','d','f','g']),
    6:set(['a','b','d','e','f','g']),
    7:set(['a','c','f']),
    8:set(['a','b','c','d','e','f','g']),
    9:set(['a','b','c','d','f','g'])
}

f = sys.stdin.readlines()
for line in f:
#for i in range(1):
    #line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n"
    line = line.split(' | ')
    #print(line)
    output = line[1][:-1].split()
    inputs = line[0]
    inputs_spl = inputs.split()

    vals = 0
    counts = {}
    one = set()
    two = set()
    three = set()
    four = set()
    five = set()
    six = set()
    seven = set()
    eight = set()
    nine = set()

    for i in output:
        v = len(i)
        if v == 2:
            p1 += 1
        elif v == 3:
            p1 += 1
        elif v == 4:
            p1 += 1
        elif v == 7:
            p1 += 1

    for i in lets:
        counts[i] = inputs.count(i)

    ttf = []
    zsn = []
    for i in inputs_spl:
        i = set(list(i))
        v = len(i)
        if v == 2:
            one = i
        elif v == 3:
            seven = i
        elif v == 4:
            four = i
        elif v == 5:
            ttf.append(set(i))
            #two, three, five
        elif v == 6:
            zsn.append(set(i))
            #zero, six, nine
        elif v == 7:
            eight = i

    a = seven.difference(one)
    b = set()
    c = set()
    d = set()
    e = set()
    f = set()
    g = set()
    bd = four.difference(one)
    eg = eight.difference(four | seven)
    e = set()
    g = set()


    for i in zsn:
        for l in eg:
            l = set(l)
            if i == eight.difference(l):
                nine = eight.difference(l)
                zsn.remove(i)
                e = l
                g = eg - l
                break

    for i in ttf:
        if e.issubset(i):
            two = i
            ttf.remove(i)
            b = eight.difference(two | one)
            break


    for i in ttf:
        if i | one == nine:
            five = i
            ttf.remove(i)
            c = nine.difference(five)
            break

    three = ttf[0]

    for i in zsn:
        if nine.difference(c) | e == i:
            six = i
            zsn.remove(i)
            c = eight.difference(six)
            break


    zero = zsn[0]
    d = eight.difference(zero)
    f = eight.difference(a|b|c|d|e|g)

    thepad = {list(a)[0]:'a',
              list(b)[0]:'b',
              list(c)[0]:'c',
              list(d)[0]:'d',
              list(e)[0]:'e',
              list(f)[0]:'f',
              list(g)[0]:'g'}

    #print(a,b,c,d,e,f,g)
    #exit(0)

    '''
    nine = eight - eg
    have ega
    len6 with eg in it = 6
    have egab
    have egabd
    six - e = 5
    eight - six = c
    have abcdeg
    eight - two - b = f

    '''

    vals = 0
    for i in output:
        word = set()
        for j in i:
            word.add(thepad[j])
        vals *= 10
        for i,v in dic.items():
            if v == word:
                vals += i
    p2 += vals



print(p1)
print(p2)
