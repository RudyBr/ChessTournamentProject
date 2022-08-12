"""Define the main controller."""

from typing import List

import models.tournament
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from views.base import View

class Controller:
    """Main controller."""

    def __init__(self, view):
        """Has a tournament and a view."""
        # models
        # self.tournament affecté dans get_tournament_details
        # players
        self.players = []
        # current_tournament
        self.current_tournament = None
        # views
        self.view = view

    def get_players_details(self):
        while len(self.tournament.player_list) < Player.PLAYER_NUMBER:
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

    def player_module(self):
        while True:
            option = self.view.player_menu()
            if option == 1:  # lister joueurs de la DB
                pass
            elif option == 2:  # ajouter joueur à la DB
                pass
            elif option == 0:  # retour au menu principal
                self.view.main_menu()
            else:
                print("Ce n'est pas un choix valide.")
                print("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.")

    def add_player_module(self):
        while True:
            option = self.view.add_player_menu()
            if option == 1:  # Créer un nouveau joueur et l'ajouter au tournoi
                data = self.view.new_player()
                player = models.player.Player(data["first_name"], data["last_name"], data["birthday_date"], data["gender"], data["ranking"])
                self.current_tournament.player_list.append(player)
            elif option == 2:  # Ajouter un joueur de la base de données au tournoi
                pass

    def tournament_module(self):
        while True:
            option = self.view.tournament_menu()
            if option == 1:  # ajouter des participants au tournoi
                pass
            elif option == 2:  # Ajouter un nouveau  tournoi
                data = self.view.new_tournament()
                self.current_tournament = models.tournament.Tournament(data["name"], data["location"], data["date"], data["round_quantity"], data["time_control"], data["description"])
                print(self.current_tournament)
                # boucle : tant que nombre_de_joueur != 8 --> ajouter joueur
                self.current_tournament.player_list = []
                while len(self.current_tournament.player_list) < 8:
                    self.add_player_module()

            elif option == 0:  # Retour au menu principal
                self.view.main_menu()
            else:
                print("Ce n'est pas un choix valide.")
                print("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.")

    def report_module(self):
        option = self.view.report_menu()


    def run(self):
        # self.get_tournament_details()
        while True:
            option = self.view.main_menu()
            if option == 1:  # menu joueurs
                self.player_module()
                pass
            if option == 2:  # menu tounois
                self.tournament_module()
                pass
            if option == 3:  # menu des rapports
                self.view.report_module()




        """self.tournament = Tournament("nom_tournoi", "Paris", "05062022", 7, "Blitz", "Description_tournoi")
        print(self.tournament)
        self.get_players_details()
        for player in self.tournament.player_list:
            print(player)
        for no_ronde in range(self.tournament.round_quantity):
            current_round = Round(self.tournament, no_ronde)
            self.tournament.rounds.append(current_round)
            print(current_round)"""
