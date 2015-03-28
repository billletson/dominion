import card_strategies

ACTIONS = {}


def cellar(deck, strategy=card_strategies.cellar):
    """
    +1 Action
    Discard any number of cards.
    +1 Card per card discarded.
    """
    deck.actions += 1
    draws = 0
    for card in strategy(deck):
        if card in deck.hand:
            deck.discard(card)
            draws += 1
    for _ in xrange(draws):
        deck.draw()


def chapel(deck, strategy=card_strategies.chapel):
    """
    Trash up to 4 cards from your hand.
    """
    for card in strategy(deck):
        if card in deck.hand:
            deck.trash(card)


def moat(deck):
    """
    +2 Cards
    When another player plays an Attack
    card, you may reveal this from your
    hand. If you do, you are unaffected
    by that Attack.
    """
    for _ in xrange(2):
        deck.draw()


def chancellor(deck, strategy=card_strategies.chancellor):
    """
    +(2)
    You may immediately put your
    deck into your discard pile.
    """
    if strategy(deck):
        deck.discard_pile += deck.library
        deck.library = []


def village(deck):
    """
    +1 Card
    +2 Actions
    """
    deck.draw()
    deck.actions += 2


def woodcutter(deck):
    """
    +1 Buy
    +(2)
    """
    deck.buy += 1
    deck.bonus_treasure += 2


def workshop(deck):
    """
    Gain a card costing up to (4).
    """
    raise NotImplementedError


def bureaucrat(deck):
    """
    Gain a silver card;
    put it on top of your deck.
    Each other player reveals a Victory card
    from his hand and puts it on his deck
    (or reveals a hand with no Victory cards)
    """
    raise NotImplementedError


def feast(deck):
    """
    Trash this card.
    Gain a card costing up to (5).
    """
    raise NotImplementedError


def smithy(deck):
    """
    +3 Cards
    """
    for _ in xrange(3):
        deck.draw()


ACTIONS['smithy'] = smithy