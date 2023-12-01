
path = 'Day1/input.txt'
lines = []
with open(path, 'r') as file:
    for line in file:
        lines.append(line.strip())

sum = 0

for line in lines:
    this_num = ''
    line = ''.join([char for char in line if not char.isalpha()]) # remove all letters, leaving only numbers
    this_num += line[0]
    this_num += line[-1]
    sum += int(this_num)

print('Total sum is:', sum)
