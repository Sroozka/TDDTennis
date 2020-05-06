import unittest
from Tdd2_tennis_gem import TennisGem
from Tdd2_tennis_set import TennisSet


class TennisTest2(unittest.TestCase):
    # def setUp(self):
    #     self.gem = TennisGem()
    #     self.set = TennisSet()
    #     pass

    def test1_start(self):
        self.gem = TennisGem(0, 0)
        self.gem.win_gem()
        self.assertEqual("0-0", self.gem.gem_result())

    def test2_P1_15_0(self):
        self.gem = TennisGem(1, 0)
        self.gem.win_gem()
        self.assertEqual("15-0", self.gem.gem_result())

    def test2_P2_15_30(self):
        self.gem = TennisGem(1, 2)
        self.gem.win_gem()
        self.assertEqual("15-30", self.gem.gem_result())

    # def test2_P1_P2_15_40_set(self):
    #     self.set.win_gem(1, 3)
    #     self.assertEqual("15-40", self.set.list_of_gem_scores[0])



