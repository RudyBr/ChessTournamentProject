class Tournament:
    def __init__(self, nom, lieu, date, nombre_de_tours, tournees, controle_du_temps, description):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_tours = nombre_de_tours
        self.tournees = tournees
        self.liste_joueurs = {"joueur01": None,
                              "joueur02": None,
                              "joueur03": None,
                              "joueur04": None,
                              "joueur05": None,
                              "joueur06": None,
                              "joueur07": None,
                              "joueur08": None,
                              }
        self.controle_du_temps = controle_du_temps
        self.description = description
