import random


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def description(self) -> str:
        names = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
        value = names.get(self.value, self.value)
        return f"{value} of {self.suit.lower()}"


class Deck:
    def __init__(self) -> None:
        _suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        _values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self._cards = [Card(suit, value) for suit in _suits for value in _values]

    def description(self) -> str:
        return f"{len(self._cards)} cards in the deck"

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def deal(self) -> Card:
        return self._cards.pop()


if __name__ == "__main__":
    deck = Deck()
    print(deck.description())
    card = deck.deal()
    print(card.description())
    deck.shuffle()
    print(deck.description())
