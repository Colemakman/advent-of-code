PATH = 'Day2/input.txt'

def parse_input(path):
    games = []
    with open(path, 'r') as file:
        for line in file:
            games.append(line.strip())
    return games

def split_game(games):
    parsed_games = []
    for round in games:
        round = [r.lstrip() for r in round.replace(":", ";").split(";")]
        for i, game in enumerate(round[1:]):
            items = [item.strip() for item in game.split(",")]
            colour_count = {}
            for item in items:
                count, colour = item.split(" ", 1)
                colour_count[colour] = int(count)
            round[i+1] = colour_count
        parsed_games.append(round) 
    return parsed_games

def find_minimum(game):
    minimum = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for item in game[1:]:
        for colour in item.keys():
            if item[colour] > minimum[colour]:
                minimum[colour] = int(item[colour])
    return minimum

def get_power(d):
    power = 1
    for val in d.values():
        power *= val
    return power


if __name__ == "__main__":
    games = parse_input(PATH)
    games = split_game(games)
    sum = 0
    for game in games:
        min = find_minimum(game)
        power = get_power(min)
        sum += power
    print(sum)