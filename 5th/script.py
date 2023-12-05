seeds, *data = open("test.txt").read().split("\n\n")

seeds = [int(x) for x in seeds.split(": ")[1].split()]

for content in data:
    numbers = []
    for line in content.splitlines()[1:]:
        str_to_num = [int(i) for i in line.split()]
        numbers.append(str_to_num)
    new_mapping = []
    current_value = 0
    print(numbers)
    for seed in seeds:
        current_value = seed
        for destination_range_start, source_range_start, range_length in numbers:
            if seed in range(source_range_start, source_range_start + range_length):
                current_value = seed + (destination_range_start - source_range_start)
                new_mapping.append(current_value)
                break
        else:
            current_value = seed
            new_mapping.append(current_value)
    seeds = new_mapping
    
print(min(seeds))