
path = 'Day1/input.txt'
lines = []
with open(path, 'r') as file:
    for line in file:
        lines.append(line.strip())

numbers = ['0','1','2','3','4','5','6','7','8','9']

def findLeft(line):
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    substr = line[0]
    i = 1
    leftmost_num_index = 999
    result = ''
    while not substr[-1].isdigit():
        substr = line[:i]
        i += 1
        if substr == line:
            break
    for word in word_to_number.keys():
        if word in substr:
            if substr.find(word) < leftmost_num_index:
                leftmost_num_index = substr.find(word)
                result = word_to_number[word]
    if result == '':
        return substr[-1]
    return result

def findRight(line):
    line = line[::-1]
    word_to_number = {
        'eno': '1',
        'owt': '2',
        'eerht': '3',
        'ruof': '4',
        'evif': '5',
        'xis': '6',
        'neves': '7',
        'thgie': '8',
        'enin': '9'
    }
    substr = line[0]
    i = 1
    leftmost_num_index = 999
    result = ''
    while not substr[-1].isdigit():
        substr = line[:i]
        i += 1
        if substr == line:
            break
    for word in word_to_number.keys():
        if word in substr:
            if substr.find(word) < leftmost_num_index:
                leftmost_num_index = substr.find(word)
                result = word_to_number[word]
    if result == '':
        return substr[-1]
    return result

sum = 0

for line in lines:
    num = 0
    num = findLeft(line) + findRight(line)
    sum += int(num)

print(sum)


