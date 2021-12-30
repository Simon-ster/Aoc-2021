import sys


def computeRoll(n,mod):
    if n > mod:
        n = (n - 1) % mod
        n += 1
    return n

p1 = 0
p2 = 0

f = sys.stdin.readlines()
d1 = int(f[0].split()[4])
d2 = int(f[1].split()[4])

pos = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}

def game(wincon,d1,d2,c):
    winner = False
    s1,s2 = 0,0
    rolls = 0
    while not winner:
        if not winner:
            for i in range(3):
                d1 += computeRoll(c,100)
                c += 1
                rolls += 1

            d1 = computeRoll(d1,10)
            s1 += d1
            if s1 >= wincon:
                winner = True
        if not winner:
            for i in range(3):
                d2 += computeRoll(c,100)
                c += 1
                rolls += 1

            d2 = computeRoll(d2,10)
            s2 += d2
            if s2 >= wincon:
                winner = True

    return rolls * min(s1,s2)

print(game(1000,d1,d2,1))


#universe, p1sum, p2sum
p1vics = 0
p2vics = 0
#p1scores = [0]*21
#p2scores = [0]*21
#pos1 = [0]*10
#pos2 = [0]*10
#pos1[d1] = 1
#pos2[d2] = 1
#p1scores[0] = 1
#p2scores[0] = 1
universes = {(d1,d2,0,0):1}
rununtil = 200

while rununtil:
    newuniverses = {}
    for u,c in universes.items():
        d1,d2,i,j = u
        #player 1
        for pf in pos:
            #p is dice sum
            newpos1 = computeRoll(d1+pf,10)
            #new pos is board position, prev + new
            newsco1 = newpos1 + i
            #new score is prevscore + new position
            #newpos[newidx-1] += pos[j]*c*pos1[i]
            if newsco1 >= 21:
                # num victories += #universes with that score * #boards in that position in this universe
                p1vics += c*pos[pf]
                continue

            #now for player 2
            for ps in pos:
                newpos2 = computeRoll(d2+ps,10)
                newsco2 = newpos2 + j
                if newsco2 >= 21:
                    p2vics += c*pos[ps]
                    continue

                if (newpos1,newpos2,newsco1,newsco2) not in newuniverses:
                    newuniverses[(newpos1,newpos2,newsco1,newsco2)] = c * pos[pf] * pos[ps]
                else:
                    newuniverses[(newpos1,newpos2,newsco1,newsco2)] += c * pos[pf] * pos[ps]

    universes = newuniverses
    #print(newuniverses)
    rununtil -= 1

print(max(p1vics,p2vics))
