import sys
from functools import cmp_to_key


file = open(sys.argv[1], 'r').read().strip().splitlines()
file = [f.split() for f in file]
hashmap = {}
for line in file:
    hashmap[line[0]] = int(line[1])
hands = [f[0] for f in file]

def compare(a,b):
    order = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    order = order[::-1]
    score_a = getScore(a) 
    score_b = getScore(b)
    if score_a > score_b:
        return a
    elif score_a < score_b:
        return b
    elif score_a == score_b:
        i = 0
        while a[i] == b[i]:
            i += 1
        else:
            if order.index(a[i]) > order.index(b[i]):
                return a # is a
            return b

def getScore(a):
    s = len(list(set(a)))
    if s == 1:
        return 700000
    for n in a:
        if a.count(n) == 4:
            return 600000
    if s == 2:
        return 500000
    for n in a:
        if a.count(n) == 3:
            if s == 3:
                return 400000
    if s == 3:
        return 300000
    elif s == 4:
        return 200000
    return 100000


total = 0

hands = sorted(hands, key=cmp_to_key(compare))
for i, r in enumerate(hands):
    total += (hashmap[r]*(i+1))
print(total)
