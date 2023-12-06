time = []
distance = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines[0] = lines[0][5:].strip().split()
    lines[1] = lines[1][10:].strip().split()
    time = lines[0]
    distance = lines[1]
time = list(map(lambda x: int(x), time))
distance = list(map(lambda x: int(x),distance))
total = 1
for i in range(len(time)):
    count = 0
    for ms in range(time[i]):
        c_time = time[i]
        c_time -= ms
        if ms*c_time > distance[i] and c_time > 0:
            count += 1
    else:
        total *= count

print(total)
