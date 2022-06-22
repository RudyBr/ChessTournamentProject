class Tournament:
    def __init__(self, name, location, date, round_quantity, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.round_quantity = round_quantity
        self.rounds = []
        # peut etre liste mieux ? pur player_list
        self.player_list = {"joueur01": None,
                            "joueur02": None,
                            "joueur03": None,
                            "joueur04": None,
                            "joueur05": None,
                            "joueur06": None,
                            "joueur07": None,
                            "joueur08": None,
                            }
        self.time_control = time_control
        self.description = description
