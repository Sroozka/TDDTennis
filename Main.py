from Tdd2_tennis_set import TennisSet

class Main:
    list_of_game_score = []
    set1 = TennisSet(5, 6)
    set2 = TennisSet(6, 0)
    set3 = TennisSet(3, 6)
    list_of_sets = [set1, set2, set3]
    for tenisset in list_of_sets:
        tenisset.win()
        list_of_game_score.append(tenisset.final_set_score)

    print(list_of_game_score)
