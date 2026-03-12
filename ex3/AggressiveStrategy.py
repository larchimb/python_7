from typing import Any, Union
from ex1 import Card, SpellCard, ArtifactCard, CreatureCard
from .GameStrategy import GameStrategy


class Player:
    def __init__(self, name: str, health: int, mana: int) -> None:
        self.name = name
        self.health = health
        self.mana = mana
        self.dic: dict[str, Union[str, int]] = {}

    def get_infos(self) -> dict[str, Union[str, int]]:
        self.dic['name'] = self.name
        self.dic['health'] = self.health
        self.dic['mana'] = self.mana
        return self.dic


class AggressiveStrategy(GameStrategy):

    def execute_turn(
         self, hand: list[Card], battlefield: list[Card]) -> dict[Any, Any]:
        dic_turn: dict[str, Any] = {}
        dic_turn['cards_played'] = []
        dic_turn['mana_used'] = 0
        dic_turn['targets_attacked'] = []
        dic_turn['damage_dealt'] = 0

        if not hand:
            print('No cards in your hand')
            return dic_turn

        player1 = Player('player1', 20, 10)
        player1_dic: dict[str, Union[int, str]] = player1.get_infos()
        player2 = Player('Enemy Player', 20, 10)
        potential_target: list[Any] = battlefield
        potential_target.append(player2)

        hand_creatures = [
            card for card in hand if isinstance(card, CreatureCard)]
        hand_spells = [
            card for card in hand if isinstance(card, SpellCard)]
        hand_artifacts = [
            card for card in hand if isinstance(card, ArtifactCard)]

        while hand_creatures:
            cheapiest1 = hand_creatures[0]
            for card in hand_creatures:
                if cheapiest1.cost > card.cost:
                    cheapiest1 = card
            if player1.mana > cheapiest1.cost:
                cheapiest1.play(player1_dic)
                dic_turn['cards_played'].append(cheapiest1.name)
                hand.remove(cheapiest1)
                hand_creatures.remove(cheapiest1)
                dic_turn['mana_used'] += cheapiest1.cost
                dic_turn['damage_dealt'] += cheapiest1.attack
                player1.mana -= cheapiest1.cost
            else:
                break

        while hand_spells:
            cheapiest2: SpellCard = hand_spells[0]
            for card1 in hand_spells:
                if cheapiest2.cost > card1.cost:
                    cheapiest2 = card1
            if player1.mana > cheapiest2.cost:
                cheapiest2.play(player1_dic)
                dic_turn['cards_played'].append(cheapiest2.name)
                hand.remove(cheapiest2)
                hand_spells.remove(cheapiest2)
                dic_turn['mana_used'] += cheapiest2.cost
                dic_turn['damage_dealt'] += cheapiest2.cost
                player1.mana -= cheapiest2.cost
            else:
                break

        dic_turn['permanents_effects'] = []
        while hand_artifacts:
            cheapiest3 = hand_artifacts[0]
            for card2 in hand_artifacts:
                if cheapiest3.cost > card2.cost:
                    cheapiest3 = card2
            if player1.mana > cheapiest3.cost:
                cheapiest3.play(player1_dic)
                dic_turn['cards_played'].append(cheapiest3.name)
                dic_turn['permanents_effects'].append(cheapiest3.effect)
                hand.remove(cheapiest3)
                hand_artifacts.remove(cheapiest3)
                dic_turn['mana_used'] += cheapiest3.cost
                player1.mana -= cheapiest3.cost
            else:
                break
        if not dic_turn['permanents_effects']:
            del dic_turn['permanents_effects']

        targets = self.prioritize_targets(potential_target)
        attack = dic_turn['damage_dealt']
        if attack <= 0:
            del dic_turn['damage_dealt']
        for target in targets:
            if attack > 0:
                dic_turn['targets_attacked'].append(target.name)
                if attack > target.health:
                    attack -= target.health
                    battlefield.remove(target)
                    if target.name == player2.name:
                        print(f"{target.name} is eliminated")
                        break
                else:
                    target.health -= attack
                    break
        return dic_turn

    def get_strategy_name(self) -> str:
        return type(self).__name__

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        targets: list[Any] = []
        for target in available_targets:
            if isinstance(target, CreatureCard):
                targets.append(target)
            elif isinstance(target, Player):
                targets.append(target)
        return targets
