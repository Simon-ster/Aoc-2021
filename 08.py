p1 = 0
p2 = 0

lets = 'abcdefg'
ls = [7,7,4,8,9,8,6]
dic = {
    'a':7,
    'b':7,
    'c':4,
    'd':8,
    'e':9,
    'f':8,
    'g':6
}

#with open('input/8.txt') as f:
with open('input/test.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n"
        line = line.split(' | ')
        print(line)
        output = line[1][:-1].split()
        inputs = line[0]
        inputs_spl = inputs.split()

        vals = 0
        counts = [0 for i in range(7)]
        for i in output:
            v = len(i)
            if v == 2 or v == 3 or v == 4 or v == 7:
                p1 += 1

        this_dict = {}
        for i in range(len(lets)):
            counts[i] = inputs.count(lets[i])
            this_dict[lets[i]] = counts[i]
        print(this_dict)
        for i in inputs_spl:
            for j in i:
                print(this_dict[j])



        """
        #take care of c,e,g
        for i in range(len(lets)):
            bug_count = counts[i]
            bug_let = lets[i]
            for key,value in dic.items():
                if value == bug_count:
                    this_dict[bug_let] = key
        """


        print(this_dict)



        p2 += vals


print(p1)
print(p2)
