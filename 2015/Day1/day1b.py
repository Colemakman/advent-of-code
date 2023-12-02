PATH = 'Day1/input.txt'

def parse_input(path):
    with open(path, 'r') as file:
        instructions = file.readline()
    return instructions

def get_result(file):
    floor = 0
    for i, p in enumerate(file):
        if p == '(':
            floor += 1
        else: floor -= 1

        if floor == -1:
            print('')
    return floor

if __name__ == '__main__':
    file = parse_input(PATH)
    get_result(file)