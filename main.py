from dominion import *
#deck = Deck(taper_big_money)

#print deck.solataire_benchmarks(10)

game = Game(Deck(optimal_big_money_w_ppr), Deck(basic_big_money))
print game.simulate()
