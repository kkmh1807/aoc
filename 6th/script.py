import numpy 

data = open("input.txt").read().split("\n")

times = [int(i) for i in data[0].split(":")[-1].split()]
distances = [int(i) for i in data[1].split(":")[-1].split()]


def generate_options(array):
    all_possible_holds = []
    for i in range(array[0]+1):
        final_distance = i * (array[0] - i)
        if(final_distance > array[1]):
            all_possible_holds.append([i, final_distance])
    return len(all_possible_holds)

def p1(times, distances):
    games_dict = {}

    for i in range(len(times)):
        if (times[i], distances[i]) not in games_dict:
            games_dict[(times[i], distances[i])] = generate_options([times[i], distances[i]])
        
    sum = []
    for values in games_dict.values():
        sum.append(values)
    
    print(numpy.prod(sum))
    
# p1(times, distances)

def p2(times, distances):
    new_time = ""
    new_dist = ""
    for time in times:
        new_time += str(time)
    for dist in distances:
        new_dist += str(dist)

    print(generate_options([int(new_time), int(new_dist)]))

p2(times, distances)