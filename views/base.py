from models import player
from models import tournament

from controllers import timestamp

from datetime import datetime
""" Base view """



class View:
    """Chess tournament application view"""

    def create_tournament(self):
        pass




    def player_entry(self):
        return {
            "nom": input("Nom de famille: "),
            "prenom": input("Prénom: "),
            "date_naissance": input("Date de naissance: "),
            "sexe": input("Sexe: "),
            "classement": int(input("classement: ")),
        }
        pass

    def tournament_entry(self):
        return{
            "nom": input("Nom du tournoi: "),
            "lieu": input("Lieu du tournoi: "),
            "date": get_timestamp(),
            "nombre de rondes": input("Nombre de rondes (4 par défaut): "),
            "controle de temps": input("Format de partie du tournoi: \n"
                                       "Bullet (une minute par joueur)\n"
                                       "BLitz (10 minutes ou moins par joueur)\n"
                                       "Coup rapide (de 10 à 60 minutes par joueur)"),
            "Description": input("Description du tournoi : ")
        }

    #def __str__(self):