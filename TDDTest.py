"""
Praktyczne wprowadzenie do TDD (Test-Driven Development) w Pythonie | #23
https://www.youtube.com/watch?v=z4yxgwbT8Ss
"""
import unittest
from TenisGem import TennisGem
from TenisSet import TenisSet


class TestTennis(unittest.TestCase):
    def setUp(self):
        self.gem = TennisGem()
        self.game = TenisSet()

    def tearDown(self):
        del self.gem
        del self.game

    def _create_bp_score(self, player_one_scored, player_two_scored):
        for _ in range(player_one_scored):
            self.gem.player_one_scored()
        for _ in range(player_two_scored):
            self.gem.player_two_scored()

    def _create_gem_score(self, player_one_scored, player_two_scored):
        for _ in range(player_one_scored):
            self.game._create_gem(4, 2)
            print(
                f" _create_gem_scoreP1 P1: {self.game._p1_gem_point}, P2: {self.game._p2_gem_point}, score {self.game.score}")
        print("Test petla 1,2")
        for _ in range(player_two_scored):
            print("test")
            self.game._create_gem(2, 4)
            print(
                f" _create_gem_scoreP2 P1: {self.game._p1_gem_point}, P2: {self.game._p2_gem_point}, score {self.game.score}")
        print(f"funkcja _create_gem_score {self.game.score}")

    def test_something(self):
        initial_score = self.gem.score
        self.assertEqual("Love - all", initial_score)

    def test_score_15_0_when_p1_scored_once(self):
        self._create_bp_score(1, 0)
        self.assertEqual("15 - Love", self.gem.score)

    def test_score_0_15_when_p2_scored_once(self):
        self._create_bp_score(0, 1)
        self.assertEqual("Love - 15", self.gem.score)

    def test_score_30_0_when_p1_scored_twice(self):
        self._create_bp_score(2, 0)
        self.assertEqual("30 - Love", self.gem.score)

    def test_score_0_30_when_p2_scored_twice(self):
        self._create_bp_score(0, 2)
        self.assertEqual("Love - 30", self.gem.score)

    def test_score_40_0_when_p1_scored_thrice(self):
        self._create_bp_score(3, 0)
        self.assertEqual("40 - Love", self.gem.score)

    def test_score_0_40_when_p2_scored_thrice(self):
        self._create_bp_score(0, 3)
        self.assertEqual("Love - 40", self.gem.score)

    def test_score_15_15_when_p1_scored_once_and_p2_once(self):
        self._create_bp_score(1, 1)
        self.assertEqual("15 - all", self.gem.score)

    def test_score_30_30_when_p1_scored_twice_and_p2_twice(self):
        self._create_bp_score(2, 2)
        self.assertEqual("30 - all", self.gem.score)

    def test_score_30_40_when_p1_scored_twice_and_p2_thrice(self):
        self._create_bp_score(2, 3)
        self.assertEqual("30 - 40", self.gem.score)

    def test_score_40_30_when_p1_scored_thrice_and_p2_twice(self):
        self._create_bp_score(3, 2)
        self.assertEqual("40 - 30", self.gem.score)

    def test_game_for_p1_when_scored_four_times(self):
        self._create_bp_score(4, 0)
        self.assertEqual("Gem for P1", self.gem.score)

    def test_game_for_p2_when_scored_four_times(self):
        self._create_bp_score(0, 4)
        self.assertEqual("Gem for P2", self.gem.score)

    def test_score_deuce(self):
        self._create_bp_score(3, 3)
        self.assertEqual("Deuce", self.gem.score)

    def test_score_deuce_7times(self):
        self._create_bp_score(7, 7)
        self.assertEqual("Deuce", self.gem.score)

    def test_Advantage_P1_adv_40(self):
        self._create_bp_score(4, 3)
        self.assertEqual("Advantage P1", self.gem.score)

    def test_Advantage_P2_40_adv(self):
        self._create_bp_score(5, 6)
        self.assertEqual("Advantage P2", self.gem.score)

    def test_win_for_p1_after_advantage(self):
        self._create_bp_score(13, 11)
        self.assertEqual("Gem for P1", self.gem.score)

    def test_win_for_p2_after_advantage(self):
        self._create_bp_score(10, 12)
        self.assertEqual("Gem for P2", self.gem.score)
    # ---------------------------------Dotąd było na filmie
    # def test_start_game(self):
    #     starting_score = self.game.score
    #     self.assertEqual("0-0", starting_score)
    #
    # def test_score_P1_won_gem_once(self):
    #     self.game._create_gem(5, 3)
    #     self.assertEqual("1-0", self.game.score)
    #
    # def test_score_P1_won_gem_twice(self):
    #     self._create_gem_score(2, 0)
    #     self.assertEqual("2-0", self.game.score)

    # def test_score_P2_won_gem_twice(self):
    #     self._create_gem_score(0, 2)
    #     self.assertEqual("0-2", self.game.score)

    def test_score_P2_won_gem_fource_P1_once(self):
        self._create_gem_score(1, 4)
        self.assertEqual("1-4", self.game.score)