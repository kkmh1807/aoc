

grid = open("test.txt").read().splitlines()
correct_coordinates = set()


for row_num, row in enumerate(grid):
    for col_num, chr in enumerate(row):
        if chr.isdigit() or chr==".":
            continue
        for col_row in range(row_num - 1, row_num + 2):
            for col_col in range(col_num -1, col_num + 2):
                if col_row < 0  or col_row >= len(grid) or col_col >= len(grid[col_row]) or not grid[col_row][col_col].isdigit():
                    continue
                while col_col > 0 and grid[col_row][col_col-1].isdigit():
                    col_col -= 1
                correct_coordinates.add((col_row, col_col))

print(correct_coordinates)

array = []

for row, col in correct_coordinates:
    number = ""
    while col < len(grid[row]) and grid[row][col].isdigit():
        number += grid[row][col]
        col += 1
    array.append(int(number))
     
print(sum(array))
