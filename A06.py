import random

def createDeck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suits = ["s", "h", "d", "c"]
    combine = []

    for i in values:
        for j in suits:
            combine.append(i + j)
    return combine

def shuffleDeck(deck):
    organizedDeck = list(deck)
    random.shuffle(deck)

    return organizedDeck, deck