import sys


path = sys.argv[1]
file = open(path, 'r').read().splitlines()
for i, f in enumerate(file):
    file[i] = list(map(lambda x: int(x), f.split()))
    file[i] = file[i][::-1]
def findNext(seq):
    diffs = [seq]
    c_diff = seq
    while len(list(set(c_diff))) != 1:
        c_diff = findDiff(c_diff)
        diffs.append(c_diff)
    else:
        return sum([d[-1] for d in diffs])
def findDiff(seq):
    diff = []
    for i in range(len(seq)-1):
        diff.append(seq[i+1]-seq[i])
    return diff
count = 0
for l in file:
    count+= findNext(l)
print(count)
