import random
from itertools import combinations

card_points= ['K', 'Q', 'J','A', '10', '9', '8', '7', '6', '5', '4', '3', '2']
card_suites= ['Hearts', 'Clubs', 'Diamonds', 'Spades']

# Generate Cards
def generate_cards():
    all_cards = []
    for suite in card_suites:
        for value in card_points:
            all_cards.append(value+' '+suite)

    assert(len(all_cards)==52)

    return all_cards

all_cards = generate_cards()

# Return Points
def return_points(card):
    point, suite = card.split(' ')
    face_cards = ['A','K', 'Q', 'J', '10']
    if (point=='10' and suite == 'Diamonds'):
        points = 2
    elif point in face_cards:
        points = 1
    elif (point=='2' and suite == 'Clubs'):
        points = 1
    else:
        points = 0

    return points

#Strip Suite
def strip_suite(card):
        if card[1]==' ':
            stripped = card[0]
        else:
            stripped = card[:2]

        return stripped

#Return Value
def return_value(stripped):
    stripped
    try:
        value = int(stripped)
    except ValueError: #This means it is a face card
        if stripped == 'K':
            value = 14
        if stripped == 'Q':
            value = 13
        if stripped == 'J':
            value = 12
        if stripped == 'A':
            value = 11 #Deal with Ace equalling 1 later

    return value

#Return Possibilities
def return_possibilities(cards,type):
    all_possibilities = []
    values=[]
    for card in cards:
        values.append(card[1])
        all_possibilities.append(card[1])

    if type == "Face Up":
        combs = list(combinations(values,r=2))
        for comb in combs:
            total = (comb[0]+comb[1])
            if  total <= 14:
                all_possibilities.append(total)
    else:
        pass

    return all_possibilities

def draw_card(cards):
        card = random.choice(cards)
        value = return_value(strip_suite(card))
        points = return_points(card)
        all_cards.remove(card)

        return {card:[value,points]}

def dealing(cards):
    #First Draw
    cards = all_cards
    players={'player1':[],'player2':[]}
    for key in players:
        draw={}
        for i in range(0,6):
            draw.update(draw_card(cards))
        players.update({key:draw})

    # #Second Draw
    # for key in players:
    #     draw={}
    #     for i in range(0,3):
    #         card = random.choice(cards)
    #         value = return_value(strip_suite(card))
    #         points = return_points(card)
    #         all_cards.remove(card)
    #
    #         draw.update({card:[value,points]})
    #     players.update({key:draw})

    return players, all_cards

dealing(all_cards)

def starting_draw(cards):
    face_up = {}
    for i in range(0,4):
        card = random.choice(cards)
        value = return_value(strip_suite(card))
        points = return_points(card)
        all_cards.remove(card)

        face_up.update({card:[value,points]})

    return face_up, all_cards

def possible_moves(hand,face_up):
    face_up_possibilities = {}
    values={}
    for card in face_up.items():
        name = card[0]
        value = card[1][0]
        points = card[1][1]
        values.update({name:[value,points]})
        face_up_possibilities.update({name:[value,points]})
    # combs = list(combinations(values,r=2))
    # for comb in combs:
    #     total = (comb[0]+comb[1])
    #     if  total <= 14:
    #         face_up_possibilities.update({card:[total,'addition']})

    hand_possibilities={}
    values={}
    for card in hand.items():
        name = card[0]
        value = card[1][0]
        points = card[1][1]
        hand_possibilities.update({name:[value,points]})

    possible_moves = list(set(face_up_possibilities) & set(hand_possibilities))

    return possible_moves

def calculate_possibilities(face_up):
    face_up_possibilities = []
    values=[]
    for name, card in face_up.items():
        #name = card[0]
        value = card[0]
        #points = card[1][1]
        values.append(value)
        face_up_possibilities.append(value)
    combs = list(combinations(values,r=2))
    for comb in combs:
        total = (comb[0]+comb[1])
        if  total <= 14:
            face_up_possibilities.append(total)
    face_up_possibilities.sort()

    return face_up_possibilities
