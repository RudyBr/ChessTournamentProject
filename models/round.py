from typing import List

from .match import Match


class Round:
    def __init__(self, tournament, number):
        """

        :param tournament:
        :param number: numéro de la ronde
        """
        self.tournament = tournament
        self.number = number
        self.match_list: List[Match] = []
        key_sort_function = lambda player: player.ranking \
            if number == 1 else lambda player: player.score

        self.ordered_player_list = sorted(self.tournament.player_list,
                                          key=lambda player: player.ranking)


        # classement pour round 2+ avec comme 1er élément de tri le score et 2eme l'élo
        self.ordered_player_list = sorted(self.tournament.player_list,
                                          key=lambda player: (player.score, player.ranking))


        # il n'y a plus qu'à créer une liste de matchs avec toutes les paires
        # de joueurs de cette liste
        print(f"Liste des joueurs classés de la ronde : {self.ordered_player_list}")

