from abc import abstractmethod, ABC
from typing import Any
from ex0 import CreatureCard


class Combatable(ABC):

    def __init__(self, attack: int, health: int) -> None:
        self.attack_power = attack
        self.health = health
        
    @abstractmethod
    def attack(self, target: CreatureCard) -> dict[Any, Any]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[Any, Any]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[Any, Any]:
        pass
