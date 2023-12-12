example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

###  Notes  ###
###############
###############
#    Card 1: 4 -> 1(itself), 2(2), 3, 4, 5
#    Card 2: 2 -> 2(itself), 3, 4
#    Card 3: 2 -> 3(itself), 4, 5
#    Card 3: 2 -> 3(itself), 4, 5
#    Card 2(copy): 2 -> 3, 4
#    Card 3(copy): 2 -> 4, 5
#    Card 4(copy): 1 -> 5
#
#
#

def get_input():
    with open('./input.txt') as f:
        puzzle_input = f.read()
    return puzzle_input

def split_games(puzzle_input: str):
    lines = puzzle_input.split('\n')
    points_won = []
    total_points = 0
    for line in lines:
        points = 0
        split = line.split('| ')
        _ = split[0].split(': ')
        card_number = _[0].replace('Card ', '')
        winning_numbers = _[1].split()
        played_numbers = split[1].split()
        for number in played_numbers:
            if number in winning_numbers:
                if points == 0: points += 1
                else: points *= 2
        points_won.append(points)    
    for point in points_won:
        total_points += point
    print(total_points)


def game_result(line: str):
    games_won = 0
    played_numbers = line.split('| ')[1].split()
    winning_numbers = line.split('| ')[0].split(': ')[1].split()
    for number in played_numbers:
        if number in winning_numbers: 
            games_won += 1
    return games_won

def part_two(puzzle_input: str):
    lines = puzzle_input.split('\n')
    copies_won = []
    total_scratchcards = 0
    for index, line in enumerate(lines):
        games_won = 0
        split = line.split('| ')
        _ = split[0].split(': ')
        card_number = _[0].replace('Card ', '')
        winning_numbers = _[1].split()
        played_numbers = split[1].split()
        for number in played_numbers:
            if number in winning_numbers:
                games_won += 1
        for x in range(games_won):
            if index+x+1 <= len(lines):
                print(lines[index+x+1])
                total_scratchcards += 1
    print(total_scratchcards)

puzzle_input = get_input()
part_two(example)