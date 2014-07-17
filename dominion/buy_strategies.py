def basic_big_money(deck):
    value = deck.hand_value()
    if value >= 8:
        return 'Province'
    elif 6 <= value <= 7:
        return 'Gold'
    elif 3 <= value <= 5:
        return 'Silver'


def basic_big_money_w_estate(deck):
    value = deck.hand_value()
    if value >= 8:
        return 'Province'
    elif 6 <= value <= 7:
        return 'Gold'
    elif 3 <= value <= 5:
        return 'Silver'
    elif value == 2:
        return 'Estate'


def basic_big_money_w_copper(deck):
    value = deck.hand_value()
    if value >= 8:
        return 'Province'
    elif 6 <= value <= 7:
        return 'Gold'
    elif 3 <= value <= 5:
        return 'Silver'
    else:
        return 'Copper'


def basic_big_money_w_duchy(deck):
    value = deck.hand_value()
    if value >= 8:
        return 'Province'
    elif 6 <= value <= 7:
        return 'Gold'
    elif value == 5:
        return 'Duchy'
    elif 3 <= value <= 5:
        return 'Silver'


def basic_big_money_always_buy(deck):
    value = deck.hand_value()
    if value >= 8:
        return 'Province'
    elif 6 <= value <= 7:
        return 'Gold'
    elif value == 5:
        return 'Duchy'
    elif 3 <= value <= 5:
        return 'Silver'
    elif value == 2:
        return 'Estate'
    else:
        return 'Copper'


def optimal_big_money(deck):
    value = deck.hand_value()
    provinces = deck.remaining_provinces()
    if value >= 8:
        if deck.count_card('Gold') == 0:
            return "Gold"
        else:
            return 'Province'
    if 6 <= value <= 7:
        if provinces <= 4:
            return "Duchy"
        else:
            return "Gold"
    elif value == 5:
        if provinces <= 5:
            return 'Duchy'
        else:
            return 'Silver'
    elif 3 <= value <= 4:
        if provinces <= 2:
            return "Estate"
        else:
            return "Silver"
    elif value == 2 and provinces <= 3:
        return 'Estate'


def optimal_big_money_w_ppr(deck):
    value = deck.hand_value()
    provinces = deck.remaining_provinces()
    if 0 < deck.deficit < 3 and provinces == 2 and value >= 5:
        return 'Duchy'
    elif value >= 8:
        if deck.count_card('Gold') == 0:
            return "Gold"
        else:
            return 'Province'
    elif 6 <= value <= 7:
        if provinces <= 4:
            return "Duchy"
        else:
            return "Gold"
    elif value == 5:
        if provinces <= 5:
            return 'Duchy'
        else:
            return 'Silver'
    elif 3 <= value <= 4:
        if provinces <= 2:
            return "Estate"
        else:
            return "Silver"
    elif value == 2 and provinces <= 3:
        return 'Estate'
