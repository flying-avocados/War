import random

class Card(object):
    def __init__(self, rank, suite):
        self.suite = suite #from 0 to 3
        self.rank = rank # from 0 to 12

    def getString(self):
        rankString = '23456789TJQKA'[self.rank]
        suiteString = 'CDHS'[self.suite]
        return rankString + ' of ' + suiteString 

class Deck(object):
    def __init__(self):
        self.cards = [ ]
        for suite in range(4):
            for rank in range(13):
                self.cards.append(Card(rank, suite))
        random.shuffle(self.cards)

    def cardsLeft(self):
        return len(self.cards)

    def dealCard(self):
        return None if (self.cards == [ ]) else self.cards.pop()

class War(object):
    def __init__(self):
        self.deck = Deck()
        self.rounds = 0
        self.playerDeck = [] 
        self.computerDeck = []
        self.warCards = [] 

    def starting(self):
        for i in range(26):
                self.playerDeck.append(self.deck.dealCard())
                self.computerDeck.append(self.deck.dealCard())

    def askYesOrNo(self, prompt):
        while True:
            result = input(prompt + ' [y]es or [n]o --> ').lower()
            if (result == 'y'): return True
            elif (result == 'n'): return False
            else: print('Please enter y or n!')

    def play(self):
        self.starting()
        while True:
            self.playTurn()
            if (not self.askYesOrNo('Keep playing?')):
                break
        print("Game over!")

    def playTurn(self):
        if (self.playerDeck == 0 or self.computerDeck == 0): False 
       
        playerCard = self.playerDeck.pop()
        print(f"Your card is {playerCard.getString()}")
        computerCard = self.computerDeck.pop()
        print(f"Computer's card is {computerCard.getString()}")
        
        if (playerCard.rank==computerCard.rank):
            self.warCards.append(playerCard)
            self.warCards.append(computerCard)
            self.war(1) 

        elif (playerCard.rank>computerCard.rank):
            self.playerWin(playerCard,computerCard)
                    
        else: 
            self.computerWin(playerCard, computerCard)
            

    def playerWin(self, playerCard, computerCard):
        print("You have higher rank")
        self.playerDeck.append(playerCard)
        self.playerDeck.append(computerCard)
        print(f"# of your cards: {len(self.playerDeck)}")
        print(f"# of computer cards: {len(self.computerDeck)}") 

    def computerWin(self, playerCard, computerCard):
        print("Computer has higher rank")
        self.computerDeck.append(playerCard)
        self.computerDeck.append(computerCard)
        print(f"# of your cards: {len(self.playerDeck)}")
        print(f"# of computer cards: {len(self.computerDeck)}") 

    def war(self, count): 
        print("WAR")
        self.warCards.append(self.playerDeck.pop()) # playerCardDown 
        self.warCards.append(self.computerDeck.pop()) # computerCardDown
        playerCardUp = self.playerDeck.pop()
        computerCardUp  = self.computerDeck.pop()
        self.warCards.append(playerCardUp) 
        self.warCards.append(computerCardUp)
        print(f"Your card is {playerCardUp.getString()}")
        print(f"Computer's card is {computerCardUp.getString()}")
        if playerCardUp.rank == computerCardUp.rank:
            self.war(count+1)
        elif (playerCardUp.rank>computerCardUp.rank):
            print("You have higher rank")
            while (self.warCards != [ ]):
                self.playerDeck.append(self.warCards.pop()) 
            print(f"# of your cards: {len(self.playerDeck)}")
            print(f"# of computer cards: {len(self.computerDeck)}") 
            print("War over")
        else:
            print("Computer has higher rank")
            while (self.warCards != [ ]):
                self.computerDeck.append(self.warCards.pop()) 
            print(f"# of your cards: {len(self.playerDeck)}")
            print(f"# of computer cards: {len(self.computerDeck)}") 
            print("War over")

def main ():
    game = War()
    game.play() 

if __name__ == '__main__':
    main()
