# from TDDTennisNames import NamePoints
class TennisGem:
    ListOfNames = ("Love", "15", "30", "40", "Deuce", "Advantage", "Gem", "Game")

    def __init__(self):
        self._p1_score = 0
        self._p2_score = 0
        self._p1_gem_point = 0
        self._p2_gem_point = 0
        # self._score = "0-0"

    @property
    def score(self):
        return self._calculate_score()

    def player_one_scored(self):
        self._p1_score += 1

    def player_two_scored(self):
        self._p2_score += 1

    def p1_scored_gem(self):
        self._p1_gem_point += 1

    def p2_scored_gem(self):
        self._p2_gem_point += 1

    def _calculate_score(self) -> str:
        if self._p1_score < 3 or self._p2_score < 3:  # wyniki gdy jeden z graczy będzie miał poniżej 40 pkt
            return self.first_3_balls()
        else:  # oboje z graczy wygrali po co najmniej 3 piłki
            return self.deuce_and_more()

    @staticmethod
    def _translate_score(player_score):
        if player_score < 6:
            return TennisGem.ListOfNames[player_score]
        else:
            return TennisGem.ListOfNames[5]

    def first_3_balls(self) -> str:
        if self._p1_score == 4 or self._p2_score == 4:  # gracz P1 wygrał 4 piłki
            if self._p1_score > self._p2_score:
                self.p1_scored_gem()
            else:
                self.p2_scored_gem()
            return f"{TennisGem.ListOfNames[6]} for " + self._player_with_highest_score()
        elif self._p1_score == self._p2_score:  # remisy
            return f"{self._translate_score(self._p1_score)} - all"
        else:  # żaden z graczy nie wygrał 4 piłek
            return f"{self._translate_score(self._p1_score)} - {self._translate_score(self._p2_score)}"

    def deuce_and_more(self) -> str:
        if self._is_deuce():
            return TennisGem.ListOfNames[4]
        elif self._is_advantage():
            return f"{TennisGem.ListOfNames[5]} {self._player_with_highest_score()}"
        else:
            x = self._player_with_highest_score()
            if x == "P1":
                self.p1_scored_gem()
            else:
                self.p2_scored_gem()
            return f"{TennisGem.ListOfNames[6]} for {x}"

    def _is_deuce(self):
        return 3 <= self._p1_score == self._p2_score >= 3  # remis po 3 i więcej piłek

    def _is_advantage(self):
        return self._p1_score >= 3 and \
               self._p2_score >= 3 and \
               abs(self._p1_score - self._p2_score) == 1

    def _player_with_highest_score(self):
        if self._p1_score > self._p2_score:
            return "P1"
        return "P2"
