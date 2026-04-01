from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from .CardFactory import CardFactory
import random

creature_name = [
    'Goblin Warrior',
    'Goblin',
    'Goblin Magician',
    'Elf Warrior',
    'Elf Archer',
    'Elf Magician',
    'Human Bersek',
    'Human knight',
    'Blob'
]
artifact_name = [
    "Ring",
    "Staff",
    "Crystal"
]
spell_damage = [
    'Fireball',
    'Ice',
    'Waterball',
    'Earthbreak',
    'Lightning',
]
effects = [
    "+1 mana",
    "+1 health",
    "+1 attack",
    "-1 cost",
]


class FantasyCardFactory(CardFactory):

    def create_creature(self,
                        name_or_power: str | int | None = None
                        ) -> CreatureCard:
        if isinstance(name_or_power, str):
            name = name_or_power
            attack = random.randint(2, 8)
        elif isinstance(name_or_power, int):
            attack = name_or_power
            name = random.choice(creature_name)
        else:
            name = random.choice(creature_name)
            attack = random.randint(2, 8)

        cost = random.randint(1, 8)
        number = random.randint(0, 100)
        if number < 60:
            rarity = 'common'
        elif number < 90:
            rarity = 'rare'
        else:
            rarity = 'legendary'
        health = random.randint(5, 10)
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self,
                     name_or_power: str | int | None = None) -> SpellCard:
        effect_type = 'damage'
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(2, 8)
        elif isinstance(name_or_power, int):
            cost = name_or_power
            name = random.choice(spell_damage)
        else:
            name = random.choice(spell_damage)
            cost = random.randint(2, 8)

        number = random.randint(0, 100)
        if number < 60:
            rarity = 'common'
        elif number < 90:
            rarity = 'rare'
        else:
            rarity = 'legendary'
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self,
                        name_or_power: str | int | None = None
                        ) -> ArtifactCard:
        if isinstance(name_or_power, str):
            name = name_or_power
            durability = random.randint(2, 8)
        elif isinstance(name_or_power, int):
            durability = name_or_power
            name = random.choice(artifact_name)
        else:
            durability = random.randint(2, 8)
            name = random.choice(artifact_name)
        number = random.randint(0, 100)
        if number < 60:
            rarity = 'common'
        elif number < 90:
            rarity = 'rare'
        else:
            rarity = 'legendary'
        cost = random.randint(1, 8)
        effect = random.choice(effects)
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict[str, Card]:
        deck: dict[str, Card] = {}
        card: Card
        while len(deck) < size:
            nb = random.randint(0, 3)
            if nb == 0:
                card = self.create_artifact()
            elif nb == 1:
                card = self.create_spell()
            else:
                card = self.create_creature()
            if card.name not in deck:
                deck[f'{card.name}'] = card
        return deck

    def get_supported_types(self) -> dict[str, list[str]]:
        dic_type: dict[str, list[str]] = {}
        dic_type['creature'] = [name for name in creature_name]
        dic_type['spell'] = [name for name in spell_damage]
        dic_type['artifact'] = [name for name in artifact_name]
        return dic_type
