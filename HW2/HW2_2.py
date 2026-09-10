import random

values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
suits = ["S","C","D","H"]

n_draws = 5

def zip_into_deck(values: list, suits: list)-> dict:
    deck = []
    for v in values:
        cards = []
        for s in suits:
            card = str(v) + s
            cards.append(card)
        deck.append(cards)
    return deck


deck = zip_into_deck(values, suits)


searching = True

def pick_value_from_deck(deck:list)-> int:
    return random.randrange(len(deck))
    
def find_straight(deck: list, hand : list)->list:
    

    for i in range(1, n_draws):

        if len(hand) > 4:
            break
        
        picked_value = pick_value_from_deck(deck)
        print(f"i : {i}, pv : {picked_value}")
        if len(hand)== 0:
            hand.append(pick_value_from_deck(deck))
            continue
        

        hand.append(picked_value)
        if len(hand) > 1:

            if picked_value != 13 and 13 not in hand:
                print("not handling 13 case")
                if abs(hand[i-1] - picked_value) > 5:
                    print(f"Impossible to create straight: {abs(hand[i-1] - picked_value)}, {hand[i-1]}, {picked_value}")
                    hand = []
                    i = 1


                
                else:
                    print(f"appending {picked_value} to {hand}" )
                    hand.append(picked_value)
  
            else:
                if  picked_value not in [10,11,12,13,1]:
                    # print("Impossible to create straight")
                    hand = []
                    i=1


                else:
                    # print(f"appending {picked_value} to {pull}" )
                    hand.append(picked_value)
            




hand = []    
while len(hand) < 1:
    find_straight(deck, hand)

print(hand)


