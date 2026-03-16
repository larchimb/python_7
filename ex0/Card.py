from abc import ABC, abstractmethod
from typing import Union, Any
from enum import Enum

class Rarity(Enum):
    COMMON = 'common'
    RARE = 'rare'
    LEGEND = 'legendary'


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.dictio: dict[str, Union[int, str]] = {}
        try:
            self.name = name
            self.cost = cost
            self.rarity = rarity
            self.type = ''
            if not (
                isinstance(self.name, str) and isinstance(self.rarity, str)
            ):
                raise TypeError
            int(self.cost)
        except (TypeError, ValueError):
            print("Name = str, cost = int, rarity = str")

    @abstractmethod
    def play(self, game_state: dict[Any, Any]) -> dict[str, Union[int, str]]:
        pass

    def get_card_info(self) -> dict[str, Union[str, int]]:
        self.dictio['name'] = self.name
        self.dictio['cost'] = self.cost
        self.dictio['rarity'] = self.rarity
        return self.dictio

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False
