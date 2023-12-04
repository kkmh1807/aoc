import math

data = open("input.txt").read().split('\n')    

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

def p2(input):
    total_cards = 0
    card_dict = {}
    for line in input:
        winning_numbers_found = 0
        card = int(line.split(":")[0].split(" ")[-1])
        
        winning_numbers = line.split(": ")[1].split(" | ")[0].split()
        card_numbers = line.split(": ")[1].split(" | ")[-1].split()

        for number in card_numbers:
            if number in winning_numbers:
                winning_numbers_found += 1
        
        next_numbers = [i for i in range (card+1, card+winning_numbers_found+1)]
        
        if card not in card_dict:
            card_dict[card] = (next_numbers, 1)
    
    for card, items in card_dict.items():
        for i in range(len(items[0])):
            card_dict[card + i + 1] = (card_dict[card + i + 1][0], card_dict[card + i + 1][1] + items[1])
    
    for card_amount in card_dict.values():
        total_cards += card_amount[1]
    
    print(total_cards)

p2(data)
        