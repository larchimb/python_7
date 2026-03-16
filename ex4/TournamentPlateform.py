from .TournamentCard import TournamentCard
import collections
import random 
from typing import Union

class TournamentPlateform:
    def __init__(self) -> None:
        self.match = 0
        self.cards: dict[str, TournamentCard] = {}
        self.ids = collections.defaultdict(int)
        
    def register_card(self, card: TournamentCard) -> str:
        words = card.name.split()
        name = words[-1].lower()
        self.ids[f'{name}'] += 1
        self.cards[f'{name}_{self.ids[f"{name}"]:03d}'] = card
        card.id = f'{name}_{self.ids[f"{name}"]:03d}'
        return (f'{card.name} (ID: {name}_{self.ids[f"{name}"]:03d})\n'
                f'- Interfaces: {[cls.__name__ for cls in TournamentCard.__bases__]}\n'
                f'- Rating: {card.rate}\n'
                f'- Record: {card.wins}-{card.losses}\n')


    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Union[str, int]]:
        dic_match: dict[str, Union[str, int]] = {}
        fighter1 = self.cards[card1_id]
        fighter2 = self.cards[card2_id]
        while fighter1.health > 0 and fighter2.health > 0:
            nb = random.randint(1, 2)
            if nb == 1:
                fighter1.attack(fighter2)
                if fighter2.health <= 0:
                    break
                fighter2.attack(fighter1)
            else:
                fighter2.attack(fighter1)
                if fighter1.health <= 0:
                    break
                fighter1.attack(fighter2)

        if fighter2.health <= 0:
            dic_match['winner'] = card1_id
            dic_match['loser'] = card2_id
            fighter1.rate += 16
            fighter2.rate -= 16
            dic_match['winner_rating'] = fighter1.rate
            dic_match['loser_rating'] = fighter2.rate
        else:
            dic_match['winner'] = card2_id
            dic_match['loser'] = card1_id
            fighter2.rate += 16
            fighter1.rate -= 16
            dic_match['winner_rating'] = fighter2.rate
            dic_match['loser_rating'] = fighter1.rate
        self.match += 1
        return dic_match

    def get_leaderboard(self) -> list[TournamentCard]:
        leaderboard = sorted([element for element in self.cards.values()], key= lambda element: element.rate, reverse = True)
        return leaderboard
    
    def generate_tournament_report(self) -> dict[str, Union[str, int]]:
        dic_tournament: dict[str, Union[str, int]] = {}
        dic_tournament['total_cards'] = len(self.cards)
        dic_tournament['matches_played'] = self.match
        dic_tournament['avg_rating'] = (
            sum(element.rate for element in self.cards.values()) / len(self.cards)
        )
        if self.cards:
            dic_tournament['platform_status'] = 'active' 
        else:
            dic_tournament['platform_status'] = 'inactive' 
        return dic_tournament

