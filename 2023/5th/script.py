seeds, *data = open("input.txt").read().split("\n\n")

def p1(data):
    seeds = [int(x) for x in seeds.split(": ")[1].split()]

    for content in data:
        numbers = []
        for line in content.splitlines()[1:]:
            str_to_num = [int(i) for i in line.split()]
            numbers.append(str_to_num)
        new_mapping = []
        current_value = 0
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
        
    print(min(new_mapping))

def p2(seeds,data):
    seed_ranges = [int(x) for x in seeds.split(": ")[1].split()]
    
    seeds_tuple = []
    for i in range(0, len(seed_ranges), 2):
        seeds_tuple.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))

    for content in data:
        numbers = []
        for line in content.splitlines()[1:]:
            str_to_num = [int(i) for i in line.split()]
            numbers.append(str_to_num)
        new_mapping = []
        while seeds_tuple:
            start_seed, end_seed = seeds_tuple.pop()
            for destination_range_start, source_range_start, range_length in numbers:
                overlap_start = max(start_seed, source_range_start)
                overlap_end = min(end_seed, source_range_start + range_length)
                if overlap_start < overlap_end:
                    new_mapping.append((overlap_start + (destination_range_start - source_range_start), overlap_end + (destination_range_start - source_range_start)))
                    if overlap_start > start_seed:
                        seeds_tuple.append((start_seed, overlap_start))
                    if end_seed > overlap_end:
                        seeds_tuple.append((overlap_end, end_seed))
                    break
            else:
                new_mapping.append((start_seed, end_seed))
        seeds_tuple = new_mapping
        print(new_mapping)
    print(min(new_mapping)[0])
    
p2(seeds, data)