from typing import List
from card import Card
from utils import Suits
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.player_hand = []
        self.cpu_hand = []
    
    def create_decks(self):
        # we need to create a card for each value for each set
        suits = Suits
        for num in range(2,14):
            self.cards.append(Card(suits.CLUBS, num))
            self.cards.append(Card(suits.DIAMONDS, num))
            self.cards.append(Card(suits.HEARTS, num))
            self.cards.append(Card(suits.SPADES, num))
        random.shuffle(self.cards)

    def deck_split(self):
        isplayer_card = True
        
        for c in self.cards:
            if isplayer_card:
                self.player_hand.append(c)
                isplayer_card = False
            else:
                self.cpu_hand.append(c)
                isplayer_card = True
