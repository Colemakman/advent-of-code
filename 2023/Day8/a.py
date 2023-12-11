from sys import argv
import math


directions, nodes = open(argv[1], 'r').read().split('\n\n')[:2]
nodes = nodes.split('\n')


d = {}
for n in nodes:
    n = n.split('=')
    d[n[0].strip()] = (n[1].strip()[1:len(n[1].strip())-1].split(',')[0], n[1].strip()[1:len(n[1].strip())-1].split(',')[1].strip())

print(d)
node = [n for n in d.keys() if n[-1] == 'A']
print(node)
count = 0
lcm = []
while not all('Z' in n for n in node):
    for way in directions:
        for i, n in enumerate(node):
            if way == 'L':
                node[i] = d[n][0]
            else: node[i] = d[n][1]
        else:
            for n in node:
                if len(lcm) < len(node):
                    if 'Z' in n:
                        lcm.append(count+1)
                else: 
                    print(lcm)
                    ans = lcm[0]
                    for x in lcm:
                        ans = math.lcm(ans, x)
                        print(ans)
                        break
            count += 1 

else:
    print(count)
