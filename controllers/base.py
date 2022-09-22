"""Define the main controller."""
import models.tournament


class Controller:
    """Main controller."""

    def __init__(self, view):
        """Has a tournament and a view."""
        # models
        # self.tournament affecté dans get_tournament_details
        # tournanment
        self.tournament = None
        # current_tournament
        self.current_tournament = None
        # views
        self.view = view

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
        option = self.view.add_player_menu()
        if option == 1:  # Créer un nouveau joueur et l'ajouter au tournoi
            data = self.view.new_player()
            player = models.player.Player(
                data["first_name"],
                data["last_name"],
                data["birthday_date"],
                data["gender"],
                data["ranking"]
            )
            self.current_tournament.player_list.append(player)
        elif option == 2:  # Ajouter un joueur de la base de données au tournoi

            pass
        elif option == 0:  # Retour au menu principal
            return

    def tournament_module(self):
        while True:
            option = self.view.tournament_menu()
            if option == 1:  # ajouter des participants au tournoi
                pass
            elif option == 2:  # Ajouter un nouveau  tournoi
                data = self.view.new_tournament()
                self.current_tournament = models.tournament.Tournament(
                    data["name"],
                    data["location"],
                    data["date"],
                    data["round_quantity"],
                    data["time_control"],
                    data["description"]
                )
                print(self.current_tournament)
                # boucle : tant que nombre_de_joueur != 8 --> ajouter joueur

                self.current_tournament.player_list = []
                while len(self.current_tournament.player_list) < 2:
                    self.add_player_module()

                # le tournoi peut démarrer
                while self.current_tournament.round_count < self.current_tournament.round_quantity:
                    self.current_tournament.add_round()
                    for match in self.current_tournament.current_round.match_list:
                        # demander le résultat du match
                        self.match_module()

            elif option == 0:  # Retour au menu principal
                break
            else:
                print("Ce n'est pas un choix valide.")
                print("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.")

    def match_module(self):
        # va faire appel à self.view.match_menu
        pass

    def report_module(self):
        option = self.view.report_menu()

    def run(self):
        # self.get_tournament_details()
        while True:
            option = self.view.main_menu()
            if option == 1:  # menu joueurs
                self.player_module()
                pass
            elif option == 2:  # menu tounois
                self.tournament_module()
                pass
            elif option == 3:  # menu des rapports
                self.view.report_module()
            elif option == 0:  # Quitte le programme avec message
                break
