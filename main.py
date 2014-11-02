from dominion import *

game = Game(Deck(buy_strategies.optimized_smithy_bm, action_strategies.smithy),
            Deck(buy_strategies.basic_big_money, action_strategies.no_actions))
print game.simulate(1000)

#deck = Deck(buy_strategies.smithy_bm, action_strategies.smithy)

#print deck.solitaire_benchmarks(100)