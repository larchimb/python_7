from abc import abstractmethod, ABC
from typing import Union
from ex0.CreatureCard import CreatureCard


class Combatable(ABC):

    def __init__(self, attack: int, health: int) -> None:
        self.attack_power = attack
        self.health = health

    @abstractmethod
    def attack(self, target: CreatureCard) -> dict[str, Union[int, str]]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Union[int, str]]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Union[int, str]]:
        pass
