PATH = 'Day1/input.txt'

def parse_input(path):
    with open(path, 'r') as file:
        instructions = file.readline()
    return instructions

def get_result(file):
    floor = 0
    for p in file:
        if p == '(':
            floor += 1
        else: floor -= 1
    return floor

if __name__ == '__main__':
    file = parse_input(PATH)
    print(get_result(file))

    