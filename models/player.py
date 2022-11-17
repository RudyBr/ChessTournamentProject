class Player:
    PLAYER_NUMBER = 8

    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        """

        :param first_name:
        :param last_name:
        :param birth_date:
        :param gender:
        :param ranking:
        """
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.score = 0

    def __str__(self):
        return f"Nom: {self.last_name} \n" \
               f"Prénom: {self.first_name} \n" \
               f"Date de naissance: {self.birth_date} \n" \
               f"Sexe: {self.gender} \n" \
               f"Classement Elo: {self.ranking}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ranking: [{self.ranking}]  score: [{self.score}]"

    def civility(self):
        return f"{self.first_name} {self.last_name}"

    def serialize(self):
        return {"id": self.id if self.id is not None else 0,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "birth_date": self.birth_date,
                "gender": self.gender,
                "ranking": self.ranking,
                "score": self.score
                }
