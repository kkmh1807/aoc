
with open("input.txt") as f:
    content = f.read().split("\n")

def find_strength(array):
    # Five of a kind
    if 5 in array:
        return 7
    # Four of a kind
    if 4 in array:
        return 6
    # Full house
    if array.count(2) == 2 and array.count(3) == 3:
        return 5
    # Three of a kind
    if 3 in array:
        return 4
    # Two pairs
    if array.count(2) == 4:
        return 3
    # One pair
    if 2 in array:
        return 2
    # High card
    if all(i == array[0] for i in array):
        return 1

def p1(data):
    labels = "AKQJT98765432"
    cards_to_compare = {}
    
    for line in data:
        hand, bid = line.split()
        num_cards = [hand.count(chr) for chr in hand]
        cards_to_compare[hand,bid] = ([labels.index(chr) for chr in hand], find_strength(num_cards))
    
    sorted_cards = sorted(cards_to_compare.items(), key=lambda x: (x[1][1], -x[1][0][0], -x[1][0][1], -x[1][0][2],-x[1][0][3],-x[1][0][4]))
    
    total = []
    for rank, plays in enumerate(sorted_cards, 1):
        play, ranking_basis = plays
        print(rank, plays)
        total.append(rank * int(play[1]))
    
    print(sum(total))
# p1(content)

def generate_array_w_joker(array):
    new_array = []
    if "J" in array:
        # If a hand only consists of joker-cards
        if (len(set(array)) == 1):
            new_array = [5,5,5,5,5]
        else:
            copy = [i for i in array if type(i) == int]
            highest_card = max(copy)
            for element in array:
                if(element == highest_card):
                    new_array.append(element+array.count("J"))
                elif element == "J":
                    new_array.append(1)
                else:
                    new_array.append(element)
    else:
        new_array = array
    return new_array

def p2(data):
    labels = "AKQT98765432J"
    cards_to_compare = {}

    for line in data:
            hand, bid = line.split()
            num_cards = []
            for chr in hand:
                if chr == "J":
                    num_cards.append("J")
                else:
                    num_cards.append(hand.count(chr))
                    
            print(hand, num_cards)
            best_hand = generate_array_w_joker(num_cards)
            print(hand, best_hand)
            cards_to_compare[hand,bid] = ([labels.index(chr) for chr in hand], find_strength(best_hand))
    
    sorted_cards = sorted(cards_to_compare.items(), key=lambda x: (x[1][1], -x[1][0][0], -x[1][0][1], -x[1][0][2],-x[1][0][3],-x[1][0][4]))

    total = []
    for rank, plays in enumerate(sorted_cards, 1):
        play, ranking_basis = plays
        # print(rank, plays)
        total.append(rank * int(play[1]))

    print(sum(total))

    # print(data)
    
p2(content)