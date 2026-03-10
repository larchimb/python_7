from ex0 import CreatureCard


def main() -> None:
    player = {
        'name': 'Adri',
        'mana': 6
    }
    print("=== DataDeck Card Foundation ===\n\n"
          "Testing Abstract Base Class Design:\n")

    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    goblin = CreatureCard('Goblin Warrior', 2, 'Common', 1, 3)
    print(f"CreatureCard Info:\n{dragon.get_card_info()}")

    print(
            f'\nPlaying {dragon.name} (cost: {dragon.cost}) '
            f'with {player["mana"]} mana available:'
        )
    dragon.play(player)
    dragon.attack_target(goblin)

    print(
            f'\nPlaying {dragon.name} (cost: {dragon.cost}) '
            f'with {player["mana"]} mana available:'
        )
    print(f'Play result: {dragon.play(player)}')
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == '__main__':
    main()
