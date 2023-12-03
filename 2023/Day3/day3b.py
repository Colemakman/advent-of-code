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
    for line_index, line in enumerate(inp):
        pass