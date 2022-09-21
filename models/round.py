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

    def rank_players(self):
        # key_sort_function = lambda player: player.ranking \
        #     if number == 1 else lambda player: player.score
        if self.number == 1:
            ordered_player_list = sorted(self.tournament.player_list, key=lambda player: player.ranking, reverse=True)
        else:
            # classement pour round 2+ avec comme 1er élément de tri le score et 2eme l'élo
            ordered_player_list = sorted(self.tournament.player_list,
                                         key=lambda player: (player.score, player.ranking), reverse=True)
        print(f"Liste des joueurs classés de la ronde : {ordered_player_list}")
        return ordered_player_list

    def players_pair(self, ordered_player_list):
        return
        while ordered_player_list:
            # on apparie le premier élément de la liiste avec le premier suivant
            # qu'il n'a pas déjà rencontré
            paire = (1, 2)
            # match = Match(1, 2)
            # match.jouer()

    def run(self):
        ordered_player_list = self.rank_players()
        self.players_pair(ordered_player_list)
    # il n'y a plus qu'à créer une liste de matchs avec toutes les paires
    # de joueurs de cette liste
