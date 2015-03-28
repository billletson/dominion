from __future__ import division
import random
from .game import Game
from .cards import VALUES, SCORES, COSTS, ACTIONS
import itertools


class Deck:
    start = ['copper'] * 7 + ['estate'] * 3

    def __init__(self, buy_strategy, action_strategy):
        self.library = []
        self.discard_pile = []
        self.hand = []
        self.set_asides = []
        self.turns = 0
        self.reset()
        self.buy_strategy = buy_strategy
        self.action_strategy = action_strategy
        self.game = Game(self)
        self.buys = 1
        self.actions = 1
        self.bonus_treasure = 0

    def turn(self):
        self.buys = 1
        self.actions = 1
        self.bonus_treasure = 0
        self.action()
        self.buy()
        self.new_hand()
        self.turns += 1

    def new_hand(self):
        self.discard_pile += self.hand
        self.hand = []
        while len(self.hand) < 5:
            self.draw()

    def draw(self):
        if not self.library:
            random.shuffle(self.discard_pile)
            self.library = self.discard[:]
            self.discard_pile = []
        self.hand.append(self.library[0])
        self.library = self.library[1:]

    def hand_value(self):
        return sum([VALUES.get(x, 0) for x in self.hand]) + self.bonus_treasure

    def deck_score(self):
        return sum([SCORES.get(x, 0) for x in self.library + self.discard_pile + self.hand])

    def deck_size(self):
        return len(self.library) + len(self.discard_pile) + len(self.hand)

    def count_card(self, card):
        return sum([1 for x in self.library + self.discard_pile + self.hand if x == card])

    def reset(self):
        self.library = self.start[:]
        random.shuffle(self.library)
        self.discard_pile = []
        self.hand = []
        self.new_hand()
        self.turns = 0

    def buy(self):
        budget = self.hand_value()
        while self.buys > 0:
            strategy = itertools.tee(self.buy_strategy(self), 1)[0]
            for card in strategy:
                if COSTS[card] <= budget and self.game.buy_card(card):
                    self.discard_pile.append(card)
                    budget -= COSTS[card]
                    self.buys -= 1
                    break
            else:
                self.buys = 0

    def action(self):
        while self.actions > 0:
            strategy = itertools.tee(self.action_strategy(self), 1)[0]
            for card in strategy:
                if card in self.hand:
                    self.set_aside(card)
                    ACTIONS[card](self)
                    self.actions -= 1
                    break
            else:
                self.actions = 0

    def discard(self, card):
        self.discard_pile.append(self.hand.pop(self.hand.index(card[0])))

    def set_aside(self, card):
        self.set_asides = self.hand.pop(self.hand.index(card[0]))

    def return_set_asides(self):
        self.hand += self.set_asides
        self.set_asides = []

    def discard_set_asides(self):
        self.discard_pile += self.set_asides
        self.set_asides = []

    def trash(self, card):
        self.hand.pop(self.hand.index(card[0]))

    def solitaire_benchmarks(self, iterations=10000):
        time = []
        scores = []
        for _ in xrange(iterations):
            while self.count_card('province') < 4:
                self.turn()
            time.append(self.turns)
            scores.append(self.deck_score())
            self.reset()
            self.game.reset()
        return sum(time)/iterations, sum(scores)/iterations

    def remaining_cards(self, card):
        return self.game.remaining_cards(card)

    def deficit(self):
        return self.game.leading_score() - self.deck_score

