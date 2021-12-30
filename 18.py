import sys
import math
from ast import literal_eval


p1 = 0
p2 = 0


class snailfish:
    def __init__(self,inputs):
        inputs = literal_eval(str(inputs))
        self.left = inputs[0]
        if type(inputs[0]) == list:
            self.left = snailfish(inputs[0])
        if type(inputs[1]) == list:
            self.right = snailfish(inputs[1])

        self.leftmost = self.getleftmost(self.left)
        self.rightmost = self.getrightmost(self.right)

    def getleftmost(self,left):
        if type(left) == list:
            self.leftmost = self.getleftmost(left[0])
        else:
            return left

    def getrightmost(self,right):
        if type(right) == list:
            self.rightmost = self.getrightmost(right[0])
        else:
            return right

    def split(self,value):
        l = math.floor(value/2)
        r = math.ceil(value/2)
        return [l,r]

    def explode(self,pair):
        l = pair[0]
        r = pair[1]
        self.leftmost += l
        self.rightmost += r
        return 0

    def checks(self,depth=0):
        l = self.left
        r = self.right

        if type(self.left == list):
            l = snailfish(self.left)
        if type(self.right == list):
            r = snailfish(self.right)

        pair = [l,r]

        if depth == 4:
            pair = explode(pair)

        if type(left) == int and left > 9:
            left = split(left)

        if type(right) == int and right > 9:
            right = split(right)

        if type(left) == list:
            left = checks(left, depth+1)

        if type(right) == list:
            right = checks(right, depth+1)

        return [left,right]

def explode(pair):
    needed = False



f = sys.stdin.readlines()
for l in range(1):
    #l= '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
    #l = '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    #l = '[[[[1,2],[3,4]],[[5,6],[7,8]]],9]'
    l = '[1,2]'
    val = snailfish(l)
    #print(val.leftmost)
    val.checks()
    #print(val.checks())
    exit(0)
print(p1)
print(p2)
