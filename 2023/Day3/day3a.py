PATH = '2023/Day3/input.txt'

def parse_input(inp):
    grid = []
    filler = '.' * 142
    grid.append(filler)
    with open(inp, 'r') as file:
        for line in file:
            line = '....' + line.strip() + '....'
            grid.append(line)
    grid.append(filler)
    return grid

def check_valid(inp):
    sum = 0
    for line_index, line in enumerate(inp):
        for char_index, char in enumerate(line):
            if char.isdigit() and not line[char_index-1].isdigit():
                j = char_index
                while line[j].isdigit():
                    j += 1
                else:
                    if list(set(inp[line_index-1][char_index-1:j+1])) == ['.'] and list(set(inp[line_index+1][char_index-1:j+1])) == ['.'] and line[char_index-1] == '.' and line[j] == '.':
                        pass
                    else:
                        sum += int(line[char_index:j])
    print(sum)

                            




inp = parse_input(PATH)
check_valid(inp)