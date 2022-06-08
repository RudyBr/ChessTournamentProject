"""Define the main controller."""

from typing import List

from models.tournament import Tournament
from models.player import Player


class Controller:
    """Main controller."""

    def __init__(self, tournament: Tournament, view):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.tournament = tournament

        # views
        self.view = view

    def get_players(self):
        while len(self.players) < Player.PLAYER_NUMBER:
            infos_joueur = self.view.saisie_joueur()
            player = Player(infos_joueur["nom"],
                            infos_joueur["prenom"],
                            infos_joueur["date_naissance"],
                            infos_joueur["sexe"],
                            infos_joueur["classement"])
            self.players.append(player)

    def run(self):
        self.get_players()