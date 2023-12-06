cubes_in_bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('./input.txt') as f:
    puzzle_input = f.read()
    for line in puzzle_input.split('\n'):
        index = line.split(':')[0].replace('Game ', '')
        game_data = line.split(':')[1]
        for game in game_data.split(';'):
            print(game.split(',')[0])
            
        red = game_data.split(';')[0]
        green = game_data.split(';')[1]
        blue = game_data.split(';')[2]
        