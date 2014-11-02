def basic_big_money(deck):
    yield 'province'
    yield 'gold'
    yield 'silver'


def basic_big_money_w_estate(deck):
    yield 'province'
    yield 'gold'
    yield 'silver'
    yield 'estate'


def basic_big_money_w_copper(deck):
    yield 'province'
    yield 'gold'
    yield 'silver'
    yield 'copper'


def basic_big_money_w_duchy(deck):
    yield 'province'
    yield 'gold'
    yield 'duchy'
    yield 'silver'


def basic_big_money_always_buy(deck):
    yield 'province'
    yield 'gold'
    yield 'duchy'
    yield 'silver'
    yield 'estate'
    yield 'copper'


def optimal_big_money(deck):
    provinces = deck.remaining_cards('province')
    if deck.count_card('Gold') == 0:
        yield "gold"
    yield 'province'
    if provinces <= 5:
        yield "duchy"
    yield "gold"
    if provinces <= 2:
        yield "estate"
    yield "silver"
    yield 'estate'


def optimal_big_money_w_ppr(deck):
    provinces = deck.remaining_cards('province')
    if 0 < deck.deficit < 3 and provinces == 2:
        yield 'duchy'
    if deck.count_card('gold') == 0:
        yield "gold"
    yield 'province'
    if provinces <= 5:
        yield 'duchy'
    yield 'gold'
    if provinces <= 2:
        yield "estate"
    yield 'silver'
    if provinces <= 3:
        yield 'estate'


def smithy_bm(deck):
    if deck.count_card('smithy') < 1:
        yield 'smithy'
    yield 'province'
    yield 'gold'
    yield 'silver'


def optimized_smithy_bm(deck):
    provinces = deck.remaining_cards('province')
    if 0 < deck.deficit < 3 and provinces == 2:
        yield 'duchy'
    if deck.count_card('gold') == 0:
        yield "gold"
    yield 'province'
    if deck.count_card('smithy') < 1:
        yield 'smithy'
    if provinces <= 5:
        yield 'duchy'
    yield 'gold'
    if provinces <= 2:
        yield "estate"
    yield 'silver'
    if provinces <= 3:
        yield 'estate'
