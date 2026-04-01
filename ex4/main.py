from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlateform import TournamentPlateform


def main() -> None:
    drag1 = TournamentCard('Fire Dragon', 5, 'common', 5, 10)
    drag2 = TournamentCard('Ice Dragon', 5, 'common', 4, 9)
    tournament = TournamentPlateform()

    print('=== DataDeck Tournament Platform ===\n')
    print('Registering Tournament Cards...\n')
    print(tournament.register_card(drag1))
    print(tournament.register_card(drag2))
    print('Creating tournament match...\n'
          f'Match result: {tournament.create_match(drag1.id, drag2.id)}\n')
    results = tournament.get_leaderboard()
    print('Tournament Leaderboard:')
    place = 1
    for card in results:
        print(f'{place}. {card.name}'
              f' - Rating: {card.rate} ({card.wins}-{card.losses})')
        place += 1

    print('\nPlateform report\n'
          f'{tournament.generate_tournament_report()}\n')

    print('=== Tournament Platform Successfully Deployed! ===\n'
          'All abstract patterns working together harmoniously!')


if __name__ == '__main__':
    main()
