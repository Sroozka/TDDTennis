class TennisGem:
    listOfNames = ("0", "15", "30", "40", "Advantage", "Gem")

    def __init__(self, p1_scored, p2_scored):
        self.P1_ball_score = 0
        self.P2_ball_score = 0
        self.p1_scored = p1_scored
        self.p2_scored = p2_scored
        self.Who_is_leading = " "
        self.Gem_ended = False

    def gem_result(self):
        return f"{TennisGem.listOfNames[self.P1_ball_score]}-{TennisGem.listOfNames[self.P2_ball_score]}"

    def win_gem(self):
        if self.p1_scored <= self.p2_scored:  # 2:4
            if self.p1_scored != 0:  # x2
                self.gem_P1_P2_scored(self.p1_scored)
            for _ in range(self.p1_scored, self.p2_scored):  # range(2,4) = 2
                self.p2_scored_ball()
        else:  # 5:3
            if self.p2_scored != 0:  # x3
                self.gem_P1_P2_scored(self.p2_scored)
            for _ in range(self.p2_scored, self.p1_scored):  # range(3,5) = 2
                self.p1_scored_ball()

    def gem_P1_P2_scored(self, punkty):
        for _ in range(punkty):
            self.p1_scored_ball()
            self.p2_scored_ball()


    def p1_scored_ball(self):
        if 4 == self.P2_ball_score and self.P1_ball_score == 3:
            self.P2_ball_score -= 1
        else:
            self.P1_ball_score += 1
        self.current_score()
        self.leading_player()
        self.gem_end()

    def p2_scored_ball(self):
        if 4 == self.P1_ball_score and self.P2_ball_score == 3:
            self.P1_ball_score -= 1
        else:
            self.P2_ball_score += 1
        self.current_score()
        self.leading_player()
        self.gem_end()

    def current_score(self):
        print(f"{TennisGem.listOfNames[self.P1_ball_score]}-{TennisGem.listOfNames[self.P1_ball_score]}")

    def leading_player(self):
        if self.P2_ball_score > self.P1_ball_score:
            self.Who_is_leading = "P2"
        else:
            self.Who_is_leading = "P1"

    def gem_end(self):
        if (abs(self.P2_ball_score - self.P1_ball_score) > 1) and ((self.P1_ball_score or self.P2_ball_score) > 3):
            self.Gem_ended = True
