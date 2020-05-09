from Tdd2_tennis_gem import TennisGem


class Game:
    def __init__(self, p1_score, p2_score):
        self.p1_score = p1_score
        self.p2_score = p2_score

    def win(self):
        pass
#  -------------------------------------------------------------------------------------------------------------------


class TennisSet():
    def __init__(self, p1_score=0, p2_score=0):
        self.list_of_gem_winners = []
        self.list_of_set_score = ["0-0"]
        self.number_of_set = 0
        self.set_winner = " "
        self.set_ended = False
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.p1_gem_score = 0
        self.p2_gem_score = 0

    def win(self):
        if self.p1_score <= self.p2_score:  # 2:4
            if self.p1_score != 0:  # x2
                self.gem_P1_P2_scored(self.p1_score)
            for _ in range(self.p1_score, self.p2_score):  # range(2,4) = 2
                self.p2_win_gem()
        else:  # 5:3
            if self.p2_score != 0:  # x3
                self.gem_P1_P2_scored(self.p2_score)
            for _ in range(self.p2_score, self.p1_score):  # range(3,5) = 2
                self.p1_win_gem()

    def gem_P1_P2_scored(self, punkty):
        for _ in range(punkty):
            self.p1_win_gem()
            self.p2_win_gem()

    def p1_win_gem(self):
        self.gem = TennisGem(4, 2)
        self.gem.win()
        self.p1_gem_score += 1
        self.list_of_gem_winners.append("P1")
        self.update_curent_score()

    def p2_win_gem(self):
        self.gem = TennisGem(2, 4)
        self.gem.win()
        self.p2_gem_score += 1
        self.list_of_gem_winners.append("P2")
        self.update_curent_score()

    def current_gem_score(self):
        print(f"{self.p1_gem_score}-{self.p2_gem_score}")
        return f"{self.p1_gem_score}-{self.p2_gem_score}"

    def update_curent_score(self):
        self.list_of_set_score[0] = self.current_gem_score()