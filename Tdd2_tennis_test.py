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
        self.gem.win()
        self.assertEqual("0-0", self.gem.gem_result())

    def test2_P1_15_0(self):
        self.gem = TennisGem(1, 0)
        self.gem.win()
        self.assertEqual("15-0", self.gem.gem_result())

    def test2_P2_15_30(self):
        self.gem = TennisGem(1, 2)
        self.gem.win()
        self.assertEqual("15-30", self.gem.gem_result())

    def test2_P1_P2_set_4_2(self):
        self.set = TennisSet(4, 2)
        self.set.win()
        print(f"{self.set.set_score}")



