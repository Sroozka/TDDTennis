import unittest
from Tdd2_tennis_gem import TennisGem
from Tdd2_tennis_set import TennisSet

class TennisTest2(unittest.TestCase):
    def setUp(self):
        self.gem = TennisGem()
        self.set = TennisSet()
        pass

    def test1_start(self):
        initial_gem_score = self.gem.gem_result()
        self.assertEqual("0-0", initial_gem_score)

    def test2_P1_15_0(self):
        self.gem.p1_scored_ball()
        gem_score = self.gem.gem_result()
        self.assertEqual("15-0", gem_score)

    def test2_P2_15_30(self):
        self.gem.p1_scored_ball()
        self.gem.p2_scored_ball()
        self.gem.p2_scored_ball()
        gem_score = self.gem.gem_result()
        self.assertEqual("15-30", gem_score)

    def test2_P1_P2_15_40(self):
        self.gem.p1_scored_ball()
        self.gem.p2_scored_ball()
        self.gem.p2_scored_ball()
        self.gem.p2_scored_ball()
        gem_score = self.gem.gem_result()
        self.assertEqual("15-40", gem_score)
