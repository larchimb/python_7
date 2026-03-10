from ex1 import CreatureCard, SpellCard
from ex2 import EliteCard


def main() -> None:
    fireball = SpellCard('Fireball', 3, 'commun', 'damage')
    spells = [
        fireball
    ]
    firedragon = CreatureCard('Fire Dragon', 5, 'rare', 7, 5)
    goblin = CreatureCard('Goblin', 2, 'commun', 1, 2)
    arcanewarrior = EliteCard('Arcane Warrior',
                              6, 'legendary', 4, 7, 4, spells)

    print('=== DataDeck Ability System ===\n')

    print(
        "EliteCard capabilities:\n"
        "- Card: ['play', 'get_card_info', 'is_playable']\n"
        "- Combatable: ['attack', 'defend', 'get_combat_stats']\n"
        "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n"
    )

    print(f'Playing {arcanewarrior.name} ({arcanewarrior.type})\n')

    print("Combat phase:\n"
          f"Attack result: {arcanewarrior.attack(goblin)}\n"
          f"Defense result: {arcanewarrior.defend(5)}\n")

    print("Magic phase:\n"
          "Spell cast: "
          f"{arcanewarrior.cast_spell('Fireball', [firedragon, goblin])}\n"
          f"Mana channel: {arcanewarrior.channel_mana(3)}\n")

    print('Multiple interface implementation successful!')


if __name__ == "__main__":
    main()
