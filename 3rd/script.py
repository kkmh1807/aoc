

grid = open("input.txt").read().splitlines()

def p1(input_grid):
    correct_coordinates = set()

    for row_num, row in enumerate(input_grid):
        for col_num, chr in enumerate(row):
            if chr.isdigit() or chr==".":
                continue
            for col_row in range(row_num - 1, row_num + 2):
                for col_col in range(col_num -1, col_num + 2):
                    if col_row < 0  or col_row >= len(input_grid) or col_col >= len(input_grid[col_row]) or not input_grid[col_row][col_col].isdigit():
                        continue
                    while col_col > 0 and input_grid[col_row][col_col-1].isdigit():
                        col_col -= 1
                    correct_coordinates.add((col_row, col_col))

    array = []

    for row, col in correct_coordinates:
        number = ""
        while col < len(grid[row]) and grid[row][col].isdigit():
            number += grid[row][col]
            col += 1
        array.append(int(number))
        
    print(sum(array))


def p2(input_grid):
    product = 0
    for row_num, row in enumerate(input_grid):
        for col_num, chr in enumerate(row):
            if chr != "*":
                continue
            
            correct_coordinates = set()

            for col_row in range(row_num - 1, row_num + 2):
                for col_col in range(col_num -1, col_num + 2):
                    if col_row < 0  or col_row >= len(input_grid) or col_col >= len(input_grid[col_row]) or not input_grid[col_row][col_col].isdigit():
                        continue
                    while col_col > 0 and input_grid[col_row][col_col-1].isdigit():
                        col_col -= 1
                    correct_coordinates.add((col_row, col_col))

            if len(correct_coordinates) != 2:
                continue
    
            array = []

            for row, col in correct_coordinates:
                number = ""
                while col < len(input_grid[row]) and input_grid[row][col].isdigit():
                    number += input_grid[row][col]
                    col += 1
                array.append(int(number))
                
            product += array[0] * array[1]
    
    print(product)

p2(grid)
