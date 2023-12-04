import math

data = open("test.txt").read().split('\n')    

def p1(input):
    points = 0
    for line in input:
        winning_numbers = line.split(": ")[1].split(" | ")[0].split()
        card_numbers = line.split(": ")[1].split(" | ")[-1].split()
        
        winning_numbers_found = 0
        for number in card_numbers:
            if number in winning_numbers:
                winning_numbers_found += 1
               
        total = math.floor(1*(2**(winning_numbers_found-1)))
        points += total

    print(points)
    
# p1(data)

        