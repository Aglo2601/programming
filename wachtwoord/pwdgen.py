import math
import random
from pathlib import Path

VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvwz"
PATTERN = "CVCCVC"
# uit blogpost


DIGIT_POSITIONS = (5, 7, 12, 14, 19)


def load_wordlist() -> list[str]:
    #Lees de woorden uit no_offense.txt
    path = Path(__file__).with_name("no_offense.txt")
    with open(path) as file:
        return [line.strip().lower() for line in file if line.strip()]


WORDLIST = load_wordlist()


def new_group() -> str:
    # teken string gegenereerd
	"""

    >>> group = new_group()
    
    >>> len(group)
    6
    >>> all(c in CONSONANTS for c in group[0] + group[2] + group[3] + group[5])
    True
    >>> all(c in VOWELS for c in group[1] + group[4])
    True
    """
    group = ""
    for kind in PATTERN:
        if kind == "C":
            group += random.choice(CONSONANTS)
        else:
            group += random.choice(VOWELS)
    return group


def new_password() -> str:
    """
    Genereert een wachtwoord, bijvoorbeeld 'funrus-Hommez-kajzo7'.

    Het wachtwoord bevat 20 tekens: 2 streepjes, 1 cijfer, 1 hoofdletter en
    verder kleine letters en staat niet in offensive wordlist txt

    >>> password = new_password()
    >>> len(password)
    20
    >>> password.count("-")
    2
    >>> sum(c.isdigit() for c in password)
    1
    >>> sum(c.isupper() for c in password)
    1
    >>> any(word in password.lower() for word in WORDLIST)
    False
    """
    while True:
        chars = list("-".join([new_group(), new_group(), new_group()]))

        chars[random.choice(DIGIT_POSITIONS)] = str(random.randrange(10))

        # Eén van de overgebleven letters wordt een hoofdletter.
        letter_positions = [i for i, c in enumerate(chars) if c.isalpha()]
        position = random.choice(letter_positions)
        chars[position] = chars[position].upper()

        password = "".join(chars)
        if not any(word in password.lower() for word in WORDLIST):
            return password


def entropy(text: str) -> float:
    """
    Aantal bits entropie via shannon's formule: -sum(p * log2(p)) * len(text)

    >>> entropy("ab")
    2.0
    >>> entropy("abcd")
    8.0
    """
    total = 0.0
    for char in set(text):
        chance = text.count(char) / len(text)
        total -= chance * math.log2(chance)
    return total * len(text)


def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """
    total = 0.0
    for _ in range(10_000):
        total += entropy(new_password())
    print(f"{total / 10_000:.1f} bits")


if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()