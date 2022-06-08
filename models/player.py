class ChessPlayer:

    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement

    @classmethod
    def entree_joueur(cls):
        return cls(
            input("Nom de famille: "),
            input("Prénom: "),
            input("Date de naissance: "),
            input("Sexe: "),
            int(input("classement: ")),
        )

    def __str__(self):
        return f"Nom: {self.nom_de_famille} \n" \
               f"Prénom: {self.prenom} \n" \
               f"Date de naissance: {self.date_de_naissance} \n" \
               f"Sexe: {self.sexe} \n" \
               f"Classement Elo: {self.classement}"

user01 = ChessPlayer.entree_joueur()

print(user01)