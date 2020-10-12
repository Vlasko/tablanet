from functions import generate_cards, dealing, starting_draw, calculate_possibilities

#Game Starts
all_cards = generate_cards()

hands, left_cards = dealing(all_cards)

face_up, left_cards_two = starting_draw(left_cards)

hands['player1']
hands['player2']
face_up

# # This is how you delete an entry in a dictionary

assert(len(left_cards_two)==36)

calculate_possibilities(face_up)

actions=[]
for name, card in hands['player1'].items():
    value = card[0]
    points = card[1]
    if value in calculate_possibilities(face_up):
        actions.append([points, [value,name]])

actions.sort(reverse=True)
actions[0]

name = actions[0][1][1]

# Remove Card from Hand
del hands['player1'][name]
# Remove Card from Centre
del face_up

# At this point I want to look up those cards from the centre that have the value equal
# to the card that I have just discarded from my hand.

## It seems wise to move towards OOP, which should allow a card to have multiple
## characteristics that can be called on, like value, name and points
