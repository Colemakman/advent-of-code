PATH = 'Day4/input.txt'

def parse_input(file):
    cards = []
    with open(file, 'r') as lines:
        for line in lines:
            line = [l.strip().split(' ') for l in line.strip().split(':')[1].split('|')]
            line = [[int(num) for num in row if num] for row in line]
            cards.append(line)
            
    return cards

def check_winning(card: list[int]) -> int:
    win = 0
    for num in card[1]:
        if num in card[0]:
            if win == 0:
                win+=1 
            else: win *= 2
            continue
    return win

cards = parse_input(PATH)
total = 0
for card in cards:
    total += check_winning(card)
print(total)
