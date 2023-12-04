PATH = 'Day4/input.txt'

def parse_input(file):
    cards = []
    with open(file, 'r') as lines:
        for line in lines:
            line = [l.strip().split(' ') for l in line.strip().split(':')[1].split('|')]
            line = [[int(num) for num in row if num] for row in line]
            cards.append(line)
            
    return cards

def winnings(card):
    count = 0
    for num in card[1]:
        if num in card[0]:
            count += 1
    return count

def scratch(cards):
    card_count = {}
    for i,j in enumerate(cards):
        card_count[str(i+1)] = 1
    for index, card in enumerate(cards):
        for count in range(card_count[str(index+1)]):
            for wins in range(winnings(card)):
                card_count[str(index+wins+2)] += 1
    else: print(sum(card_count.values())); print(card_count)

    


file = parse_input(PATH)
scratch(file)

