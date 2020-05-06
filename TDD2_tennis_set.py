from Tdd2_tennis_gem import TennisGem


class TennisSet:
    def __init__(self):
        self.gem = TennisGem()
        self.list_of_gems = []
        self.list_of_gem_scores = []
        self.set_winner = " "
        self.set_ended = False

    def begin_gem(self):
        if self.list_of_gems == [] or self.is_gem_running():  # is True
            pass

    def is_gem_running(self):
        if self.list_of_gems[-1]:  # is True
            return False
        else:
            return True

    def win_gem(self, p1_score, p2_score):
        if p1_score <= p2_score:  # 2:4
            if p1_score != 0:  # x2
                self.gem_P1_P2_scored(p1_score)
            for _ in range(p1_score, p2_score):  # range(2,4) = 2
                self.gem.p2_scored_ball()
            self.list_of_gems.append(self.gem.Gem_ended)

        else:  # 5:3
            if p2_score != 0:  # x3
                self.gem_P1_P2_scored(p2_score)
            for _ in range(p2_score, p1_score):  # range(3,5) = 2
                self.gem.p1_scored_ball()
            self.list_of_gems.append(self.gem.Gem_ended)

    def gem_P1_P2_scored(self, punkty):
        for _ in range(punkty):
            self.gem.p1_scored_ball()
            self.gem.p2_scored_ball()