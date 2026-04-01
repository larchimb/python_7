from ex0.Card import Card
from typing import Union, Any


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.type = 'Artifact'
        try:
            if not isinstance(effect, str):
                raise TypeError('"effect" must be a string')
            if not isinstance(durability, int):
                raise TypeError(
                    'Durability must be a int'
                )
            self.durability = durability
            self.effect = effect
        except (TypeError) as e:
            print(e)

    def play(
        self, game_state: dict[Any, Any]
    ) -> dict[str, Union[str, int]]:
        dic_play: dict[str, Union[str, int]] = {}
        dic_play['card_played'] = self.name
        if not (game_state['mana'] and self.is_playable(game_state['mana'])):
            return dic_play
        game_state['mana'] += 1
        dic_play['mana_used'] = self.cost
        dic_play['effect'] = self.effect
        return dic_play

    def activate_ability(self) -> dict[str, Union[str, int]]:
        dic_effect: dict[str, Union[str, int]] = {}
        dic_effect['remaining_time'] = self.durability
        dic_effect['effect'] = '+1 mana'
        dic_effect['activ'] = True
        if self.durability == 0:
            print(f'{self.name} effect is over')
            dic_effect['activ'] = False
        self.durability -= 1
        return dic_effect
