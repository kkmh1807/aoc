# Uses way too much memory on real input data
data = open("test.txt").read()

seeds = data.split("\n\n")[0].split(": ")[-1].split()
seed_to_soil = {"seed": [], "soil": []}
soil_to_fertilizer = {"soil": [], "fertilizer": []}
fertilizer_to_water = {"fertilizer": [], "water": []}
water_to_light = {"water": [], "light": []}
light_to_temperature = {"light": [], "temperature": []}
temperature_to_humidity = {"temperature": [], "humidity": []}
humidity_to_location = {"humidity": [], "location": []}

# numbers is on the form [1 2 3]. Returns a dictionary of mapped values. 
def calculate_mapping(numbers, label1, label2):
    destination_range_start = int(numbers[0])
    source_range_start = int(numbers[1])
    range_length = int(numbers[2])
    
    destination_range = [i for i in range(destination_range_start, destination_range_start+range_length)]
    source_range = [i for i in range(source_range_start, source_range_start+range_length)]
        
    return {label1: source_range, label2: destination_range}

for lines in data.split("\n\n")[1:]:
    content = lines.split("\n")
    labels = [content[0].split("-")[0],content[0].split("-")[-1].split()[0]]
    all_numbers = content[1:]
    
    for numbers in all_numbers:
        if labels[0] == "seed" and labels[1] == "soil":
            seed_to_soil[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["seed"])
            seed_to_soil[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["soil"])
        if labels[0] == "soil" and labels[1] == "fertilizer":
            soil_to_fertilizer[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["soil"])
            soil_to_fertilizer[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["fertilizer"])
        if labels[0] == "fertilizer" and labels[1] == "water":
            fertilizer_to_water[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["fertilizer"])
            fertilizer_to_water[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["water"])
        if labels[0] == "water" and labels[1] == "light":
            water_to_light[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["water"])
            water_to_light[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["light"])
        if labels[0] == "light" and labels[1] == "temperature":
            light_to_temperature[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["light"])
            light_to_temperature[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["temperature"])
        if labels[0] == "temperature" and labels[1] == "humidity":
            temperature_to_humidity[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["temperature"])
            temperature_to_humidity[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["humidity"])
        if labels[0] == "humidity" and labels[1] == "location":
            humidity_to_location[labels[0]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["humidity"])
            humidity_to_location[labels[1]].append(calculate_mapping(numbers.split(), labels[0], labels[1])["location"])

def find_mapping(value, list_1, list_2):
    index = 0
    if len(list_1) > 1:
        for list_index in range(len(list_1)):
            if value in list_1[list_index]:
                index = list_1[list_index].index(value)
                return list_2[list_index][index]
    else:
        if value in list_1:
            index = list_1.index(value)
        return list_2[index]
    return value


def get_location(seed):
    current_value = seed
    # hver gang vi finner en ny value i et av dictionariesene skal current_value bli oppdatert
    # Step 1 - seed to soil
    seed_list = seed_to_soil.get("seed")
    soil_list = seed_to_soil.get("soil")
    current_value = find_mapping(current_value, seed_list, soil_list)
    
    # Step 2 - soil to fertilizer
    stf_list1 = soil_to_fertilizer.get("soil")
    stf_list2 = soil_to_fertilizer.get("fertilizer")
    current_value = find_mapping(current_value, stf_list1, stf_list2)
    
    # Step 3 - fertilizer to water
    ftw_list1 = fertilizer_to_water.get("fertilizer")
    ftw_list2 = fertilizer_to_water.get("water")
    current_value = find_mapping(current_value, ftw_list1, ftw_list2)
    
    # Step 4 - water to light
    wtl_list1 = water_to_light.get("water")
    wtl_list2 = water_to_light.get("light")
    current_value = find_mapping(current_value, wtl_list1, wtl_list2)
    
    # Step 5 - light to temperature
    ltt_list1 = light_to_temperature.get("light")
    ltt_list2 = light_to_temperature.get("temperature")
    current_value = find_mapping(current_value, ltt_list1, ltt_list2)
    
    # Step 6 - temperature to humidity
    tth_list1 = temperature_to_humidity.get("temperature")
    tth_list2 = temperature_to_humidity.get("humidity")
    current_value = find_mapping(current_value, tth_list1, tth_list2)
    
    # Step 7 - humidity to location
    htl_list1 = humidity_to_location.get("humidity")
    htl_list2 = humidity_to_location.get("location")
    current_value = find_mapping(current_value, htl_list1, htl_list2)
    
    return current_value
            
locations = []

for seed in seeds:
    locations.append(get_location(int(seed)))

print(min(locations))
