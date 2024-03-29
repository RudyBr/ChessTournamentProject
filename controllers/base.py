"""Define the main controller."""

from tinydb import TinyDB, Query
from pprint import pprint

import models.tournament
import models.player
import models.round
import models.match


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
                db = TinyDB('db.json', indent=4)
                players_list = db.table("players")
                player_count = 1
                for user in players_list:
                    print(f"{player_count}. Prénom: {user['first_name']}, "
                          f"Nom: {user['last_name']}, "
                          f"Date de naissance: {user['birth_date']}, "
                          f"Sexe: {user['gender']}, "
                          f"Classement Elo: {user['ranking']}")
                    player_count += 1
                pass
            elif option == 2:  # ajouter joueur à la DB
                self.add_db_player_module()
            elif option == 0:  # retour au menu principal
                self.view.main_menu()
            else:
                print("Ce n'est pas un choix valide.")
                print("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.")

    def add_db_player_module(self):
        data = self.view.new_player()
        player = models.player.Player(
            data["first_name"],
            data["last_name"],
            data["birthday_date"],
            data["gender"],
            data["ranking"])

        db = TinyDB('db.json', indent=4)
        players_table = db.table("players")

        player_id = players_table.insert(player.serialize())
        player.id = player_id
        players_table.update(player.serialize(), doc_ids=[player.id])

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

            db = TinyDB('db.json', indent=4)
            players_table = db.table("players")

            pprint(players_table.all())
            player_query = Query()
            pprint(players_table.search(player_query.id == 1))

            player_voulu = players_table.get(doc_id=1)
            pprint(player_voulu)

            player_id = players_table.insert(player.serialize())
            player.id = player_id

            self.current_tournament.player_list.append(player)
            self.current_tournament.matches_history[player] = []
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

                db = TinyDB('db.json', indent=4)
                tournament_table = db.table("tournament")

                pprint(tournament_table.all())
                tournament_query = Query()
                pprint(tournament_table.search(tournament_query.id == 1))

                tournament_voulu = tournament_table.get(doc_id=1)
                pprint(tournament_voulu)

                tournament_id = tournament_table.insert(self.current_tournament.serialize())
                self.current_tournament.id = tournament_id
                tournament_table.update(self.current_tournament.serialize(), doc_ids=[self.current_tournament.id])

                affichage_tournoi = str(self.current_tournament)
                print(affichage_tournoi)

                self.current_tournament.player_list = []
                while len(self.current_tournament.player_list) < 8:
                    self.add_player_module()
                tournament_table.update(self.current_tournament.serialize(), doc_ids=[tournament_id])

                # le tournoi peut démarrer
                while self.current_tournament.round_count < self.current_tournament.round_quantity:
                    self.current_tournament.add_round()
                    db = TinyDB('db.json', indent=4)
                    rounds_table = db.table("rounds")
                    _round = self.current_tournament.current_round
                    round_id = rounds_table.insert(_round.serialize())
                    _round.id = round_id
                    rounds_table.update(_round.serialize(), doc_ids=[_round.id])
                    for match in _round.match_list:
                        # demander le résultat du match
                        self.match_module(match)
                        tournament_table.update(self.current_tournament.serialize(), doc_ids=[tournament_id])
                    # la ronde est terminée >  renseigner date de fin de la ronde

                ordered_player_list = self.current_tournament.get_ordered_player_list()
                view_play_list = [{"civility": player.first_name + ' ' + player.last_name,
                                   "score": player.score}
                                  for player in ordered_player_list]
                self.view.final_result(view_play_list)

            elif option == 0:  # Retour au menu principal
                break
            else:
                print("Ce n'est pas un choix valide.")
                print("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.")

    def match_module(self, match):
        entree_valide = False
        option = None
        while not entree_valide:
            option = self.view.match_menu(match.joueur1.civility(), match.joueur2.civility())
            if option == 1:  # Le joueur 1 est vainqueur
                entree_valide = True
                match.joueur1.score += 1
                match.result = 1
            elif option == 2:  # Le joueur 2 est vainqueur
                entree_valide = True
                match.joueur2.score += 1
                match.result = 2
            elif option == 3:  # Match nul
                entree_valide = True
                match.joueur1.score += 0.5
                match.joueur2.score += 0.5
                match.result = 0
            else:
                print("Ce n'est pas un choix valide.")
                print("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.")
        print(f"Résultat du match : {option}")
        db = TinyDB('db.json', indent=4)
        players_table = db.table("players")
        players_table.update(match.joueur1.serialize(), doc_ids=[match.joueur1.id])
        players_table.update(match.joueur2.serialize(), doc_ids=[match.joueur2.id])
        matches_table = db.table("matches")
        match_id = matches_table.insert(match.serialize())
        match.id = match_id
        matches_table.update(match.serialize(), doc_ids=[match.id])
        return option

    def report_module(self):
        option = self.view.report_menu()
        while True:
            if option == 1:

                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 0:  # Quitte le programme avec message
                break

    def player_listing_module(self):
        option = self.view.player_listing_menu()
        while True:
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 0:  # Quitte le programme avec message
                break

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
