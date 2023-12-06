import sys
import math


t, d = open(sys.argv[1]).read().strip().split('\n')
times = [str(x) for x in t.split(':')[1].split()]
dist = [str(x) for x in d.split(':')[1].split()]
time = int(''.join(times))
dist = int(''.join(dist))
print(time, dist)
def quad(a,b,c): 
    disc = b**2 - (4*a*c)
    l = (-b + math.sqrt(disc))/(2*a)
    r = (-b - math.sqrt(disc))/(2*a)
    return (l,r)
x1,x2 = quad(1,time,dist)
x1,x2 = math.floor(x1), math.ceil(x2)
print(abs(x1-x2))
