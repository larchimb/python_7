from .CreatureCard import CreatureCard
from typing import Any


def main() -> None:
    game_state: dict[str, dict[str, Any]] = {
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
    print("=== DataDeck Card Foundation ===\n\n"
          "Testing Abstract Base Class Design:\n")

    dragon = CreatureCard('Fire Dragon', 5, 'legendary', 7, 5)
    goblin = CreatureCard('Goblin Warrior', 2, 'common', 1, 3)
    game_state['Luc']['battlefield'].append(goblin)
    print(f"CreatureCard Info:\n{dragon.get_card_info()}")

    print(
            f'\nPlaying {dragon.name} (cost: {dragon.cost}) '
            f'with {game_state["Adri"]["mana"]} mana available:'
        )
    result = dragon.play(game_state['Adri'])
    if result.get('playable'):
        print("Playable: True")
        print(f"Play result: {result}")
    else:
        print("Playable: False")
    game_state['Adri']['battlefield'].append(dragon)
    dragon.attack_target(goblin)

    print(
            f'\nPlaying {dragon.name} (cost: {dragon.cost}) '
            f'with {game_state["Adri"]["mana"]} mana available:'
        )
    result = dragon.play(game_state['Adri'])
    if result.get('playable'):
        print(f"Play result: {result}")
    else:
        print("Playable: False")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == '__main__':
    main()
