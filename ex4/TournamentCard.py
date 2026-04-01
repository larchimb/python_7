from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Union, Any


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.losses = 0
        self.wins = 0
        self.rate = 0
        self.id = ''
        self.calculate_rating()

    def calculate_rating(self) -> int:
        self.rate += self.cost * self.health * self.attack_power * 10
        if self.rarity == 'common':
            self.rate += 50
        elif self.rarity == 'rare':
            self.rate += 100
        elif self.rarity == 'legendary':
            self.rate += 200
        return self.rate

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict[str, int]:
        return {
            'rating': self.rate,
            'wins': self.wins,
            'losses': self.losses
            }

    def attack(self, target: Any) -> dict[str, Union[int, str]]:
        dic_att: dict[str, Union[int, str]] = {}
        dic_att['attacker'] = self.name
        dic_att['target'] = target.name
        dic_att['damage'] = self.attack_power
        dic_att['combat_type'] = 'melee'
        target.defend(self.attack_power)
        if target.health <= 0:
            self.update_wins(1)
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
            self.update_losses(1)
        else:
            dic_def['still_alive'] = True
        return dic_def

    def get_combat_stats(self) -> dict[str, Union[str, int]]:
        dic_combat_stat: dict[str, Union[str, int]] = {}
        dic_combat_stat['remaining_health'] = self.health
        dic_combat_stat['damage_done'] = self.attack_power
        return dic_combat_stat

    def play(self, game_state: dict[Any, Any]) -> dict[str, Union[int, str]]:
        dic_play: dict[str, Union[int, str]] = {}
        dic_play['card_played'] = self.name
        dic_play['mana_used'] = self.cost
        if not self.is_playable(game_state['mana']):
            dic_play['playable'] = False
            return dic_play
        dic_play['playable'] = True
        dic_play['effect'] = 'Creature summoned to battlefield'
        game_state['mana'] -= self.cost
        return dic_play
