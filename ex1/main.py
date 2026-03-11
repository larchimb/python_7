from ex1 import CreatureCard, SpellCard, ArtifactCard, Deck, Card
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
    deck_cards: list[Card] = [
        SpellCard('Lightning Bolt', 3, 'rare', 'damage'),
        ArtifactCard(
            'Mana Crystal', 2, 'common', 4, 'Permanent: +1 mana per turn'),
        CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5),
    ]
    print('=== DataDeck Deck Builder ===\n')
    deck = Deck()
    for card in deck_cards:
        deck.add_card(card)
    print('Building deck with different card types...\n'
          f'Deck stats: {deck.get_deck_stats()}\n')

    print('Drawing and playing cards:\n')

    for i in range(0, len(deck.deck)):
        card = deck.draw_card()
        print(f'Drew: {card.name} ({card.type})')
        print(f"Play result: {card.play(game_state['Luc'])}")
        if not isinstance(card, SpellCard):
            game_state['Luc']['battlefield'].append(card)
        print()

    print('Polymorphism in action: Same interface, different card behaviors!')


if __name__ == "__main__":
    main()
