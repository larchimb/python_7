from ex1 import Card, CreatureCard
from typing import Union, Any


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.type = 'Spell'
        try:
            if not isinstance(effect_type, str):
                raise TypeError('"effect_type" must be a string')
            if not (
                effect_type == 'damage'
                or effect_type == 'heal'
                or effect_type == 'buff'
                or effect_type == 'debuff'
            ):
                raise ValueError(
                    'Effect must be: "damage", "heal", "buff" or "debuff"'
                )
            self.effect_type = effect_type
        except (TypeError, ValueError) as e:
            print(e)

    def play(
        self, game_state: dict[Any, Any]
    ) -> dict[str, Union[str, int]]:
        dic_play: dict[str, Union[str, int]] = {}
        dic_play['card_played'] = self.name
        if not (game_state['mana'] and self.is_playable(game_state['mana'])):
            dic_play['is_playable'] = False
            return dic_play
        dic_play['is_playable'] = True
        game_state['mana'] -= self.cost
        dic_play['mana_used'] = self.cost
        if self.effect_type == 'damage':
            dic_play['effect'] = f'Deal {self.cost} damage to target'
        elif self.effect_type == 'heal':
            dic_play['effect'] = f'Heal {self.cost} HP to target'
        elif self.effect_type == 'buff':
            dic_play['effect'] = ('Increase attack point '
                                  f'by {int(self.cost / 2)}')
        else:
            dic_play['effect'] = ('Decrease attack point '
                                  f'by {int(self.cost / 2)}')
        return dic_play

    def resolve_effect(
         self, targets: list[CreatureCard]) -> dict[str, Union[str, int]]:
        dic_effect: dict[str, Union[str, int]] = {}
        for target in targets:
            if self.effect_type == 'damage':
                dic_effect[f'{target.name}'] = f'lost {self.cost} HP'
                target.health -= self.cost
            elif self.effect_type == 'heal':
                dic_effect[f'{target.name}'] = f'win {self.cost} HP'
                target.health += self.cost
            elif self.effect_type == 'buff':
                dic_effect[f'{target.name}'] = ('Attack increase by '
                                                f'{int(self.cost / 2)}')
                target.attack += int(self.cost / 2)
            else:
                dic_effect[f'{target.name}'] = ('Attack decrease by '
                                                f'{int(self.cost / 2)}')
                target.attack -= int(self.cost / 2)
        return dic_effect
