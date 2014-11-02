from __future__ import division
import random
from .game import Game
from .cards import VALUES, SCORES, COSTS
import itertools


class Deck:
    start = ['copper'] * 7 + ['estate'] * 3

    def __init__(self, buy_strategy):
        self.library = []
        self.discard = []
        self.hand = []
        self.turns = 0
        self.reset()
        self.buy_strategy = buy_strategy
        self.game = Game(self)

    def turn(self):
        self.buy()
        self.new_hand()
        self.turns += 1

    def new_hand(self):
        self.discard += self.hand
        if len(self.library) >= 5:
            self.hand = self.library[:5]
            self.library = self.library[5:]
        else:
            self.hand = self.library[:]
            random.shuffle(self.discard)
            self.library = self.discard[:]
            self.discard = []
            remaining = 5 - len(self.hand)
            self.hand += self.library[:remaining]
            self.library = self.library[remaining:]

    def hand_value(self):
        return sum([VALUES.get(x, 0) for x in self.hand])

    def deck_score(self):
        return sum([SCORES.get(x, 0) for x in self.library + self.discard + self.hand])

    def deck_size(self):
        return len(self.library) + len(self.discard) + len(self.hand)

    def count_card(self, card):
        return sum([1 for x in self.library + self.discard + self.hand if x == card])

    def reset(self):
        self.library = self.start[:]
        random.shuffle(self.library)
        self.discard = []
        self.hand = []
        self.new_hand()
        self.turns = 0

    def buy(self):
        strategy = itertools.tee(self.buy_strategy(self), 1)[0]
        budget = self.hand_value()
        for card in strategy:
            if COSTS[card] <= budget and self.game.buy_card(card):
                self.discard.append(card)
                break

    def solitaire_benchmarks(self, iterations=10000):
        time = []
        scores = []
        for _ in xrange(iterations):
            while self.count_card('province') < 4:
                self.turn()
            time.append(self.turns)
            scores.append(self.deck_score())
            self.reset()
        return sum(time)/iterations, sum(scores)/iterations

    def remaining_cards(self, card):
        return self.game.remaining_cards(card)

    def deficit(self):
        return self.game.leading_score() - self.deck_score

