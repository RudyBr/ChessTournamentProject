class Player:
    PLAYER_NUMBER = 8

    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def __str__(self):
        return f"Nom: {self.last_name} \n" \
               f"Prénom: {self.first_name} \n" \
               f"Date de naissance: {self.birth_date} \n" \
               f"Sexe: {self.gender} \n" \
               f"Classement Elo: {self.ranking}"
