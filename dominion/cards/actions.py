ACTIONS = {}


def cellar(deck):
    raise NotImplementedError


def chapel(deck):
    raise NotImplementedError


def moat(deck):
    for _ in xrange(2):
        deck.draw()


def chancellor(deck):
    raise NotImplementedError


def village(deck):
    deck.draw()
    deck.actions += 2


def woodcutter(deck):
    deck.buy += 1
    deck.bonus_treasure += 2


def workshop(deck):
    raise NotImplementedError


def smithy(deck):
    for _ in xrange(3):
        deck.draw()


ACTIONS['smithy'] = smithy