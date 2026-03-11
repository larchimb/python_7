from ex0.Card import Card
from typing import Union, Any


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        try:
            super().__init__(name, cost, rarity)
            self.type = 'Creature'
            self.attack = int(attack)
            if self.attack < 0:
                raise ValueError
            self.dictio['attack'] = self.attack
            self.health = int(health)
            if self.health <= 0:
                raise ValueError
            self.dictio['health'] = self.health
        except ValueError:
            print("You need positive integer for attack and health")

    def play(self, game_state: dict[Any, Any]) -> dict[str, Union[int, str]]:
        dic_play: dict[str, Union[int, str]] = {}
        dic_play['card_played'] = self.name
        dic_play['mana_used'] = self.cost
        if not self.is_playable(game_state['mana']):
            dic_play['playable'] = False
            return dic_play
        dic_play['playable'] = True
        dic_play['effect'] = 'Creature summoned to battlefield'
        game_state['mana'] -= self.cost
        return dic_play

    def attack_target(
        self, target: "CreatureCard"
    ) -> dict[str, Union[int, str]]:
        dic_att: dict[str, Union[int, str]] = {}
        dic_att['attacker'] = self.name
        dic_att['target'] = target.name
        dic_att['damage_dealt'] = self.attack
        if self.attack >= target.health:
            dic_att['combat_resolved'] = True
        else:
            dic_att['combat_resolved'] = False
            target.health -= self.attack
        print(
            f"\n{self.name} attacks {target.name}:\n"
            f"Attack result: {dic_att}"
        )
        return dic_att
