"""Define the main controller."""

from typing import List

from models.tournament import Tournament
from models.player import Player
import models.data_test


class Controller:
    """Main controller."""

    def __init__(self, tournament: Tournament, view):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.players = models.data_test.PLAYERS_DETAILS

        self.tournament = tournament

        # views
        self.view = view

    def get_players_details(self):
        while len(self.players) < Player.PLAYER_NUMBER:
            player_details = self.view.player_entry()
            player = Player(player_details["nom"],
                            player_details["prenom"],
                            player_details["date_naissance"],
                            player_details["sexe"],
                            player_details["classement"])
            self.players.append(player)

    def run(self):
        #self.get_players_details()
        pass
