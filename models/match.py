class Match:
    def __init__(self, _round, joueur1, joueur2):
        self.id = None
        self.round = _round
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.result = None
        # manque résultat

    def serialize(self):
        return {"id": self.id if self.id is not None else 0,
                "round_id": self.round.id,
                "joueur1": self.joueur1.id,
                "joueur2": self.joueur2.id,
                "result": self.result
                }
