import A06
import random

def dealCards(hands, cards, deck):
    all_players =   [[] for player in range(hands)]
    organizedDeck = list(deck)
    for card in range(cards):
        for hand in range(hands):
            if(organizedDeck):
                random_index = random.randint(0, len(organizedDeck) - 1)
                all_players[hand].append(organizedDeck.pop(random_index))
                print(f"Player {hand + 1} received {all_players[hand][-1]}")
    return all_players, organizedDeck

class Cards():
    cards=[]
    def create (self):
        self.cards=[]
        #Your program goes here
        #Construct the deck here
        self.cards = A06.createDeck()


    def shuffle (self):
        #Your program goes here
        #use constructed card deck by using "self.cards" and shuffle them
        A06.shuffleDeck(self.cards)

    def deal (self,hands,card_num):
        #Your program goes here
        #use constructed card deck by using "self.cards" and deal based on the number of hands, "hands", and number of cards in each hand, "num-cards", that are recevied from the user
        hands, updated_deck = dealCards(hands, card_num, self.cards)
        self.cards = updated_deck
        return hands

#initialte your programs with this functions
card_01 = Cards()
card_01.create()
card_01.shuffle()
hands = card_01.deal(3, 3) #Change X and Y 

print("\nDealt hands:")
for idx, hand in enumerate(hands):
    print(f"Player {idx + 1}: {hand}")

print(f"\nRemaining cards in deck: {len(card_01.cards)}")