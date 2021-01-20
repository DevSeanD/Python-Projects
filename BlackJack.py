"""
BlackJack.py
DevSeanD
1/18/2020
"""
import random
import sys

class Card: # Each card has the 2 values: Suit and Value
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self): # Method to output card values 
        print("{} of {}".format(self.value,self.suit))

    def returnVal(self):
        return self.value

class Deck: 
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Diamonds", "Hearts", "Clubs", "Spades"]:
            for v in range(2,11):
                self.cards.append(Card(s,v))
        for s in ["Diamonds", "Hearts", "Clubs", "Spades"]:
            self.cards.append(Card(s,"Ace"))
            self.cards.append(Card(s,"Jack"))
            self.cards.append(Card(s,"Queen"))
            self.cards.append(Card(s,"King"))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.playerHand = []
    
    def draw(self,deck):
        self.playerHand.append(deck.drawCard())
        return self
    
    def playerCountHand(self):
        handTotal = 0
        for card in self.playerHand:
            temp = card[:1] 
            handTotal += temp 
            
    def showHand(self):
        for card in self.playerHand:
            card.show()
            
    def addHand(self):
        total = 0
        for card in self.playerHand:
            if(isinstance(card.returnVal(), int)):
                total += card.returnVal()
            if(card.returnVal() == "Ace"):
                ask = input("Would you like to use the Ace as a 1 or an 11? Type 1 for 1 and 11 for 11.\n")
                if(ask == "1"):
                    total += 1
                if(ask == "11"):
                    total += 11
            if(card.returnVal() == "Jack") or (card.returnVal() == "Queen") or (card.returnVal() == "King"):
                total += 10

        return total

 
   
# main 
print("")
print("")
print("=========================")
print("| Welcome To Black Jack |")
print("=========================")
print("")
print("")

deck = Deck()
deck.shuffle()

player1 = Player()
player1.draw(deck)
player1.draw(deck)

player2 = Player()
player2.draw(deck)
player2.draw(deck)
player2HandTotal = player2.addHand()

player1.showHand()
player1HandTotal = player1.addHand()

playerInput = input("(1) Hit (2) Stay \n")

if(playerInput == "2"):
    print("Stay")
    if(player1HandTotal <= 21) and (player1HandTotal > player2HandTotal):
        print("You Win!")
    if(player1HandTotal <= 21) and (player1HandTotal < player2HandTotal):
        print("You Lose!")
    if(player1HandTotal <= 21) and (player1HandTotal == player2HandTotal):
        print("You Tied!")
    sys.exit()

player1.draw(deck)
player1HandTotal = player1.addHand()
player1.showHand()

if(player1HandTotal > 21):
    print("You have busted")
if(player2HandTotal > 21):
    print("You Win! Your opponent busted")
if(player1HandTotal < 21) and (player2HandTotal < 21) and (player1HandTotal > player2HandTotal):
    print("You Win!")
if(player1HandTotal == 21) and (player2HandTotal == 21):
    print("You Tied!")
if(player1HandTotal == 21) and (player2HandTotal != 21):
    print("You Win!")
if(player1HandTotal < 21) and (player2HandTotal < 21) and (player1HandTotal < player2HandTotal):
    print("You Lose!")
