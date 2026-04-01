from abc import abstractmethod, ABC
from typing import Union
from ex0 import CreatureCard
from ex1.SpellCard import SpellCard


class Magical(ABC):

    def __init__(self, mana: int, spell_list: list[SpellCard]) -> None:
        self.mana = mana
        self.spells = spell_list

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[CreatureCard]
                   ) -> dict[str, Union[int, str, list[str]]]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Union[int, str]]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Union[int, str]]:
        pass
