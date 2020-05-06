class TennisGem:
    listOfNames = ("0", "15", "30", "40", "Advantage", "Gem")

    def __init__(self):
        self.P1_ball_score = 0
        self.P2_ball_score = 0
        self.Gem_ended = False

    def gem_result(self):
        return f"{TennisGem.listOfNames[self.P1_ball_score]}-{TennisGem.listOfNames[self.P2_ball_score]}"

    def p1_scored_ball(self):
        if 4 == self.P2_ball_score and self.P1_ball_score == 3:
            self.P2_ball_score -= 1
        else:
            self.P1_ball_score += 1
        self.current_score()

    def p2_scored_ball(self):
        if 4 == self.P1_ball_score and self.P2_ball_score == 3:
            self.P1_ball_score -= 1
        else:
            self.P2_ball_score += 1
        self.current_score()

    def current_score(self):
        print(f"{TennisGem.listOfNames[self.P1_ball_score]}-{TennisGem.listOfNames[self.P1_ball_score]}")
