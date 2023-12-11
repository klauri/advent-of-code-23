
example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def get_input():
    with open('./input.txt') as f:
        puzzle_input = f.read()
    return puzzle_input


def get_numbers(puzzle_input: str) -> list:
    lines = puzzle_input.split('\n')
    row_index = [x for x in range(0, lines[0].__len__())]
    part_numbers = []
    for col_index, line in enumerate(lines):
        for row in row_index:
            if row == 0 or line[row-1:row] == '.': 
                if line[row:row+1].isnumeric():
                    char_count = 0
                    if line[row+1:row+2].isnumeric(): 
                        char_count += 1
                        if line[row+2:row+3] == '.':
                            char_count += 1
                            part_numbers.append([ line[row:row+char_count], col_index, row, char_count ])
                        elif line[row+2:row+3].isnumeric():
                            char_count += 1
                            if line[row+2:row+3].isnumeric():
                                char_count += 1
                                part_numbers.append([ line[row:row+char_count], col_index, row, char_count ])
    
    return part_numbers

def partone(puzzle_input: str):
    part_numbers = get_numbers(puzzle_input)
    lines = puzzle_input.split('\n')
    for part_number in part_numbers:
        number = part_number[0]
        col_index = part_number[1]
        row_start_index = part_number[2]
        char_count = part_number[3]
        for x in range(0, char_count+1):
            cur_row = lines[col_index]
            if col_index == 0:
                test_char = cur_row[row_start_index+x-1:row_start_index+x]
                below_row = lines[col_index + 1]
                if test_char.isalnum() and test_char != '*':
                    test_char = below_row[row_start_index+x-1:row_start_index+x]
                    if test_char.isalnum() and test_char != '*':
                        print(number)
            elif col_index == lines.__len__() - 1:
                above_row = lines[col_index - 1]
                test_char = above_row[row_start_index+x-1:row_start_index+x]
                if test_char.isalnum() and test_char != '*':
                    test_char = cur_row[row_start_index+x-1:row_start_index+x]
                    if test_char.isalnum() and test_char != '*':
                        print(number)
            else:
                above_row = lines[col_index - 1]
                below_row = lines[col_index + 1]
                test_char = above_row[row_start_index+x-1:row_start_index+x]
                if test_char.isalnum() and test_char != '*':
                    test_char = cur_row[row_start_index+x-1:row_start_index+x]
                    if test_char.isalnum() and test_char != '*':
                        test_char = below_row[row_start_index+x-1:row_start_index+x]
                        if test_char.isalnum() and test_char != '*':
                            print(number)

puzzle_input = get_input()
partone(example)