from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from typing import Any, Union


class GameEngine:

    def __init__(self) -> None:
        self.counter = 0
        self.nb_cards = 0

    def configure_engine(
         self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print(f'Configuring Fantasy Card Game...\n'
              f'Factory: {type(factory).__name__}\n'
              f'Strategy: {strategy.get_strategy_name()}\n'
              f'Available types: {factory.get_supported_types()}\n')

    def simulate_turn(self) -> dict[Any, Any]:
        self.counter += 1
        self.dic_game = {}
        dic_hand = self.factory.create_themed_deck(3)
        dic_battlefield = self.factory.create_themed_deck(2)
        self.nb_cards = len(dic_hand) + len(dic_battlefield)
        hand = [element for element in dic_hand.values()]
        battlefield = [element for element in dic_battlefield.values()]
        print(f"Hand: "
              f"{[f'{element.name} ({element.cost})' for element in hand]}")
        self.dic_game = self.strategy.execute_turn(hand, battlefield)
        return self.dic_game

    def get_engine_status(self) -> dict[Any, Any]:
        dic_status: dict[str, Union[str, int]] = {}
        dic_status['turns_simulated'] = self.counter
        dic_status['strategy_used'] = type(self.strategy).__name__
        dic_status['total_damage'] = self.dic_game['damage_dealt']
        dic_status['cards_created'] = self.nb_cards
        return dic_status
