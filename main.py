from dominion import *

game = Game(Deck(buy_strategies.optimized_smithy_bm, action_strategies.smithy),
            Deck(buy_strategies.optimal_big_money_w_ppr, action_strategies.no_actions))
print game.simulate(100)

#deck = Deck(buy_strategies.smithy_bm, action_strategies.smithy)

#print deck.solitaire_benchmarks(100)