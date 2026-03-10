from abc import abstractmethod, ABC
from typing import Any
from ex2 import Card


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(
         self, hand: list[Card], battlefield: list[Card]) -> dict[Any, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        pass

