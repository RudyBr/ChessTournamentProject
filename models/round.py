from typing import List

# from .tournament import Tournament

from .match import Match


class Round:
    def __init__(self, tournament, number):
        """

        :param tournament:
        :param number: numéro de la ronde
        """
        self.id = None
        self.tournament = tournament
        self.number = number
        self.match_list: List[Match] = []

    """def rank_players(self):
        # key_sort_function = lambda player: player.ranking \
        #     if number == 1 else lambda player: player.score
        if self.number == 1:
            ordered_player_list = sorted(self.tournament.player_list, key=lambda player: player.ranking, reverse=True)
        else:
            # classement pour round 2+ avec comme 1er élément de tri le score et 2eme l'élo
            ordered_player_list = sorted(self.tournament.player_list,
                                         key=lambda player: (player.score, player.ranking), reverse=True)
        print(f"Liste des joueurs classés de la ronde : {ordered_player_list}")
        return ordered_player_list"""

    def players_pair(self, ordered_player_list):
        if self.number == 1:
            half_players_number = int(len(ordered_player_list) / 2)
            list1 = ordered_player_list[:half_players_number]
            list2 = ordered_player_list[half_players_number:]
            for no_player in range(len(list1)):
                match = Match(self, list1[no_player], list2[no_player])
                self.match_list.append(match)
                self.tournament.matches_history[match.joueur1].append(match.joueur2)
                self.tournament.matches_history[match.joueur2].append(match.joueur1)
        else:
            while ordered_player_list:  # Tant que ordered_player_list n'est pas une liste vide
                # on apparie le premier élément de la liste avec le premier suivant
                i = 1
                while i < len(ordered_player_list):
                    if len(ordered_player_list) == 2 or \
                            ordered_player_list[i] not in self.tournament.matches_history[ordered_player_list[0]]:
                        match = Match(self, ordered_player_list[0], ordered_player_list[i])
                        print(ordered_player_list)
                        player_0 = ordered_player_list[0]
                        player_i = ordered_player_list[i]
                        ordered_player_list.remove(player_0)
                        ordered_player_list.remove(player_i)
                        self.match_list.append(match)
                        self.tournament.matches_history[match.joueur1].append(match.joueur2)
                        self.tournament.matches_history[match.joueur2].append(match.joueur1)
                        break
                    else:
                        i += 1
                # qu'il n'a pas déjà rencontré

                # match = Match(1, 2)
                # match.jouer()

    def set_matches(self):
        ordered_player_list = self.tournament.get_ordered_player_list()
        self.players_pair(ordered_player_list)

    def serialize(self):
        return {"id": self.id if self.id is not None else 0,
                "tournoi_id": self.tournament.id
                }