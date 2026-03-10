from ex1 import Card, CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Union
import random


class Deck():
    def __init__(self) -> None:
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        try:
            if not isinstance(card, Card):
                raise TypeError("You can only add a Card")
            self.deck.append(card)
        except TypeError as e:
            print(e)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        nb_cards = len(self.deck)
        tmp_deck: list[Card] = []
        for i in range(0, nb_cards):
            tmp_deck.append(random.choice(self.deck))
            self.remove_card(tmp_deck[i].name)
        self.deck = tmp_deck

    def draw_card(self) -> Card:
        try:
            if not self.deck[0]:
                raise IndexError('The deck is empty')
            temp = self.deck[0]
            self.remove_card(self.deck[0].name)
            return temp
        except IndexError as e:
            print(e)
            return CreatureCard('Deck empty', 0, 'NA', 0, 0)

    def get_deck_stats(self) -> dict[str, Union[int, float]]:
        dic_stats: dict[str, Union[int, float]] = {}
        creature = 0
        spell = 0
        artifact = 0
        total_cost = 0
        for card in self.deck:
            if isinstance(card, CreatureCard):
                creature += 1
            elif isinstance(card, SpellCard):
                spell += 1
            elif isinstance(card, ArtifactCard):
                artifact += 1
            total_cost += card.cost
        dic_stats['total_cards'] = len(self.deck)
        dic_stats['creatures'] = creature
        dic_stats['spells'] = spell
        dic_stats['artifacts'] = artifact
        dic_stats['avg_cost'] = round(total_cost / len(self.deck), 1)
        return dic_stats
