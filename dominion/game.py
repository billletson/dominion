from __future__ import division


class Game:
    def __init__(self, *args):
        self.players = args
        for p in self.players:
            p.game = self
        if len(self.players) == 1:
            self.starting_provinces = 4
        elif len(self.players) == 2:
            self.starting_provinces = 8
        else:
            self.starting_provinces = 12

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
        return [w/iterations for w in wins]

    def game_complete(self):
        if self.remaining_provinces() == 0:
            return True
        else:
            return False

    def remaining_provinces(self):
        return self.starting_provinces - sum([deck.count_card('Province') for deck in self.players])

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


