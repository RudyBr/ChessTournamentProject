class Tournament:
    def __init__(self, nom, lieu, date, nombre_de_tours, tournees, controle_du_temps, description):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_tours = nombre_de_tours
        self.tournees = tournees
        self.liste_joueurs = []
        self.controle_du_temps = controle_du_temps
        self.description = description
        