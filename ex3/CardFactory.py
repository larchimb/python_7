from abc import abstractmethod, ABC
from ex2 import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Card]:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, list[str]]:
        pass
