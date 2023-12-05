inputs, *blocks = open('input.txt', 'r').read().split('\n\n')

inputs = list(map(int,inputs.split(':')[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i+1]+inputs[i]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        a,b,c = map(int,line.split())
        ranges.append([a,b,c])
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for destination,source,range in ranges:
            os = max(s,source)
            oe = min(e, source+range)
            if os < oe:
                new.append((os - source + destination, oe - source + destination))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s,e))
    seeds = new

print(min(seeds)[0])
    
        