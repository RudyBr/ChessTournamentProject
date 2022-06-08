"""Entry point."""

from models.tournament import Tournament

from controllers.base import Controller

from views.base import View


def main():
    tournament = Tournament("nom_tournoi", "Paris", "05062022", 7, [], "Blitz", "Description_tournoi")

    view = View()

    game = Controller(tournament, view)
    game.run()


if __name__ == "__main__":
    main()
