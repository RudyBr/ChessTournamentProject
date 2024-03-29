from typing import List

from .player import Player
from .round import Round


class Tournament:
    def __init__(self, name, location, date, round_quantity, time_control, description):
        self.id = None
        self.name = name
        self.location = location
        self.date = date
        self.round_quantity = round_quantity
        self.rounds = []
        self.round_count = 0
        self.current_round = None
        self.player_list: List[Player] = []
        self.time_control = time_control
        self.description = description
        self.matches_history = {}

    def __str__(self):
        return f"Id du tournoi: {self.id}\n" \
               f"Nom du tournoi: {self.name}\n" \
               f"Lieu du tournoi: {self.location}\n" \
               f"Date du tournoi: {self.date.strftime('%d/%m/%Y')}\n" \
               f"Nombre de rounds: {self.round_quantity}\n" \
               f"Format de match: {self.time_control}\n" \
               f"Description du tournoi: {self.description}\n"

    def add_round(self):
        # création de la prochaine ronde
        self.round_count += 1
        print(f"création de la ronde n°{self.round_count}")
        self.current_round = Round(self, self.round_count)
        self.rounds.append(self.current_round)
        print(f"démarrage de la ronde n°{self.round_count}")
        self.current_round.set_matches()

    def get_ordered_player_list(self):
        # key_sort_function = lambda player: player.ranking \
        #     if number == 1 else lambda player: player.score
        if self.round_count == 1:
            ordered_player_list = sorted(self.player_list, key=lambda player: player.ranking, reverse=True)
        else:
            # classement pour round 2+ avec comme 1er élément de tri le score et 2eme l'élo
            ordered_player_list = sorted(self.player_list,
                                         key=lambda player: (player.score, player.ranking), reverse=True)
        print(f"Liste des joueurs classés de la ronde : {ordered_player_list}")
        return ordered_player_list

    def serialize(self):
        return{"id": self.id if self.id is not None else 0,
               "name": self.name,
               "location": self.location,
               "date": self.date.strftime("%d/%m/%Y"),
               "round_quantity": self.round_quantity,
               "player_list": [player.id for player in self.player_list],
               "description": self.description,
               "matches_history": {player.id: [player.id for player in opponents_list]
                                   for (player, opponents_list) in self.matches_history.items()}
               }
