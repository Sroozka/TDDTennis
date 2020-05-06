from Tdd2_tennis_gem import TennisGem


class TennisSet:
    def __init__(self):
        self.gem = TennisGem()
        self.list_of_gems = []
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

    def add_points(self, p1_score, p2_score):
        pass
