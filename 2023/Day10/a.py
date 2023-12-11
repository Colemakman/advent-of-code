from sys import argv


file = []

with open(argv[1], 'r') as f:
    for line in f:
        file.append(list(line.strip()))


#check recursively to see if a given point forms a loop. if not, set all checked points to empty '.'
def is_loop(grid, x, y, checked_points):
    if (x,y) in checked_points:
        return checked_points
    else:
        if checked_points == []:
            prev = (x,y)
            checked_points.append((x,y))
        else:
            checked_points.append((x,y))
            prev = checked_points[-2]
    print(checked_points, 'status')
    if 0 < x < len(grid[0]) and 0 < y < len(grid):
        symbol = grid[x][y]
        if symbol == '.':
            return checked_points
        elif symbol == 'F':
            if prev[1] < y:
                return is_loop(grid, x+1, y, checked_points)
            else:
                return is_loop(grid, x, y-1, checked_points)
        elif symbol == 'J':
            if prev[1] > y:
                return is_loop(grid, x-1, y, checked_points)
            else:
                return is_loop(grid, x, y+1, checked_points)
        elif symbol == 'L':
            if prev[1] > y:
                return is_loop(grid, x+1, y, checked_points)
            else:
                return is_loop(grid, x, y+1, checked_points)
        elif symbol == '7':
            if prev[1] < y:
                return is_loop(grid, x-1, y, checked_points)
            else:
                return is_loop(grid, x, y-1, checked_points)
        elif symbol == '-':
            if prev[0] < x:
                return is_loop(grid, x+1, y, checked_points)
            else:
                return is_loop(grid, x-1, y, checked_points)
        elif symbol == '|':
            if prev[1] < y:
                return is_loop(grid, x, y+1, checked_points)
            else:
                return is_loop(grid, x, y-1, checked_points)
    else:
        return checked_points

for line_index, line in enumerate(file):
    for char_index, char in enumerate(line):
        if char in ['F', 'J', '7', 'L']:
            points = is_loop(file, line_index, char_index, [])
            for p in points:
                file[p[0]-1][p[1]-1] = '.'
            for line in file:
                print(''.join(line))



