from Tdd2_tennis_gem import TennisGem


class Game:
    def __init__(self, p1_score, p2_score):
        self.p1_score = p1_score
        self.p2_score = p2_score

    def win(self):
        pass

class TennisSet(Game):
    def __init__(self, p1_score=0, p2_score=0):
        self.gem = TennisGem()
        self.list_of_gem_scores = []
        self.list_of_gem_winners = []
        self.set_winner = " "
        self.set_ended = False
        self.p1_score = p1_score
        self.p2_score = p2_score

    def begin_gem(self, p1_score, p2_score):
        if self.list_of_gem_scores == [] or self.is_gem_running():  # is True
            self.win(p1_score, p2_score)
        else:
            pass  # dodać co robić, jak wywołujemy nowy gem, a gem nadal trwa

    def is_gem_running(self):
        if self.gem.Gem_ended:  # is True
            return False
        else:
            return True

    def win(self, p1_score, p2_score):
        if p1_score <= p2_score:  # 2:4
            if p1_score != 0:  # x2
                self.gem_P1_P2_scored(p1_score)
            for _ in range(p1_score, p2_score):  # range(2,4) = 2
                self.gem.p2_scored_ball()
            # self.list_of_gem_scores.append(self.gem.gem_result())
            # self.list_of_gem_winners.append(self.gem.Who_is_leading)
        else:  # 5:3
            if p2_score != 0:  # x3
                self.gem_P1_P2_scored(p2_score)
            for _ in range(p2_score, p1_score):  # range(3,5) = 2
                self.gem.p1_scored_ball()
            # self.list_of_gem_scores.append(self.gem.gem_result())
            # self.list_of_gem_winners.append(self.gem.Who_is_leading)

    def gem_P1_P2_scored(self, punkty):
        for _ in range(punkty):
            self.gem.p1_scored_ball()
            self.gem.p2_scored_ball()
