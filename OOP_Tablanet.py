import random
from itertools import combinations

class Game:
    def __init__(self):
        self.players=[adam,bob]

    def drawHand(self):
        adam.draw(deck)
        bob.draw(deck)

    lastTaker=''
    def runHand(self):
        global lastTaker
        while len(self.players[0].hand) + len(self.players[1].hand) > 0:
            for player in self.players:
                try:
                    player.pickupMove(player.possibleMoves(table))
                    lastTaker=player
                except IndexError:
                    player.dropCard(table, player.hand[0])

class Card:
    def __init__(self, suite, rank, points, value):
        self.suite = suite
        self.rank = rank
        self.points = points
        self.value = value
        self.id = rank + ' ' + suite

    def show(self):
        print("{} {}".format(self.id, self.points))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suites = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['K', 'Q', 'J', 'A', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        face_cards = ['A','K', 'Q', 'J', '10']

        def return_value(rank):
            try:
                value = int(rank)
            except ValueError: #This means it is a face card
                if rank == 'K':
                    value = 14
                if rank == 'Q':
                    value = 13
                if rank == 'J':
                    value = 12
                if rank == 'A':
                    value = 11 #Deal with Ace equalling 1 later

            return value

        for suite in suites:
            for rank in ranks:
                if (rank=='10' and suite == 'Diamonds'):
                    points = 2
                    value = return_value(rank)
                elif rank in face_cards:
                    points = 1
                    value = return_value(rank)
                elif (rank=='2' and suite == 'Clubs'):
                    points = 1
                    value = return_value(rank)
                else:
                    points = 0
                    value = return_value(rank)

                self.cards.append(Card(suite, rank, points, value))

    def show(self):
        for card in self.cards:
            card.show()

    def draw(self):
        index = random.randint(0,len(self.cards)-1)
        try:
            return self.cards.pop(index)
        except IndexError:
            print('Index Error',index)
            print(self.cards[index])

    def left(self):
        return len(self.cards)

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.stack = []
        self.points = 0

    def draw(self,deck):
        for i in range(0,6):
            self.hand.append(deck.draw())
        return self

    def showHand(self):
        print(self.name)
        for card in self.hand:
            card.show()

    def showStack(self):
        print(self.name)
        for card in self.stack:
            card.show()

    def scoreStack(self):
        pass
        self.points=0
        #Start here
        if len(self.stack) > 26:
            self.points +=3
        else:
            pass

        for card in self.stack:
            self.points += card.points

        return self.points

    def moveCard(self,toRemove):
        object = [card for card in self.hand if card == toRemove][0]
        self.hand.remove(object)
        # Add in removal of card(s) from table
        self.stack.append(object)
        print('cards moved', object)
        # This does not keep adding points
        # self.points=+object.points

    def dropCard(self, table, toRemove):
        object = [card for card in self.hand if card == toRemove][0]
        self.hand.remove(object)
        table.hand.append(object)

    def possibleMoves(self, table):
        handOptions={}
        for card in self.hand:
            handOptions.update({card:card.value})

        tableOptions={}
        for card in table.hand:
            tableOptions.update({card:card.value})

        combins = list(combinations(tableOptions,r=2))
        for comb in combins:
            total = comb[0].value + comb[1].value
            if total <15:
                tableOptions.update({comb:total})
                # tableOptions.update({card:card.value})

        possible = set(handOptions.values()) & set(tableOptions.values())
        moves = {}
        for possiblity in list(possible):
            for handCard, handValue in handOptions.items():
                if handValue == possiblity:
                    moves.update({possiblity:[handCard]})
            for tableCard, tableValue in tableOptions.items():
                tableCards=[]
                if tableValue == possiblity:
                    tableCards.append(tableCard)
                    moves[possiblity].append(tableCards)
        # This does not yet work for picking up more than one card

        return moves

    def pickupMove(self,moves):
        possible = list(moves.keys())
        # try:
        handCard = moves[possible[-1]][0]
        self.moveCard(handCard)
        pickup = moves[list(possible)[-1]][1][0]
        if type(pickup) == tuple:
            for pickupCard in pickup:
                table.moveCard(pickupCard, self)
        else:
            table.moveCard(pickup,self)


        # except IndexError:
        #     self.moveCard(moves[possible[-1]][0])
        #     firstCard = list(moves[possible[-1]][1][0])[0]
        #     secondCard = list(moves[possible[-1]][1][0])[1]
        #     table.moveCard(firstCard)
        #     table.moveCard(secondCard)

    def dropMove(self):
        try:
            index = random.randint(0,len(self.hand))
            self.dropCard(table, self.hand[index])
        except IndexError:
            #No cards left in hand
            pass

class Table:
    def __init__(self,deck):
        self.hand = []
        for i in range(0,4):
            self.hand.append(deck.draw())

    def cleanUp(self,lastTaker):
        for card in list(table.hand):
            self.moveCard(card, lastTaker)

    def show(self):
        print('Table')
        for card in self.hand:
            card.show()

    def moveCard(self,toRemove, player):
        object = [card for card in self.hand if card == toRemove][0]
        # print(object.id)
        self.hand.remove(object)
        player.stack.append(object)

#Intialise deck, player and
game = Game()
deck = Deck()
adam = Player("Adam")
bob = Player("Bob")
players = [adam,bob]
assert(deck.left()==52)

# Draw cards for Adam, Bob and Table
game.drawHand()
table = Table(deck)
assert(deck.left()==36)
game.runHand()

# Hands two, three and four
left = 24
for i in range(0,3):
    game.drawHand()
    assert(deck.left()==left)
    game.runHand()
    left -= 12

table.show()
table.cleanUp(lastTaker)
table.show()

adam.scoreStack()
bob.scoreStack()
