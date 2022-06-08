from models import player
from models import tournament
""" Base view """



class View:
    """Chess tournament application view"""

    def creation_tournoi(self):
        pass




    def saisie_joueur(self):
        return {
            "nom": input("Nom de famille: "),
            "prenom": input("Prénom: "),
            "date_naissance": input("Date de naissance: "),
            "sexe": input("Sexe: "),
            "classement": int(input("classement: ")),
        }
