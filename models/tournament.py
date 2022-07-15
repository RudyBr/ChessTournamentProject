from typing import List

import models.data_test
from player import Player

class Tournament:
    def __init__(self, name, location, date, round_quantity, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.round_quantity = round_quantity
        self.rounds = []
        self.player_list: List[Player] = []
        self.player_list = models.data_test.PLAYERS_DETAILS
        self.time_control = time_control
        self.description = description
