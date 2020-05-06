class TennisGem:
    listOfNames = ("0", "15", "30", "40", "Advantage", "Gem")

    def __init__(self):
        self.P1_ball_score = 0
        self.P2_ball_score = 0
        self.Who_is_leading = " "
        self.Gem_ended = False

    # def gem_result(self):
    #     return f"{TennisGem.listOfNames[self.P1_ball_score]}-{TennisGem.listOfNames[self.P2_ball_score]}"

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
