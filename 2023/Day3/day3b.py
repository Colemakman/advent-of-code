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

def find_gears(inp):
    gears= {}
    sum = 0
    for line_index, line in enumerate(inp):
        for char_index, char in enumerate(line):
            if char.isdigit() and not line[char_index-1].isdigit():
                j = char_index
                while line[j].isdigit():
                    j += 1
                gear_x = 0
                gear_y = 0
                top = inp[line_index-1][char_index-1:j+1]
                bottom = inp[line_index+1][char_index-1:j+1]
                left = line[char_index-1]
                right = line[j]
                number = int(line[char_index:j])
                if left == '*':
                    if (char_index-1, line_index) in gears.keys():
                        sum += number * int(gears[(char_index-1, line_index)])
                    else: gears[(char_index-1, line_index)] = number
                elif right == '*':
                    if (j, line_index) in gears.keys():
                        sum += number * int(gears[(j, line_index)])
                    else: gears[(j, line_index)] = number
                elif '*' in top:
                    gear_x = top.find('*')
                    gear_x += (char_index-1)
                    if (gear_x, line_index-1) in gears.keys():
                        sum += number * int(gears[(gear_x, line_index-1)])
                    else: gears[(gear_x, line_index-1)] = number
                elif '*' in bottom:
                    gear_x = bottom.find('*')
                    gear_x += (char_index-1)
                    if (gear_x, line_index+1) in gears.keys():
                        sum += number * int(gears[(gear_x, line_index+1)])
                    else: gears[(gear_x, line_index+1)] = number
    print(sum)

x = parse_input(PATH)
find_gears(x)


