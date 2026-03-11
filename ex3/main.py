from .AggressiveStrategy import AggressiveStrategy
from typing import Any

def main() -> None:
    game_state: dict[str, dict[Any, Any]] = {
        'Adri': {
            'mana': 6,
            'battlefield': [],
            'hand': []
        },
        'Luc': {
            'mana': 6,
            'battlefield': [],
            'hand': []
        },
    }
    test = AggressiveStrategy()
    print(test.get_strategy_name())


if __name__ == '__main__':
    main()