from .actions import ACTIONS


def cellar(deck):
    discard_list = ['copper'] + ACTIONS.keys()
    return [x for x in deck.hand if x in discard_list]


def chapel(deck):
    return [x for x in deck.hand if x == 'copper']
