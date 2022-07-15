"""Define the main controller."""

from typing import List

from models.tournament import Tournament
from models.player import Player


class Controller:
    """Main controller."""

    def __init__(self, tournament: Tournament, view):
        """Has a tournament and a view."""
        # models
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

    def get_tournament_details(self):
        tournament_details = self.view.tournament_entry()
        nombre_de_rondes = tournament_details["nombre de rondes"]
        nombre_de_rondes = int(nombre_de_rondes) if nombre_de_rondes else 4
        self.tournament = Tournament(tournament_details["nom"],
                                     tournament_details["lieu"],
                                     tournament_details["date"],
                                     nombre_de_rondes,
                                     tournament_details["controle de temps"],
                                     tournament_details["description"])

    def run(self):
        # self.get_players_details()
        # self.get_tournament_details()
        pass
