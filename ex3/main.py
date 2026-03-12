from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory


def main() -> None:

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print('=== DataDeck Game Engine ===\n')
    engine.configure_engine(factory, strategy)
    print('Simulating aggressive turn...')
    print(f'{engine.simulate_turn()}\n')
    print('Game report\n'
          f'{engine.get_engine_status()}\n')
    print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')


if __name__ == '__main__':
    main()
