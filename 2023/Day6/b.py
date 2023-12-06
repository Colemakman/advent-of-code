time = 47986698
distance = 400121310111540
total = 0

for ms in range(time):
    c_time = time
    c_time -= ms
    if ms*c_time > distance and c_time > 0:
        total += 1

print(total)
        
