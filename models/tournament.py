from typing import List

from .player import Player
from .round import Round


class Tournament:
    def __init__(self, name, location, date, round_quantity, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.round_quantity = round_quantity
        self.rounds = []
        self.round_count = 0
        self.player_list: List[Player] = []
        self.time_control = time_control
        self.description = description

    def add_round(self):
        # création de la prochaine ronde
        self.round_count += 1
        print(f"création de la ronde n°{self.round_count}")
        current_round = Round(self, self.round_count)
        self.rounds.append(round)
        print(f"démarrage de la ronde n°{self.round_count}")
        current_round.run()
