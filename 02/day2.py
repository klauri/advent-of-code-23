example = 'Game 1: 7 green, 14 red, 5 blue; 8 red, 4 green; 16 green, 18 red, 9 blue\nGame 100: 8 green; 2 red, 20 green; 12 green, 1 red, 1 blue; 4 red, 1 blue; 1 blue, 6 red\nGame 99: 1 blue, 2 green, 8 red; 1 blue, 7 red, 1 green; 11 red, 2 green; 1 red, 1 blue'

# cubes_in_bag = {
#     'red': 12,
#     'green': 13,
#     'blue': 14
# }

# all_points = 5050

def get_input():
    with open('./input.txt') as f:
        puzzle_input = f.read()
    return puzzle_input

def txt_to_dict(puzzle_input: str):
    sum = 0
    # check each game
    for line in puzzle_input.split('\n'):
        min_green_balls = 0
        min_red_balls = 0
        min_blue_balls = 0
        index = int(line.split(': ')[0].replace('Game ', ''))
        game_data = line.split(': ')[1].split('; ')
        
        for game in game_data:
            red_index = game.find('red')
            green_index = game.find('green')
            blue_index = game.find('blue')
            if green_index > 0:
                if green_index - 3 < 0: start_index = 0
                else: start_index = green_index - 3
                green_balls = int(game[start_index:green_index])
                if green_balls > min_green_balls: min_green_balls = green_balls
            if red_index > 0:
                if red_index - 3 < 0: start_index = 0
                else: start_index = red_index - 3
                red_balls = int(game[start_index:red_index])
                if red_balls > min_red_balls: min_red_balls = red_balls
            if blue_index > 0:
                if blue_index - 3 < 0: start_index = 0
                else: start_index = blue_index - 3
                blue_balls = int(game[start_index:blue_index])
                if blue_balls > min_blue_balls: min_blue_balls = blue_balls
        sum += (min_green_balls * min_red_balls * min_blue_balls)
    print(sum)
puzzle_input = get_input()
puzzle_dict = txt_to_dict(puzzle_input)
