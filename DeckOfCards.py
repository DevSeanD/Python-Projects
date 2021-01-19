import random
print("")
print("Deck of 52 Cards")

class Card: # Each card has the 2 values: Suit and Value
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self): # Method to output card values
        print("{} of {}".format(self.value,self.suit))

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
   
# main 
deck = Deck()
deck.shuffle()
print("")
print("Shuffled Cards")
print("")
deck.show()
print("")
