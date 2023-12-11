from sys import argv


galaxy = []
with open(argv[1], 'r') as file:
    for line in file:
        galaxy.append(list(line.strip()))

cols_to_expand = []
rows_to_expand = []

for i, line in enumerate(galaxy):
    if all(x=='.' for x in line):
        rows_to_expand.append(i)

for i, char in enumerate(galaxy[0]):
    if all(x[i]=='.' for x in galaxy):
        cols_to_expand.append(i)

stars = {}
star_count = 0
for line_index, line in enumerate(galaxy):
    for char_index, char in enumerate(line):
        if char == '#':
            star_count += 1
            stars[star_count] = (line_index, char_index)

total = 0

for i in range(1, star_count+1):
    for j in range(i+1, star_count+1):
        i_width, i_height = stars[i][0], stars[i][1]
        j_width, j_height = stars[j][0], stars[j][1]
        add_to_width, add_to_height = 0, 0
        for r in rows_to_expand:
            if max(i_width,j_width) > r > min(i_width,j_width):
                add_to_width += 999999
        for c in cols_to_expand:
            if max(i_height,j_height) > c > min(i_height,j_height):
                add_to_height += 999999
        width = abs(i_width-j_width) + add_to_width
        height = abs(i_height-j_height) + add_to_height
        total += width + height

print(total)
