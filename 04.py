p1 = 0
p2 = 0
def return_sum(board,list_v):
    sums = 0
    list_v = set(list_v)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] not in list_v:
                sums += board[i][j]
    return sums


with open('input/4.txt') as f:
    lines = f.readlines()
    vals = lines[0]
    vals = list(map(int,vals[:-1].split(',')))
    lines = lines[1:]
    bingo = []
    part1 = False


    for line in lines:
        if line == '\n':
            bingo.append([])
        else:
            bingo[-1].append(list(map(int,line[:-1].split())))
    boards = list(range(len(bingo)))

    list_v = []
    for v in vals:
        list_v.append(v)
        if len(boards) == 1:
            sums = return_sum(bingo[boards[0]],list_v)
            print(list_v[-1]*sums)
            exit(0)
        for i in range(len(bingo)):
            for j in range(5):
                count1 = 0
                count2 = 0
                for k in range(5):
                    if int(bingo[i][j][k]) in set(list_v):
                        count1 += 1
                        if count1 == 5:
                            if i in boards:
                                boards.pop(boards.index(i))
                            sums = return_sum(bingo[i],list_v)
                            if not part1:
                                print(list_v[-1]*sums)
                                part1 = True
                    if bingo[i][k][j] in set(list_v):
                        count2 += 1
                        if count2 == 5:
                            if i in boards:
                                boards.pop(boards.index(i))
                            sums = return_sum(bingo[i],list_v)
                            if not part1:
                                print(list_v[-1]*sums)
                                part1 = True

print(p1)
print(p2)
