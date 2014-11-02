from __future__ import division


class Game:
    def __init__(self, *args):
        self.players = args
        for p in self.players:
            p.game = self
        self.kingdom = None
        self.reset()

    def reset(self):
        self.kingdom = {'copper': 1000, 'silver': 1000, 'gold': 1000, 'estate': 1000, 'duchy': 1000, 'curse': 1000}
        if len(self.players) == 1:
            self.kingdom['province'] = 4
        elif len(self.players) == 2:
            self.kingdom['province'] = 8
        else:
            self.kingdom['province'] = 12

    def simulate(self, iterations=10000):
        wins = [0] * len(self.players)
        for _ in xrange(iterations):
            while not self.game_complete():
                for deck in self.players:
                    deck.turn()
                    if self.game_complete():
                        break
            for w in self.determine_winners():
                wins[w] += 1
            for deck in self.players:
                deck.reset()
            self.reset()
        return [w/iterations for w in wins]

    def game_complete(self):
        if self.remaining_cards('province') == 0:
            return True
        else:
            return False

    def remaining_cards(self, card):
        return self.kingdom.get(card, 0)

    def buy_card(self, card):
        if card in self.kingdom and self.kingdom[card] > 0:
            self.kingdom[card] -= 1
            return True
        else:
            return False

    def determine_winners(self):
        max_score = 0
        winners = []
        for i in xrange(len(self.players)):
            score = self.players[i].deck_score()
            if score > max_score:
                max_score = score
                winners = [i]
            elif score == max_score:
                winners.append(i)
        if len(winners) > 1:
            winners = [w for w in winners if self.players[w].turns == self.players[-1].turns]
        return winners

    def leading_score(self):
        return max(self.players, lambda x: x.deck_score())


