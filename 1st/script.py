
array = []
with open("all_data.txt") as f:
    data = f.read().split('\n')
    for line in data:
        number = [int(i) for i in line if i.isdigit()]
        combined_number = int(str(number[0])+str(number[-1]))
        array.append(combined_number)

print(sum(array))