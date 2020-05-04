from TenisGem import TennisGem
#import random

class TenisSet:
    def __init__(self):
        self.gem = TennisGem()
        self.score = "0-0"
        self._p1_gem_point = 0
        self._p2_gem_point = 0

    def _win_gem(self, punkty):
        for _ in range(punkty):
            self.gem.player_one_scored()
            self.gem.player_two_scored()

    def _zero_gem(self):
        self.gem._p1_gem_point = 0
        self.gem._p2_gem_point = 0

    def _create_gem(self, playerOneScore, playerTwoScore):
        self._zero_gem()
        if playerOneScore < playerTwoScore:
            # print("test P2>P1")
            if playerOneScore != 0:
                self._win_gem(playerOneScore)
            for _ in range(playerOneScore, playerTwoScore):
                self.gem.player_two_scored()
        else:
            # print(f"111 test P1>P2 P1:{self._p1_gem_point} P2:{self._p2_gem_point} Score: {self.score}")
            if playerTwoScore != 0:
                self._win_gem(playerTwoScore)
            for _ in range(playerTwoScore, playerOneScore):
                self.gem.player_one_scored()
                # print("_ " + str(_) +"|" + self.gem.score)
        # print("1 for _ in range(playerTwoScore, playerOneScore):" + self.score)
        # print("gem points z I modułu: ", self.gem._p1_gem_point, self.gem._p2_gem_point)
        if "Gem" in self.gem.score:
            self._p1_gem_point += self.gem._p1_gem_point
            self._p2_gem_point += self.gem._p2_gem_point
            self.score = f"{self._p1_gem_point}-{self._p2_gem_point}"
            # print(
            #     f"Część dodająca punkt gemowy za wygrany gem P1:{self.gem._p1_gem_point} P2: {self.gem._p2_gem_point}")
            # print(
            #     f"gem points z I modułu(final): P1:{self._p1_gem_point} P2:{self._p2_gem_point} Score: {self.score}")
        # print(f"gem points z I modułu(final): P1:{self.gem._p1_gem_point} P2:{self.gem._p2_gem_point} Score: {self.score}")

'''
    def Set(self):
        while 1:
            x = random.randrange(2)
'''