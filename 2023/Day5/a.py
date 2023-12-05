seeds, *blocks = open('sample.txt', 'r').read().split('\n\n')

seeds = list(map(int,seeds.split(':')[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        a,b,c = map(int,line.split())
        ranges.append([a,b,c])
    new = []
    for seed in seeds:
        for a, b, c in ranges:
            if seed in range(b, b+c):
                new.append(seed - b + a)
                break
        else:
            new.append(seed)
    seeds = new
    
print(min(seeds))
    
        