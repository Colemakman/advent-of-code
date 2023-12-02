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

def test_game(game):
    max_colours = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    passes_test = True
    for round in game[1:]:
        for key in round.keys():
            if round[key] > max_colours[key]:
                passes_test = False
    return passes_test

def sum_game(games):
    sum = 0
    for i, game in enumerate(games):
        if test_game(game):
            print('GAME', i+1,'Passes')
            sum += get_ID(game)
    return sum

def get_ID(game):
    return int(game[0].split(' ')[1])

if __name__ == "__main__":
    games = parse_input(PATH)
    games = split_game(games)
    result = sum_game(games)
    print(result)






