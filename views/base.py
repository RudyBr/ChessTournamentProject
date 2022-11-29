from models import player
from models import tournament

from controllers.timestamp import get_timestamp

from datetime import datetime
""" Base view """



class View:
    """Chess tournament application view"""

    def create_tournament(self):
        pass

    @staticmethod
    def menu_choice_error(message, option_min, option_max):
        choice_is_invalid = True
        while choice_is_invalid:
            choice = input(message)
            if choice.isdigit() and (option_min <= (num_choice := int(choice)) <= option_max):
                choice_is_invalid = False
            else:
                print("Veuillez choisir une option valide.")
        return num_choice

    @staticmethod
    def number_check(message):
        input_is_not_number = True
        while input_is_not_number:
            information = input(message)
            if information.isdigit():
                input_is_not_number = False
            else:
                print("Veuillez entrer un chiffre?")
        return int(information)

    def player_entry(self):
        return {
            "nom": input("Nom de famille: "),
            "prenom": input("Prénom: "),
            "date_naissance": input("Date de naissance: "),
            "sexe": input("Sexe: "),
            "classement": int(input("classement: ")),
        }


    #def tournament_entry(self):
    #    return{
    #        "nom": input("Nom du tournoi: "),
    #        "lieu": input("Lieu du tournoi: "),
    #        "date": get_timestamp(),
    #        "nombre de rondes": input("Nombre de rondes (4 par défaut): "),
    #        "controle de temps": input("Format de partie du tournoi: \n"
    #                                   "Bullet (une minute par joueur)\n"
    #                                   "BLitz (10 minutes ou moins par joueur)\n"
    #                                   "Coup rapide (de 10 à 60 minutes par joueur)"),
    #        "description": input("Description du tournoi : ")
    #    }

    #def __str__(self):

    def main_menu(self):
        print("\n")
        print(r""" 
         _____ _                     _____                                                 _    
        /  __ \ |                   |_   _|                                               | |   
        | /  \/ |__   ___  ___ ___    | | ___  _   _ _ __ _ __   __ _ _ __ ___   ___ _ __ | |_  
        | |   | '_ \ / _ \/ __/ __|   | |/ _ \| | | | '__| '_ \ / _` | '_ ` _ \ / _ \ '_ \| __| 
        | \__/\ | | |  __/\__ \__ \   | | (_) | |_| | |  | | | | (_| | | | | | |  __/ | | | |_  
         \____/_| |_|\___||___/___/   \_/\___/ \__,_|_|  |_| |_|\__,_|_| |_| |_|\___|_| |_|\__| 


          ___      _           _       _     _             _                                    
         / _ \    | |         (_)     (_)   | |           | |                                   
        / /_\ \ __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _| |_ ___  _ __                        
        |  _  |/ _` | '_ ` _ \| | '_ \| / __| __| '__/ _` | __/ _ \| '__|                       
        | | | | (_| | | | | | | | | | | \__ \ |_| | | (_| | || (_) | |                          
        \_| |_/\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__\___/|_|                          
        """)

        print("Choix 1  -->  Menu Joueurs")
        print("Choix 2  -->  Menu Tournois")
        print("Choix 3  -->  Menu des Rapports")
        print("Choix 0  -->  Quitter le programme")
        message = "Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   "
        return View.menu_choice_error(message, 0, 3)


    def player_menu(self):
        while True:
            print("\n")
            print(r"\\\\\\\\\\\\\\\\  MENU JOUEURS  ////////////////")
            print("Choix 1  -->  Liste des joueurs de la base de données")
            print("Choix 2  -->  Ajouter un nouveau joueur à la base de données")
            print("Choix 0  -->  Retour au menu principal")
            message = "Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   "
            return View.menu_choice_error(message, 0, 2)

    def tournament_menu(self):
        while True:
            print("\n")
            print(r"\\\\\\\\\\\\\\\\  MENU DU TOURNOI  ////////////////")
            print("Choix 1  -->  Liste des joueurs participants au tournoi")
            print("Choix 2  -->  Ajouter un nouveau tournoi")
            print("Choix 0  -->  Retour au menu principal")
            message = "Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   "
            return View.menu_choice_error(message, 0, 2)

    def new_tournament(self):
        print("\n")
        print(r"\\\\\\\\\\\\\\\\  CREATION D'UN NOUVEAU TOURNOI  ////////////////")
        name = input("Nom du tournoi:   ")
        location = input("Lieu du tournoi:   ")
        # Gestion format date:
        date_is_invalid = True
        while date_is_invalid:
            date_str = input("Date du tournoi (au format jj/mm/aaaa) :   ")
            try:
                date = datetime.strptime(date_str, "%d/%m/%Y")
                if date < datetime.now():
                    print("Vous avez entré une date dans le passé, ce qui est impossible")
                else:
                    date_is_invalid = False
            except ValueError:
                print("Format de date invalide")
        # Vérification round_quantity est un nombre
        message_round_quatity = "Nombre de rondes (4 par défaut):"
        round_quantity = View.number_check(message_round_quatity)
        # Vérfication option valide du format de match
        time_control_choices = ["Bullet (une minute par joueur)",
                                "Blitz (10 minutes ou moins par joueur)",
                                "Coup rapide (de 10 à 60 minutes par joueur)"]
        time_control_message = f"Choisisez le format de match:\n" \
                               f"Format de partie du tournoi:\n" \
                               f"Choix 1  -->  {time_control_choices[0]}\n" \
                               f"Choix 2  -->  {time_control_choices[1]}\n" \
                               f"Choix 3  -->  {time_control_choices[2]}\n"
        time_control_choice = View.menu_choice_error(time_control_message, 1, 3)
        time_control = f"{time_control_choices[time_control_choice-1]}"
        description = input("Description du tournoi   ")
        return {"name":name,
                "location":location,
                "date":date,
                "round_quantity":round_quantity,
                "time_control":time_control,
                "description":description
                }

    def new_player(self):
        print("\n")
        print(r"\\\\\\\\\\\\\\\\  CREATION D'UN NOUVEAU JOUEUR  ////////////////")
        first_name = input("Prénom du joueur:   ") # string
        last_name = input("Nom de famille du joueur:   ") # string
        birthday_date = input("Date de naissance du joueur (au format jj/mm/aaaa) :   ")
        # Gestion format date:
        date_is_invalid = True
        while date_is_invalid:
            date_str = input("Date de naissance du joueur (au format jj/mm/aaaa) :   ")
            try:
                date = datetime.strptime(date_str, "%d/%m/%Y")
                if date > datetime.now():
                    print("Vous avez entré une date dans le futur, ce qui est impossible")
                else:
                    date_is_invalid = False
            except ValueError:
                print("Format de date invalide")
        gender = input("Sexe du joueur (F ou M) :   ")
        ranking = int(input("Classement du joueur :   "))
        return {"first_name": first_name, "last_name": last_name, "birthday_date": birthday_date, "gender": gender,
                "ranking": ranking}

    def add_player_menu(self):
        while True:
            print("\n")
            print(r"\\\\\\\\\\\\\\\\  CHOIX DE L'AJOUT DE JOUEUR  ////////////////")
            print("Choix 1  -->  Créer un nouveau joueur et l'ajouter au tournoi")
            print("Choix 2  -->  Ajouter un joueur de la base de données au tournoi")
            choice = input("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 2:
                print("Veuillez choisir une option valide.")
                continue
            else:
                return int(choice)

    def report_menu(self):
        while True:
            print("\n")
            print(r"\\\\\\\\\\\\\\\\  MENU DES RAPPORTS  ////////////////")
            print("Choix 1  -->  Affichage liste des joueurs")
            print("Choix 2  -->  Affichage de tous les tournois")
            print("Choix 0  -->  Retour au menu principal")
            choice = input("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   ")
            if not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
                print("Veuillez choisir une option valide.")
                continue
            else:
                return int(choice)

    def player_listing_menu(self):
        while True:
            print("\n")
            print(r"\\\\\\\\\\\\\\\\  AFFICHAGE DES JOUEURS DE LA BASE DE DONNEES  ////////////////")
            print("Choix 1  -->  Lister les joueurs par ordre alphabétique")
            print("Choix 2  -->  Lister les joueurs par classement elo")
            print("Choix 0  -->  Retour au menu principal")
            choice = input("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   ")
            if not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
                print("Veuillez choisir une option valide.")
                continue
            else:
                return int(choice)

    def tournament_listing_menu(self):
        print("\n")
        print(r"\\\\\\\\\\\\\\\\  AFFICHAGE DES TOURNOIS  ////////////////")
        print() # affichage de tous les tournois de la base de données avec un indice/une clé à sélectionner


    def match_menu(self, joueur1_civility, joueur2_civility):
        while True:
            print("\n")
            print(r"\\\\\\\\\\\\\\\\  RESULTAT DU MATCH  ////////////////")
            print(f"Veuillez indiquer le résultat du match:  {joueur1_civility}  VS {joueur2_civility}")
            print(f"Choix 1  -->  Le joueur {joueur1_civility} est vainqueur")
            print(f"Choix 2  -->  Le joueur {joueur2_civility} est vainqueur")
            print("Choix 3  -->  C'est un match nul")
            choice = input("Tapez le numéro correspondant à votre choix, puis appuyez sur la touche Entrée.   ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
                print("Veuillez choisir une option valide.")
                continue
            else:
                return int(choice)
