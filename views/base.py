from models import player
from models import tournament
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
