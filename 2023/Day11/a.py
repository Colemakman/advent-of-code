import sys



galaxy = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        galaxy.append(line.strip())

def expand(gal):
    to_insert = []
    for index, line in enumerate(gal):
        if '#' not in line:
            to_insert.append(index)
    for i in to_insert:
        gal.insert(i+1, '.'*len(gal[0]))

    cols = {}
    for line in gal:
        for index, char in enumerate(line):
            if char == '.':
                if index in cols:
                    cols[index] += 1
                else:
                    cols[index] = 1
    else:
        rows_to_insert = []
        for k in cols.keys():
            if cols[k] == max(cols.values()):
                rows_to_insert.append(k)
        gal = [[str(element) + '.' if index in rows_to_insert else element for index, element in enumerate(sublist)] for sublist in gal]
        for i, g in enumerate(gal):
            gal[i] = [element for sublist in gal[i] for element in sublist]
    return gal

galaxy = expand(galaxy)
star_count = 1
stars = {}

for line_index, line in enumerate(galaxy):
    for char_index, char in enumerate(line):
        if char == '#':
            galaxy[line_index][char_index] = star_count
            stars[star_count] = (line_index+1, char_index+1)
            star_count += 1
total = 0

for i in range(1, star_count):
    for j in range(i+1, star_count):
        width = abs(stars[i][0] - stars[j][0])
        height = abs(stars[i][1] - stars[j][1])
        total += width + height

for g in galaxy:
    print(g)
print(total)
