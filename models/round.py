from typing import List

from .match import Match
from .tournament import Tournament


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
        # il n'y a plus qu'à créer une liste de matchs avec toutes les paires
        # de joueurs de cette liste
