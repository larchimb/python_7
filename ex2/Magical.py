from abc import abstractmethod, ABC
from typing import Any
from ex0 import CreatureCard
from ex1 import SpellCard


class Magical(ABC):

    def __init__(self, mana: int, spell_list: list[SpellCard]) -> None:
        self.mana = mana
        self.spells = spell_list

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[CreatureCard]
                   ) -> dict[Any, Any]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[Any, Any]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[Any, Any]:
        pass
