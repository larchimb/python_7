from typing import Any, Union
from ex1 import Card, SpellCard, ArtifactCard, CreatureCard
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(
         self, hand: list[Card], battlefield: list[Card]) -> dict[Any, Any]:
        dic_turn: dict[str, Any] = {}
        dic_turn['cards_played'] = []
        dic_turn['mana_used'] = 0
        dic_turn['damage_dealt'] = 0
        dic_turn['permanents_effects'] = []
        player1: dict[str, int] = {}
        player2: dict[str, Union[int, str]] = {}
        player1['mana'] = 10
        player2['health'] = 20
        player2['name'] = 'Enemy Player'
        try:
            cheapiest = hand[0]
        except IndexError:
            print('No cards in your hand')
            return dic_turn
        for card in hand:
            if cheapiest.cost > card.cost:
                cheapiest = card
        while player1['mana'] > cheapiest.cost:
            cheapiest.play(player1)
            battlefield.append(cheapiest)
            hand.remove(cheapiest)
            dic_turn['cards_played'].append(cheapiest)
            dic_turn['mana_used'] += cheapiest.cost
            if isinstance(cheapiest, CreatureCard):
                dic_turn['damage_dealt'] += cheapiest.attack
            elif isinstance(cheapiest, SpellCard):
                dic_turn['damage_dealt'] += cheapiest.cost
            elif isinstance(cheapiest, ArtifactCard):
                dic_turn['permanents_effects'] += cheapiest.effect
            for card in hand:
                if cheapiest.cost > card.cost:
                    cheapiest = card
        if dic_turn['damage_dealt'] > 0:
            dic_turn['targets_attacked'] = player2['name']
        return dic_turn


    def get_strategy_name(self) -> str:
        return type(self).__name__

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        
