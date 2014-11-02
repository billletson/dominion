from dominion import *

game = Game(Deck(optimal_big_money_w_ppr), Deck(basic_big_money))
print game.simulate(1000)
