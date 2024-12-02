import numpy 

def extract_num(list):
    num = ""
    for chr in list:
        if chr.isdigit():
            num += chr
    return num

games_dict = {}

with open("all_data.txt") as f:
    data = f.read().split('\n')
    for line in data:
        content = line.split(": ")
        game_num = int(extract_num(content[0]))
        
        game_sets_dict = {"red": 0, "green": 0, "blue": 0}
        sets_array = content[1].replace(", ", " ").replace("; ", " ").split()
        for element in sets_array:
            if element not in game_sets_dict.keys() and not element.isdigit():
                    game_sets_dict[element] = 0

        for ids, element in enumerate(sets_array):
            if element.isdigit() and int(element) > game_sets_dict[sets_array[ids+1]]:
                game_sets_dict[sets_array[ids+1]] = int(element)
        
        if game_num not in games_dict.keys():
            games_dict[game_num] = game_sets_dict

valid_keys = []
values = []

for key, value_dict in games_dict.items():
    if (value_dict["red"] <= 12 and 
        value_dict["green"] <= 13 and 
        value_dict["blue"] <= 14):
        valid_keys.append(key)
    values.append([value_dict["red"],value_dict["green"],value_dict["blue"]])

# print(valid_keys)
print("\n ----------- Part 1 ----------- ")
print("The answer is", sum(valid_keys))
print("\n ----------- Part 2 ----------- ")
sum_list = []
for list in values:
    sum_list.append(numpy.prod(list))

print("The answer of part 2 is", sum(sum_list))


