import sys


t, d = open(sys.argv[1]).read().strip().split('\n')
times = [int(x) for x in t.split(':')[1].split()]
dist = [int(x) for x in d.split(':')[1].split()]

def f(t, d):
    total = 0
    for ms in range(t):
        if ms*(t-ms) > d:
            total += 1
    return total

ans = 1

for i in range(len(times)):
    ans *= f(times[i], dist[i])
else:
    print(ans)
