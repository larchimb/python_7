from ex0 import Card, CreatureCard
from ex1 import SpellCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any, Union


class EliteCard(Card, Magical, Combatable):

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int,
        mana: int, spell_list: list[SpellCard]
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack
        self.health: int = health
        self.type = 'Elite Card'
        self.mana = mana
        self.spells: list[SpellCard] = spell_list
        self.dic: dict[str, Union[str, int]] = {}
        self.dic['name'] = self.name
        self.dic['health'] = self.health
        self.dic['mana'] = self.mana

    def play(self, game_state: dict[Any, Any]) -> dict[str, Union[int, str]]:
        dic_play: dict[str, Union[int, str]] = {}
        dic_play['card_played'] = self.name
        print(f"Playing: {self.name} ({self.type})\n")
        if not self.is_playable(game_state['mana']):
            return dic_play
        dic_play['type'] = self.type
        dic_play['mana_used'] = self.cost
        dic_play['effect'] = 'Creature summoned to battlefield'
        game_state['mana'] -= self.cost
        return dic_play

    def attack(self, target: CreatureCard) -> dict[str, Union[int, str]]:
        dic_att: dict[str, Union[int, str]] = {}
        dic_att['attacker'] = self.name
        dic_att['target'] = target.name
        dic_att['damage'] = self.attack_power
        dic_att['combat_type'] = 'melee'
        target.health -= self.attack_power
        return dic_att

    def defend(self, incoming_damage: int) -> dict[str, Union[int, str]]:
        dic_def: dict[str, Union[int, str]] = {}
        dic_def['defender'] = self.name
        dic_def['damage_blocked'] = int(self.cost / 2)
        dic_def['damage_taken'] = max(
            0, incoming_damage - int(dic_def['damage_blocked'])
            )
        self.health -= int(dic_def['damage_taken'])
        if self.health <= 0:
            dic_def['still_alive'] = False
        else:
            dic_def['still_alive'] = True
        return dic_def

    def get_combat_stats(self) -> dict[str, Union[str, int]]:
        dic_combat_stat: dict[str, Union[str, int]] = {}
        dic_combat_stat['remaining_health'] = self.health
        dic_combat_stat['damage_done'] = self.attack_power

        return dic_combat_stat

    def cast_spell(
        self, spell_name: str, targets: list[CreatureCard]
    ) -> dict[str, Union[int, str, list[str]]]:
        dic_spell: dict[str, Union[str, int, list[str]]] = {}
        spell: SpellCard = SpellCard('None', 0, 'commun', 'damage')
        for element in self.spells:
            if element.name == spell_name:
                spell = element
        dic_play = spell.play(self.dic)
        if dic_play['is_playable']:
            spell.resolve_effect(targets)
        dic_spell['caster'] = self.name
        dic_spell['spell'] = spell.name
        dic_spell['targets'] = [element.name for element in targets]
        dic_spell['mana_used'] = spell.cost

        return dic_spell

    def channel_mana(self, amount: int) -> dict[str, Union[int, str]]:
        dic_mana: dict[str, Union[int, str]] = {}
        dic_mana['channeled'] = amount
        self.mana += amount
        self.dic['mana'] = self.mana
        dic_mana['total_mana'] = self.dic['mana']

        return dic_mana

    def get_magic_stats(self) -> dict[str, Union[int, str]]:
        dic_magic_stat: dict[str, Union[str, int]] = {}
        dic_magic_stat['remaining_mana'] = self.dic['mana']
        return dic_magic_stat
