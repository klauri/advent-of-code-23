import re
word_to_num_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

word_list = list(word_to_num_map.keys())

def word_to_num(word):
    number = word_to_num_map[word]
    return number

def get_input():
    with open('./input.txt') as f:
        data = f.read()
        bad_values = data.split('\n')
        return bad_values
    
# def clean_input(bad_values):
#     start = 0
#     for value in bad_values:
        
            # start = value.find(word)
            # end = start + len(word)
            # new_value = value[0:start] + str(word_to_num(word)) + value[end:]
            # print(new_value)

def translate(v: str) -> str:
    return v if v.isdigit() else str(word_list.index(v)+1)

def part2(lines: list[str]):
    result = 0
    for line in lines:
        nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        result += int(translate(nums[0]) + translate(nums[-1]))
    print('part 2:', result)

def get_result(bad_values):
    result = 0
    for value in bad_values:
        value_list = list(value)
        digits = []
        # for word in word_list:
        #     if word in value: digits.append(str(word_to_num(word)))
        for char in value_list:
            if char.isnumeric():
                digits.append(char)
        number = ''.join(digits)
        answer = number[0:1] + number[-1:]
        result += int(answer)
    return result

if __name__=='__main__':
    bad_values = get_input()
    part2(bad_values)
    # print(get_result(clean_values))